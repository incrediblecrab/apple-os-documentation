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

## Topics

### Essentials
- **SensorKit updates** - Learn about important changes to SensorKit.

### Setup
- [Configuring your project for sensor reading](https://developer.apple.com/documentation/sensorkit/configuring_your_project_for_sensor_reading) - Add metadata to your app to attain system and user permission to access sensor data.
- **SRSensorReader** - An object that establishes user authorization and records data for a particular sensor.

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
- **SR_ARKIT_SUPPORTED: Int32** - A flag that indicates whether the ARKit framework is available in the SDK for the SensorKit framework.

### Recording wrist temperatures
- **SRWristTemperatureSession** - An object that represents wrist temperatures that a device records during a period of time.
- **SRWristTemperature** - The temperature of the user's wrist while the user sleeps.

### Recording ectrocardiogram data
- **SRElectrocardiogramSample** - The sample electrocardiogram sensor data.

### Recording photoplethysmogram data
- **SRPhotoplethysmogramSample** - The sample photoplethysmogram (PPG) sensor data.

### Classes
- **SRAcousticSettings** - Beta
- **SRSleepSession** - Beta

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SensorKit)*