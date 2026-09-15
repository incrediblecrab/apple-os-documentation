# SensitiveContentAnalysis

Detect sensitive media and provide an appropriate intervention before displaying it.

**Image/file analysis:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | visionOS 2.0+. Video-stream analysis has separate availability below.

## Overview

This framework enables an app to check content for nudity and other supported categories of sensitive material. In iOS and macOS, the Sensitive Content Warning user preference or Communication Safety parental control in Screen Time offer people the option to indicate their desire to guard against unexpected or unwanted exposure. Provide people with the experience they request in these settings by using SensitiveContentAnalysis to check for sensitive content before displaying it.

Consider situations in which your app acquires externally-sourced images or video, and use this framework to check if the media is sensitive. For example, a messaging app checks each image it receives from a contact. A classroom app evaluates uploads from personal devices to a shared location for classwork submission or other classroom activities. A video-conferencing app can use the supported stream-analysis APIs for incoming video.

### Authorization and privacy boundaries

Enable `com.apple.developer.sensitivecontentanalysis.client` through the Sensitive Content Analysis capability. The entitlement reference declares an array of strings, not a Boolean; use the capability's provisioned configuration rather than inventing a value. Apple's integration guide excludes Enterprise development and free accounts.

Before analysis, inspect `SCSensitivityAnalyzer.analysisPolicy`. `.simpleInterventions` reflects Sensitive Content Warning, while `.descriptiveInterventions` reflects Communication Safety and calls for a more explanatory, age-appropriate response. The latter guidance covers both incoming media and intervention before transmitting sensitive media; the adult warning flow need not block unchecked outgoing content.

If the policy is `.disabled`, the app cannot use the framework to detect sensitive content. This can reflect missing entitlement, disabled system settings, or the person turning warnings off for the app. Recheck policy as settings change; do not interpret a disabled analyzer or an analysis error as a clean-content result.

Apple's integration guide explicitly says not to transmit information off-device about whether the framework identified media as sensitive. Keep detection outcomes local rather than turning the API into behavioral reporting. Handle processing delays and failures without prematurely revealing content the app is still checking.

### OS 27: content categories

**Reviewed September 8, 2026:** [`SCSensitivityAnalysis.detectedTypes`](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/detectedtypes) is new in iOS/iPadOS 27.0, Mac Catalyst 27.0, macOS 27.0, and visionOS 27.0. Its `ContentType` values distinguish `.sexuallyExplicit` from `.goreOrViolence`.

The set is populated only when `isSensitive` is `true`. Gate this property separately from the framework's older image-analysis APIs, support multiple detected categories, and retain an `isSensitive`-based path for older systems. A classification is an intervention signal, not an exhaustive judgment about all possible harms.

### Intervene when content is sensitive

If the framework determines that some media contains sensitive content, call the user's attention to the issue and avoid displaying the media until the user decides what to do. Apple's iOS 17 Messages example uses a blurred image with controls that:

- Displays the flagged content, if the user chooses.
- Offers a menu of additional actions, such as blocking the contact.

## Topics

### Setup
- [Detecting sensitive content in media and providing intervention options](https://developer.apple.com/documentation/sensitivecontentanalysis/detecting-nudity-in-media-and-providing-intervention-options) - Apply the active policy and keep detection outcomes on-device.

### Authorization
- **com.apple.developer.sensitivecontentanalysis.client** - A code-signing entitlement that enables an app to detect nudity in images and video.

### Image and video file analysis
- **SCSensitivityAnalyzer** - An object that analyzes media for sensitive content.
- **SCSensitivityAnalysisPolicy** - Configurations that represent the way the framework checks for sensitive content and how the app responds.

### Video stream analysis
- **SCVideoStreamAnalyzer** - Monitors video frames; documented for iOS/iPadOS/Catalyst 26.0+. Create one analyzer per stream, handle initialization or analysis errors, and do not apply this class's availability to the older file APIs.

### Analysis results
- **SCSensitivityAnalysis** - An object that indicates whether sensitive content is present and includes intervention guidance.

### Testing
- [Testing your app's response to sensitive media](https://developer.apple.com/documentation/sensitivecontentanalysis/testing-your-app-s-response-to-sensitive-media) - Use Apple's test QR code and installed profile, then reboot the development device. The documented 27-generation test produces a sensitive result containing `.sexuallyExplicit`; it does not demonstrate detection of every category.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SensitiveContentAnalysis)*

*Changed-content sources: [integration and privacy constraints](https://developer.apple.com/documentation/sensitivecontentanalysis/detecting-nudity-in-media-and-providing-intervention-options.md) and [detectedTypes availability](https://developer.apple.com/tutorials/data/documentation/sensitivecontentanalysis/scsensitivityanalysis/detectedtypes.json).*
