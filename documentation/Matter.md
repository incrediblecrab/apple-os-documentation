# Matter

Communicate with and control smart home devices from a variety of manufacturers.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.1+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

The Matter smart home connectivity standard enables interoperability between compatible devices and ecosystems. Use [MatterSupport](https://developer.apple.com/documentation/mattersupport) for the system onboarding flow and network provisioning, then use Matter to commission an accessory onto a fabric and control it. Network connectivity, discovery, and authorization to control an accessory are different stages.

Commissioning establishes the accessory's membership and credentials for a fabric. Device functions are organized into clusters: for example, On/Off controls a light's power state and Level Control controls a dimmable light's brightness. A generated cluster API existing in an SDK does not mean that every accessory implements that cluster.

Preserve controller storage, fabric identity, and key material across launches. Configure appropriate device-attestation trust and do not bypass attestation validation merely to make onboarding succeed. Handle controller startup errors, commissioning-session errors, and the final commissioning result separately; beginning a session is not proof that commissioning completed.

## Availability by API generation

The header gives framework catalog minimums, not the minimum for every symbol below. `MTRDeviceController` and `MTRDeviceControllerStartupParams` start at iOS/iPadOS/Mac Catalyst/tvOS 16.1, macOS 13, visionOS 1, and watchOS 9.1. The onboarding guide's `MTRDeviceControllerFactory` requires 16.4, macOS 13.3, visionOS 1, and watchOS 9.4.

The generated symbol lists below include later additions:

| Generation | Representative APIs | Platform minimums |
| --- | --- | --- |
| 18.2 | `MTRDeviceType`, `MTRXPCDeviceControllerParameters`, color-control bitmaps/enums, event/command name functions | iOS/iPadOS/Mac Catalyst/tvOS 18.2; macOS 15.2; visionOS 2.2; watchOS 11.2 |
| 18.3 | `MTRAttributeValueWaiter` and some XPC registration/protocol additions | iOS/iPadOS/Mac Catalyst/tvOS 18.3; macOS 15.3; visionOS 2.3; watchOS 11.3 |
| 18.4 | Most remaining listed cluster classes, feature bitmaps, and enums | iOS/iPadOS/Mac Catalyst/tvOS 18.4; macOS 15.4; visionOS 2.4; watchOS 11.4 |

Check each declaration for its precise floor rather than applying one generation to all XPC protocols, keys, or members.

## Topics

### Matter device onboarding
- [Onboarding a Matter device](https://developer.apple.com/documentation/matter/onboarding-a-matter-device) - Prepare persistent controller state, device-attestation trust, and the commissioning lifecycle.

### Matter device interactions
- [Controller initialization](https://developer.apple.com/documentation/matter/controller-initialization) - Initialize the object that controls Matter accessories.
- [Accessory commissioning](https://developer.apple.com/documentation/matter/accessory-commissioning) - Commission a Matter accessory onto a fabric.
- [Accessory control](https://developer.apple.com/documentation/matter/accessory-control) - Communicate with commissioned Matter accessories.
- [Clusters](https://developer.apple.com/documentation/matter/clusters) - Interact with groups of related functionality that Matter accessories expose.

### Reference
- [Matter Constants](https://developer.apple.com/documentation/matter/matter-constants)
- [Matter Functions](https://developer.apple.com/documentation/matter/matter-functions)

### Classes
- **MTRAccessControlClusterAccessRestrictionEntryStruct**
- **MTRAccessControlClusterAccessRestrictionStruct**
- **MTRAccessControlClusterCommissioningAccessRestrictionEntryStruct**
- **MTRAccessControlClusterFabricRestrictionReviewUpdateEvent**
- **MTRAccessControlClusterReviewFabricRestrictionsParams**
- **MTRAccessControlClusterReviewFabricRestrictionsResponseParams**
- **MTRAccountLoginClusterLoggedOutEvent**
- **MTRAttributeValueWaiter**
- **MTRBaseClusterCommissionerControl** - Cluster Commissioner Control
- **MTRBaseClusterContentAppObserver** - Cluster Content App Observer
- **MTRBaseClusterDeviceEnergyManagement** - Cluster Device Energy Management
- **MTRBaseClusterDeviceEnergyManagementMode** - Cluster Device Energy Management Mode
- **MTRBaseClusterDishwasherAlarm** - Cluster Dishwasher Alarm
- **MTRBaseClusterDishwasherMode** - Cluster Dishwasher Mode
- **MTRBaseClusterEnergyEVSE** - Cluster Energy EVSE
- **MTRBaseClusterEnergyEVSEMode** - Cluster Energy EVSE Mode
- **MTRBaseClusterICDManagement** - Cluster ICD Management
- **MTRBaseClusterLaundryDryerControls** - Cluster Laundry Dryer Controls
- **MTRBaseClusterLaundryWasherControls** - Cluster Laundry Washer Controls
- **MTRBaseClusterLaundryWasherMode** - Cluster Laundry Washer Mode
- **MTRBaseClusterMessages** - Cluster Messages
- **MTRBaseClusterMicrowaveOvenControl** - Cluster Microwave Oven Control
- **MTRBaseClusterMicrowaveOvenMode** - Cluster Microwave Oven Mode
- **MTRBaseClusterOvenCavityOperationalState** - Cluster Oven Cavity Operational State
- **MTRBaseClusterOvenMode** - Cluster Oven Mode
- **MTRBaseClusterPowerTopology** - Cluster Power Topology
- **MTRBaseClusterRefrigeratorAlarm** - Cluster Refrigerator Alarm
- **MTRBaseClusterRefrigeratorAndTemperatureControlledCabinetMode** - Cluster Refrigerator And Temperature Controlled Cabinet Mode
- **MTRBaseClusterServiceArea** - Cluster Service Area
- **MTRBaseClusterTemperatureControl** - Cluster Temperature Control
- **MTRBaseClusterThreadBorderRouterManagement** - Cluster Thread Border Router Management
- **MTRBaseClusterThreadNetworkDirectory** - Cluster Thread Network Directory
- **MTRBaseClusterTimeSynchronization** - Cluster Time Synchronization
- **MTRBaseClusterWaterHeaterManagement** - Cluster Water Heater Management
- **MTRBaseClusterWaterHeaterMode** - Cluster Water Heater Mode
- **MTRBaseClusterWiFiNetworkManagement** - Cluster Wi-Fi Network Management
- **MTRClusterCommissionerControl** - Supports the ability for clients to request the commissioning of themselves or other nodes onto a fabric which the cluster server can commission onto.
- **MTRClusterContentAppObserver** - This cluster provides an interface for sending targeted commands to an Observer of a Content App on a Video Player device.
- **MTRClusterDeviceEnergyManagement** - This cluster allows a client to manage the power draw of a device.
- **MTRCommandWithRequiredResponse** - An object representing a single command to be invoked and the response required for the invoke to be considered successful.
- **MTRCommissioneeInfo** - Information read from the commissionee device during commissioning.
- **MTRDeviceType** - Meta-data about a device type defined in the Matter specification.
- **MTREndpointInfo** - Meta-data about an endpoint of a Matter node.
- **MTRXPCDeviceControllerParameters**

### Protocols
- **MTRXPCClientProtocol**
- **MTRXPCClientProtocol_MTRDevice**
- **MTRXPCClientProtocol_MTRDeviceController**
- **MTRXPCServerProtocol**
- **MTRXPCServerProtocol_MTRDevice**
- **MTRXPCServerProtocol_MTRDeviceController**

### Structures
- **MTRAccessControlFeature**
- **MTRBridgedDeviceBasicInformationFeature**
- **MTRChannelRecordingFlagBitmap**
- **MTRColorControlColorCapabilitiesBitmap**
- **MTRColorControlOptionsBitmap**
- **MTRColorControlUpdateFlagsBitmap**
- **MTRCommissionerControlSupportedDeviceCategoryBitmap**
- **MTRDeviceEnergyManagementFeature**
- **MTRDishwasherAlarmAlarmBitmap**
- **MTRDishwasherAlarmFeature**
- **MTREnergyEVSEFeature**
- **MTREnergyEVSETargetDayOfWeekBitmap**
- **MTRGeneralDiagnosticsFeature**
- **MTRICDManagementFeature**
- **MTRICDManagementUserActiveModeTriggerBitmap**
- **MTRLaundryWasherControlsFeature**
- **MTRMessagesFeature**
- **MTRMessagesMessageControlBitmap**
- **MTRMicrowaveOvenControlFeature**
- **MTRNetworkCommissioningThreadCapabilitiesBitmap**
- **MTROccupancySensingFeature**
- **MTRPowerTopologyFeature**
- **MTRRefrigeratorAlarmAlarmBitmap**
- **MTRServiceAreaFeature**
- **MTRTemperatureControlFeature**
- **MTRThermostatACErrorCodeBitmap**
- **MTRThermostatHVACSystemTypeBitmap**
- **MTRThermostatOccupancyBitmap**
- **MTRThermostatPresetTypeFeaturesBitmap**
- **MTRThermostatProgrammingOperationModeBitmap**
- **MTRThermostatRelayStateBitmap**
- **MTRThermostatRemoteSensingBitmap**
- **MTRThermostatScheduleTypeFeaturesBitmap**
- **MTRThreadBorderRouterManagementFeature**
- **MTRTimeSynchronizationFeature**
- **MTRWaterHeaterManagementFeature**
- **MTRWaterHeaterManagementWaterHeaterHeatSourceBitmap**

### Variables
- **MTRDeviceControllerRegistrationControllerCompressedFabricIDKey**
- **MTRDeviceControllerRegistrationControllerContextKey**
- **MTRDeviceControllerRegistrationControllerIsRunningKey**
- **MTRDeviceControllerRegistrationControllerNodeIDKey**
- **MTRDeviceControllerRegistrationDeviceInternalStateKey**
- **MTRDeviceControllerRegistrationNodeIDKey**
- **MTRDeviceControllerRegistrationNodeIDsKey**

### Functions
- **MTREventNameForID** - Resolve Matter event IDs into a descriptive string.
- **MTRRequestCommandNameForID** - Resolve Matter request (client to server) command IDs into a descriptive string.
- **MTRResponseCommandNameForID** - Resolve Matter response (server to client) command IDs into a descriptive string.

### Enumerations
- **MTRAccessControlAccessRestrictionType**
- **MTRChannelType**
- **MTRColorControlDirection**
- **MTRColorControlDriftCompensation**
- **MTRColorControlEnhancedColorMode**
- **MTRColorControlMoveMode**
- **MTRColorControlStepMode**
- **MTRContentAppObserverStatus**
- **MTRDataTypeAtomicRequestTypeEnum**
- **MTRDataTypeLandmarkTag**
- **MTRDataTypePositionTag**
- **MTRDataTypeRelativePositionTag**
- **MTRDeviceEnergyManagementAdjustmentCause**
- **MTRDeviceEnergyManagementCause**
- **MTRDeviceEnergyManagementCostType**
- **MTRDeviceEnergyManagementESAState**
- **MTRDeviceEnergyManagementESAType**
- **MTRDeviceEnergyManagementForecastUpdateReason**
- **MTRDeviceEnergyManagementModeModeTag**
- **MTRDeviceEnergyManagementOptOutState**
- **MTRDeviceEnergyManagementPowerAdjustReason**
- **MTRDeviceTypeIDType**
- **MTRDishwasherModeModeTag**
- **MTRElectricalEnergyMeasurementMeasurementType**
- **MTREnergyEVSEEnergyTransferStoppedReason**
- **MTREnergyEVSEFaultState**
- **MTREnergyEVSEModeModeTag**
- **MTREnergyEVSEState**
- **MTREnergyEVSESupplyState**
- **MTRICDManagementClientType**
- **MTRICDManagementOperatingMode**
- **MTRLaundryDryerControlsDrynessLevel**
- **MTRLaundryWasherControlsNumberOfRinses**
- **MTRLaundryWasherModeModeTag**
- **MTRMediaPlaybackCharacteristic**
- **MTRMessagesFutureMessagePreference**
- **MTRMessagesMessagePriority**
- **MTRMicrowaveOvenModeModeTag**
- **MTROvenCavityOperationalStateErrorState**
- **MTROvenCavityOperationalStateOperationalState**
- **MTROvenModeModeTag**
- **MTRRefrigeratorAndTemperatureControlledCabinetModeModeTag**
- **MTRServiceAreaOperationalStatus**
- **MTRServiceAreaSelectAreasStatus**
- **MTRServiceAreaSkipAreaStatus**
- **MTRThermostatACCapacityFormat**
- **MTRThermostatACCompressorType**
- **MTRThermostatACLouverPosition**
- **MTRThermostatACRefrigerantType**
- **MTRThermostatACType**
- **MTRThermostatPresetScenario**
- **MTRThermostatSetpointChangeSource**
- **MTRThermostatStartOfWeek**
- **MTRThermostatTemperatureSetpointHold**
- **MTRTimeSynchronizationStatusCode**
- **MTRTimeSynchronizationTimeZoneDatabase**
- **MTRWaterHeaterManagementBoostState**
- **MTRWaterHeaterModeModeTag**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Matter)*
