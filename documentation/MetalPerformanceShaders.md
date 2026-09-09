# Metal Performance Shaders

Optimize graphics and compute performance with kernels that are fine-tuned for the unique characteristics of each Metal GPU family.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The Metal Performance Shaders framework contains compute and graphics shaders designed to integrate with Metal apps. These data-parallel primitives are tuned for the hardware characteristics of different GPU families; performance still depends on the device, data, and workload.

Using Metal Performance Shaders can reduce the need to maintain separate hand-written kernels for each GPU family. The framework works with existing Metal resources (such as **MTLCommandBuffer**, **MTLTexture**, and **MTLBuffer**) and shaders; profile the complete workload rather than assuming a universal speedup.

The Metal Performance Shaders framework supports the following functionality:

- Apply high-performance filters to, and extract statistical and histogram data from images.
- Implement and run neural networks for machine learning training and inference.
- Solve systems of equations, factorize matrices and multiply matrices and vectors.
- Accelerate ray tracing with high-performance ray-geometry intersection testing.

## Topics

### Fundamentals
- **The MPSKernel Class**
- **Tuning Hints**
- **Device Support**
- [`MPSSupportsMTLDevice(_:)`](https://developer.apple.com/documentation/metalperformanceshaders/mpssupportsmtldevice(_:)) - Determines whether the Metal Performance Shaders framework supports a Metal device.

### Image Filters
- [Image Filters](https://developer.apple.com/documentation/metalperformanceshaders/image-filters) - Apply high-performance filters to, and extract statistical and histogram data from images.

### Neural Networks
Implement and run deep learning using previously obtained training data.
- [Training a Neural Network with Metal Performance Shaders](https://developer.apple.com/documentation/metalperformanceshaders/training-a-neural-network-with-metal-performance-shaders) - Use an MPS neural network graph to train a simple neural network digit classifier.
- **MPSImage** - A texture that may have more than four channels for use in convolutional neural networks.
- **MPSTemporaryImage** - A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/objects-that-simplify-the-creation-of-neural-networks) - Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](https://developer.apple.com/documentation/metalperformanceshaders/convolutional-neural-network-kernels) - Build neural networks with layers.
- [Recurrent Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/recurrent-neural-networks) - Create recurrent neural networks.

### Matrices and Vectors
- [Matrices and Vectors](https://developer.apple.com/documentation/metalperformanceshaders/matrices-and-vectors) - Solve systems of equations, factorize matrices and multiply matrices and vectors.

### Kernel Base Classes
- **MPSKernel** - A standard interface for Metal Performance Shaders kernels.

### Keyed Archivers
- **NSKeyedArchiver** - An encoder that stores an object's data to an archive referenced by keys.
- **MPSKeyedUnarchiver** - A keyed archiver that supports Metal Performance Shaders kernel decoding.
- **MPSDeviceProvider** - An interface that enables the setting of a Metal device for unarchived objects.

### Ray Tracing
- [Accelerating ray tracing and motion blur using Metal](https://developer.apple.com/documentation/metal/accelerating-ray-tracing-and-motion-blur-using-metal) - Generate ray-traced images with motion blur using GPU-based parallel processing.
- **MPSRayIntersector** - A kernel that performs intersection tests between rays and geometry.

### Deprecated
- **MPSAccelerationStructureGroup** (Deprecated) - A group of acceleration structures.
- **MPSInstanceAccelerationStructure** (Deprecated) - An acceleration structure built over instances of other acceleration structures.
- **MPSTriangleAccelerationStructure** (Deprecated) - An acceleration structure built over triangles.
- **MPSAccelerationStructure** (Deprecated) - The base class for data structures that are built over geometry and used to accelerate ray tracing.

### Articles
- **MetalPerformanceShaders Constants**
- **MetalPerformanceShaders Data Types**
- **MetalPerformanceShaders Enumerations**
- **MetalPerformanceShaders Functions**
- **MetalPerformanceShaders Structures**

### See Also
- **Metal** - Render advanced 3D graphics and compute data in parallel with graphics processors.
- **Metal Programming Guide**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetalPerformanceShaders)*
