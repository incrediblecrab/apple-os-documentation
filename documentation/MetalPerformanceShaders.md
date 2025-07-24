# Metal Performance Shaders

Optimize graphics and compute performance with kernels that are fine-tuned for the unique characteristics of each Metal GPU family.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The Metal Performance Shaders framework contains a collection of highly optimized compute and graphics shaders that are designed to integrate easily and efficiently into your Metal app. These data-parallel primitives are specially tuned to take advantage of the unique hardware characteristics of each GPU family to ensure optimal performance.

Apps adopting the Metal Performance Shaders framework achieve great performance without needing to create and maintain hand-written shaders for each GPU family. Metal Performance Shaders can be used along with your app's existing Metal resources (such as the **MTLCommandBuffer**, **MTLTexture**, and **MTLBuffer** objects) and shaders.

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
- **MPSSupportsMTLDevice()** - Determines whether the Metal Performance Shaders framework supports a Metal device.

### Image Filters
- [Image Filters](https://developer.apple.com/documentation/metalperformanceshaders/image_filters) - Apply high-performance filters to, and extract statistical and histogram data from images.

### Neural Networks
Implement and run deep learning using previously obtained training data.
- [Training a Neural Network with Metal Performance Shaders](https://developer.apple.com/documentation/metalperformanceshaders/training_a_neural_network_with_metal_performance_shaders) - Use an MPS neural network graph to train a simple neural network digit classifier.
- **MPSImage** - A texture that may have more than four channels for use in convolutional neural networks.
- **MPSTemporaryImage** - A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Objects that Simplify the Creation of Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/objects_that_simplify_the_creation_of_neural_networks) - Simplify the creation of neural networks using networks of filter, image, and state nodes.
- [Convolutional Neural Network Kernels](https://developer.apple.com/documentation/metalperformanceshaders/convolutional_neural_network_kernels) - Build neural networks with layers.
- [Recurrent Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/recurrent_neural_networks) - Create recurrent neural networks.

### Matrices and Vectors
- [Matrices and Vectors](https://developer.apple.com/documentation/metalperformanceshaders/matrices_and_vectors) - Solve systems of equations, factorize matrices and multiply matrices and vectors.

### Kernel Base Classes
- **MPSKernel** - A standard interface for Metal Performance Shaders kernels.

### Keyed Archivers
- **NSKeyedArchiver** - An encoder that stores an object's data to an archive referenced by keys.
- **MPSKeyedUnarchiver** - A keyed archiver that supports Metal Performance Shaders kernel decoding.
- **MPSDeviceProvider** - An interface that enables the setting of a Metal device for unarchived objects.

### Ray Tracing
- [Accelerating ray tracing and motion blur using Metal](https://developer.apple.com/documentation/metalperformanceshaders/accelerating_ray_tracing_and_motion_blur_using_metal) - Generate ray-traced images with motion blur using GPU-based parallel processing.
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