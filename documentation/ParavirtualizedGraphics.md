# Paravirtualized Graphics

Add graphics acceleration to your guest driver stack.

**Platforms:** Mac Catalyst 14.0+ | macOS 11.0+

## Overview

If you have an app that implements hardware-level virtualization, performance inside the virtual machine is critical, particularly for graphics. The **ParavirtualizedGraphics** framework implements hardware-accelerated graphics for macOS running in a virtual machine, hereafter known as the guest. The operating system provides a graphics driver that runs inside the guest, communicating with the framework in the host operating system to take advantage of Metal-accelerated graphics.

To implement accelerated graphics inside your virtualization solution, you need to take the following steps for each virtual machine:

1. Advertise the virtual graphics card in the virtual machine hardware so that macOS can install the correct driver.

2. Create a **PGDeviceDescriptor**, providing the necessary blocks to connect your virtual machine implementation to the ParavirtualizedGraphics framework. Use this descriptor to create a **PGDevice** object, which you keep alive as long as the virtual machine is still active. The ParavirtualizedGraphics framework calls your blocks when it needs to allocate memory or take other relevant actions.

3. Create a **PGDisplayDescriptor** for each virtual display that you want to connect to the device, specifying the display's properties and blocks for the framework to call for display events. Use this descriptor to create a **PGDisplay** object. Handle the appropriate display events to display the graphics data that the framework provides.

## Topics

### PCI Device Characteristics
- **PG_PCI_DEVICE_ID** - The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_VENDOR_ID** - The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_BAR_MMIO** - The base address register to use when advertising the graphics stack inside a virtual machine.
- **PG_PCI_MAX_MSI_VECTORS** - The number of MSI vectors that you need to allocate for the graphics configuration.
- **PGCopyOptionROMURL()** - Copies the URL of the ROM image to use on the guest graphics device.

### Devices
- **PGNewDeviceWithDescriptor()** - Creates a new paravirtualized graphics device.
- **PGDeviceDescriptor** - A description of the paravirtualized graphics device to create.
- **PGDevice** - A paravirtualized GPU device object.

### Displays
- **PGDisplayDescriptor** - A descriptor for a virtual display.
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
- **PGCreateDeviceWithDescriptor()** - Creates a new paravirtualized graphics device.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ParavirtualizedGraphics)*