# VideoDriverKit

Build user-space drivers for video capture and playback hardware.

**Platforms:** macOS; DriverKit 27.0+ SDK

**Status:** Beta APIs as of September 8, 2026. Apple publishes DriverKit-version availability and explicitly identifies macOS as the supported platform.

## Overview

VideoDriverKit supplies the video-specific objects for a DriverKit extension. It manages communication between the driver and CoreMedia, avoiding the need to build that integration with `IOVideoFamily` kernel extensions and CoreMediaIO Device Abstraction Layer plug-ins.

Subclass `IOUserVideoDriver`, an `IOService` subclass, for the driver entry point. Represent devices, streams, timing, and controls with the framework's corresponding classes. `IOUserVideoDevice` inherits from `IOUserVideoClockDevice` and owns its streams. This is a hardware-driver framework, not an application video-rendering API.

The host controls when device I/O starts and stops. For a device configuration change that affects I/O or structure, request the change with `RequestDeviceConfigurationChange` and wait for the host's `PerformDeviceConfigurationChange` callback before applying it. Clock-device timestamps relate device sample time to Mach absolute time; changing active device state without this coordination is not the documented lifecycle.

## Installation and constraints

Use [SystemExtensions](SystemExtensions.md) to activate and update the driver on macOS. Follow [DriverKit](DriverKit.md) signing, provisioning, and entitlement requirements; importing VideoDriverKit does not authorize driver installation or hardware access.

The driver needs the Boolean [`com.apple.developer.driverkit`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit) entitlement. The `IOUserVideoDriver` reference also requires Boolean [`com.apple.developer.driverkit.allow-any-userclient-access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.allow-any-userclient-access) on the extension for host communication. This permits connections from apps without an individual user-client-access grant; it is not a narrowly scoped grant to just the containing app. The containing app separately needs Boolean [`com.apple.developer.system-extension.install`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.install). Enable each required capability with `true` in the appropriate signed target.

Configure the video driver's user-client properties as described in the [`IOUserVideoDriver` reference](https://developer.apple.com/documentation/videodriverkit/iouservideodriver); the framework supplies the video user client. Use the documented provisioning requirements rather than guessing a family entitlement.

Activation can require user approval or fail. Keep the containing app usable while activation is pending, and handle device removal and unavailable driver services rather than assuming installation guarantees a connected video device.

Do not infer iPadOS support from other DriverKit families. Likewise, legacy Intel support in the base DriverKit reference is not evidence that an Intel Mac can run a particular macOS 27 host configuration.

## Topics

- [IOUserVideoDriver](https://developer.apple.com/documentation/videodriverkit/iouservideodriver) — Driver entry point.
- [IOUserVideoObject](https://developer.apple.com/documentation/videodriverkit/iouservideoobject) — Common video-object base; do not subclass or allocate it directly.
- [IOUserVideoDevice](https://developer.apple.com/documentation/videodriverkit/iouservideodevice) and [IOUserVideoClockDevice](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice) — Devices and clocking.
- [IOUserVideoStream](https://developer.apple.com/documentation/videodriverkit/iouservideostream) — Video streams.
- [IOUserVideoControl](https://developer.apple.com/documentation/videodriverkit/iouservideocontrol) — Base for Boolean, selector, slider, level, and other controls; use the concrete control classes rather than subclassing or allocating this base directly.
- [Requesting DriverKit entitlements](https://developer.apple.com/documentation/driverkit/requesting-entitlements-for-driverkit-development)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/videodriverkit)
- [Readable framework documentation](https://developer.apple.com/documentation/videodriverkit.md)
- [SDK availability metadata](https://developer.apple.com/tutorials/data/documentation/videodriverkit.json)
