# Containerization

Run Linux containers on macOS using lightweight virtual machines optimized for Apple silicon.

**Platforms:** macOS 26.0+ (Apple Silicon only)

## Overview

Containerization is an open-source Swift framework that enables native Linux container support on macOS. Unlike traditional containerization solutions that run multiple containers within a single large virtual machine, Apple's approach runs each Linux container inside its own lightweight virtual machine, providing hardware-level isolation with sub-second startup times.

The framework eliminates the need for third-party tools like Docker by providing a native, Swift-based solution optimized for Apple silicon and integrated with macOS 26's enhanced virtualization capabilities.

## Key Features

### Hardware-Level Isolation
Each Linux container runs inside its own lightweight VM, providing stronger security guarantees than traditional namespace-based container runtimes. This hypervisor-isolated approach is a from-scratch implementation optimized for Apple Silicon.

### Sub-Second Startup
Despite running containers in individual VMs, the framework achieves sub-second startup times through:
- **Optimized Linux Kernel** - Minimal, purpose-built kernel configuration
- **EXT4 Block Devices** - Container filesystems exposed as formatted EXT4 block devices
- **Apple Silicon Optimization** - Native ARM64 performance with hardware virtualization

### OCI Compatibility
The framework produces and consumes OCI-compatible container images, enabling:
- Pull and run images from any standard container registry
- Push locally-built images to registries
- Run images in any OCI-compatible application

> **macOS Golden Gate 27+:** Requires Apple silicon, which is now the only macOS 27 configuration. macOS 27 is the last release with full Rosetta 2 support, so any Intel-only image tooling in your container workflow needs a native replacement. See [Apple Silicon](apple-silicon.md).

## Topics

### Essentials

- [Meet Containerization](https://developer.apple.com/videos/play/wwdc2025/346/) - WWDC 2025 introduction video
- **Containerization** - Swift package for running Linux containers on macOS
- **Container CLI** - Command-line tool for creating and managing containers

### Architecture Components

**vminitd Init System**
A Swift-built init system that runs as the first process in each virtual machine. Handles critical tasks including:
- IP address assignment
- Filesystem mounting
- Process supervision

vminitd runs in an extremely constrained environment with no core utilities, dynamic libraries, or libc implementation to minimize attack surface.

**Virtualization.framework Integration**
Containerization leverages macOS's Virtualization.framework to create and manage lightweight VMs with hardware acceleration on Apple silicon.

**Static Linux SDK**
Uses Swift's Static Linux SDK to cross-compile static Linux binaries directly from macOS, utilizing musl for excellent static linking support.

### Container Operations

- **Creating containers** - Build container images from Dockerfiles or scratch
- **Running containers** - Execute containers with resource limits and networking
- **Managing images** - Pull, push, and manage OCI-compatible images
- **Networking** - Configure container networking and port forwarding
- **Volume mounting** - Share files between host and container

### Security Model

The framework provides multiple layers of security:

- **VM Isolation** - Each container runs in its own virtual machine
- **Minimal Attack Surface** - vminitd contains no unnecessary components
- **Hardware Security** - Leverages Apple silicon's hardware virtualization features
- **Sandboxing** - Containers operate in isolated environments

## Requirements

| Requirement | Details |
|-------------|---------|
| **Hardware** | Mac with Apple silicon (M1 or later) |
| **Operating System** | macOS 26.0 or later |
| **Xcode** | Xcode 26 or later (for development) |

> **Note:** Intel-based Macs are not supported. The framework requires Apple silicon's hardware virtualization capabilities.

## Getting Started

### Installation

The Containerization framework is available as a Swift package:

```swift
// Package.swift
dependencies: [
    .package(url: "https://github.com/apple/containerization.git", from: "1.0.0")
]
```

### Basic Usage

```swift
import Containerization

// Pull and run a container image
let container = try await Container.pull("alpine:latest")
try await container.run(command: ["echo", "Hello from container"])
```

### Container CLI

For command-line usage, the `container` CLI tool provides Docker-like commands:

```bash
# Pull an image
container pull alpine:latest

# Run a container
container run alpine:latest echo "Hello, World!"

# Build an image
container build -t myapp:latest .

# Push to registry
container push myapp:latest registry.example.com/myapp:latest
```

## Comparison with Docker

| Feature | Containerization | Docker Desktop |
|---------|------------------|----------------|
| **Isolation** | VM per container | Shared VM |
| **Startup Time** | Sub-second | Seconds |
| **Native Integration** | macOS native | Third-party |
| **Language** | Swift | Go |
| **Open Source** | Yes | Partial |
| **Apple Silicon** | Optimized | Supported |

## Open Source

Containerization is fully open-source under the Apache 2.0 license:

- **Framework**: [github.com/apple/containerization](https://github.com/apple/containerization)
- **CLI Tool**: [github.com/apple/container](https://github.com/apple/container)

## Related Frameworks

- [Virtualization](https://developer.apple.com/documentation/virtualization) - Create virtual machines on Apple silicon
- [Hypervisor](https://developer.apple.com/documentation/hypervisor) - Low-level virtualization APIs
- [Foundation](https://developer.apple.com/documentation/foundation) - Core system framework

## Developer Documentation

- [Containerization Framework](https://developer.apple.com/documentation/containerization) - API reference
- [Virtualization Framework](https://developer.apple.com/documentation/virtualization) - VM management
- [Swift Package Manager](https://developer.apple.com/documentation/xcode/swift-packages) - Package integration

## Videos

- [Meet Containerization](https://developer.apple.com/videos/play/wwdc2025/346/) - WWDC 2025 introduction
- [What's new in Virtualization](https://developer.apple.com/videos/play/wwdc2025/10132/) - macOS 26 virtualization updates

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/containerization) | [GitHub](https://github.com/apple/containerization)*
