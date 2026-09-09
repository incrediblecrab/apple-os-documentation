# System Configuration

Inspect network configuration settings and observe changes to system networking state.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.1+ | tvOS 9.0+ | visionOS 1.0+

## Overview

System Configuration provides network-configuration interfaces and legacy synchronous and asynchronous reachability APIs. Reachability means that a packet can leave the local device; it does not guarantee that the destination receives it or that a service request succeeds.

Apple deprecates the [SCNetworkReachability functions](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachability-g7d). Do not use them to preflight a connection. Attempt the connection and handle its state or errors; `URLSessionConfiguration.waitsForConnectivity` and Network framework connection-state handling support waiting for connectivity. This deprecation does not deprecate the entire System Configuration framework.

## Topics

### Reference
- **DHCPClientPreferences**
- **SCDynamicStore**
- **SCDynamicStoreCopyDHCPInfo**
- **SCDynamicStoreCopySpecific**
- **SCDynamicStoreKey**
- **SCNetwork**
- **SCNetworkConfiguration**
- **SCNetworkConnection**
- **SCNetworkReachability**
- **SCPreferences**
- **SCPreferencesPath**
- **SCPreferencesSetSpecific**
- **SCSchemaDefinitions**
- **System Configuration**
- **SystemConfiguration Enumerations**
- **SystemConfiguration Constants**
- **SystemConfiguration Functions**
- **SystemConfiguration Data Types**

### Entitlements
- **Access Wi-Fi Information Entitlement** - A Boolean value indicating whether your app can access information about the connected Wi-Fi network

### Type Aliases
- **AuthorizationRef**

### See Also
- [System Configuration Programming Guidelines](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/SystemConfigFrameworks/SC_Intro/SC_Intro.html)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SystemConfiguration)*
