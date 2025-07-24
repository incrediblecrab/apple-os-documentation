# Core Media I/O

Securely support custom camera devices in macOS.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.7+

## Overview

Use the Core Media I/O framework to enable support for custom camera devices in macOS. Starting in macOS 12.3, the framework builds on System Extensions to enable you to support custom devices while maintaining system privacy and security protections. The system prevents apps from loading extension code into their process to ensure that they can't bypass macOS privacy protections or mask their identity.

**Important**  
Apple recommends replacing legacy Device Abstraction Layer (DAL) plug-ins with Core Media I/O extensions.

## Topics

### Providers
- [Creating a camera extension with Core Media I/O](https://developer.apple.com/documentation/coremediaio/creating_a_camera_extension_with_core_media_i_o) - Build high-performance camera drivers that are secure and simple to deploy.
- [Overriding the default USB video class extension](https://developer.apple.com/documentation/coremediaio/overriding_the_default_usb_video_class_extension) - Create a simple DriverKit extension to override the default driver-matching behavior for USB devices.
- **CMIOExtensionProvider** - An object that manages device connections for a provider.
- **CMIOExtensionProviderSource** - A protocol for objects that act as provider sources.
- **CMIOExtensionProviderProperties** - An object that manages the properties of an extension provider.

### Devices
- **CMIOExtensionDevice** - An object that represents a physical or virtual device.
- **CMIOExtensionDeviceSource** - A protocol for objects that act as device sources.
- **CMIOExtensionDeviceProperties** - An object that defines the properties of a device.

### Streams
- **CMIOExtensionStream** - An object that represents a stream of media data.
- **CMIOExtensionStreamSource** - A protocol for objects that act as stream sources.
- **CMIOExtensionStreamProperties** - An object that describes the properties of an extension stream.
- **CMIOExtensionClient** - An object that represents a client of the extension.

### Properties
- **CMIOExtensionProperty** - A structure that defines the properties that providers, devices, and streams support.
- **CMIOExtensionPropertyState** - An object that describes the state of a property.
- **CMIOExtensionPropertyAttributes** - An object that describes the attributes of a property.
- **CMIOExtensionInfoDictionaryKey** - A key that specifies the extension information dictionary.
- **CMIOExtensionMachServiceNameKey** - A key that specifies the mach service name.

### DAL Plug-Ins
- [Device Abstraction Layer (DAL) Plug-Ins](https://developer.apple.com/documentation/coremediaio/device_abstraction_layer_dal_plug-ins) - API reference for legacy DAL plug-ins.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreMediaIO)*