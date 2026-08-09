# Core AI

Deploy on-device AI models with a modern Swift API and deep Apple silicon integration.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

> **Medium confidence:** Core AI details are based on WWDC 2026 coverage, including session 324, “Meet Core AI.” Confirm availability and API details against Apple's documentation and the Xcode 27 SDK. The full API surface is not documented here.

## Overview

Core AI is a new OS 27 framework for deploying on-device AI models with a modern, memory-safe Swift API. WWDC 2026 coverage describes deep Apple silicon integration across the CPU, GPU, and Neural Engine.

Use [Foundation Models](FoundationModels.md) for Apple's on-device language model, `LanguageModel`-conforming providers, guided generation, and tool calling. Use Core AI for on-device AI model deployment once the documented API surface is available.

## Topics

### Essentials
- **Core AI framework** - A new OS 27 framework for on-device AI model deployment, pending confirmation of its documented API surface.
- [Foundation Models](FoundationModels.md) - Build language-model features on Apple's on-device model or other `LanguageModel`-conforming providers.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/)*
