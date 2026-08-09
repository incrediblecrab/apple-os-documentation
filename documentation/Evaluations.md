# Evaluations

Verify AI features across dynamic conditions and profile their behavior with Instruments.

**Platforms:** Apple OS 27 generation (developer beta; exact per-platform availability not documented here)

## Overview

The Evaluations framework is new in the OS 27 generation. It helps validate that AI features behave correctly across dynamic conditions, going beyond what unit tests typically catch, and integrates with Instruments for profiling.

Use Evaluations alongside [Foundation Models](FoundationModels.md) when building AI features that depend on model behavior, tool calling, dynamic instructions, or changing runtime context.

## Topics

### Essentials
- [Foundation Models](FoundationModels.md) - Build AI features that can be evaluated across prompts, tools, and dynamic conditions.
- **Evaluations framework** - Validate AI feature behavior and profile results with Instruments.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/)*
