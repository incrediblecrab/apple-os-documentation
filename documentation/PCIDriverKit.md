# PCIDriverKit

Develop device drivers for Peripheral Component Interconnect (PCI) accessories.

**Platforms:** DriverKit 19.0+ | macOS 11.1+

## Overview

Use the **PCIDriverKit** framework to develop drivers that manage custom features on your Peripheral Component Interconnect (PCI) and PCI-Express hardware. When the system loads your custom PCI driver, it passes an **IOPCIDevice** object as the provider to your driver. Use that object to read and write the configuration and memory of your PCI hardware.

On macOS, use the System Extensions framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

**Note:** PCIDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series chip.

## Topics

### Entitlements
- **com.apple.developer.driverkit.transport.pci** - An array of PCI device descriptors that your custom driver supports.

### Sample Code
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Device Interface
- [Creating Custom PCIe Drivers for Thunderbolt Devices](https://developer.apple.com/documentation/pcidriverkit/creating_custom_pcie_drivers_for_thunderbolt_devices) - Create a DriverKit extension to support your Thunderbolt device's custom features.
- **IOPCIDevice** - A DriverKit provider object that manages access to your custom PCI hardware.

### Reference
- **PCIDriverKit Enumerations**
- **PCIDriverKit Data Types**
- **PCIDriverKit Macros**

### Macros
- **kIOPCIACSCapabilitiesKey**
- **kIOPCIAERCapabilitiesKey**
- **kIOPCIExpressDeviceCapabilities2Key**
- **kIOPCIExpressDeviceCapabilitiesKey**
- **kIOPCIExpressLinkCapabilities2Key**
- **kIOPCIExpressRootCapabilitiesKey**
- **kIOPCIExpressSlotCapabilities2Key**
- **kIOPCIFPBCapabilitiesKey**
- **kIOPCIL1PMCapabilitiesKey**
- **kIOPCIMSIMessageControlKey**
- **kIOPCIMSIXMessageControlKey**
- **kIOPCIPTMCapabilitiesKey**
- **kIOPCIPowerManagementCapabilitiesKey**

### Enumeration Cases
- **kIOPCICapabilityIDAF**
- **kIOPCICapabilityIDEnhancedAllocation**
- **kIOPCICapabilityIDSATAConfiguration**
- **kIOPCIExpressCapabilityIDAMD**
- **kIOPCIExpressCapabilityIDATS**
- **kIOPCIExpressCapabilityIDAlternateProtocol**
- **kIOPCIExpressCapabilityIDCAC**
- **kIOPCIExpressCapabilityIDDPA**
- **kIOPCIExpressCapabilityIDDPC**
- **kIOPCIExpressCapabilityIDDVSEC**
- **kIOPCIExpressCapabilityIDDataLinkFeature**
- **kIOPCIExpressCapabilityIDFRSQueueing**
- **kIOPCIExpressCapabilityIDHierarchyID**
- **kIOPCIExpressCapabilityIDLNR**
- **kIOPCIExpressCapabilityIDLaneMarginingRx**
- **kIOPCIExpressCapabilityIDMFVC**
- **kIOPCIExpressCapabilityIDMPCIe**
- **kIOPCIExpressCapabilityIDMRIOV**
- **kIOPCIExpressCapabilityIDMulticast**
- **kIOPCIExpressCapabilityIDNPEM**
- **kIOPCIExpressCapabilityIDPASID**
- **kIOPCIExpressCapabilityIDPL16GTs**
- **kIOPCIExpressCapabilityIDPL32GTs**
- **kIOPCIExpressCapabilityIDPMUX**
- **kIOPCIExpressCapabilityIDPRI**
- **kIOPCIExpressCapabilityIDRCECEndpointAssociation**
- **kIOPCIExpressCapabilityIDRCInternalLinkCtrl**
- **kIOPCIExpressCapabilityIDRCLinkDeclaration**
- **kIOPCIExpressCapabilityIDReadinessTimeReporting**
- **kIOPCIExpressCapabilityIDResizableBAR**
- **kIOPCIExpressCapabilityIDRootComplexRegBlock**
- **kIOPCIExpressCapabilityIDSFI**
- **kIOPCIExpressCapabilityIDSPCIe**
- **kIOPCIExpressCapabilityIDSRIOV**
- **kIOPCIExpressCapabilityIDTPHRequester**
- **kIOPCIExpressCapabilityIDVC_MFVCPresent**
- **kIOPCIExpressCapabilityIDVFResizableBAR**
- **kIOPCIExpressCapabilityIDVSEC**
- **kIOPCISlotStatusAttentionButtonPressed**
- **kIOPCISlotStatusCommandCompleted**
- **kIOPCISlotStatusDataLinkLayerStateChanged**
- **kIOPCISlotStatusElectromechanicalInterlockState**
- **kIOPCISlotStatusMRLSensorChanged**
- **kIOPCISlotStatusMRLSensorState**
- **kIOPCISlotStatusPowerFaultDetected**
- **kIOPCISlotStatusPresenceDetectChanged**
- **kIOPCISlotStatusPresenceDetectState**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PCIDriverKit)*