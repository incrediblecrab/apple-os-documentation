# Core Motion

Process accelerometer, gyroscope, pedometer, and environment-related events.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Core Motion exposes motion and environmental measurements from supported sensors, including accelerometers, gyroscopes, magnetometers, and barometers. It also provides derived fitness information such as step counts, headphone motion, and specialized Apple Watch measurements. Apps can use these inputs for interaction, activity tracking, or appropriately authorized health workflows; for example, a game can respond to device tilt.

The framework provides raw sensor measurements and processed, sensor-fused measurements. For example, `CMDeviceMotion.userAcceleration` excludes the gravity component; total acceleration is the sum of `userAcceleration` and `gravity`. This distinction does not mean that every processed motion value excludes gravity.

Not all services are available on all devices, and some services might be unavailable even on devices with the required hardware. For example, many Core Motion services are available to visionOS apps, but those services aren't available to compatible iPad and iPhone apps running in visionOS. Check the relevant manager, not only `CMMotionManager`: altimeter, headphone, pedometer, fall-detection, and submersion services have their own capability and authorization checks. The framework catalog minimums above do not apply to every symbol; for example, `CMMotionManager` declares Mac Catalyst 13.1+.

**Privacy and lifecycle:** Supply the required string-valued usage descriptions in `Info.plist`. Motion and fitness services such as `CMPedometer` require [`NSMotionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmotionusagedescription); fall detection additionally requires [`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfalldetectionusagedescription). Missing required descriptions can terminate the app. Permission and hardware availability are separate: handle denied or changed authorization and unavailable data. Use one `CMMotionManager` per app and stop its update services when no longer needed.

## Topics

### Essentials
- [Core Motion updates](https://developer.apple.com/documentation/updates/coremotion) - Learn about important changes to Core Motion.
- **CMMotionManager** - The object for starting and managing motion services.

### Device Motion
- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) - Retrieve sensor-fused attitude, rotation, gravity, and user-acceleration measurements.
- **CMDeviceMotion** - Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- **CMAttitude** - The device's orientation relative to a known frame of reference at a point in time.
- **CMAttitudeReferenceFrame** - Constants that indicate the frame of reference for attitude-related motion data.
- **CMHeadphoneMotionManager** - An object that starts and manages headphone motion services.

### Accelerometers
- [Getting raw accelerometer events](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events) - Retrieve data from the onboard accelerometer.
- **CMAccelerometerData** - A three-axis acceleration sample.
- **CMRecordedAccelerometerData** - A single piece of accelerometer data that was recorded by the device.
- **CMSensorRecorder** - An object that gathers and retrieves accelerometer data from a device.
- **CMSensorDataList** - A list of the accelerometer data recorded by the system.

### Gyroscopes
- [Getting raw gyroscope events](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events) - Retrieve data from the onboard gyroscope.
- **CMGyroData** - A single measurement of the device's rotation rate.

### Magnetometer
- **CMMagnetometerData** - Measurements of the Earth's magnetic field relative to the device.

### Altitude Data
- **CMAltimeter** - An object that initiates the delivery of altitude-related changes.
- **CMAbsoluteAltitudeData** - An absolute-altitude measurement.
- **CMAltitudeData** - Data for a recorded change in altitude.

### Ambient Pressure
- **CMRecordedPressureData** - A recorded measurement of pressure data.
- **CMAmbientPressureData** - A measurement of the ambient pressure and temperature.

### Water Submersion

Live submersion monitoring uses Apple Watch Ultra and watchOS 9+, not the presence of similarly named iOS data types. Check `CMWaterSubmersionManager.waterSubmersionAvailable`; Simulator cannot supply these measurements. The Shallow Depth and Pressure capability permits readings to 6 meters; the separately approved Submerged Depth and Pressure capability permits readings to 40 meters. These are API access limits, not assurances that a dive is safe.

Configure `NSMotionUsageDescription` and the `WKBackgroundModes` array value `underwater-depth`. Assigning the manager's delegate starts updates and requests authorization when needed; clearing it stops updates. Handle errors and missing measurements, including a `nil` `maximumDepth` when unauthorized. The linked guide describes the special extended-runtime and Water Lock lifecycle; this is not general-purpose unlimited background execution.

- [Accessing submersion data](https://developer.apple.com/documentation/coremotion/accessing-submersion-data) - Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- **CMWaterSubmersionManager** - An object for managing the collection of pressure and temperature data during submersion.
- **CMWaterSubmersionManagerDelegate** - A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- **CMWaterSubmersionEvent** - An event indicating that the device's submersion state has changed.
- **CMWaterSubmersionMeasurement** - An update that contains data about the pressure and depth.
- **CMWaterTemperature** - An update that contains data about the water temperature.

### Activity

`CMHeadphoneActivityManager` requires iOS/iPadOS/Mac Catalyst 18+, macOS 15+, or watchOS 11+, supported headphones, and its activity/status availability checks. Its motion usage description is required on macOS as well as iOS. Apple's headphone-activity sample needs a physical iOS 18+ device and compatible headphones, such as AirPods Pro 2 or AirPods 4.

- **CMMotionActivityManager** - An object that manages access to the motion data stored by the device.
- **CMHeadphoneActivityManager** - An object that starts and manages headphone activity services.
- **CMMotionActivity** - The data for a single motion update event.
- [Getting motion-activity data from headphones](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones) - Configure your app to listen for motion-activity changes from headphones.

### Pedometer and Fitness
- **CMPedometer** - Retrieves live and historical step, distance, and supported floor-count data.
- **CMPedometerData** - Information about the distance traveled by a user on foot.
- **CMPedometerEvent** - A change in the user's pedestrian activity.
- **CMStepCounter** - Legacy step-count queries and updates; deprecated in iOS 8 in favor of `CMPedometer`.

### Workout Data
- **CMOdometerData** - A class that represents odometer data for workouts.
- **CMHighFrequencyHeartRateData** - Heart-rate data collected at 1 Hz; iOS/iPadOS/Mac Catalyst 17+ and watchOS 10+. Neither this class nor `CMOdometerData` is marked deprecated in the current references.

### Movement Disorder

`CMMovementDisorderManager` is a watchOS 5+ manager requiring Apple's movement-disorder entitlement approval and `NSMotionUsageDescription`. Apple's workflow is for people diagnosed with Parkinson's disease, with appropriate clinical guidance, symptom confirmation, transparent data-use information, and an opt-out. It measures resting tremor in the 3–7 Hz range and choreiform dyskinetic symptoms at the watch-wearing wrist; it is not a general diagnosis or a detector of every kind of tremor.

Processing is periodic and opportunistic, not real-time. Monitoring requests last at most seven days and may be renewed; processed results remain on the device for seven days. Check availability, errors, and `lastProcessedDate()` before querying. Activity, watch fit, other conditions, and which arm wears the watch can affect results and produce false positives or negatives.

- [Getting movement disorder symptom data](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data) - Retrieve data from the Apple Watch's movement disorder manager.
- [Adhering to the movement disorder data collection requirements](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements) - Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog) - A chronological log of notable changes to the movement disorder algorithm.
- **CMMovementDisorderManager** - A manager for recording and querying movement disorder data.
- **CMTremorResult** - A result object that contains data about the presence and strength of tremors during a one-minute interval.
- **CMDyskineticSymptomResult** - A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.

### Fall Detection

`CMFallDetectionManager` requires watchOS 7.2+ and supported Apple Watch hardware; check its availability rather than treating an iOS usage-description or entitlement listing as an iOS fall-detection service. Obtain Apple's approval for the Boolean [`com.apple.developer.health.fall-detection`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.health.fall-detection) entitlement and include the fall-detection usage description.

Retain one manager for the app's lifetime, install its delegate early, and request authorization after the interface loads. Authorization can change later. Fall callbacks offer only a brief background response opportunity; call their completion handler promptly. Direct notifications from this manager are distinct from the delayed and filtered fall history available through HealthKit.

- **CMFallDetectionManager** - An object for managing fall detection events.
- **CMFallDetectionDelegate** - A delegate that receives information about fall detection events and authorization status changes.
- **CMFallDetectionEvent** - An object that contains data about a fall detection event.
- **NSFallDetectionUsageDescription** - A message to the user that explains the app's request for permission to access fall detection event data.

### Batched Sensor Data
- **CMBatchedSensorManager** - Provides the latest batches of accelerometer and device-motion readings. Its watchOS introduction is 10.0; check `isAccelerometerSupported`, `isDeviceMotionSupported`, and authorization, and read the reported data frequencies rather than assuming a universal sampling rate.

### Common Data
- **CMLogItem** - A timestamped base class for motion-event measurements, not the superclass of every Core Motion data object.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreMotion)*
