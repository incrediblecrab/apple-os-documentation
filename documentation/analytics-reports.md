# Analytics Reports

A list of app development reports, their field descriptions, and glossaries.

## Overview

Use the Analytics Report API to analyze data about your apps on Apple platforms. This page provides details on downloading reports, report changes, and a list of available reports. You can look at specific reports to read descriptions of report fields, glossaries of values, definitions of key terms, and coverage across platforms.

This is an [App Store Connect API](AppStoreConnectAPI.md) service, not an OS 27-only framework. Territory, platform, historical coverage, consent requirements, and completeness vary by report.

The [download guide](https://developer.apple.com/documentation/appstoreconnectapi/downloading-analytics-reports) distinguishes managing requests from reading results. Only an Admin key can create or delete report requests; these roles can list and download reports:
- ADMIN
- SALES_AND_REPORTS
- FINANCE

For a report-processing integration, use appropriately limited credentials and protect the private key on the server. `SALES_AND_REPORTS` can download Sales and Trends reports but cannot use the Finance Reports endpoint. Do not distribute an unrestricted developer-account key or embed a private key in a client.

### Download and process reports

To start generation, an Admin creates a request with [Request reports](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-analyticsreportrequests). `ONGOING` generates new reports; `ONE_TIME_SNAPSHOT` collects available historical data without continuing generation after the request date. Apple gives 1–2 days for the first report, rather than promising an immediate download.

Follow the resource hierarchy:
- [Read report request information](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_) checks the request's state, including `stoppedDueToInactivity`. If that flag is true, create a new request to resume generation.
- [Read reports for a specific request](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportrequests-_id_-reports) lists report definitions.
- [Read a list of instances of a report](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreports-_id_-instances) selects data by granularity and processing date.
- [Read the segments for a report](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-analyticsreportinstances-_id_-segments) provides the downloadable files.

An instance can consist of multiple segments. Download every segment to obtain its complete data set, follow pagination, and use `sizeInBytes` and `checksum` to check the downloads. Segment download URLs expire after 5 minutes; obtain fresh URLs when needed. Handle authorization, rate-limit, and transfer failures separately from a request that is still generating data.

Each report instance has a specific granularity: daily, weekly, or monthly, as available for that report. Daily instances may contain data for more than one day. The Date column identifies the reporting period, while `processingDate` identifies when Apple produced the instance. Weekly instances cover Monday through Sunday; monthly instances cover a full month.

Follow each report's completeness rules. For the report types covered by [Data Completeness and Corrections](https://developer.apple.com/documentation/analytics-reports/data-completeness-corrections), newer processing dates replace older data for the same reporting period; blindly appending overlapping instances would double-count events.

**Note:** For weekly and monthly report instances, the Date column represents the first day of the week and month, respectively.

### Retrieve missed reports

A generated instance is available for 35 days before automatic deletion. A one-time snapshot request can recover historical data that remains available for the report; it is not a guarantee of unlimited history. Apple documents a limit of one such snapshot request per month.

### Monitor future report changes

Report column position might change over time. Rely on column names instead of column positions in the report files to ensure smoother schema upgrades. Report values are not case sensitive.

Use each report's glossary: some numeric values are histogram bucket indexes or report-specific codes, not raw durations or SDK enum values. Event counts, unique devices, and unique users are not interchangeable or necessarily additive across rows. Privacy thresholding or noise can omit or alter values; a missing row is not proof of zero activity. See [Protecting user privacy in report data](https://developer.apple.com/documentation/analytics-reports/privacy).

## Topics

### Essentials
- [Data Completeness and Corrections](https://developer.apple.com/documentation/analytics-reports/data-completeness-corrections) - Understand how the Analytics Reports API provides complete data sets.
- [Protecting user privacy in report data](https://developer.apple.com/documentation/analytics-reports/privacy) - Understand measures that help protect user privacy.

### App Store Engagement
- [App Store Discovery and Engagement](https://developer.apple.com/documentation/analytics-reports/app-store-discovery-and-engagement) - Analyze how users interact with your app on the App Store.
- [App Store Web Preview](https://developer.apple.com/documentation/analytics-reports/app-store-web-preview) - Analyze how users engage with your app's product pages and in-app events on web browsers.

### App Store Commerce
- [App Store Downloads](https://developer.apple.com/documentation/analytics-reports/app-download) - Analyze how many times people download your app on the App Store.
- [App Store Pre-orders](https://developer.apple.com/documentation/analytics-reports/app-store-pre-order) - Analyze details on the number of pre-orders that people place and cancel for your app on the App Store.
- [App Store Purchases](https://developer.apple.com/documentation/analytics-reports/app-store-purchase) - Analyze paid-app and in-app purchases, including estimated USD sales and proceeds.

### App Usage
- [App Clip Usage](https://developer.apple.com/documentation/analytics-reports/app-clip-usage) - Analyze how users engage with your App Clips.
- [App Crashes](https://developer.apple.com/documentation/analytics-reports/app-crashes) - Review crashes for your App Store apps based on app version and device type.
- [App Store Installations and Deletions](https://developer.apple.com/documentation/analytics-reports/app-installs) - Analyze details on the number of times users install and delete your apps.
- [App Store Opt-in](https://developer.apple.com/documentation/analytics-reports/app-store-opt-in) - Analyze the percentage of first-time app downloaders who choose to share their data with you.
- [App Sessions](https://developer.apple.com/documentation/analytics-reports/app-sessions) - Analyze how often people open your App Store apps, and the average session duration.
- [CarPlay App Usage](https://developer.apple.com/documentation/analytics-reports/carplay-app-usage) - Review how people use CarPlay in your app.
- [Platform App Installs](https://developer.apple.com/documentation/analytics-reports/platform-app-installs) - Analyze EU iOS/iPadOS installations across App Store, TestFlight, and alternative distribution channels.

### Framework Usage
- [AccessorySetupKit Accessory Picker Sessions](https://developer.apple.com/documentation/analytics-reports/accessorysetupkit-accessory-picker-sessions) - Review accessory-picker activations and contributing devices.
- [AccessorySetupKit Usage](https://developer.apple.com/documentation/analytics-reports/accessorysetupkit-usage) - Analyze how often your app uses AccessorySetupKit.
- [AirPlay Discovery Sessions](https://developer.apple.com/documentation/analytics-reports/airplay-discovery-sessions) - Review information about AirPlay discovery sessions.
- [Animoji Stickers Sent](https://developer.apple.com/documentation/analytics-reports/animoji-stickers-sent) - Analyze how many times people use Memoji stickers in your app.
- [App Added to Focus](https://developer.apple.com/documentation/analytics-reports/app-added-to-focus) - Review information about your app's relationship to Focus modes.
- [App Disk Space Usage](https://developer.apple.com/documentation/analytics-reports/app-disk-space-usage) - Analyze your app's disk space use.
- [App Runtime Usage](https://developer.apple.com/documentation/analytics-reports/app-runtime-usage) - Review sampled symbol and dynamic-library activity, rather than an exact invocation counter.
- [App Sessions Context](https://developer.apple.com/documentation/analytics-reports/app-sessions-context) - Review daily device/session context across iOS and iPadOS distribution methods, not only the App Store.
- [Application Preferred Language Settings](https://developer.apple.com/documentation/analytics-reports/application-preferred-language-settings) - Review how people use language preference settings in your app.
- [ARKit ARSession Duration](https://developer.apple.com/documentation/analytics-reports/arkit-arsession-duration) - Review information about ARKit ARSession duration.
- [ARKit ARSession Failures](https://developer.apple.com/documentation/analytics-reports/arkit-arsession-failures) - Analyze details about ARKit ARSession failures.
- [ARKit Capture Frame Rate Throttling](https://developer.apple.com/documentation/analytics-reports/arkit-capture-frame-rate-throttling) - Analyze how long it takes for ARKit to throttle the camera frame rate.
- [ARKit Collaborative Session Features](https://developer.apple.com/documentation/analytics-reports/arkit-collaborative-session-features) - Review how your app uses ARKit collaborative session features.
- [ARKit Face Tracking](https://developer.apple.com/documentation/analytics-reports/arkit-face-tracking) - Analyze how often your app uses ARKit face tracking.
- [ARKit Video Formats](https://developer.apple.com/documentation/analytics-reports/arkit-video-formats) - Review information about ARKit video formats and high-resolution frames.
- [ARKit World Tracking](https://developer.apple.com/documentation/analytics-reports/arkit-world-tracking) - Review the configured settings for world tracking in your app.
- [ARKit World Tracking Image Detection](https://developer.apple.com/documentation/analytics-reports/arkit-world-tracking-image-detection) - Review configured detection-image counts for world tracking.
- [Audio Input Muting](https://developer.apple.com/documentation/analytics-reports/audio-input-muting) - Analyze details about audio-input muting and unmuting gestures during a call with conferencing apps.
- [Audio Input Route and Duration and Call Mode](https://developer.apple.com/documentation/analytics-reports/audio-input-route-and-duration-and-call-mode) - Review how your app uses audio session inputs.
- [Audio Session Audio Unit Usage](https://developer.apple.com/documentation/analytics-reports/audio-session-audio-unit-usage) - Analyze your app's audio unit use.
- [Audio Volume Levels and Duration](https://developer.apple.com/documentation/analytics-reports/audio-volume-levels-and-duration) - Review how your app uses volume and duration for output audio.
- [Automatic Speech Recognition Usage](https://developer.apple.com/documentation/analytics-reports/automatic-speech-recognition-usage) - Analyze how often people use dictation or Siri in your app.
- [Bluetooth LE Advertising](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-advertising) - Review how your app uses Bluetooth Low Energy (LE) advertising.
- [Bluetooth LE Connection Results](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-connection-results) - Analyze how often your app uses Low Energy (LE) connections and the connection results.
- [Bluetooth LE Connections Per App](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-connections-per-app) - Analyze the number of completed Bluetooth Low Energy (LE) connections for your app.
- [Bluetooth LE Disconnection Results](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-disconnection-results) - Review Low Energy (LE) disconnections for your app.
- [Bluetooth LE Scans](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-scans) - Review how your app uses Bluetooth Low Energy (LE) scans.
- [Bluetooth LE Sessions](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-sessions) - Analyze how often your app uses Bluetooth Low Energy (LE) connections.
- [Browser Choice Screen Engagement (iOS versions before 18.2)](https://developer.apple.com/documentation/analytics-reports/browser-choice-screen-engagement) - Review the older EU iOS browser-choice screen's engagement and completed-choice events.
- [Call Services and Call Performance](https://developer.apple.com/documentation/analytics-reports/call-services-and-call-performance) - Review your app's use of call services and call performance.
- [CarPlay Navigation](https://developer.apple.com/documentation/analytics-reports/carplay-navigation) - Analyze how often people start route-guidance sessions in your app.
- [Collaboration Message Usage](https://developer.apple.com/documentation/analytics-reports/collaboration-message-usage) - Analyze how often people use collaboration messages in your app.
- [Core Location Authorization Results](https://developer.apple.com/documentation/analytics-reports/core-location-authorization-results) - Review authorizations that people grant as a result of requests from your app.
- [Core Location Geofencing](https://developer.apple.com/documentation/analytics-reports/core-location-geofencing) - Review how your app uses geo fences.
- [CRABS-Based Video Playback Usage](https://developer.apple.com/documentation/analytics-reports/crabs-based-video-playback-usage) - Analyze how often your app uses CRABS video playback or video playback that uses the CRABS protocol.
- [Custom Language Model Builds Started](https://developer.apple.com/documentation/analytics-reports/custom-language-model-builds-started) - Analyze how often your app triggers a rebuild of custom language models.
- [Customized Transcription Requests](https://developer.apple.com/documentation/analytics-reports/customized-transcription-requests) - Analyze transcription request use of custom language models.
- [DockKit App Usage](https://developer.apple.com/documentation/analytics-reports/dockkit-app-usage) - Review how your application uses DockKit accessories.
- [Dynamic Island Layout Changes](https://developer.apple.com/documentation/analytics-reports/dynamic-island-layout-changes) - Analyze changes in Dynamic Island layout state.
- [File-Based Video Playback Usage](https://developer.apple.com/documentation/analytics-reports/file-based-video-playback-usage) - Analyze how often your app uses file playback or playback that occurs on the local file system.
- [Flashlight Usage](https://developer.apple.com/documentation/analytics-reports/flashlight-usage) - Review information about flashlight state.
- [Game Controller Haptics Engine Creation](https://developer.apple.com/documentation/analytics-reports/game-controller-haptics-engine-creation) - Analyze how your app uses haptic localities and which controllers it uses.
- [Game Controller Sessions](https://developer.apple.com/documentation/analytics-reports/game-controller-sessions) - Analyze how often and how long people are in game-controller sessions in your app.
- [Haptics Engine Usage](https://developer.apple.com/documentation/analytics-reports/haptics-engine-usage) - Review how often your app plays haptics.
- [Home Screen Widget Installs](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-installs) - Analyze how often people add your widget to their Home Screens.
- [Home Screen Widget Rotations](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-rotations) - Analyze how often your app's widget rotates to the front of a Smart Stack.
- [Home Screen Widget Usage](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-usage) - Analyze how many people are interacting with your Widget.
- [Home Screen Widgets](https://developer.apple.com/documentation/analytics-reports/home-screen-widgets) - Analyze when the system adds your app widget to a default Smart Stack on the Home Screen.
- [HTTP Live Streaming Playback Count](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-playback-count) - Review your app's use of HTTP Live Streaming (HLS) assets in AVFoundation APIs.
- [HTTP Live Streaming Video Playback Usage](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-video-playback-usage) - Review information about how your app uses HTTP live streaming (HLS) video playback or video playback that uses the HLS protocol.
- [Keyboard Dictation Usage](https://developer.apple.com/documentation/analytics-reports/keyboard-dictation-usage) - Analyze how people use keyboard dictation in your app.
- [Live Activity Use](https://developer.apple.com/documentation/analytics-reports/live-activity-use) - Review how your app uses Live Activity.
- [Load CoreML Models Metrics](https://developer.apple.com/documentation/analytics-reports/load-coreml-models-metrics) - Review Core ML model-loading metrics and load errors.
- [Local Network Privacy](https://developer.apple.com/documentation/analytics-reports/local-network-privacy) - Analyze results of the Local Network Privacy prompt.
- [Location Sessions](https://developer.apple.com/documentation/analytics-reports/location-sessions) - Review how your app uses Core Location APIs.
- [Lock Screen Widget Configuration](https://developer.apple.com/documentation/analytics-reports/lock-screen-widget-configuration) - Analyze how often people configure your widgets on the Lock Screen.
- [Metal Command Queues](https://developer.apple.com/documentation/analytics-reports/metal-command-queues) - Review peak concurrent command-queue usage.
- [Mode Activity Notifications](https://developer.apple.com/documentation/analytics-reports/mode-activity-notifications) - Review information about how users resolve notifications in your app.
- [Multiple Game Controllers Usage](https://developer.apple.com/documentation/analytics-reports/multiple-game-controllers-usage) - Review how people using your app use multiple game controllers.
- [Notification Summary Engagement](https://developer.apple.com/documentation/analytics-reports/notification-summary-engagement) - Analyze how often people engage with notification summaries in your app.
- [Photogrammetry ObjectCaptureSession API Usage](https://developer.apple.com/documentation/analytics-reports/photogrammetry-objectcapturesession-api-usage) - Review how often your app uses object capture for photogrammetry.
- [PhotogrammetrySession API Usage](https://developer.apple.com/documentation/analytics-reports/photogrammetrysession-api-usage) - Review how often your app uses object modeling for photogrammetry.
- [PhotoKit Imports](https://developer.apple.com/documentation/analytics-reports/photokit-imports) - Review how your app imports PhotoKit assets.
- [Photos Library Access](https://developer.apple.com/documentation/analytics-reports/photos-library-access) - Review responses to photo and video access prompts.
- [Photos Picker](https://developer.apple.com/documentation/analytics-reports/photos-picker) - Analyze out-of-process Photos picker selections and configuration.
- [Photos Sharing](https://developer.apple.com/documentation/analytics-reports/photos-sharing) - Analyze how often people share Photos in your app.
- [Reminders Usage](https://developer.apple.com/documentation/analytics-reports/reminders-usage) - Analyze how often your app interacts with system reminders.
- [RoomPlan Usage](https://developer.apple.com/documentation/analytics-reports/roomplan-usage) - Review how people use RoomPlan in your app.
- [Safari Extensions Enablement](https://developer.apple.com/documentation/analytics-reports/safari-extensions-enablement) - Review devices on which your Safari extension is enabled, rather than a count of enable-button taps.
- [Safari Extensions Usage](https://developer.apple.com/documentation/analytics-reports/safari-extensions-usage) - Review how people use your Safari extension.
- [Shared With You Content Engagement](https://developer.apple.com/documentation/analytics-reports/shared-with-you-content-engagement) - Review information about people engaging with Shared with You content in your app.
- [SharePlay Usage by Activity Type](https://developer.apple.com/documentation/analytics-reports/shareplay-usage-by-activity-type) - Review how people use SharePlay in your app.
- [ShazamKit Usage](https://developer.apple.com/documentation/analytics-reports/shazamkit-usage) - Analyze how your app utilizes ShazamKit.
- [Spatial Audio Usage](https://developer.apple.com/documentation/analytics-reports/spatial-audio-usage) - Analyze changes in spatial audio modes.
- [Speech Framework Transcription Request Audio Duration](https://developer.apple.com/documentation/analytics-reports/speech-framework-transcription-request-audio-duration) - Analyze the distribution of audio duration for transcription requests in your app.
- [Speech Framework Transcription Requests](https://developer.apple.com/documentation/analytics-reports/speech-framework-transcription-requests) - Review transcription requests in your app.
- [Text-Input Actions](https://developer.apple.com/documentation/analytics-reports/text-input-actions) - Review information on text-input actions.
- [Translation Request Usage](https://developer.apple.com/documentation/analytics-reports/translation-request-usage) - Review information about how people use speech-to-text translation in your app.
- [Verify With Wallet Document Request Availability](https://developer.apple.com/documentation/analytics-reports/verify-with-wallet-document-request-availability) - Review `canRequestDocument` availability checks and their outcomes.
- [Verify with Wallet Document Requests](https://developer.apple.com/documentation/analytics-reports/verify-with-wallet-document-requests) - Review `requestDocument` calls, requested elements and retention settings, and outcomes—not the returned identity values.
- [Video Duration Information](https://developer.apple.com/documentation/analytics-reports/video-duration-information) - Review information about video duration.
- [Video PiP Duration](https://developer.apple.com/documentation/analytics-reports/video-pip-duration) - Review active PiP duration, excluding sessions of 8 seconds or less.
- [VisionKit Data Detectors](https://developer.apple.com/documentation/analytics-reports/visionkit-data-detectors) - Review your app's use of data detector invocation for VisionKit.
- [VisionKit Image Analysis](https://developer.apple.com/documentation/analytics-reports/visionkit-image-analysis) - Analyze VisionKit analysis requests on images.
- [VisionKit Live Text Usage](https://developer.apple.com/documentation/analytics-reports/visionkit-live-text-usage) - Review information about how people interact with Live Text.
- [VisionKit Sessions](https://developer.apple.com/documentation/analytics-reports/visionkit-sessions) - Review VisionKit sessions in your app.
- [Browser Choice Screen Selection](https://developer.apple.com/documentation/analytics-reports/browser-choice-screen-selection) - Review EU browser-choice selection metrics for iOS and iPadOS 18.2 onward.
- [Default Browser Usage Rate](https://developer.apple.com/documentation/analytics-reports/default-browser-usage-rate) - Review default-browser percentages from weekly device observations.
- [Wi-Fi Known Network Modifications](https://developer.apple.com/documentation/analytics-reports/wi-fi-known-network-modifications) - Analyze known-network additions, removals, and updates attributed to your app.

### Performance
- [AirPlay Errors](https://developer.apple.com/documentation/analytics-reports/airplay-errors) - Analyze AirPlay errors in your apps.
- [AirPlay Performance](https://developer.apple.com/documentation/analytics-reports/airplay-performance) - Review AirPlay performance in your apps.
- [App Crashes Expanded](https://developer.apple.com/documentation/analytics-reports/app-crashes-expanded) - Review crashes including those that do not generate a crash log.
- [App Installs Performance](https://developer.apple.com/documentation/analytics-reports/app-installs-performance) - Analyze details about installation success and failure rates for your apps.
- [App Storage Reads and Writes](https://developer.apple.com/documentation/analytics-reports/app-storage-reads-and-writes) - Analyze bytes read and written by your app.
- [Audio Overloads](https://developer.apple.com/documentation/analytics-reports/audio-overloads) - Analyze how many audio glitches people experience in your app.
- [Bluetooth LE Session Duration](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-session-duration) - Analyze how long your app uses Bluetooth Low Energy (LE) connections.
- [Bluetooth System Wakes](https://developer.apple.com/documentation/analytics-reports/bluetooth-system-wakes) - Analyze details about bluetooth system wakes that your app causes.
- [CAMetalLayer Performance](https://developer.apple.com/documentation/analytics-reports/cametallayer-performance) - Review CAMetalLayer metadata and performance in your app.
- [Custom Language Model Builds Failed](https://developer.apple.com/documentation/analytics-reports/custom-language-model-builds-failed) - Analyze how often your app-triggered rebuild of a custom language model failed.
- [Display Power Information](https://developer.apple.com/documentation/analytics-reports/display-power-information) - Review your app's impact on display pixel attributes.
- [HTTP Live Streaming Playback Errors](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-playback-errors) - Analyze playback errors that your app receives.
- [Launch Image Over Memory Limit](https://developer.apple.com/documentation/analytics-reports/launch-image-over-memory-limit) - Analyze launch-image loading failures caused by a memory limit, not all app-launch failures.
- [Networking Connection Activity](https://developer.apple.com/documentation/analytics-reports/networking-connection-activity) - Review how your app uses network connections.
- [Spotlight Query Performance](https://developer.apple.com/documentation/analytics-reports/spotlight-query-performance) - Review how your app uses Spotlight queries.
- [Streaming Downloads Performance](https://developer.apple.com/documentation/analytics-reports/streaming-downloads-performance) - Review aggregate HLS download performance for eligible apps using `AVAssetDownloadTask`.
- [Streaming Playback Performance](https://developer.apple.com/documentation/analytics-reports/streaming-playback-performance) - Review aggregate HLS playback performance for eligible apps using `AVPlayerItem`.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/analytics-reports)*
