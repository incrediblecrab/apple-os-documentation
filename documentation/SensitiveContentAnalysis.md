# SensitiveContentAnalysis

Provide a safer experience in your app by detecting and alerting users to nudity in images and videos before displaying them onscreen.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+

## Overview

This framework enables an app to check content for nudity. In iOS and macOS, the Sensitive Content Warning user preference or Communication Safety parental control in Screen Time offer people the option to indicate their desire to guard against unexpected or unwanted exposure to images that contain nudity. Provide people with the experience they request in these settings by using SensitiveContentAnalysis to check for sensitive content before displaying it.

Consider situations in which your app acquires externally-sourced images or video, and use this framework to check if the media is sensitive. For example, a messaging app checks each image it receives from a contact. A classroom app evaluates uploads from personal devices to a shared location for classwork submission or other classroom activities. A video-conferencing app analyzes the video streams of all perticipants, live on a call.

### Intervene when content is sensitive

If the framework determines that some media contains sensitive content, call the user's attention to the issue and avoid displaying the media until the user decides what to do. For example, the following image depicts Messages in iOS 17 as a potentially explicit image arrives. The user interface blurs the image and:

- Displays the flagged content, if the user chooses.
- Offers a menu of additional actions, such as blocking the contact.

## Topics

### Setup
- [Detecting nudity in media and providing intervention options](https://developer.apple.com/documentation/sensitivecontentanalysis/detecting_nudity_in_media_and_providing_intervention_options) - Alert people before displaying images or video that might be sensitive.

### Authorization
- **com.apple.developer.sensitivecontentanalysis.client** - A code-signing entitlement that enables an app to detect nudity in images and video.

### Image and video file analysis
- **SCSensitivityAnalyzer** - An object that analyzes media for sensitive content.
- **SCSensitivityAnalysisPolicy** - Configurations that represent the way the framework checks for sensitive content and how the app responds.

### Video stream analysis
- **SCVideoStreamAnalyzer** - An object that monitors a stream of video by analyzing frames for sensitive content.

### Analysis results
- **SCSensitivityAnalysis** - An object that indicates whether sensitive content is present and includes intervention guidance.

### Testing
- [Testing your app's response to sensitive media](https://developer.apple.com/documentation/sensitivecontentanalysis/testing_your_app_s_response_to_sensitive_media) - Trigger your app's intervention flow by using a special QR code and profile that Apple provides for testing.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SensitiveContentAnalysis)*