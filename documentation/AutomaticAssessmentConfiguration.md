# Automatic Assessment Configuration

Enter single-app mode and prevent students from accessing specific system features while taking an exam.

**Platforms:** iOS 13.4+ | iPadOS 13.4+ | Mac Catalyst 13.4+ | macOS 10.15.4+

## Overview

Use the AutomaticAssessmentConfiguration framework to create an assessment session that limits access to system features. The session prevents a user from using the device to retrieve information beyond that which your app provides, or distributing sensitive information from within your app. This limited access helps you protect the integrity of an assessment, like an exam, conducted by your app.

Apps that use the AutomaticAssessmentConfiguration framework must have the com.apple.developer.automatic-assessment-configuration entitlement. With the entitlement set, use an instance of the AEAssessmentSession class to start and stop assessment sessions.

A session provides protections by preventing access to desktop elements like:
- The Dock
- The Application Menu Bar
- Mission Control
- Notification Center
- Spaces other than the current one
- Other apps, except those that you selectively allow

Additionally, a session:
- Prevents screen recording and screen capture
- Disables Siri
- Stops media playing
- Allows network access for only your app
- Disables Handoff
- Clears the pasteboard buffer when starting and stopping the session

> **Note:** If you publish an educational app that delivers exams to students, you can request permission to use the com.apple.developer.automatic-assessment-configuration entitlement by filling in the Automatic Assessment Configuration Entitlement Request form.

The framework reports an error if you try to start an assessment from an app running in visionOS.

## Topics

### Essentials
- **com.apple.developer.automatic-assessment-configuration** - A Boolean value that indicates whether an app may create an assessment session.

### Sessions
- [Preparing an educational assessment app for distribution](https://developer.apple.com/documentation/automaticassessmentconfiguration/preparing_an_educational_assessment_app_for_distribution) - Ensure your app maintains academic integrity by reviewing assessment practices and managing system capabilities.
- [Build an Educational Assessment App](https://developer.apple.com/documentation/automaticassessmentconfiguration/build_an_educational_assessment_app) - Ensure the academic integrity of your assessment app by using Automatic Assessment Configuration.
- **AEAssessmentConfiguration** - Configuration information for an assessment session.
- **AEAssessmentSession** - A session that your app uses to protect an assessment.

### Errors
- **AEAssessmentError** - Errors issued by an assessment session to its delegate.
- **Code** - Error codes that the framework returns if a session fails.
- **AEAssessmentErrorDomain** - A constant representing the error domain that the framework uses when issuing errors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration)*