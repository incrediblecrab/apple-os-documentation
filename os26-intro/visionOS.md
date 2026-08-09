# visionOS 26.0 Developer Introduction

Apple Vision Pro offers an infinite canvas to explore, experiment, and play — giving you the freedom to completely rethink your app's spatial computing experience. Using familiar frameworks and tools, you can design and build an entirely new universe of apps and games for Vision Pro.

**Platform:** visionOS 26.0+

> **Generation status:** visionOS 26 is the current shipping line — **visionOS 26.6**, released July 27, 2026. visionOS 27 is in beta; see [os27-intro/visionOS.md](../os27-intro/visionOS.md).

## Overview

visionOS 26.0 represents the future of spatial computing, enabling developers to create immersive experiences that seamlessly blend digital content with the physical world. This release introduces advanced spatial capabilities, enhanced performance, and new frameworks for building the next generation of applications.

## Key Features

### Spatial Computing

**A spectrum of immersion**  
Create experiences that range from familiar app windows to fully immersive environments. Transition smoothly between different levels of immersion based on user intent and context.

**3D Interface Design**  
Design interfaces that exist in three-dimensional space, allowing users to interact with content naturally using their eyes, hands, and voice.

**Spatial Positioning**  
Place content precisely in the user's environment, creating persistent spatial relationships that enhance usability and create magical experiences.

### Development Frameworks

**SwiftUI for visionOS**  
Build beautiful, compelling apps using familiar SwiftUI patterns enhanced for spatial computing. Create interfaces that automatically adapt to different immersion levels and spatial contexts.

**RealityKit Integration**  
Add depth and dimension to your applications with RealityKit. Create realistic 3D content, lighting, and physics that respond naturally to the user's environment.

**ARKit Capabilities**  
Understand your surroundings with advanced ARKit features. Access world tracking, plane detection, and occlusion to create spatially-aware experiences.

### User Interaction

**Eye and Hand Tracking**  
Leverage precise eye and hand tracking for intuitive, natural interactions. Users can look at objects to focus on them and use hand gestures to manipulate content.

**Voice Integration**  
Support Siri and voice commands for hands-free interaction, especially useful in immersive experiences where traditional touch interfaces aren't available.

**Accessibility Excellence**  
Create experiences that work for everyone with built-in accessibility features including VoiceOver for spatial interfaces and switch control support.

### Advanced Capabilities

**Immersive Environments**  
Transport users to entirely new worlds with full immersion experiences. Create environments that replace the user's surroundings for gaming, entertainment, and specialized applications.

**Shared Experiences**  
Enable multiple Vision Pro users to share the same spatial experience, perfect for collaboration, gaming, and social applications.

**Passthrough Integration**  
Seamlessly blend digital content with the real world using high-quality passthrough video that maintains spatial relationships.

## What's New in visionOS 26.0

Dive into the latest key technologies and capabilities:

- **Liquid Glass Design**: Unified design language across Apple platforms with spatial adaptations
- **Enhanced Spatial Tracking**: Improved precision and stability for world tracking
- **Advanced Hand Tracking**: More accurate finger tracking and gesture recognition
- **Performance Optimizations**: Better graphics performance and thermal management
- **Expanded RealityKit**: New materials, lighting models, and physics capabilities
- **Improved Accessibility**: Enhanced VoiceOver and assistive technology support
- **Developer Tools**: Better debugging and profiling tools for spatial applications
- **Shared AR**: Multi-user spatial experiences and collaboration features
- **Spatial Widgets**: Widgets that integrate seamlessly into the user's space
- **Spatial Scenes**: Photos that come alive in the user's environment
- **Spatial Browsing**: Enhanced Safari experience for spatial computing

### visionOS 26.1 Updates (November 2025)
- **Vision Pro app for iPad**: Control and interact with Vision Pro from iPad
- Performance improvements and bug fixes
- Enhanced collaboration features

### visionOS 26.2 Updates
- Stability and bug-fix release; see the [visionOS 26.2 Release Notes](https://developer.apple.com/documentation/visionOS-Release-Notes/visionos-26_2-release-notes) for details

### visionOS 26.3 Updates
- Stability and bug-fix release; see the [visionOS 26.3 Release Notes](https://developer.apple.com/documentation/visionOS-Release-Notes/visionos-26_3-release-notes) for details

### visionOS 26.4 Updates
- **Foveated Streaming with NVIDIA CloudXR**: Stream high-resolution, low-latency immersive content to Vision Pro using foveated streaming via the new [`FoveatedStreaming`](https://developer.apple.com/documentation/foveatedstreaming) framework
- **Background Assets offline APIs**: Check asset-pack status offline; ensure latest version is available locally
- **StoreKit revocation fields**: New `Transaction.revocationType` and `Transaction.revocationPercentage` properties
- **SwiftUI fix**: `.userActivity` now correctly surfaces as the current user activity
- **Networking fix**: Resolves `CFRunLoopSource` leaks when PAC or Auto proxy discovery is configured

### visionOS 26.5 and 26.6 Updates
- visionOS 26.5 shipped during spring 2026
- **visionOS 26.6 (July 27, 2026)** is the current shipping release of the OS 26 line
- See the [visionOS Release Notes](https://developer.apple.com/documentation/visionos-release-notes) for the latest changes

> **Looking ahead:** visionOS 27 is in developer beta as of August 2026. See the [visionOS 27 Developer Introduction](../os27-intro/visionOS.md).

## Getting Started

**New to visionOS development?**  
Check out the [visionOS Pathway](https://developer.apple.com/visionos/), an easy-to-navigate collection of resources to get started with spatial computing development.

### Development Tools

**Xcode for visionOS**  
Visualize and build spatial applications with enhanced Xcode support including visionOS simulators and spatial debugging tools.

**Reality Composer Pro**  
Create 3D content for your apps with Reality Composer Pro. Design scenes, import 3D models, and configure materials and lighting without writing code.

**Unity Integration**  
Bring existing Unity projects to visionOS or create new spatial experiences using familiar Unity workflows and tools.

## Developer Success Stories

### Blackbox
Learn how Ryan McLeod rebooted his inventive puzzle game for visionOS, taking advantage of spatial interfaces and immersive gameplay mechanics.

### Super Fruit Ninja
How Halfbrick cultivated Super Fruit Ninja on Apple Vision Pro, creating an entirely new way to experience the classic game in 3D space.

### djay
Realizing their vision: How djay designed for visionOS, transforming traditional DJ workflows into spatial, immersive experiences.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment with visionOS simulators
- [Reality Composer Pro](https://developer.apple.com/augmented-reality/reality-composer-pro/) - 3D content creation and scene design
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for visionOS apps

### Documentation
- [visionOS Developer Documentation](https://developer.apple.com/documentation/visionos/)
- [RealityKit Documentation](https://developer.apple.com/documentation/realitykit/)
- [ARKit Documentation](https://developer.apple.com/documentation/arkit/)
- [Spatial Computing Guidelines](https://developer.apple.com/design/human-interface-guidelines/spatial-computing/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Mobile companion experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - Desktop development and content creation
- [tvOS](tvOS.md) - Living room entertainment
- [watchOS](watchOS.md) - Wearable integration

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to create groundbreaking spatial computing experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) to access beta software, advanced app capabilities, and distribution through the App Store for Apple Vision Pro.

### Design Principles
- **Spatial Interface Guidelines**: Best practices for designing in three-dimensional space
- **Immersion Patterns**: Effective transitions between different levels of immersion
- **Accessibility in Spatial Computing**: Creating inclusive experiences for all users

---

*Platform requirements and feature availability may vary. Apple Vision Pro availability varies by region. Some capabilities may require specific hardware features.*

*Reviewed 2026-08-09 against the OS 27 generation. See [os27-intro](../os27-intro/) for the current beta line.*
