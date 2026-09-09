# Local Authentication Embedded UI

Present a standard local authentication view icon in a custom authentication view.

**Supported view:** macOS 12.0+. `LAAuthenticationView` is an AppKit `NSView`, not a UIKit or Catalyst view.

The framework catalog lists additional SDK platforms, but the actual view reference is macOS-only and the public 26.5 SDK explicitly excludes the iOS family. Do not use that catalog listing as permission to embed this component in an iPhone, iPad, or Catalyst app.

## Overview
When you authenticate users with the Local Authentication framework, the framework handles all user interaction by default. If you want to create a custom authentication user interface, build it around an LAAuthenticationView instance. The authentication view displays an icon that users associate with biometric authentication, like the Touch ID icon, and then modifies that icon over time to reflect changes in the authentication state. You can add other text, images, or interactive elements to your custom view as needed.

Attach the view to its `LAContext` before starting policy evaluation. The surrounding UI must explain why authentication is needed, because the component is primarily an icon. Do not infer authorization from the icon alone: handle the context's success, cancellation, and error results.

For all local authentication operations, the system manages the underlying biometric data, but with a local authentication view, you can customize the authentication interface to match the design of your app. At the same time, familiar iconography helps users understand what you are asking from them.

The compact view is designed for supported biometric or companion authentication. Do not assume it can supply a generic password fallback when those mechanisms are unavailable. For a SwiftUI Mac interface, also see `LocalAuthentication.LocalAuthenticationView` (macOS 13+).

## Topics

### The Local Authentication View
- **LAAuthenticationView** - A graphical representation of the state of biometric authentication.

### Reference
- **Local Authentication Embedded UI Data Types**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LocalAuthenticationEmbeddedUI)*
