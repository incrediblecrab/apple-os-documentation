# Virtualization

Create virtual machines and run macOS and Linux-based operating systems.

**Platforms:** macOS 11.0+

## Overview

The Virtualization framework provides high-level APIs for creating and managing virtual machines (VM) on Apple silicon and Intel-based Mac computers. Use this framework to boot and run macOS or Linux-based operating systems in custom environments that you define. The framework supports the Virtual I/O Device (VIRTIO) specification, which defines standard interfaces for many device types, including network, socket, serial port, storage, entropy, and memory-balloon devices.

To set up a VM, configure a VZVirtualMachineConfiguration. If you're creating a macOS guest also configure a VZMacPlatformConfiguration, and then add the devices you want to expose to the guest operating system. Then, create a VZVirtualMachineConfiguration object with your configuration data, and use that VM object to start, pause, and resume the VM environment. To interact with the guest, you create a VZVirtualMachineView with the VZVirtualMachine object to display and interact with the graphical content in a window.

## Topics

### Essentials
- [Adding the Virtualization Entitlement to Your Project](https://developer.apple.com/documentation/virtualization/adding_the_virtualization_entitlement_to_your_project) - Configure your project to use the Virtualization framework.
- [com.apple.security.virtualization](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_virtualization) - A Boolean value that indicates whether your app can use the Virtualization framework.
- [Using iCloud with macOS virtual machines](https://developer.apple.com/documentation/virtualization/using_icloud_with_macos_virtual_machines) - Access iCloud from macOS guest virtual machines.

### Virtual machine setup
- [Configure and boot different guest operating systems](https://developer.apple.com/documentation/virtualization/virtual_machine_setup)
- [Running macOS in a virtual machine on Apple silicon](https://developer.apple.com/documentation/virtualization/running_macos_in_a_virtual_machine_on_apple_silicon) - Install and run macOS in a virtual machine using the Virtualization framework.
- [Running Linux in a Virtual Machine](https://developer.apple.com/documentation/virtualization/running_linux_in_a_virtual_machine) - Run a Linux operating system on your Mac using the Virtualization framework.
- [Running GUI Linux in a virtual machine on a Mac](https://developer.apple.com/documentation/virtualization/running_gui_linux_in_a_virtual_machine_on_a_mac) - Install and run GUI Linux in a virtual machine using the Virtualization framework.
- [Installing macOS on a Virtual Machine](https://developer.apple.com/documentation/virtualization/installing_macos_on_a_virtual_machine) - Download a macOS restore image and install it in a new VM.
- [Creating and Running a Linux Virtual Machine](https://developer.apple.com/documentation/virtualization/creating_and_running_a_linux_virtual_machine) - Design and run custom Linux guests on Apple silicon or Intel-based Mac Computers.
- [Virtualize macOS on a Mac](https://developer.apple.com/documentation/virtualization/virtualize_macos_on_a_mac) - Configure and run macOS guests on Apple silicon.
- [Virtualize Linux on a Mac](https://developer.apple.com/documentation/virtualization/virtualize_linux_on_a_mac) - Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs with Rosetta](https://developer.apple.com/documentation/virtualization/running_intel_binaries_in_linux_vms_with_rosetta) - Run x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](https://developer.apple.com/documentation/virtualization/accelerating_the_performance_of_rosetta) - Improve Rosetta performance by adding support for the total store ordering (TSO) memory model to your Linux kernel.

### Runtime
- [View or control guest operating systems](https://developer.apple.com/documentation/virtualization/runtime)
- **VZVirtualMachine** - An object that manages the overall state and configuration of your VM.
- **VZVirtualMachineView** - A view that allows user interaction with a VM.
- **VZLinuxRosettaDirectoryShare** - The Linux directory share for Rosetta.

### Devices
- [Configure and connect devices to guest operating system instances](https://developer.apple.com/documentation/virtualization/devices)

#### Audio
- [Configure audio devices that enable the guest operating system to perform audio playback and capture through the host's audio devices](https://developer.apple.com/documentation/virtualization/audio)

#### Graphics
- [Configure a device for a guest to display its UI](https://developer.apple.com/documentation/virtualization/graphics)

#### Keyboards and pointing devices
- [Configure devices that connect a mouse and keyboard to the guest system](https://developer.apple.com/documentation/virtualization/keyboards_and_pointing_devices)

#### Memory
- [Configure a memory balloon device to change the allocated memory for the guest system](https://developer.apple.com/documentation/virtualization/memory)

#### Network
- [Configure the devices that connect the guest system to the network](https://developer.apple.com/documentation/virtualization/network)

#### Randomization
- [Configure a device for the guest system to use to generate random numbers](https://developer.apple.com/documentation/virtualization/randomization)

#### Serial ports
- [Configure the serial devices that you use to communicate with the guest system](https://developer.apple.com/documentation/virtualization/serial_ports)

#### Shared directories
- [Configure devices that share directories from the host into the guest system](https://developer.apple.com/documentation/virtualization/shared_directories)

#### Sockets
- [Configure a device that manages port-based communication with the guest system](https://developer.apple.com/documentation/virtualization/sockets)

#### Storage
- [Configure the block-storage devices that represent the disks of the guest system](https://developer.apple.com/documentation/virtualization/storage)

#### Consoles
- [Configure a device that manages multiport console communication with the guest system](https://developer.apple.com/documentation/virtualization/consoles)

#### Clipboard sharing
- [Share the pasteboard between the host and guest system](https://developer.apple.com/documentation/virtualization/clipboard_sharing)

#### USB Devices
- [USB Devices](https://developer.apple.com/documentation/virtualization/usb_devices)

### Enumerations
- [Virtualization enumerations](https://developer.apple.com/documentation/virtualization/virtualization_enumerations) - Control the caching modes, disk synchronization, and macOS auxiliary storage options of VMs.

### Errors
- **VZErrorDomain** - The error domain for the Virtualization framework.
- **VZError** - Errors that you might encounter when configuring or using a VM.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Virtualization)*