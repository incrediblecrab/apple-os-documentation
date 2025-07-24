# Metal Performance Shaders Graph

Build, compile, and execute compute graphs utilizing all the different compute devices on the platform, including GPU, CPU, and Neural Engine.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+

## Overview

Metal Performance Shaders Graph provides high-performance, energy-efficient computation on Apple platforms by leveraging different hardware compute blocks. You can use this framework to generate a symbolic compute graph of operations, where each operation can output a set of tensors used as edges of the graph. The tensors represent multidimensional data that objects like MTLBuffer or MTLTexture can back. After you construct the graph, you can compile it into an executable to optimize for performance and subsequently run the executable on your input data. This framework also provides the ability to serialize the executables and load executables from a serialized .mpsgraphpackage.

## Topics

### Essentials
- [Adding Custom Functions to a Shader Graph](https://developer.apple.com/documentation/metalperformanceshadersgraph/adding_custom_functions_to_a_shader_graph) - Run your own graph functions on the GPU by building the function programmatically.
- [Training a Neural Network using MPS Graph](https://developer.apple.com/documentation/metalperformanceshadersgraph/training_a_neural_network_using_mps_graph) - Train a simple neural network digit classifier.
- [Filtering Images with MPSGraph FFT Operations](https://developer.apple.com/documentation/metalperformanceshadersgraph/filtering_images_with_mpsgraph_fft_operations) - Filter an image with MPSGraph fast Fourier transforms using the convolutional theorem.

### Classes
- **MPSGraph** - The optimized representation of a compute graph of operations and tensors.
- **MPSGraphCompilationDescriptor** - A class that consists of all the levers for compiling graphs.
- **MPSGraphConvolution2DOpDescriptor** - A class that describes the properties of a 2D-convolution operator.
- **MPSGraphConvolution3DOpDescriptor** - A class that describes the properties of a 3D-convolution operator.
- **MPSGraphCreateSparseOpDescriptor** - A class that describes the properties of a create sparse operation.
- **MPSGraphDepthwiseConvolution2DOpDescriptor** - A class that defines the parameters for a 2D-depthwise convolution operation.
- **MPSGraphDepthwiseConvolution3DOpDescriptor** - The class that defines the parameters for a 3D-depthwise convolution operation.
- **MPSGraphDevice** - A class that describes the compute device.
- **MPSGraphExecutable** - The compiled representation of a compute graph executable.
- **MPSGraphExecutableExecutionDescriptor** - A class that consists of all the levers to synchronize and schedule executable execution.
- **MPSGraphExecutableSerializationDescriptor** - A class that consists of all the levers to serialize an executable.
- **MPSGraphExecutionDescriptor** - A class that consists of all the levers to synchronize and schedule graph execution.
- **MPSGraphFFTDescriptor** - The class that defines the parameters for a fast Fourier transform (FFT) operation.
- **MPSGraphGRUDescriptor** - The class that defines the parameters for a gated recurrent unit (GRU) operation.
- **MPSGraphImToColOpDescriptor** - The class that defines the parameters for an image to column or column to image operation.
- **MPSGraphLSTMDescriptor** - The class that defines the parameters for a long short-term memory (LSTM) operation.
- **MPSGraphObject** - The common base class for all Metal Performance Shaders Graph objects.
- **MPSGraphOperation** - A symbolic representation of a compute operation.
- **MPSGraphPooling2DOpDescriptor** - The class that defines the parameters for a 2D pooling operation.
- **MPSGraphPooling4DOpDescriptor** - The class that defines the parameters for a 4D pooling operation.
- **MPSGraphRandomOpDescriptor** - A class that describes the random operation.
- **MPSGraphShapedType** - The shaped type class for types on tensors with a shape and data type.
- **MPSGraphSingleGateRNNDescriptor** - The class that defines the parameters for a single gate RNN operation.
- **MPSGraphStencilOpDescriptor** - The class that defines the parameters for a stencil operation.
- **MPSGraphTensor** - The symbolic representation of a compute data type.
- **MPSGraphTensorData** - The representation of a compute data type.
- **MPSGraphType** - The base type class for types on tensors.
- **MPSGraphVariableOp** - The class that defines the parameters for a variable.

### Type Aliases
- **MPSGraphCompilationCompletionHandler** - A notification that appears when compilation finishes.
- **MPSGraphCompletionHandler** - A notification that appears when graph execution finishes.
- **MPSGraphControlFlowDependencyBlock** - The scope where all the operations defined in this block get control-dependency operations.
- **MPSGraphExecutableCompletionHandler** - A notification when graph executable execution finishes.
- **MPSGraphExecutableScheduledHandler** - A notification when graph executable execution schedules.
- **MPSGraphForLoopBodyBlock** - A block for the body in the for loop.
- **MPSGraphIfThenElseBlock** - A block of operations executed under either the if or else condition.
- **MPSGraphScheduledHandler** - A notification that appears when graph execution schedules.
- **MPSGraphWhileAfterBlock** - The block that executes after the condition evaluates for each iteration.
- **MPSGraphWhileBeforeBlock** - The block that executes before the condition evaluates for each iteration.

### Enumerations
- **MPSGraphDeploymentPlatform** - The options available to a graph.
- **MPSGraphDeviceType** - The device type.
- **MPSGraphExecutionStage** - Execution events that can be used with shared events.
- **MPSGraphFFTScalingMode** - The scaling modes for Fourier transform operations.
- **MPSGraphLossReductionType** - The type of the reduction the graph applies in the loss operations.
- **MPSGraphNonMaximumSuppressionCoordinateMode** - The non-maximum suppression coordinate mode.
- **MPSGraphOptimization** - The optimization levels to trade compilation time for even more runtime performance by running more passes.
- **MPSGraphOptimizationProfile** - The optimization profile used as a heuristic as the graph compiler optimizes the network.
- **MPSGraphOptions** - The options available to a graph.
- **MPSGraphPaddingMode** - The tensor padding mode.
- **MPSGraphPaddingStyle** - The tensor padding style.
- **MPSGraphPoolingReturnIndicesMode** - The flattening mode for returned indices with max-pooling.
- **MPSGraphRNNActivation** - The activation modes for RNN operations.
- **MPSGraphRandomDistribution** - The distributions supported by random operations.
- **MPSGraphRandomNormalSamplingMethod** - The sampling method to use when generating values in the normal distribution.
- **MPSGraphReductionMode** - The reduction mode.
- **MPSGraphResizeMode** - The resize mode to use for resizing.
- **MPSGraphResizeNearestRoundingMode** - The rounding mode to use when using nearest resize mode.
- **MPSGraphScatterMode** - The scatter mode.
- **MPSGraphSparseStorageType** - The sparse storage options in the Metal Performance Shaders Graph framework.
- **MPSGraphTensorNamedDataLayout** - The tensor layout.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetalPerformanceShadersGraph)*