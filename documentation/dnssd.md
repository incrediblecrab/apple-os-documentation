# dnssd

Discover, publish, and resolve network services on a local area or wide area network.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 10.12+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The DNS Service Discovery API helps you to perform three main tasks:

- Registering a service.
- Browsing for services.
- Resolving service names to host names.

In support of these main tasks, this API can directly assist you in performing two subsidiary tasks:

- Enumerating domains (finding recommended service domains).
- Updating registrations (changing your DNS registration data dynamically).

Most apps shouldn't use this API, and instead should use a higher-level service discovery API like NetService. Use dnssd if you're writing BSD-style applications or cross-platform programs that don't need to link to higher-level frameworks. You can also use dnssd if you need specific lower-level functionality exposed by this API.

**Important**: Apps that use the local network must provide a usage string in their Info.plist file with the key NSLocalNetworkUsageDescription. Apps that use Bonjour must also declare the services they browse, using the NSBonjourServices key.

## Topics

### Reference
- **DNS Service Discovery C** - See the Overview section above for header-level documentation.
- **dnssd Enumerations**
- **dnssd Functions**
- **dnssd Data Types**
- **dnssd Constants**

### Variables
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