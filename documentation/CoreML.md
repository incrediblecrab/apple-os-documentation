# Core ML

Integrate machine learning models into your app.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 11.0+ | visionOS 1.0+ | watchOS 4.0+

## Overview

Use Core ML to integrate machine learning models into your app. Core ML provides a common model representation and APIs for on-device predictions. Models configured to support updates can also be retrained or fine-tuned with a person's data.

Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled "your app".

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the Create ML app bundled with Xcode. Models trained using Create ML are in the Core ML model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use Core ML Tools to convert the model into the Core ML format. For on-device training, check the model description's [`isUpdatable`](https://developer.apple.com/documentation/coreml/mlmodeldescription/isupdatable.md) property; downloading a model does not make every model updatable.

Core ML optimizes on-device performance using available CPU, GPU, and Neural Engine resources. Once the required model and input data are on the device, local inference does not need a network connection. Model delivery or other app services may still need networking.

The framework is the foundation for domain-specific frameworks and functionality. It supports Vision for analyzing images, Natural Language for processing text, Speech for converting audio to text, and Sound Analysis for identifying sounds in audio. Core ML itself builds on top of low-level primitives like Accelerate and BNNS, as well as Metal Performance Shaders.

A block diagram of the machine learning stack. The top layer is a single block labeled "Your app," which spans the entire width of the block diagram. The second layer has four blocks labeled "Vision," "Natural Language," "Speech," and "Sound Analysis." The third layer is labeled "Core ML," which also spans the entire width. The fourth and final layer has two blocks, "Accelerate and BNNS" and "Metal Performance Shaders."

### Choosing an inference surface

[Core AI](CoreAI.md) offers OS 27 neural-model deployment, specialization, and inference APIs. Its [framework documentation](https://developer.apple.com/documentation/coreai.md) explicitly directs non-neural model types, including decision trees and tabular feature engineering, to Core ML. Do not treat Core AI's introduction as a blanket Core ML deprecation or raise existing Core ML deployment minimums.

For language-model sessions, structured output, or tool calling, consider [Foundation Models](FoundationModels.md). Its OS 27 provider protocol does not supply every third-party model implementation. Use [Evaluations](Evaluations.md) for model-quality measurement alongside deterministic unit and performance tests.

## Topics

### Core ML models
- [Getting a Core ML Model](https://developer.apple.com/documentation/coreml/getting-a-core-ml-model.md) - Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](https://developer.apple.com/documentation/coreml/updating-a-model-file-to-a-model-package.md) - Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/coreml/integrating-a-core-ml-model-into-your-app.md) - Add a simple model to an app, pass input data to the model, and process the model's predictions.
- **MLModel** - An encapsulation of all the details of your machine learning model.
- [Model Customization](https://developer.apple.com/documentation/coreml/model-customization.md) - Expand and modify your model with new layers.
- [Model Personalization](https://developer.apple.com/documentation/coreml/model-personalization.md) - Update your model to adapt to new data.

### Model inputs and outputs
- [Making Predictions with a Sequence of Inputs](https://developer.apple.com/documentation/coreml/making-predictions-with-a-sequence-of-inputs.md) - Integrate a recurrent neural network model to process sequences of inputs.
- **MLFeatureValue** - A generic wrapper around an underlying value and the value's type.
- **MLSendableFeatureValue** - A sendable feature value.
- **MLFeatureProvider** - An interface that represents a collection of values for either a model's input or its output.
- **MLDictionaryFeatureProvider** - A convenience wrapper for the given dictionary of data.
- **MLBatchProvider** - An interface that represents a collection of feature providers.
- **MLArrayBatchProvider** - A convenience wrapper for batches of feature providers.
- **MLModelAsset** - An abstraction of a compiled Core ML model asset.

### App integration
- [Downloading and Compiling a Model on the User's Device](https://developer.apple.com/documentation/coreml/downloading-and-compiling-a-model-on-the-user-s-device.md) - Install Core ML models on the user's device dynamically at runtime.
- [Model Integration Samples](https://developer.apple.com/documentation/coreml/model-integration-samples.md) - Integrate tabular, image, and text classification models into your app.

### Model encryption
- [Generating a Model Encryption Key](https://developer.apple.com/documentation/coreml/generating-a-model-encryption-key.md) - Create a model encryption key to encrypt a compiled model or model archive.
- [Encrypting a Model in Your App](https://developer.apple.com/documentation/coreml/encrypting-a-model-in-your-app.md) - Encrypt your app's built-in model at compile time by adding a compiler flag.

### Compute devices
- **MLComputeDevice** - Compute devices for framework operations.
- **MLCPUComputeDevice** - An object that represents a CPU compute device.
- **MLGPUComputeDevice** - An object that represents a GPU compute device.
- **MLNeuralEngineComputeDevice** - An object that represents a Neural Engine compute device.
- **MLComputeDeviceProtocol** - An interface that represents a compute device type.

### Compute plan
- **MLComputePlan** - A class representing the compute plan of a model.
- **MLModelStructure** - An enum representing the structure of a model.
- **MLComputePolicy** - The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- **withMLTensorComputePolicy(_:_:)** - Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

### Model state
- **MLState** - Handle to the state buffers.
- **MLStateConstraint** - Constraint of a state feature value.

### Model tensor
- **MLTensor** - A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- **MLTensorScalar** - A type that represents the tensor scalar types supported by the framework. Don't use this type directly.
- **MLTensorRangeExpression** - A type that can be used to slice a dimension of a tensor. Don't use this type directly.

### Model structure
- **MLModelStructure** - An enum representing the structure of a model.

### Model errors
- **MLModelError** - Information about a Core ML model error.
- **MLModelError.Code** - Information about a Core ML model error.
- **MLModelErrorDomain** - The domain for Core ML errors.

### Model deployments
- **MLModelCollection** - A set of Core ML models from a model deployment. (Deprecated)

### Reference
- [CoreML Enumerations](https://developer.apple.com/documentation/coreml/coreml-enumerations.md)

### Functions
- [pointwiseMax(_:_:)](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:).md) - Computes the element-wise maximum of two tensors with broadcastable shapes.
- [pointwiseMin(_:_:)](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:).md) - Computes the element-wise minimum of two tensors with broadcastable shapes.

### Enumerations
- **MLShapedArrayBufferLayout** - Buffer layout enum

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreML)*
