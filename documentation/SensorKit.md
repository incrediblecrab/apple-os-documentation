# SensorKit

Retrieve data and derived metrics from sensors on an iPhone, or paired Apple Watch.

**Platforms:** iOS 14.0+ | iPadOS 14.0+

## Overview

As the system gathers information using various sensors on a device, SensorKit enables an app to access select raw data, or metrics that the system processes from a sensor, such as:

- Steps information
- Accelerometer or rotation-rate data
- The configuration of a watch on the user's wrist
- Ambient light in the physical environment
- Details about a user's routine commute or travel

See SRSensor for the complete list.

**Note:** This framework ignores calls from Mac apps that you build with Mac Catalyst, and from compatible iPad and iPhone apps running in visionOS.

SensorKit access is for Apple-approved research studies. The [reader entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sensorkit.reader.allow), `com.apple.developer.sensorkit.reader.allow`, is an **array of sensor-name strings**, not a Boolean grant to all data. The configuration guide requires an explicit App ID and an approved, manually created provisioning profile. Entitlement approval does not replace the participant's consent.

Provide the study-purpose string [`NSSensorKitUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedescription), the per-sensor [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail) dictionary, and [`NSSensorKitPrivacyPolicyURL`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitprivacypolicyurl). A sensor's usage-detail dictionary can mark data as required for the study; this does not override denial. Participants can subsequently change individual sensor permissions in Settings.

### Typed readers in the 27 beta

[`SRReader<Sensor>`](https://developer.apple.com/documentation/sensorkit/srreader) is the new typed reader, with `Sensor` conforming to [`SRDataSensor`](https://developer.apple.com/documentation/sensorkit/srdatasensor). Its iOS/iPadOS 27 declarations include an observable `authorizationStatus`, asynchronous throwing recording methods, and [`samples(matching:)`](https://developer.apple.com/documentation/sensorkit/srreader/samples(matching:)), which returns an asynchronous sequence of typed fetch responses. Handle authorization changes, fetch errors, and cancellation.

`SRSensorReader` is deprecated in 27 in favor of `SRReader<Sensor>`; this is not removal of SensorKit or of all its sample/query types. When maintaining the legacy reader, request authorization with `requestAuthorization(sensors:completion:)` and inspect the reader's authorization status rather than treating request completion as consent. The typed reader's Catalyst SDK declaration does not supersede the framework's documented runtime exclusion.

Individual sample types have later minima than the framework: speech, face, and wrist-temperature types listed below require iOS/iPadOS 17; ECG and PPG sample types require 17.4; acoustic settings and sleep sessions require 26.

## Topics

### Essentials
- [SensorKit updates](https://developer.apple.com/documentation/updates/sensorkit) - Dated framework change summaries.

### Setup
- [Configuring your project for sensor reading](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading) - Configure the research entitlement, study metadata, and per-sensor consent request.
- **SRSensorReader** - The legacy reader for per-sensor authorization and recording; deprecated in 27 in favor of the typed reader.

### Authorization
- **com.apple.developer.sensorkit.reader.allow** - The necessary entitlement to access sensor data that's required by your app's preapproved research study.

### Querying data
- **SRFetchRequest** - An object that defines the criteria for a sample query.
- **SRFetchResult** - Recorded data that a sensor reader fetches.

### Interpreting data
- **SRAmbientLightSample** - The amount of ambient light in the user's environment.
- **SRDeviceUsageReport** - The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- **SRKeyboardMetrics** - The configuration of a device's keyboard and its usage patterns.
- **SRMediaEvent** - A user interaction with a media object, such as an image or a video.
- **SRMessagesUsageReport** - An object that describes the user's Messages app activity over a period of time.
- **SRPhoneUsageReport** - An object that describes the user's phone activity over a period of time.
- **SRVisit** - The user's progress in their daily travel routine.
- **SRWristDetection** - The configuration of a watch on the wearer's wrist.

### Deleting samples
- **SRDeletionRecord** - An object that describes the reason the framework deletes samples.

### Analyzing speech
- **SRSpeechMetrics** - An object that represents metrics about a range of speech.
- **SRSpeechExpression** - An object that represents the metrics and voice analytics for a range of speech.

### Analyzing faces
- **SRFaceMetrics** - An object that represents metrics about the user's face.
- **SR_ARKIT_SUPPORTED: Int32** - A flag indicating ARKit's availability in the SDK, not a runtime hardware-capability check.

### Recording wrist temperatures
- **SRWristTemperatureSession** - An object that represents wrist temperatures that a device records during a period of time.
- **SRWristTemperature** - The temperature of the user's wrist while the user sleeps.

### Recording electrocardiogram data
- **SRElectrocardiogramSample** - The sample electrocardiogram sensor data.

### Recording photoplethysmogram data
- **SRPhotoplethysmogramSample** - The sample photoplethysmogram (PPG) sensor data.

### Classes
- **SRAcousticSettings** - An object that describes the acoustic settings of a device during sleep.
- **SRSleepSession** - An object that represents a user's sleep session data.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SensorKit)*
