# System Configuration

Allow applications to access a device's network configuration settings. Determine the reachability of the device, such as whether Wi-Fi or cell connectivity are active.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.1+ | tvOS 9.0+ | visionOS 1.0+

## Overview

This collection of documents describes the programming interfaces of the System Configuration framework. The System Configuration framework provides functions that determine the reachability of target hosts in both a synchronous and an asynchronous manner. It also provides error detection facilities.

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
- [System Configuration Programming Guidelines](https://developer.apple.com/documentation/systemconfiguration/system_configuration_programming_guidelines)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SystemConfiguration)*