# Hypervisor

Build virtualization solutions on top of a lightweight hypervisor, without third-party kernel extensions.

**Platforms:** macOS 10.10+

## Overview

Hypervisor provides C APIs for hardware-assisted virtualization in user space, without requiring a third-party kernel extension. It supplies lower-level VM, memory-mapping, and virtual-CPU operations rather than the complete guest configuration and virtual devices of the [Virtualization](Virtualization.md) framework.

Use this framework to create and control hardware-facilitated virtual machines and virtual processors (VMs and vCPUs) from your entitled, sandboxed, user-space process. Hypervisor abstracts virtual machines as processes, and virtual processors as threads.

### Requirements

The Hypervisor framework has the following requirements:

**Supported hardware**  
The Hypervisor framework requires hardware support to virtualize hardware resources. On Apple silicon, that includes the Virtualization Extensions. On Intel-based Mac computers, the framework supports machines with an Intel VT-x feature set that includes Extended Page Tables (EPT) and Unrestricted Mode.

At runtime, determine whether the Hypervisor APIs are available on a particular machine with the sysctl command, passing kern.hv_support as an argument.

These are historical framework hardware requirements, not a list of Macs eligible for every later macOS release. Use the architecture-specific API reference and test runtime support; running Intel applications through Rosetta does not make an Intel Mac eligible to host macOS 27.

**Entitlements**  
Every process using the current Hypervisor APIs needs the Boolean [`com.apple.security.hypervisor`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hypervisor) entitlement, not only sandboxed processes. It was introduced in macOS 11. Apps deploying to macOS 10.15 or earlier must additionally include the legacy Boolean `com.apple.vm.hypervisor` entitlement. These are distinct from `com.apple.security.virtualization`, used by the higher-level framework.

### Virtual Resource Mapping

A guest is an operating system that runs on top of the virtual hardware. The operating system and processes that run the virtualized hardware are together called the host. Virtual hardware in the guest maps to specific resources on the host.

Each virtual machine corresponds to a process on the host. There can only be one Hypervisor VM at a time per process; the host process creates it with `hv_vm_create`.

Virtual CPUs map to POSIX threads. Create a vCPU for the current thread with `hv_vcpu_create`, then run it with `hv_vcpu_run`. The Apple silicon C function takes three arguments, including an exit-information output pointer; the Intel function takes two. The Apple silicon API family starts in macOS 11, rather than the framework's historical Intel minimum of 10.10.

Hypervisor maps guest physical memory to virtual memory in the host process with `hv_vm_map`. Access to unmapped guest physical memory causes a VM exit. A VMM can handle a memory-mapped device access at that exit and reenter the guest with `hv_vcpu_run`.

### Example VM Life Cycle

The following is a resource-lifecycle outline, not a complete bootable VMM. A working implementation also needs guest code, initial CPU state, and appropriate device handling. Use the architecture-specific signatures and handle errors at each step.

At the start of a task:

1. Create a VM with `hv_vm_create`.
2. Map host memory into the guest physical address space with `hv_vm_map`.
3. Create one or more POSIX threads with `pthread_create`.

In each thread:

1. Create a virtual CPU with the architecture-specific `hv_vcpu_create`.
2. Call `hv_vcpu_run` to run the vCPU.

When a thread receives an exit event:

1. Handle the event.
2. Reenter the guest with `hv_vcpu_run` or destroy the vCPU with `hv_vcpu_destroy`.

After all threads finish:

1. Unmap the memory region with `hv_vm_unmap`.
2. Destroy the VM with `hv_vm_destroy`.

### Intermediate physical address granules

The `hv_ipa_granule_t` type, `HV_IPA_GRANULE_4KB`, `HV_IPA_GRANULE_16KB`, and the three granule configuration functions listed below are **macOS 26+ Apple silicon APIs**. Query the default and validate configuration results rather than assuming that an Intel VM or an older system supports these choices.

## Topics

### Platforms
- [Apple Silicon](https://developer.apple.com/documentation/hypervisor/apple-silicon) - Architecture-specific APIs starting in macOS 11.
- [Intel-based Mac](https://developer.apple.com/documentation/hypervisor/intel-based-mac) - Historical Intel APIs starting in macOS 10.10.

### Entitlements
- [com.apple.security.hypervisor](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hypervisor) - Current Boolean entitlement for Hypervisor use.
- [com.apple.vm.networking](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.networking) - Separate, restricted Boolean entitlement for virtual-network access without root privileges; not marked deprecated.
- [com.apple.vm.device-access](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.device-access) - Separate Boolean entitlement for IOUSBHost USB-device capture; not marked deprecated.

### Legacy entitlement
- [com.apple.vm.hypervisor](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.hypervisor) - Deprecated in macOS 11; include alongside the current entitlement when back-deploying earlier than macOS 11.

### Reference
- [Hypervisor Structures](https://developer.apple.com/documentation/hypervisor/hypervisor-structures)
- [Hypervisor Constants](https://developer.apple.com/documentation/hypervisor/hypervisor-constants)
- [Hypervisor Functions](https://developer.apple.com/documentation/hypervisor/hypervisor-functions)
- [Hypervisor Data Types](https://developer.apple.com/documentation/hypervisor/hypervisor-data-types)

### Structures
- **hv_ipa_granule_t**

### Variables
- **HV_IPA_GRANULE_16KB**
- **HV_IPA_GRANULE_4KB**

### Functions
- **hv_vm_config_get_default_ipa_granule**
- **hv_vm_config_get_ipa_granule**
- **hv_vm_config_set_ipa_granule**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Hypervisor)*
