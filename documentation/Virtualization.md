# Virtualization

Create virtual machines and run macOS and Linux-based operating systems.

**Platforms:** macOS 11.0+

## Overview

The Virtualization framework provides high-level APIs for creating and managing virtual machines (VM) on Apple silicon and Intel-based Mac computers. Use this framework to boot and run macOS or Linux-based operating systems in custom environments that you define. The framework supports the Virtual I/O Device (VIRTIO) specification, which defines standard interfaces for many device types, including network, socket, serial port, storage, entropy, and memory-balloon devices.

To set up a VM, populate a `VZVirtualMachineConfiguration`, including its platform, boot loader, and devices. For a macOS guest, use `VZMacPlatformConfiguration` on supported Apple silicon hardware. Then create a **`VZVirtualMachine`** from the configuration; the VM, not the configuration object, owns the running guest's lifecycle. A `VZVirtualMachineView` can display and interact with its graphical output.

### Host, guest, and translation support

The framework's historical availability on Intel and Apple silicon is not a statement that every macOS release supports both as hosts. `VZVirtualMachine` virtualizes the host's architecture. Linux kernel and installation images must match that architecture. macOS guest support uses `VZMacPlatformConfiguration` on Apple silicon and starts in macOS 12; `VZVirtualMachineView` also starts in 12, not the framework's 11.0 minimum.

For macOS installation, select a restore image whose hardware model the host supports; `mostFeaturefulSupportedConfiguration` can be `nil`. Preserve the hardware model, machine identifier, and auxiliary storage when reopening that VM. New VMs need their own identifiers and auxiliary storage.

Check `VZVirtualMachine.isSupported`, validate the guest configuration, and handle startup and lifecycle errors. Every process using Virtualization requires the Boolean `com.apple.security.virtualization` entitlement. That entitlement does not itself require App Sandbox and does not grant arbitrary disk, directory, or microphone access. A bridged network attachment additionally requires the restricted `com.apple.vm.networking` entitlement; a NAT attachment does not.

### Intel Linux translation and iCloud

Intel Linux translation runs supported x86_64 applications inside an **ARM Linux guest**; it does not boot an Intel Linux kernel on Apple silicon. In macOS 13–26, check Rosetta availability and handle authorization, download, and installation failures.

**macOS 27 beta changes this requirement:** Intel Linux translation is included in macOS. Apple's guide states that `VZLinuxRosettaDirectoryShare.availability` returns `.installed` and `installRosetta` completes immediately. The Rosetta-named directory-share API and guest-side mounting/binary-handler setup still apply. Dynamically linked applications also need their matching Linux libraries. Do not apply the separate macOS-app Rosetta upgrade warning to this built-in Linux translation path.

iCloud access requires a qualifying VM created on macOS 15+ from a macOS 15+ restore image on Apple silicon. Merely upgrading an older VM does not enable iCloud. Moving the VM to another Mac, or running an additional clone concurrently, changes its derived identity and requires reauthentication.

### macOS 27 beta: disk-image and device integration

**Reviewed September 8, 2026:** [DiskImageKit](DiskImageKit.md) adds standalone and stacked ASIF/raw images through `VZDiskImageStorageDeviceAttachment(diskImage:)`. Its additional caching and synchronization arguments have defaults. Gate this path on macOS 27 rather than the framework's 11.0 minimum.

Keep disk-image layering separate from guest-filesystem resizing and VM snapshots. Handle incompatible image stacks and storage errors. See DiskImageKit for layer ordering and UUID constraints.

The 27 beta also adds custom Virtio devices for Linux guests and physical USB passthrough. `VZCustomVirtioDeviceConfiguration` describes a device that the VMM implements through the delegate/provider APIs; this is not a host DriverKit driver. `VZUSBPassthroughDeviceConfiguration` takes an [AccessoryAccess](AccessoryAccess.md) `AAUSBAccessory`, not a raw arbitrary USB identifier. Capture occurs when the VM starts or attaches the device, not merely when the configuration object is created.

## Topics

### Essentials
- [Adding the Virtualization Entitlement to Your Project](https://developer.apple.com/documentation/virtualization/adding-the-virtualization-entitlement-to-your-project) - Configure your project to use the Virtualization framework.
- [com.apple.security.virtualization](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.virtualization) - A Boolean value that indicates whether your app can use the Virtualization framework.
- [Using iCloud with macOS virtual machines](https://developer.apple.com/documentation/virtualization/using-icloud-with-macos-virtual-machines) - Identity and reauthentication requirements for qualifying macOS 15+ guests.

### Virtual machine setup
Configure the boot loader, platform, and devices for the selected guest.

- [Running macOS in a virtual machine on Apple silicon](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon) - Installer and GUI sample apps in Swift and Objective-C; the sample's default deployment target is macOS 14.
- [Running Linux in a Virtual Machine](https://developer.apple.com/documentation/virtualization/running-linux-in-a-virtual-machine) - A command-line kernel/initial-RAM-disk sample with a serial console.
- [Running GUI Linux in a virtual machine on a Mac](https://developer.apple.com/documentation/virtualization/running-gui-linux-in-a-virtual-machine-on-a-mac) - Install from an architecture-matching ISO and run a GUI guest; the sample defaults to macOS 14.
- [Installing macOS on a Virtual Machine](https://developer.apple.com/documentation/virtualization/installing-macos-on-a-virtual-machine) - Download a compatible restore image and install it into a stopped VM.
- [Creating and Running a Linux Virtual Machine](https://developer.apple.com/documentation/virtualization/creating-and-running-a-linux-virtual-machine) - Design and run custom Linux guests on Apple silicon or Intel-based Mac computers.
- [Virtualize macOS on a Mac](https://developer.apple.com/documentation/virtualization/virtualize-macos-on-a-mac) - Configure and run macOS guests on Apple silicon.
- [Virtualize Linux on a Mac](https://developer.apple.com/documentation/virtualization/virtualize-linux-on-a-mac) - Configure and run Linux guests on Apple silicon and Intel-based Mac computers.
- [Running Intel Binaries in Linux VMs](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms) - Run supported x86_64 Linux binaries under ARM Linux on Apple silicon.
- [Accelerating the performance of Rosetta](https://developer.apple.com/documentation/virtualization/accelerating-the-performance-of-rosetta) - Add Linux-kernel support for a per-thread total store ordering (TSO) memory model.

### Runtime
View and control the guest through runtime objects, not the configuration object.
- **VZVirtualMachine** - An object that manages the overall state and configuration of your VM.
- **VZVirtualMachineView** - A view that displays the VM and forwards input through configured devices; macOS 12+.
- **VZLinuxRosettaDirectoryShare** - Directory sharing for Intel Linux translation; macOS 13+, with built-in translation availability in 27.

### Devices
Configure devices appropriate to the guest and host, including their individual availability and access requirements.

#### Audio
- [Audio](https://developer.apple.com/documentation/virtualization/audio) - Configure playback and input devices. Host microphone input requires `NSMicrophoneUsageDescription` and permission; Linux Virtio sound needs `CONFIG_SND_VIRTIO`.

#### Graphics
- [Configure a device for a guest to display its UI](https://developer.apple.com/documentation/virtualization/graphics)

#### Keyboards and pointing devices
- [Configure devices that connect a mouse and keyboard to the guest system](https://developer.apple.com/documentation/virtualization/keyboards-and-pointing-devices)

#### Memory
- [Memory](https://developer.apple.com/documentation/virtualization/memory) - Request physical-memory reclamation through a Virtio balloon. The guest may decline to return pages; this is not guaranteed forced reclamation.

#### Network
- [Configure the devices that connect the guest system to the network](https://developer.apple.com/documentation/virtualization/network)

#### Randomization
- [Configure a device for the guest system to use to generate random numbers](https://developer.apple.com/documentation/virtualization/randomization)

#### Serial ports
- [Configure the serial devices that you use to communicate with the guest system](https://developer.apple.com/documentation/virtualization/serial-ports)

#### Shared directories
- [Shared directories](https://developer.apple.com/documentation/virtualization/shared-directories) - Expose selected host directories through VirtioFS. macOS guests require macOS 13+; Linux guests need `CONFIG_VIRTIO_FS`.

#### Sockets
- [Configure a device that manages port-based communication with the guest system](https://developer.apple.com/documentation/virtualization/sockets)

#### Storage
- [Configure the block-storage devices that represent the disks of the guest system](https://developer.apple.com/documentation/virtualization/storage)

#### Consoles
- [Configure a device that manages multiport console communication with the guest system](https://developer.apple.com/documentation/virtualization/consoles)

#### Clipboard sharing
- [Clipboard sharing](https://developer.apple.com/documentation/virtualization/clipboard-sharing) - SPICE-agent clipboard support starts in macOS 13; Linux guests need `spice-vdagent`.

#### USB Devices
- [USB Devices](https://developer.apple.com/documentation/virtualization/usb-devices) - Controllers and virtual USB devices; physical passthrough uses the separate 27 beta APIs.

#### Custom Virtio devices
- [Custom Virtio drivers](https://developer.apple.com/documentation/virtualization/custom-drivers) - Implement custom Virtio devices for Linux guests using the macOS 27 beta configuration, delegate, and queue APIs.

### Enumerations
- [Virtualization enumerations](https://developer.apple.com/documentation/virtualization/virtualization-enumerations) - Control the caching modes, disk synchronization, and macOS auxiliary storage options of VMs.

### Errors
- **VZErrorDomain** - The error domain for the Virtualization framework.
- **VZError** - Errors that you might encounter when configuring or using a VM.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Virtualization)*

*Additional primary sources: [VZVirtualMachine](https://developer.apple.com/documentation/virtualization/vzvirtualmachine.md), [Intel Linux translation](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms.md), [DiskImageKit](https://developer.apple.com/documentation/diskimagekit.md), and [macOS 27 release notes — Disk Images](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md).*
