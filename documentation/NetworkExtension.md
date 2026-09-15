# Network Extension

Customize and extend core networking features.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.1+ | macOS 10.10+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

With the NetworkExtension framework, you can customize and extend the system's core networking features. Specifically, you can:

- Change the system's Wi-Fi configuration
- Integrate your app with the hotspot network subsystem (Hotspot Helper)
- Create and manage VPN configurations, using the built-in VPN protocols (Personal VPN) or a custom VPN protocol
- Create and manage network relay configurations
- Implement an on-device content filter
- Create and manage system-wide DNS configurations, using the built-in DNS protocols or a custom on-device DNS proxy

The NetworkExtension framework is available in macOS, iOS, tvOS, and visionOS, but not all features are available on all platforms and some features have specific restrictions (for example, some features only work on supervised iOS devices). The documentation for each feature describes these restrictions.

The platform header is umbrella metadata, not a provider-deployment matrix. [TN3134](https://developer.apple.com/documentation/technotes/tn3134-network-extension-provider-deployment) distinguishes native apps, Catalyst, iOS apps on Mac, and app versus system extensions. On macOS, an app-extension provider terminates when its user logs out; a system-extension provider runs independently of the logged-in user.

### Entitlements, consent, and deployment

- [`com.apple.developer.networking.networkextension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.networkextension) is an **array of strings**, not a Boolean. Select the values for the provider and packaging you actually implement, such as `packet-tunnel-provider`, `dns-settings`, or the documented system-extension variant.
- Personal VPN uses the separate string-array entitlement [`com.apple.developer.networking.vpn.api`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.vpn.api), containing `allow-vpn`. The person must authorize the first saved Personal VPN configuration. Managed configurations can take precedence over a Personal VPN default route.
- Hotspot integration requires Apple's special Boolean [`com.apple.developer.networking.HotspotHelper`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.HotspotHelper) grant. It is not a general-purpose Wi-Fi scanning, accessory-setup, or location API.
- Filter and DNS-proxy deployment has supervision, managed per-app, and platform-specific rules. The Screen Time content-filter exception requires **child** authorization on a child's family device; individual authorization is not that exception. DNS Settings configurations must be explicitly enabled by the person.

Treat denied authorization, disabled or removed configurations, and provider startup or routing failures as normal outcomes. A saved configuration or an entitlement alone does not prove that traffic is flowing through the provider.

### OS 27 networking notes

**Reviewed September 8, 2026:** The iOS/iPadOS 27 release notes mark the wired-CarPlay exclusion issue as resolved: a VPN using `includeAllNetworks = true` previously failed to honor `excludeLocalNetworks` for wired CarPlay. Test routing and reconnect behavior on the OS versions you support rather than assuming older betas had the fix.

The separate 27 TLS hardening concerns selected management, enrollment, installation, and update **system processes**. It is not an instruction to apply one new policy indiscriminately to every VPN flow. See [Security](Security.md) for exact scope and server-side requirements.

### Options for implementing VPN

The NetworkExtension framework has extensive support for virtual private networks (VPN). A VPN is a form of network tunnel, where a VPN client uses the public Internet to create a connection to a VPN server and then passes private network traffic over that connection.

VPNs have many different uses. For example, an enterprise might set up a VPN to give remote employees access to enterprise network resources that are not available on the public Internet. Or a consumer wanting to access the Internet from an untrusted network, such as the free Wi-Fi at an airport, might set up VPN to secure their traffic.

The supported operating systems include a number of different VPN APIs, distinguished by the protocols they support:

- Use Personal VPN to create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- Create a Packet tunnel provider to implement a VPN client for a packet-oriented, custom VPN protocol.
- Create an App proxy provider to implement a VPN client for a flow-oriented, custom VPN protocol.

### About Always-on VPN

An Always-on VPN is a managed device configuration, not merely a Personal VPN that reconnects on demand. On supervised iOS/iPadOS devices, the system normally drops traffic while the Always-on tunnel is unavailable, including before it starts during boot. Network-control traffic is excluded, and the profile can define captive-network, application, and service exceptions. Do not describe it as having no possible bypass traffic. See [VPN routing](https://developer.apple.com/documentation/networkextension/routing-your-vpn-network-traffic) and the [`VPN.AlwaysOn` payload](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary).

## Topics

### Wi-Fi management

#### Wi-Fi configuration
- Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.
- [Configuring a Wi-Fi accessory to join a network](https://developer.apple.com/documentation/networkextension/configuring-a-wi-fi-accessory-to-join-a-network) - Associate an iOS device with an accessory's network to deliver network configuration information.

#### Hotspot helper
- [Hotspot helper](https://developer.apple.com/documentation/networkextension/hotspot-helper) - Integrate with hotspot authentication under the special entitlement; use the deployment matrix for newer hotspot-provider targets.
- `NEHotspotHelper` is deprecated in **26.0**, not 27. Its replacement, [`NEHotspotManager`](https://developer.apple.com/documentation/networkextension/nehotspotmanager), manages separate hotspot-evaluation and authentication provider extensions.

### Virtual private networks
- [Routing your VPN network traffic](https://developer.apple.com/documentation/networkextension/routing-your-vpn-network-traffic) - Configure inclusions, exclusions, per-app rules, and Always-on exceptions. Even `includeAllNetworks` has documented system-traffic exceptions.

#### Personal VPN
- [Personal VPN](https://developer.apple.com/documentation/networkextension/personal-vpn) - Configure the built-in IPsec or IKEv2 protocols, not arbitrary legacy protocols such as PPTP or L2TP.

#### Packet tunnel provider
- [Packet tunnel provider](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider) - Forward IP packets through a custom VPN protocol; per-app deployment has separate management requirements.

#### App proxy provider
- [App proxy provider](https://developer.apple.com/documentation/networkextension/app-proxy-provider) - Forward TCP connections and UDP conversations through a flow-oriented custom VPN.

### Network relays

#### Relays
- [Relays](https://developer.apple.com/documentation/networkextension/relays) - Configure built-in proxying for TCP and UDP traffic over HTTP/3 and HTTP/2.

### Content filters

#### Content filter providers
- Create an on-device network content filter.
- [Content filter providers](https://developer.apple.com/documentation/networkextension/content-filter-providers) - Keep inspected user content inside the restrictive data-provider sandbox; the control provider supplies rules without receiving that content.
- [Filtering Network Traffic](https://developer.apple.com/documentation/networkextension/filtering-network-traffic) - Use the Network Extension framework to allow or deny network connections.

### URL filters
- [URL filters](https://developer.apple.com/documentation/networkextension/url-filters) - Available for iOS/macOS 26.0+ provider deployments. The system combines an on-device Bloom filter with private-information-retrieval lookups against the provider's server. Register the configuration in CloudKit Console's Identity & Trust area.
- WebKit and `URLSession` requests participate automatically. A custom loading stack must call the `NEURLFilter` participation API and honor its verdict; do not assume every arbitrary socket request is URL-filtered.

### DNS configurations

#### DNS settings
- [DNS settings](https://developer.apple.com/documentation/networkextension/dns-settings) - Configure DNS-over-TLS or DNS-over-HTTPS; the person must enable the configuration.

#### DNS proxy provider
- [DNS proxy provider](https://developer.apple.com/documentation/networkextension/dns-proxy-provider) - Handle DNS queries using an on-device provider, subject to the provider-deployment requirements.

### Local networking

#### Local push connectivity
- [Local push connectivity](https://developer.apple.com/documentation/networkextension/local-push-connectivity) - Deliver notifications and CallKit alerts on configured restricted networks, rather than granting arbitrary persistent background work. The approved `app-push-provider` entitlement value is required on both app and provider targets.

### App extensions
- **NEAppExtensionConfiguration** - Configuration for NetworkExtension app extensions, introduced in 26.0 on its declared iOS/iPadOS, Catalyst, macOS, and visionOS targets.
### Classes
- [NEVPNIKEv2PPKConfiguration](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration) - Post-quantum pre-shared-key configuration conforming to RFC 8784; iOS/iPadOS/Catalyst/tvOS 18, macOS 15, and visionOS 2 or later.

### Protocols
- **NEAppProxyUDPFlowHandling** - UDP-flow handling protocol introduced in iOS/iPadOS/Catalyst 18, macOS 15, and visionOS 2.

### Structures
- **NETunnelProviderError** - An error that the tunnel provider encounters.
- **NEVPNError** - Information about an error encountered while configuring or using a VPN.

### Variables
- **NERelayClientErrorDomain**

### Enumerations
- **NERelayManagerClientError**
- [NEVPNIKEv2PostQuantumKeyExchangeMethod](https://developer.apple.com/documentation/networkextension/nevpnikev2postquantumkeyexchangemethod) - IKEv2 quantum-secure key-exchange choices introduced in 26.0; separate from pre-shared-key configuration.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NetworkExtension)*

*27 source: [iOS/iPadOS release notes — NetworkExtension and Network Security](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md).*
