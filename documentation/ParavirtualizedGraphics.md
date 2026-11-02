# Paravirtualized Graphics

Add graphics acceleration to your guest driver stack.

**Platforms:** macOS 11.0+ for the native virtual-machine graphics interfaces described here.

Mac Catalyst is omitted on purpose. Apple's framework and symbol pages list Mac Catalyst 14.0, but the SDK headers mark the framework's interfaces unavailable on iOS, and the compiler carries that to Mac Catalyst: in both the macOS 26.5 and 27.2 SDKs, a Mac Catalyst build rejects `PGDeviceDescriptor`, `PGDevice`, `PGDisplayDescriptor`, `PGCreateDeviceWithDescriptor(_:)` and `PGCopyOptionROMURL()` as unavailable. Only the `PG_PCI_*` values, which are preprocessor constants with no availability annotation, compile there. Do not infer a working Catalyst virtualization path from that catalog entry.

## Overview

If you have an app that implements hardware-level virtualization, performance inside the virtual machine is critical, particularly for graphics. The **ParavirtualizedGraphics** framework implements hardware-accelerated graphics for macOS running in a virtual machine, hereafter known as the guest. The operating system provides a graphics driver that runs inside the guest, communicating with the framework in the host operating system to take advantage of Metal-accelerated graphics.

To implement accelerated graphics inside your virtualization solution, you need to take the following steps for each virtual machine:

1. Advertise the virtual graphics card in the virtual machine hardware so that macOS can install the correct driver.

2. Create a **PGDeviceDescriptor**, providing the necessary blocks to connect your virtual machine implementation to the ParavirtualizedGraphics framework. On macOS 15.2 and later, use `PGCreateDeviceWithDescriptor(_:)` to create the device and handle a `nil` result. Keep the device alive while the virtual machine uses it. The framework calls the descriptor's `raiseInterrupt` block to raise interrupts in the guest. The descriptor's guest-memory blocks (`createTask`, `destroyTask`, `mapMemory`, `unmapMemory`, `readMemory`, `addTraceRange` and `removeTraceRange`) are obsoleted in macOS 27.0: the macOS 27 SDK header says the legacy memory-mapping path has been removed, and code that sets them fails to compile for a macOS 27 deployment target.

3. Create a **PGDisplayDescriptor** for each virtual display that you want to connect to the device, specifying the display's properties and blocks for the framework to call for display events. Use this descriptor to create a **PGDisplay** object. Handle the appropriate display events to display the graphics data that the framework provides.

## Topics

### PCI Device Characteristics
- **PG_PCI_DEVICE_ID** - The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_VENDOR_ID** - The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_BAR_MMIO** - The base address register to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_MAX_MSI_VECTORS** - The number of MSI vectors that you need to allocate for the graphics configuration.
- **PGCopyOptionROMURL()** - Copies the URL of the ROM image to use on the guest graphics device. Deprecated in macOS 27.0; the SDK header says the option ROM is no longer used.

### Devices
- **PGNewDeviceWithDescriptor(_:)** - The legacy factory, introduced in macOS 11 and deprecated in macOS 15.2 in favor of `PGCreateDeviceWithDescriptor`. The replacement has the corrected ARC ownership annotation. The macOS 27 SDK still declares the legacy factory but marks it obsoleted in macOS 27.0: a call builds with a deprecation warning for a macOS 15.2 deployment target and fails as unavailable for a macOS 27.0 target.
- **PGDeviceDescriptor** - A description of the paravirtualized graphics device to create.
- **PGDevice** - A paravirtualized GPU device object.

### Displays
- **PGDisplayDescriptor** - A descriptor for a virtual display. Its legacy `cursorGlyphHandler` is obsoleted in macOS 27.0.
- **PGDisplay** - An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- **PGDisplayMode** - A description of a supported display mode.
- **PGDisplayCoord_t** - Coordinates that describe sizes or offsets within a 2D array of pixels.

### Reference
- **ParavirtualizedGraphics Constants**
- **ParavirtualizedGraphics Functions**
- **ParavirtualizedGraphics Data Types**

### Variables
- **HAS_NS_BITMAP_HEADER**
- **PG_SUPPORT_CREATE_DEVICE**

### Functions
- [PGCreateDeviceWithDescriptor(_:)](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcreatedevicewithdescriptor(_:)) - The macOS 15.2+ factory returns an optional `PGDevice` implementation.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ParavirtualizedGraphics)*
