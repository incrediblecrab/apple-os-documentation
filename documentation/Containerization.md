# Containerization

Run Linux containers on macOS using lightweight virtual machines optimized for Apple silicon.

**Platforms:** macOS 26.0+ for the documented Mac workflow; Apple silicon required

**Status:** Open-source Swift package, not an OS 27 SDK framework. Reviewed at source revisions available September 8, 2026.

## Overview

The `apple/containerization` Swift package supplies low-level Linux-container, image, filesystem, and process-management components. On Mac it uses Virtualization.framework and runs each container in its own lightweight Linux VM.

The separate `apple/container` project builds a command-line application on that package. Library APIs, the `cctl` development executable, and commands provided by the `container` application are different interfaces. Do not assume Docker CLI or Docker Engine API compatibility merely because they can consume OCI images.

## Projects and responsibilities

| Project | Use it for |
| --- | --- |
| [apple/containerization](https://github.com/apple/containerization) | Embedding the Swift libraries for OCI images, registries, ext4 filesystems, virtual machines, and containerized processes. |
| [apple/container](https://github.com/apple/container) | Installing and using the `container` CLI, including its service, image, run, and build commands. |

Containerization's Mac architecture includes an optimized Linux kernel, ext4-backed storage, and `vminitd`, a guest init process that manages processes and communicates with the host over vsock. The upstream README describes sub-second startup as a design characteristic, not a latency guarantee for every image, download, or workload.

OCI compatibility concerns image formats and registry interaction. It does not guarantee that an image's architecture, required kernel features, privileges, or host integrations are supported.

The checked upstream revision also documents a Linux backend using cloud-hypervisor and KVM. That is a separate host setup; this page's Mac requirements and example do not describe that backend.

## Topics

### Library integration

- [Package API documentation](https://apple.github.io/containerization/documentation/) — Products and public types.
- [OCI image operations in `cctl`](https://github.com/apple/containerization/blob/9eacc197d7c3663eb29cbab6d51244ede6d1cd7d/Sources/cctl/ImageCommand.swift) — A checked example of image-store and registry operations.
- [Container lifecycle in `cctl`](https://github.com/apple/containerization/blob/9eacc197d7c3663eb29cbab6d51244ede6d1cd7d/Sources/cctl/RunCommand.swift) — A checked example that prepares the image and root filesystem, creates a container, and starts it.
- [LinuxContainer](https://github.com/apple/containerization/blob/9eacc197d7c3663eb29cbab6d51244ede6d1cd7d/Sources/Containerization/LinuxContainer.swift) — Library implementation for a container's VM lifecycle.
- [LinuxProcess](https://github.com/apple/containerization/blob/9eacc197d7c3663eb29cbab6d51244ede6d1cd7d/Sources/Containerization/LinuxProcess.swift) — Containerized process management.

Select a real package release and consult the examples for that revision. The package is under active development and may change source interfaces between minor releases. Use the checked lifecycle examples rather than assuming a single-call pull-and-run Swift API.

## Requirements

| Requirement | Details |
|-------------|---------|
| **Mac hardware** | Apple silicon; an Intel Mac is not a supported Mac host for these projects. |
| **Mac operating system** | Upstream documents macOS 26 support and does not support older macOS releases. Validate newer beta hosts with the selected release. |
| **Library build tools** | The checked Containerization README specifies Xcode 26; its package manifest uses Swift tools version 6.2. Follow that revision's build instructions. |
| **Using Xcode 27 beta 6** | Xcode requires macOS Tahoe 26.4 or later. It does not require a macOS 27 host. |

The pinned `Package.swift` declares a macOS 15 deployment floor for package products. That compilation setting is different from the README's supported macOS 26 Mac workflow; it does not establish support for running the complete container stack on macOS 15.

Running `linux/amd64` applications in an ARM Linux VM is not equivalent to running an Intel host or guest kernel. On the supported macOS 26 workflow, handle Rosetta availability and installation separately from VM support. **macOS 27 includes Intel Linux translation directly:** Apple's Virtualization guide says the Rosetta-named availability API returns `.installed` and installation completes immediately. The directory-share and guest-runtime setup still apply.

The macOS 27 release-note warning about Rosetta not being restored on upgrade concerns the separate macOS-app translation path; do not treat it as a requirement to install Rosetta for Linux containers on 27.

## CLI example

After installing the **separate `container` application** from its official releases, its checked README demonstrates:

```bash
container system start
container run --rm alpine echo hello
```

The run command pulls the image if necessary, starts a Linux VM, executes the command, and removes the container after exit. It requires working image access and a usable local service; it is not Swift library code. For other operations, use the [checked CLI command reference](https://github.com/apple/container/blob/9a8917ca2da5cd6ba059b9ba5ca5a74892e9bb7d/docs/command-reference.md).

## Resource access and failures

VM isolation does not make images trustworthy or remove the impact of shared files and network access. Grant only the host mounts and connectivity the workload needs. Keep credentials out of images and diagnostic output.

Handle registry authorization failures, missing images or kernels, unsupported image architectures, storage exhaustion, VM startup failures, and process exit status. Clean up only resources owned by the failed operation, preserving user data and unrelated containers.

An embedded Mac VM implementation still needs the appropriate [Virtualization entitlement](https://developer.apple.com/documentation/virtualization/adding-the-virtualization-entitlement-to-your-project); installing the CLI is not a substitute for configuring the embedding app.

## Related Frameworks

- [Virtualization](Virtualization.md) - High-level VM configuration and lifecycle.
- [Hypervisor](https://developer.apple.com/documentation/hypervisor) - Low-level virtualization APIs

## Sources

- [Containerization README at September 8 cutoff](https://github.com/apple/containerization/blob/9eacc197d7c3663eb29cbab6d51244ede6d1cd7d/README.md)
- [container README at September 8 cutoff](https://github.com/apple/container/blob/9a8917ca2da5cd6ba059b9ba5ca5a74892e9bb7d/README.md)
- [Xcode 27 beta 6 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md)
- [Intel Linux translation, including the macOS 27 change](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms)
- [macOS 27 release notes — Rosetta](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md)
