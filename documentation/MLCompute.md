# ML Compute

Accelerate training and validation of neural networks across the CPU and one or more GPUs.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ (Deprecated)

## Overview

**Deprecated:** ML Compute is deprecated. Instead, use BNNS for CPU tasks, Metal Performance Shaders for GPU work, and Core ML for tensor APIs.

ML Compute uses high performance BNNS primitives from the Accelerate framework for the CPU, and Metal Performance Shaders for the GPU.

## Topics

### Components
- **MLCTensor** - The data object you use throughout the framework.
- **MLCPlatform** - A utility class for setting global properties in the framework.

### Layers
Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.

### Training and Validation
Create, train, and validate a graph to produce acceptable prediction results.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MLCompute)*