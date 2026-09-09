# App Clips

Offer focused app functionality or a demo without requiring installation of the full app.

**Platforms:** iOS 14.0+ | iPadOS 14.0+

## Overview

An App Clip delivers a focused part of its corresponding app, such as placing an order or trying a game. People invoke it through configured links, codes, and other supported surfaces; discovery and download are not instantaneous-delivery guarantees.

Demo experiences have additional size and invocation rules. Check the [current constraints](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip) rather than assuming the largest allowance applies to every supported OS or invocation. At an appropriate point, your app can recommend the full app using `SKOverlay` or SwiftUI's App Store overlay; an arbitrary completed task doesn't automatically create that prompt.

### Offer a great user experience

Keep the task self-contained; don't require installation of the full app to finish it. App Clips don't appear as full apps on the Home Screen, and the system may remove them after inactivity. Don't assume their local data persists indefinitely.

For design guidance, see the [App Clips HIG](https://developer.apple.com/design/human-interface-guidelines/app-clips).

### Review App Clip creation

Limit the function of an App Clip to ensure a fast launch experience, protect user privacy, and preserve resources for in-the-moment experiences and demo versions of your app. Before you create an App Clip:

- Review technology available to App Clips and constraints that ensure a good user experience.
- Identify which of your app's functionalities might make a great App Clip.
- Learn how people discover and launch App Clips with invocations and how you configure App Clip experiences and use invocation URLs to offer a great launch experience.

For more information, refer to Choosing the right functionality for your App Clip and Configuring App Clip experiences.

Each full app has one App Clip target, which can serve multiple experiences. The full app must include the App Clip's functionality and handle its invocations after installation replaces the App Clip. Handle launches without an invocation URL, including returns from notifications.

Framework importability doesn't establish runtime support inside an App Clip. Review unavailable frameworks, restricted background work, permissions, and demo-specific exceptions before sharing full-app code.

When you've identified functionality for your App Clip and identified invocations:

- Make changes to your app's Xcode project and your code; for example, add an App Clip target and share code between your App Clip and full app.
- Add code to respond to invocations and to handle invocation URLs.
- Create App Clip experiences in App Store Connect.
- Optionally, associate your App Clip with your website to support additional invocations and advanced App Clip experiences.
- Optionally, create App Clip Codes that offer the best experience for people to discover and launch your App Clip.

## Topics

### Essentials
- [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip) - Review available frameworks and App Clip constraints before choosing features.
- [Configuring App Clip experiences](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip) - Configure invocation URLs and default, demo, or advanced experiences.
- [App Clips updates](https://developer.apple.com/documentation/updates/appclips) - Learn about important changes in App Clips.

### Creation
- [Creating an App Clip with Xcode](https://developer.apple.com/documentation/appclip/creating-an-app-clip-with-xcode) - Add an App Clip target to your Xcode project and share code between the App Clip and its corresponding full app.
- [Fruta: Building a Feature-Rich App with SwiftUI](https://developer.apple.com/documentation/appclip/fruta-building-a-feature-rich-app-with-swiftui) - Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Parent Application Identifiers Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.parent-application-identifiers) - An App Clip's array containing exactly one parent application identifier; iOS/iPadOS 14+.
- [`com.apple.developer.associated-appclip-app-identifiers`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.associated-appclip-app-identifiers) - The full app's one-entry App Clip identifier array, added by Xcode when archiving; its reference lists iOS/iPadOS 15.4+.
- [`com.apple.developer.on-demand-install-capable`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.on-demand-install-capable) - A Boolean applied during signing to identify the App Clip; it needn't appear in the project's source entitlements file.

### Launch
- [Responding to invocations](https://developer.apple.com/documentation/appclip/responding-to-invocations) - Add code to respond to invocations and offer a focused launch experience.
- [Associating your App Clip with your website](https://developer.apple.com/documentation/appclip/associating-your-app-clip-with-your-website) - Configure website association for advanced experiences and support on iOS 16.3 or earlier; generated default links on newer systems have a different workflow.
- [Supporting invocations from your website and the Messages app](https://developer.apple.com/documentation/appclip/supporting-invocations-from-your-website-and-the-messages-app) - Configure website banners/cards and Messages invocations.
- [Confirming a person's physical location](https://developer.apple.com/documentation/appclip/confirming-a-person-s-physical-location) - Check an invocation against an expected region without obtaining the person's precise location.
- [Launching another app's App Clip from your app](https://developer.apple.com/documentation/appclip/launching-another-app-s-app-clip-from-your-app) - Use App Clip links and rich previews from another app.
- [`APActivationPayload`](https://developer.apple.com/documentation/appclip/apactivationpayload) - Launch information carried by `NSUserActivity`. Its Catalyst declaration doesn't establish a native Mac App Clip experience.
- [`NSAppClip`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappclip) - The property-list dictionary for temporary notification and location-confirmation requests.

### App Clip Codes
- [Creating App Clip Codes](https://developer.apple.com/documentation/appclip/creating-app-clip-codes) - Help users discover your App Clip by using an NFC-integrated or scan-only App Clip Code.
- [Encoding a URL in an App Clip Code](https://developer.apple.com/documentation/appclip/encoding-a-url-in-an-app-clip-code) - Choose an invocation URL for your App Clip Code that you can encode efficiently.
- [Preparing multiple App Clip Codes for production](https://developer.apple.com/documentation/appclip/preparing-multiple-app-clip-codes-for-production) - Prepare your App Clip Codes to send to a professional printing service.
- [Interacting with App Clip Codes in AR](https://developer.apple.com/documentation/appclip/interacting-with-app-clip-codes-in-ar) - Display content and provide services in an AR experience with App Clip Codes.

### App Clip to full app transition
- [Recommending your app to App Clip users](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users) - Offer installation with an overlay without preventing completion of the App Clip's task.
- [Sharing data between your App Clip and your full app](https://developer.apple.com/documentation/appclip/sharing-data-between-your-app-clip-and-your-full-app) - Follow the corresponding-app identity, container, defaults, and keychain transition rules. App Clip CloudKit access starts with public-database reads in iOS 16, not public writes or private/shared database access.

### Notifications
- [Enabling notifications in App Clips](https://developer.apple.com/documentation/appclip/enabling-notifications-in-app-clips) - Configure temporary notifications or request explicit permission for longer use; check the person's current authorization.

### Live Activities
- [Offering Live Activities with your App Clip](https://developer.apple.com/documentation/appclip/offering-live-activities-with-your-app-clip) - Add a separate App Clip-only widget extension with the App Clip Extension capability. It may contain Live Activities, not Home Screen, Lock Screen, or Today View widgets. The guide describes the iOS 16 generation; concrete `Activity` APIs require iOS/iPadOS 16.1+.

### Testing
- [Testing the launch experience of your App Clip](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip) - Debug invocations and verify the configuration of your released App Clip.

### Distribution
- [Distributing your App Clip](https://developer.apple.com/documentation/appclip/distributing-your-app-clip) - Archive the corresponding full app and distribute its App Clip through App Store Connect.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppClip)*
