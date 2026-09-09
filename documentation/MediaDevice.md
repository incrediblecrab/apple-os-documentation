# Media Device

Expose a hardware media-sharing protocol through the system's media device picker.

**Platforms:** iOS 27.0+ | iPadOS 27.0+

**Status:** OS 27 beta APIs, reviewed September 8, 2026. This is a provider-extension framework, not a general-purpose desktop media library.

**Mac Catalyst discrepancy:** The framework reference lists Mac Catalyst 27.0, while [Apple's routing and streaming guide](https://developer.apple.com/documentation/avsystemrouting/routing-and-streaming-media-to-remote-devices) explicitly excludes Mac Catalyst and visionOS. Treat Catalyst deployment as unconfirmed by these conflicting sources, not as guaranteed support.

## Overview

A Media Device extension discovers receivers, connects to a selected device, and translates system playback operations into its hardware protocol. Supporting media apps use [AVSystemRouting](AVSystemRouting.md) while the extension owns protocol-specific communication.

The lifecycle is discovery, activation, then playback. A discovered device is not automatically an active connection, and the system may show a cached device before the extension rediscovers it.

## Topics

- [Creating a media device extension](https://developer.apple.com/documentation/mediadevice/creating-a-media-device-extension) — Target setup, protocol registration, discovery, pairing, playback, and real-time streaming.
- [MediaDeviceExtension](https://developer.apple.com/documentation/mediadevice/mediadeviceextension) — Implements the provider lifecycle.
- [MediaOutputDevice](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice) — Describes a receiver and its actual capabilities.
- [MediaDeviceRoutingManager](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager) — Reports discovery, activation results, and device or playback changes to the system.
- [MediaOutputSession](https://developer.apple.com/documentation/mediadevice/mediaoutputsession) — Identifies the active output session.
- [RealtimeSampleHandling](https://developer.apple.com/documentation/mediadevice/realtimesamplehandling) — Adds real-time sample delivery to a provider.
- [MediaDeviceError](https://developer.apple.com/documentation/mediadevice/mediadeviceerror) — Reports discovery, authorization, connection, and session failures.

## Registration and authorization

Both the extension and its container app require the [media-device-extension entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.media-device-extension). Its value is the media-sharing protocol identifier, not a Boolean.

Apple's routing and streaming guide specifies a dedicated container app for deploying the extension and explaining its use, rather than bundling unrelated application functionality into that provider app.

Use that same identifier for the exported uniform type and the extension's `protocolType`. The exported type must conform to `public.media-sharing-protocol`. Configure the extension point as `com.apple.media-device-extension` in `EXAppExtensionAttributes`.

Report only capabilities the receiver implements. When pairing is needed, use the routing manager's authorization flow, handle canceled or invalid input, and report activation success only after the connection succeeds. Installing the extension does not authorize arbitrary screen or microphone capture.

Discovery has its own privacy requirements. Apple's routing guide requires `NSBluetoothAlwaysUsageDescription` when using Core Bluetooth, and `NSLocalNetworkUsageDescription` plus appropriate `NSBonjourServices` entries for `NWBrowser`-based local discovery.

## Lifecycle and failure guidance

- Start and stop discovery when requested by the system. An empty result is normal; do not report it as `discoveryFailed(_:)`.
- Use stable device identifiers so cached discovery entries refer to the same physical receiver. Report devices that disappear rather than leaving stale choices indefinitely.
- Maintain persistent connections only for devices the system has activated. Release session resources on deactivation.
- Report activation and playback failures through the routing manager so the picker and media app receive a result.
- Notify the system of externally caused volume changes, but do not echo system-initiated volume commands back as new changes.

## Real-time streaming requirements

URL playback and sample streaming are separate capabilities. Screen-mirroring video requires real-time audio support as well; advertise both capabilities when applicable.

Real-time delivery requires an audio server driver plug-in exposing a single output device whose unique identifier matches the media device. That audio device must appear promptly upon activation; otherwise, the system deactivates the receiver and reports **Unable to Connect**. Follow the [audio server driver guide](https://developer.apple.com/documentation/coreaudio/creating-an-audio-server-driver-plug-in), not just the URL-playback example.

The audio plug-in supplies audio samples; [ScreenCaptureKit](ScreenCaptureKit.md) supplies video during screen mirroring. Encoding uses Audio Toolbox or Video Toolbox as appropriate. Test these paths on the intended receiver and OS version rather than inferring streaming support from successful discovery.

## Sources

- [Media Device reference](https://developer.apple.com/documentation/mediadevice)
- [Creating a media device extension](https://developer.apple.com/documentation/mediadevice/creating-a-media-device-extension)
- [AVSystemRouting reference](https://developer.apple.com/documentation/avsystemrouting)
