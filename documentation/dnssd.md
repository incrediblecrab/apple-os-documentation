# dnssd

Discover, publish, and resolve network services on a local area or wide area network.

**Module catalog baselines:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 10.12+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The DNS Service Discovery API helps you to perform three main tasks:

- Registering a service.
- Browsing for services.
- Resolving a service instance to its target host, port, and TXT data.

In support of these main tasks, this API can directly assist you in performing two subsidiary tasks:

- Enumerating domains (finding recommended service domains).
- Updating registrations (changing your DNS registration data dynamically).

For new app discovery code, prefer [Network](Network.md) for Bonjour advertising, browsing, and connections. The **27 SDK deprecates Foundation's `NetService`** in favor of Network framework, so it is no longer the preferred migration target. Use DNS-SD's C API when cross-platform integration or specialized operations, such as resolving a service without connecting, require lower-level control. See [TN3151](https://developer.apple.com/documentation/technotes/tn3151-choosing-the-right-networking-api).

### Permissions, failures, and availability

Local-network privacy applies on iOS/iPadOS 14+, macOS 15+, and visionOS 1+, not tvOS or watchOS. Add `NSLocalNetworkUsageDescription` for an app that needs local-network access, and list the specific Bonjour service types it registers or browses in `NSBonjourServices`. On iOS/iPadOS/visionOS, working with arbitrary service types or browsing all advertised types additionally requires `com.apple.developer.networking.multicast`; ordinary declared-service discovery does not require that additional entitlement.

Permission may be denied before a pending prompt is answered. Handle `kDNSServiceErr_PolicyDenied`, cancellation, and retry without treating an empty result set as proof that no services exist. The person can later change access in Settings. [TN3179](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy) describes macOS exemptions, extension behavior, and physical-device testing.

The module's catalog minimum is not a guarantee that every listed constant or operation is available there. For example, `DNSServiceAAAAPolicy` begins at iOS/iPadOS/tvOS 15, macOS 12, and watchOS 8. watchOS also restricts low-level Bonjour networking to the supported circumstances in [TN3135](https://developer.apple.com/documentation/technotes/tn3135-low-level-networking-on-watchos).

## Topics

### Reference
- [DNS Service Discovery C](https://developer.apple.com/documentation/dnssd/dns-service-discovery-c) - Header-level C API documentation.
- [dnssd Enumerations](https://developer.apple.com/documentation/dnssd/dnssd-enumerations)
- [dnssd Functions](https://developer.apple.com/documentation/dnssd/dnssd-functions)
- [dnssd Data Types](https://developer.apple.com/documentation/dnssd/dnssd-data-types)
- [dnssd Constants](https://developer.apple.com/documentation/dnssd/dnssd-constants)

### Variables

These are read-only imported SDK constants, not mutable configuration variables. Use each flag only in the operations documented for it. In particular, `kDNSServiceFlagsPrivateOne` through `kDNSServiceFlagsPrivateFive` are explicitly private and must not be used, despite appearing in the public header and generated catalog.

- `var kDNSServiceAAAAPolicyFallback: DNSServiceAAAAPolicy`
- `var kDNSServiceAAAAPolicyNone: DNSServiceAAAAPolicy`
- `var kDNSServiceClass_IN: Int`
- `var kDNSServiceErr_AlreadyRegistered: Int`
- `var kDNSServiceErr_BadFlags: Int`
- `var kDNSServiceErr_BadInterfaceIndex: Int`
- `var kDNSServiceErr_BadKey: Int`
- `var kDNSServiceErr_BadParam: Int`
- `var kDNSServiceErr_BadReference: Int`
- `var kDNSServiceErr_BadSig: Int`
- `var kDNSServiceErr_BadState: Int`
- `var kDNSServiceErr_BadTime: Int`
- `var kDNSServiceErr_DefunctConnection: Int`
- `var kDNSServiceErr_DoubleNAT: Int`
- `var kDNSServiceErr_Firewall: Int`
- `var kDNSServiceErr_Incompatible: Int`
- `var kDNSServiceErr_Invalid: Int`
- `var kDNSServiceErr_NATPortMappingDisabled: Int`
- `var kDNSServiceErr_NATPortMappingUnsupported: Int`
- `var kDNSServiceErr_NATTraversal: Int`
- `var kDNSServiceErr_NameConflict: Int`
- `var kDNSServiceErr_NoAuth: Int`
- `var kDNSServiceErr_NoError: Int`
- `var kDNSServiceErr_NoMemory: Int`
- `var kDNSServiceErr_NoRouter: Int`
- `var kDNSServiceErr_NoSuchKey: Int`
- `var kDNSServiceErr_NoSuchName: Int`
- `var kDNSServiceErr_NoSuchRecord: Int`
- `var kDNSServiceErr_NotInitialized: Int`
- `var kDNSServiceErr_NotPermitted: Int`
- `var kDNSServiceErr_PolicyDenied: Int`
- `var kDNSServiceErr_PollingMode: Int`
- `var kDNSServiceErr_Refused: Int`
- `var kDNSServiceErr_ServiceNotRunning: Int`
- `var kDNSServiceErr_StaleData: Int`
- `var kDNSServiceErr_Timeout: Int`
- `var kDNSServiceErr_Transient: Int`
- `var kDNSServiceErr_Unknown: Int`
- `var kDNSServiceErr_Unsupported: Int`
- `var kDNSServiceFlagAnsweredFromCache: UInt32`
- `var kDNSServiceFlagsAdd: UInt32`
- `var kDNSServiceFlagsAllowExpiredAnswers: UInt32`
- `var kDNSServiceFlagsAllowRemoteQuery: UInt32`
- `var kDNSServiceFlagsAutoTrigger: UInt32`
- `var kDNSServiceFlagsBackgroundTrafficClass: UInt32`
- `var kDNSServiceFlagsBogus: UInt32`
- `var kDNSServiceFlagsBrowseDomains: UInt32`
- `var kDNSServiceFlagsDefault: UInt32`
- `var kDNSServiceFlagsEnableDNSSEC: UInt32`
- `var kDNSServiceFlagsExpiredAnswer: UInt32`
- `var kDNSServiceFlagsForce: UInt32`
- `var kDNSServiceFlagsForceMulticast: UInt32`
- `var kDNSServiceFlagsIncludeAWDL: UInt32`
- `var kDNSServiceFlagsIncludeP2P: UInt32`
- `var kDNSServiceFlagsIndeterminate: UInt32`
- `var kDNSServiceFlagsInsecure: UInt32`
- `var kDNSServiceFlagsKnownUnique: UInt32`
- `var kDNSServiceFlagsLongLivedQuery: UInt32`
- `var kDNSServiceFlagsMoreComing: UInt32`
- `var kDNSServiceFlagsNoAutoRename: UInt32`
- `var kDNSServiceFlagsPrivateFive: UInt32`
- `var kDNSServiceFlagsPrivateFour: UInt32`
- `var kDNSServiceFlagsPrivateOne: UInt32`
- `var kDNSServiceFlagsPrivateThree: UInt32`
- `var kDNSServiceFlagsPrivateTwo: UInt32`
- `var kDNSServiceFlagsQueueRequest: UInt32`
- `var kDNSServiceFlagsRegistrationDomains: UInt32`
- `var kDNSServiceFlagsReturnIntermediates: UInt32`
- `var kDNSServiceFlagsSecure: UInt32`
- `var kDNSServiceFlagsShareConnection: UInt32`
- `var kDNSServiceFlagsShared: UInt32`
- `var kDNSServiceFlagsSuppressUnusable: UInt32`
- `var kDNSServiceFlagsThresholdFinder: UInt32`
- `var kDNSServiceFlagsThresholdOne: UInt32`
- `var kDNSServiceFlagsThresholdReached: UInt32`
- `var kDNSServiceFlagsTimeout: UInt32`
- `var kDNSServiceFlagsUnicastResponse: UInt32`
- `var kDNSServiceFlagsUnique: UInt32`
- `var kDNSServiceFlagsValidate: UInt32`
- `var kDNSServiceFlagsValidateOptional: UInt32`
- `var kDNSServiceFlagsWakeOnResolve: UInt32`
- `var kDNSServiceFlagsWakeOnlyService: UInt32`
- `var kDNSServiceProtocol_IPv4: Int`
- `var kDNSServiceProtocol_IPv6: Int`
- `var kDNSServiceProtocol_TCP: Int`
- `var kDNSServiceProtocol_UDP: Int`
- `var kDNSServiceType_A: Int`
- `var kDNSServiceType_A6: Int`
- `var kDNSServiceType_AAAA: Int`
- `var kDNSServiceType_AFSDB: Int`
- `var kDNSServiceType_ANY: Int`
- `var kDNSServiceType_APL: Int`
- `var kDNSServiceType_ATMA: Int`
- `var kDNSServiceType_AXFR: Int`
- `var kDNSServiceType_CERT: Int`
- `var kDNSServiceType_CNAME: Int`
- `var kDNSServiceType_DHCID: Int`
- `var kDNSServiceType_DNAME: Int`
- `var kDNSServiceType_DNSKEY: Int`
- `var kDNSServiceType_DS: Int`
- `var kDNSServiceType_EID: Int`
- `var kDNSServiceType_GID: Int`
- `var kDNSServiceType_GPOS: Int`
- `var kDNSServiceType_HINFO: Int`
- `var kDNSServiceType_HIP: Int`
- `var kDNSServiceType_HTTPS: Int`
- `var kDNSServiceType_IPSECKEY: Int`
- `var kDNSServiceType_ISDN: Int`
- `var kDNSServiceType_IXFR: Int`
- `var kDNSServiceType_KEY: Int`
- `var kDNSServiceType_KX: Int`
- `var kDNSServiceType_LOC: Int`
- `var kDNSServiceType_MAILA: Int`
- `var kDNSServiceType_MAILB: Int`
- `var kDNSServiceType_MB: Int`
- `var kDNSServiceType_MD: Int`
- `var kDNSServiceType_MF: Int`
- `var kDNSServiceType_MG: Int`
- `var kDNSServiceType_MINFO: Int`
- `var kDNSServiceType_MR: Int`
- `var kDNSServiceType_MX: Int`
- `var kDNSServiceType_NAPTR: Int`
- `var kDNSServiceType_NIMLOC: Int`
- `var kDNSServiceType_NS: Int`
- `var kDNSServiceType_NSAP: Int`
- `var kDNSServiceType_NSAP_PTR: Int`
- `var kDNSServiceType_NSEC: Int`
- `var kDNSServiceType_NSEC3: Int`
- `var kDNSServiceType_NSEC3PARAM: Int`
- `var kDNSServiceType_NULL: Int`
- `var kDNSServiceType_NXT: Int`
- `var kDNSServiceType_OPT: Int`
- `var kDNSServiceType_PTR: Int`
- `var kDNSServiceType_PX: Int`
- `var kDNSServiceType_RP: Int`
- `var kDNSServiceType_RRSIG: Int`
- `var kDNSServiceType_RT: Int`
- `var kDNSServiceType_SIG: Int`
- `var kDNSServiceType_SINK: Int`
- `var kDNSServiceType_SOA: Int`
- `var kDNSServiceType_SPF: Int`
- `var kDNSServiceType_SRV: Int`
- `var kDNSServiceType_SSHFP: Int`
- `var kDNSServiceType_SVCB: Int`
- `var kDNSServiceType_TKEY: Int`
- `var kDNSServiceType_TSIG: Int`
- `var kDNSServiceType_TXT: Int`
- `var kDNSServiceType_UID: Int`
- `var kDNSServiceType_UINFO: Int`
- `var kDNSServiceType_UNSPEC: Int`
- `var kDNSServiceType_WKS: Int`
- `var kDNSServiceType_X25: Int`

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/dnssd)*
