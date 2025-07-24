# CFNetwork

Access network services and handle changes in network configurations. Build on abstractions of network protocols to simplify tasks such as working with BSD sockets, administering HTTP and FTP servers, and managing Bonjour services.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+

## Topics

### Errors
- **CFNetworkErrors** - This enumeration contains error codes returned under the error domain kCFErrorDomainCFNetwork.
- [Error Dictionary Keys](https://developer.apple.com/documentation/cfnetwork/error_dictionary_keys) - Networking-related keys that may be available in a CFErrorRef object's userInfo dictionary.
- [Error Domains](https://developer.apple.com/documentation/cfnetwork/error_domains) - High-level error domains.

### Hosts
- **CFHost** - An opaque reference representing an CFHost object.
- **CFHostInfoType** - Values indicating the type of data that is to be resolved or the type of data that was resolved.
- **CFHostClientContext** - A structure containing user-defined data and callbacks for CFHost objects.
- **CFHostCancelInfoResolution** - Cancels the resolution of a host.

#### Deprecated
- **CFHostCreateCopy** - Creates a new host object by copying.
- **CFHostCreateWithAddress** - Uses an address to create an instance of a host object.
- **CFHostCreateWithName** - Uses a name to create an instance of a host object.
- **CFHostGetAddressing** - Gets the addresses from a host.
- **CFHostGetNames** - Gets the names from a CFHost.
- **CFHostGetReachability** - Gets reachability information from a host.
- **CFHostGetTypeID** - Gets the Core Foundation type identifier for the CFHost opaque type.
- **CFHostScheduleWithRunLoop** - Schedules a CFHost on a run loop.
- **CFHostSetClient** - Associates a client context and a callback function with a CFHost object or disassociates a client context and callback function that were previously set.
- **CFHostStartInfoResolution** - Starts resolution for a host object.
- **CFHostUnscheduleFromRunLoop** - Unschedules a CFHost from a run loop.

### Global Proxy Configuration
- **CFNetworkCopyProxiesForURL** - Returns the list of proxies that should be used to download a given URL.
- **CFNetworkCopyProxiesForAutoConfigurationScript** - Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- **CFNetworkExecuteProxyAutoConfigurationScript** - Downloads a proxy autoconfiguration script and executes it.
- **CFNetworkExecuteProxyAutoConfigurationURL** - Downloads a proxy autoconfiguration script and executes it.
- **CFNetworkCopySystemProxySettings** - Returns a CFDictionary containing the current systemwide internet proxy settings.
- **CFProxyAutoConfigurationResultCallback** - Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](https://developer.apple.com/documentation/cfnetwork/property_keys) - Keys for calls to property get/set functions such as CFReadStreamSetProperty(_:_:_:) and CFReadStreamCopyProperty(_:_:).
- [Proxy Types](https://developer.apple.com/documentation/cfnetwork/proxy_types) - Constants that specify the type of proxy.
- [Global Proxy Settings Constants](https://developer.apple.com/documentation/cfnetwork/global_proxy_settings_constants) - Constants for keys in the global proxy settings dictionary returned by CFNetworkCopySystemProxySettings().

### HTTP Authentication
- **CFHTTPAuthentication** - An opaque reference representing HTTP authentication information.
- **CFHTTPAuthenticationAppliesToRequest** - Returns a Boolean value that indicates whether a CFHTTPAuthentication object is associated with a CFHTTPMessage object.
- **CFHTTPAuthenticationCopyDomains** - Returns an array of domain URLs to which a given CFHTTPAuthentication object can be applied.
- **CFHTTPAuthenticationCopyMethod** - Gets the strongest authentication method that will be used when a CFHTTPAuthentication object is applied to a request.
- **CFHTTPAuthenticationCopyRealm** - Gets an authentication information's namespace.
- **CFHTTPAuthenticationCreateFromResponse** - Uses an authentication failure response to create a CFHTTPAuthentication object.
- **CFHTTPAuthenticationGetTypeID** - Gets the Core Foundation type identifier for the CFHTTPAuthentication opaque type.
- **CFHTTPAuthenticationIsValid** - Returns a Boolean value that indicates whether a CFHTTPAuthentication object is valid.
- **CFHTTPAuthenticationRequiresAccountDomain** - Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires an account domain.
- **CFHTTPAuthenticationRequiresOrderedRequests** - Returns a Boolean value that indicates whether authentication requests should be made one at a time.
- **CFHTTPAuthenticationRequiresUserNameAndPassword** - Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires a username and a password.
- **kCFHTTPAuthenticationAccountDomain** - Account domain to use for authentication.
- **kCFHTTPAuthenticationPassword** - Password to use for authentication.
- **kCFHTTPAuthenticationSchemeBasic** - Request the HTTP basic authentication scheme.
- **kCFHTTPAuthenticationSchemeDigest** - Request the HTTP digest authentication scheme.
- **kCFHTTPAuthenticationSchemeKerberos** - Request the HTTP Kerberos authentication scheme.
- **kCFHTTPAuthenticationSchemeNTLM** - Request the HTTP NTLM authentication scheme.
- **kCFHTTPAuthenticationSchemeNegotiate** - Request the HTTP Negotiate authentication scheme.
- **kCFHTTPAuthenticationSchemeNegotiate2** - Request the HTTP Negotiate v2 authentication scheme.
- **kCFHTTPAuthenticationSchemeXMobileMeAuthToken** - Request the HTTP XMobileMeAuthToken authentication scheme.
- **kCFHTTPAuthenticationUsername** - Username to use for authentication.

### HTTP Messages
- **CFHTTPMessage** - An opaque reference representing an HTTP message.
- **CFHTTPMessageAddAuthentication** - Adds authentication information to a request.
- **CFHTTPMessageAppendBytes** - Appends data to a CFHTTPMessage object.
- **CFHTTPMessageApplyCredentialDictionary** - Use a dictionary containing authentication credentials to perform the authentication method specified by a CFHTTPAuthentication object.
- **CFHTTPMessageApplyCredentials** - Performs the authentication method specified by a CFHTTPAuthentication object.
- **CFHTTPMessageCopyAllHeaderFields** - Gets all header fields from a CFHTTPMessage object.
- **CFHTTPMessageCopyBody** - Gets the body from a CFHTTPMessage object.
- **CFHTTPMessageCopyHeaderFieldValue** - Gets the value of a header field from a CFHTTPMessage object.
- **CFHTTPMessageCopyRequestMethod** - Gets the request method from a CFHTTPMessage object.
- **CFHTTPMessageCopyRequestURL** - Gets the URL from a CFHTTPMessage object.
- **CFHTTPMessageCopyResponseStatusLine** - Gets the status line from a CFHTTPMessage object.
- **CFHTTPMessageCopySerializedMessage** - Serializes a CFHTTPMessage object.
- **CFHTTPMessageCopyVersion** - Gets the HTTP version from a CFHTTPMessage object.
- **CFHTTPMessageCreateCopy** - Gets a copy of a CFHTTPMessage object.
- **CFHTTPMessageCreateEmpty** - Creates and returns a new, empty CFHTTPMessage object.
- **CFHTTPMessageCreateRequest** - Creates and returns a CFHTTPMessage object for an HTTP request.
- **CFHTTPMessageCreateResponse** - Creates and returns a CFHTTPMessage object for an HTTP response.
- **CFHTTPMessageGetResponseStatusCode** - Gets the status code from a CFHTTPMessage object representing an HTTP response.
- **CFHTTPMessageGetTypeID** - Returns the Core Foundation type identifier for the CFHTTPMessage opaque type.
- **CFHTTPMessageIsHeaderComplete** - Determines whether a message header is complete.
- **CFHTTPMessageIsRequest** - Returns a Boolean indicating whether the HTTP message is a request or a response.
- **CFHTTPMessageSetBody** - Sets the body of a CFHTTPMessage object.
- **CFHTTPMessageSetHeaderFieldValue** - Sets the value of a header field in an HTTP message.
- **kCFHTTPVersion1_0** - Specifies HTTP version 1.0.
- **kCFHTTPVersion1_1** - Specifies HTTP version 1.1.
- **kCFHTTPVersion2_0** - HTTP version 2.0.

### FTP (Deprecated)
- **CFFTPCreateParsedResourceListing** - Parses an FTP listing to a dictionary.
- **kCFFTPResourceGroup** - CFDictionary key for getting the CFString containing the name of a group that shares the FTP resource.
- **kCFFTPResourceLink** - CFDictionary key for getting the CFString containing the symbolic link information. If the item is a symbolic link, the CFString contains the path to the item that the link references.
- **kCFFTPResourceModDate** - CFDictionary key for getting the CFDate containing the last date and time the FTP resource was modified.
- **kCFFTPResourceMode** - CFDictionary key for getting the CFNumber containing the access permissions, defined in sys/types.h, of the FTP resource.
- **kCFFTPResourceName** - CFDictionary key for getting the CFString containing the name of the FTP resource.
- **kCFFTPResourceOwner** - CFDictionary key for getting the CFString containing the name of the owner of the FTP resource.
- **kCFFTPResourceSize** - CFDictionary key for getting the CFNumber containing the size in bytes of the FTP resource.
- **kCFFTPResourceType** - CFDictionary key for getting the CFNumber containing the type of the FTP resource as defined in sys/dirent.h.

### Network Diagnostics (Deprecated)
- **CFNetDiagnostic** - An opaque reference representing a CFNetDiagnostic.
- **CFNetDiagnosticStatusValues** - Constants for diagnostic status values.
- **CFNetDiagnosticCopyNetworkStatusPassively** - Gets a network status value.
- **CFNetDiagnosticCreateWithStreams** - Creates a network diagnostic object from a pair of CFStreams.
- **CFNetDiagnosticCreateWithURL** - Creates a CFNetDiagnosticRef from a CFURLRef.
- **CFNetDiagnosticDiagnoseProblemInteractively** - Opens a Network Diagnostics window.
- **CFNetDiagnosticSetName** - Overrides the displayed application name.

### Network Services (Deprecated)
- **CFNetService** - An opaque reference representing a CFNetService.
- **CFNetServiceBrowser** - An opaque reference representing a CFNetServiceBrowser.
- **CFNetServiceBrowserFlags** - Flags that the system passes to net service browser callbacks.
- **CFNetServiceMonitor** - An opaque reference for a service monitor.
- **CFNetServiceMonitorType** - Record type specifier used to tell a service monitor the type of record changes to watch for.
- **CFNetServiceClientContext** - A structure provided when a CFNetService is associated with a callback function or when a CFNetServiceBrowser is created.
- **CFNetServiceRegisterFlags** - Options to use when registering a service on the network.
- **CFNetServicesError** - Error codes that may be returned by CFNetServices functions or passed to CFNetServices callback functions.

### Streams
- **CFReadStreamCreateForHTTPRequest** (Deprecated) - Creates a read stream for a CFHTTP request message.
- **CFReadStreamCreateForStreamedHTTPRequest** (Deprecated) - Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.
- **kCFStreamPropertyHTTPFinalRequest** (Deprecated) - HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set.
- **kCFStreamPropertyHTTPFinalURL** (Deprecated) - HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set.
- **kCFStreamPropertyHTTPResponseHeader** (Deprecated) - HTTP Response Header property. When copied by CFReadStreamCopyProperty(_:_:), the header of an HTTP response message is returned.
- **kCFStreamPropertyHTTPShouldAutoredirect** (Deprecated) - HTTP Should Auto Redirect property. Set this property to kCFBooleanTrue to enable autoredirection; set this property to kCFBooleanFalse to disable autoredirection.
- **CFWriteStreamCreateWithFTPURL** (Deprecated) - Creates an FTP write stream.
- **CFReadStreamCreateWithFTPURL** (Deprecated) - Creates an FTP read stream.
- **kCFStreamPropertyFTPFileTransferOffset** (Deprecated) - FTP File Transfer Offset stream property key for set and copy operations. The value of this property is a CFNumber of type kCFNumberLongLongType representing the file offset at which to start the transfer.
- **kCFStreamPropertyFTPPassword** (Deprecated) - FTP Password stream property key for set and copy operations. A value of type CFString for storing the login password. Don't set this property when anonymous FTP is desired.
- **kCFStreamPropertyFTPProxy** (Deprecated) - FTP Proxy stream property key for set and copy operations. The property is a value of type CFDictionary that holds proxy dictionary key-value pairs. The dictionary returned by SystemConfiguration can also be set as the value of this property.
- **kCFStreamPropertyFTPResourceSize** (Deprecated) - FTP Resource Size read stream property key copy operations. This property stores a CFNumber of type kCFNumberLongLongType representing the size of a resource in bytes.
- **kCFStreamPropertyFTPUsePassiveMode** (Deprecated) - FTP Passive Mode stream property key for set and copy operations. Set this property to kCFBooleanTrue to enable passive mode; set this property to kCFBooleanFalse to disable passive mode.
- **kCFStreamPropertyFTPUserName** (Deprecated) - FTP User Name stream property key for set and copy operations. A value of type CFString for storing the login user name. Don't set this property when anonymous FTP is desired.
- **CFSocketStreamSOCKSGetError** - This function gets error codes in the kCFStreamErrorDomainSOCKS domain from the CFStreamError returned by a stream operation.
- **CFSocketStreamSOCKSGetErrorSubdomain** - Gets the error subdomain associated with errors in the kCFStreamErrorDomainSOCKS domain from the CFStreamError returned by a stream operation.
- **CFStreamCreatePairWithSocketToCFHost** (Deprecated) - Creates readable and writable streams connected to a given CFHost object.
- **CFStreamCreatePairWithSocketToNetService** (Deprecated) - Creates a pair of streams for a CFNetService.
- **kCFStreamNetworkServiceType** - The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See Stream Service Types for a list of possible values.
- **kCFStreamNetworkServiceTypeBackground** - Specifies that the stream is a background download.
- **kCFStreamNetworkServiceTypeCallSignaling** - A call signaling service.
- **kCFStreamNetworkServiceTypeVideo** - Specifies that the stream is providing interactive video data.
- **kCFStreamNetworkServiceTypeVoIP** (Deprecated) - Specifies that the stream is providing VoIP service.
- **kCFStreamNetworkServiceTypeVoice** - Specifies that the stream is providing interactive voice data.
- **kCFStreamErrorDomainFTP** - The error code is an FTP error code.
- **kCFStreamErrorDomainHTTP** - The error code is an HTTP error code.
- **kCFStreamErrorDomainMach** - The error code is a Mach error code defined in mach/error.h.
- **kCFStreamErrorDomainNetDB** - The error code is an error code defined in netdb.h.
- **kCFStreamErrorDomainNetServices** - The error code is a CFNetService error code. For details, see the CFNetServicesError enumeration.
- **kCFStreamErrorDomainSOCKS** - The error code is a SOCKS proxy error.
- **kCFStreamErrorDomainSSL** - The error code is an SSL error code as defined in `Security/SecureTransport.h`.
- **kCFStreamErrorDomainSystemConfiguration** - The error code is a system configuration error code as defined in System/ConfigurationSystemConfiguration.h.
- **kCFStreamErrorDomainWinSock** - When running CFNetwork code on Windows, this domain returns error codes associated with the underlying TCP/IP stack. You should also note that non-networking errors such as ENOMEM are delivered through the POSIX domain. See the header winsock2.h for relevant error codes.
- **kCFStreamPropertyConnectionIsCellular** - A boolean value indicating whether the stream is connected over a cellular (WWAN) interface. This is a read-only property, and is false until the connection has been established.
- **kCFStreamPropertyNoCellular** - A Boolean value indicating that the connection should not be established over a cellular (WWAN) connection. This value can only be set before you open the stream.
- **kCFStreamPropertyProxyLocalBypass** - Proxy Local Bypass property key.
- **kCFStreamPropertySOCKSPassword** - Constant for the key required to set a user's password.
- **kCFStreamPropertySOCKSProxy** - SOCKS proxy property key.
- **kCFStreamPropertySOCKSProxyHost** - Constant for the SOCKS proxy host key.
- **kCFStreamPropertySOCKSProxyPort** - Constant for the SOCKS proxy host port key.
- **kCFStreamPropertySOCKSUser** - Constant for the key required to set a user name.
- **kCFStreamPropertySOCKSVersion** - Constant for the SOCKS version key.
- **kCFStreamPropertySSLContext**
- **kCFStreamPropertySSLPeerCertificates** - SSL Peer Certificates property key for copy operations, which return a CFArray object containing SecCertificateRef objects.
- **kCFStreamPropertySSLPeerTrust** - SSL Peer Trust property key for copy operations, which return a SecTrustRef object containing the result of the SSL handshake.
- **kCFStreamPropertySSLSettings** - SSL Settings property key for set operations.
- **kCFStreamPropertyShouldCloseNativeSocket** - Should Close Native Socket property key.
- **kCFStreamPropertySocketExtendedBackgroundIdleMode** - A Boolean value to request that the system keep a socket open and delays reclaiming it when the process moves to the background.
- **kCFStreamPropertySocketRemoteHost** - The key's value is a CFHostRef for the remote host if it is known. If not, its value is NULL.
- **kCFStreamPropertySocketRemoteNetService** - The key's value is a CFNetServiceRef for the remote network service if it is known. If not, its value is NULL.
- **kCFStreamPropertySocketSecurityLevel** - Socket Security Level property key.
- **kCFStreamSSLAllowsAnyRoot** - Security property key whose value indicates whether root certificates should be allowed.
- **kCFStreamSSLAllowsExpiredCertificates** - Security property key whose value indicates whether expired certificates are allowed.
- **kCFStreamSSLAllowsExpiredRoots** - Security property whose value indicates whether expired root certificates are allowed.
- **kCFStreamSSLCertificates** - Security property key whose value is a CFArray of SecCertificateRefs except for the first element in the array, which is a SecIdentityRef.
- **kCFStreamSSLIsServer** - Security property key whose value indicates whether the connection is to act as a server in the SSL process.
- **kCFStreamSSLLevel** - Security property key whose value specifies the stream's security level.
- **kCFStreamSSLPeerName** - Security property key whose value overrides the name used for certificate verification.
- **kCFStreamSSLValidatesCertificateChain** - Security property key whose value indicates whether the certificate chain should be validated.
- **kCFStreamSocketSOCKSVersion4** - Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- **kCFStreamSocketSOCKSVersion5** - Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- **kCFStreamSocketSecurityLevelNegotiatedSSL** - Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.
- **kCFStreamSocketSecurityLevelNone** - Specifies that no security level be set.
- **kCFStreamSocketSecurityLevelSSLv2** (Deprecated) - Specifies that SSL version 2 be set as the security protocol for a socket stream.
- **kCFStreamSocketSecurityLevelSSLv3** (Deprecated) - Specifies that SSL version 3 be set as the security protocol for a socket stream pair.
- **kCFStreamSocketSecurityLevelTLSv1** - Specifies that TLS version 1 be set as the security protocol for a socket stream.
- **CFStreamErrorHTTP** - Error codes that a read stream for an HTTP request may return.
- **CFStreamErrorHTTPAuthentication** - Authentication error codes that may be returned when trying to apply authentication to a request.
- [Secure Sockets (SOCKS) Errors](https://developer.apple.com/documentation/cfnetwork/secure_sockets_socks_errors) - Error codes returned by the kCFStreamErrorDomainSOCKS error domain.

### Reference
- [CFNetwork Data Types](https://developer.apple.com/documentation/cfnetwork/cfnetwork_data_types) - Callback types for various network services.
- [CFNetwork Enumerations](https://developer.apple.com/documentation/cfnetwork/cfnetwork_enumerations) - Enumerated values related to SOCKS.
- [CFNetwork Constants](https://developer.apple.com/documentation/cfnetwork/cfnetwork_constants) - Constants for use with CFNetwork.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CFNetwork)*