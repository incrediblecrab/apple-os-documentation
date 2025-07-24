# Matter

Communicate with and control smart home devices from a variety of manufacturers.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.1+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

The Matter smart home connectivity standard enables interoperability between various smart home devices and ecosystems. Use MatterSupport to bring accessories onto a local network, then commission and control those accessories using Matter.

To access a Matter accessory on a network, you must commission it. Commissioning provides credentials to enable secure communication and performs initial accessory configuration. Once you commission an accessory, it exposes areas of functionality called clusters that you use to control it. For example, a light exposes the On/Off cluster to control whether it's on or off. A dimmable light also exposes the Level Control cluster to control its brightness.

## Topics

### Matter device onboarding
- [Onboarding a Matter device](https://developer.apple.com/documentation/matter/onboarding_a_matter_device) - Prepare your app to discover and control a Matter device.

### Matter device interactions
- [Controller initialization](https://developer.apple.com/documentation/matter/controller_initialization) - Initialize the object that controls Matter accessories.
- [Accessory commissioning](https://developer.apple.com/documentation/matter/accessory_commissioning) - Commission a Matter accessory onto a network.
- [Accessory control](https://developer.apple.com/documentation/matter/accessory_control) - Communicate with commissioned Matter accessories.
- [Clusters](https://developer.apple.com/documentation/matter/clusters) - Interact with groups of related functionality that Matter accessories expose.

### Reference
- [Matter Constants](https://developer.apple.com/documentation/matter/matter_constants)
- [Matter Functions](https://developer.apple.com/documentation/matter/matter_functions)

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