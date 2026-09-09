# Wi-Fi Infrastructure

Share authorized Wi-Fi network credentials with a paired accessory.

**Platforms:** iOS 26.2+ | iPadOS 26.2+

**Status:** Reviewed September 8, 2026. Developer testing is available in all regions; customer use requires a device located in the EU and an Apple Account with an EU country or region. Mac Catalyst symbol listings do not establish a working transport on Mac.

## Overview

WiFiInfrastructure helps companion apps provision an accessory without asking people to enter a Wi-Fi password on limited accessory hardware. It shares networks with an accessory paired through [AccessorySetupKit](AccessorySetupKit.md), using [AccessoryTransportExtension](AccessoryTransportExtension.md) to deliver the information.

People choose the sharing scope, including automatic sharing or approval of an individual network. This is not an unrestricted API for reading saved Wi-Fi passwords.

## Configuration and transport

Enable [`com.apple.developer.wifi-infrastructure`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.wifi-infrastructure) through the Wi-Fi Infrastructure capability. Its value is an **array of strings** containing `WiFiNetworkSharing`. The sharing extension additionally requires the Boolean [`com.apple.developer.accessory-transport-extension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-transport-extension) entitlement set to `true`.

The accessory must be paired and use **Bluetooth Secure Connections as specified by Apple's Bluetooth 4.2 requirement**. Apple's entitlement reference specifies Secure Simple Pairing and AES-128 encryption of the data. Network sharing occurs while the accessory is connected over Bluetooth; proximity without an authorized, secure connection is insufficient.

Use `WINetworkSharingController` only in the containing app for sharing requests and system UI. Use `WINetworkSharingProvider` only in the extension for the asynchronous sequence of shared-network information and related sharing UI. Both require the Wi-Fi Infrastructure entitlement with `WiFiNetworkSharing`. The transport framework ignores calls from Mac Catalyst apps and iOS apps running on Macs or visionOS.

## Authorization and failures

Inspect the sharing authorization state instead of assuming pairing implies consent. `WINetworkSharingAskToShareState` distinguishes `.undetermined`, `.denied`, and `.approved` for the current network and accessory. Respect refusal, per-network choices, and later changes or removal of authorization. Avoid retaining or logging credentials beyond what the accessory needs to join the authorized network.

Handle unavailable Bluetooth, unsupported security, disconnection, declined sharing, and network-sharing errors. Errors also distinguish app permission from accessory authorization, foreground requirements, timeouts, and excessive requests. A successful credential transfer is not proof that the accessory joined the network; keep network-selection and retry behavior explicit.

Apple's sample uses two physical iOS/iPadOS 26.2+ devices on the same Wi-Fi network and cannot run in Simulator because it depends on Bluetooth. One app simulates a Bluetooth dice accessory; the companion app exercises network sharing. These are sample setup requirements, not a requirement that a real accessory already know the Wi-Fi credentials being provisioned.

## Topics

- [Sharing Wi-Fi network credentials](https://developer.apple.com/documentation/wifiinfrastructure/sharing-wi-fi-network-credentials)
- [WINetworkSharingController](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller)
- [WINetworkSharingProvider](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider)
- [WINetworkSharingAskToShareState](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingasktosharestate)
- [WINetworkSharingError](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingerror)
- [WISSID](https://developer.apple.com/documentation/wifiinfrastructure/wissid), [WIChannel](https://developer.apple.com/documentation/wifiinfrastructure/wichannel), and [WIMACAddress](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/wifiinfrastructure)
- [Runtime and regional requirements](https://developer.apple.com/documentation/wifiinfrastructure.md)
- [Entitlement and Bluetooth security requirements](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.wifi-infrastructure.md)
