# Automatic Assessment Configuration

Restrict system capabilities during an exam, with platform-specific options for permitted supporting apps.

**Platforms:** iOS 13.4+ | iPadOS 13.4+ | Mac Catalyst 14.0+ | macOS 10.15.4+

## Overview

Use the AutomaticAssessmentConfiguration framework to create an assessment session that limits access to system features according to its configuration. On macOS, configured participants can provide permitted tools alongside the assessment app. These controls help protect an exam but do not replace review of the app's own content, menus, keyboards, and network behavior.

Apps that use the AutomaticAssessmentConfiguration framework must have the com.apple.developer.automatic-assessment-configuration entitlement. With the entitlement set, use an instance of the AEAssessmentSession class to start and stop assessment sessions.

Default session protections can restrict desktop elements such as the following; use the applicable configuration to determine what is permitted:
- The Dock
- The Application Menu Bar
- Mission Control
- Notification Center
- Spaces other than the current one
- Other apps, except those that you selectively allow

Additional default protections include the following, subject to platform-specific exceptions:
- Prevents screen recording and screen capture
- Disables Siri
- Stops media playing
- Restricts network access on macOS to allowed participants and processes working on their behalf
- Disables Handoff
- Clears the pasteboard buffer when starting and stopping the session

For example, [`allowsActivityContinuation`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsactivitycontinuation) can permit Handoff on its supported platforms. [`allowsScreenshots`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsscreenshots), available on macOS and Mac Catalyst 26.1+, permits screenshots copied to the clipboard, not unrestricted screen capture. Configure participating apps' [`allowsNetworkAccess`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/allowsnetworkaccess) rather than assuming network access is always exclusive to the assessment app.

> **Note:** Request permission to use the assessment entitlement through the [Automatic Assessment Configuration Entitlement Request](https://developer.apple.com/contact/request/automatic-assessment-configuration/) form and include the granted entitlement in the provisioning profile. For deployment targets earlier than macOS 11, the [entitlement documentation](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.automatic-assessment-configuration) also requires `com.apple.security.temporary-exception.mach-lookup.global-name` with an array containing `com.apple.assessmentagent`.

The framework reports an error if you try to start an assessment from an app running in visionOS.

## macOS 27 assessment configuration

The [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) describe granular Dock, menu-bar, and accessibility controls, system pre-checks, and app-launch restrictions. This is a platform-specific assessment change, not a blanket expansion of iOS or visionOS support.

For example, [`allowsDock`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsdock) and [`allowsMenuBar`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsmenubar) default to hiding those elements and permit them when explicitly enabled. Their declarations list macOS and Mac Catalyst 27.0. Review [`AEAssessmentConfiguration`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration) for the individual controls instead of assuming every restriction must always be active.

Acquire the assessment entitlement, validate your configuration, and observe [`AEAssessmentSessionDelegate`](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsessiondelegate) callbacks. Keep a strong reference to the session and do not expose protected exam content until `assessmentSessionDidBegin(_:)`. Calling `begin()` returns before protection is established. On interruption, immediately stop the assessment, hide sensitive content, preserve appropriate work, and call `end()`. Wait for `assessmentSessionDidEnd(_:)` before reporting completion.

## Topics

### Essentials
- **com.apple.developer.automatic-assessment-configuration** - A Boolean value that indicates whether an app may create an assessment session.

### Sessions
- [Preparing an educational assessment app for distribution](https://developer.apple.com/documentation/automaticassessmentconfiguration/preparing-an-educational-assessment-app-for-distribution) - Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](https://developer.apple.com/documentation/automaticassessmentconfiguration/build-an-educational-assessment-app) - Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- **AEAssessmentConfiguration** - Configuration information for an assessment session.
- **AEAssessmentSession** - A session that your app uses to protect an assessment.

### Errors
- **AEAssessmentError** - Errors issued by an assessment session to its delegate.
- [**AEAssessmentError.Code**](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code) - Error codes that the framework returns if a session fails.
- **AEAssessmentErrorDomain** - A constant representing the error domain that the framework uses when issuing errors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration)*
