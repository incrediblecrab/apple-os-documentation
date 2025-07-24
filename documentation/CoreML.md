# Core ML

Integrate machine learning models into your app.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 11.0+ | visionOS 1.0+ | watchOS 4.0+

## Overview

Use Core ML to integrate machine learning models into your app. Core ML provides a unified representation for all models. Your app uses Core ML APIs and user data to make predictions, and to train or fine-tune models, all on a person's device.

Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled "your app".

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the Create ML app bundled with Xcode. Models trained using Create ML are in the Core ML model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use Core ML Tools to convert the model into the Core ML format. Once a model is on a person's device, you can use Core ML to retrain or fine-tune it on-device, with that person's data.

Core ML optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine while minimizing its memory footprint and power consumption. Running a model strictly on a person's device removes any need for a network connection, which helps keep a person's data private and your app responsive.

The framework is the foundation for domain-specific frameworks and functionality. It supports Vision for analyzing images, Natural Language for processing text, Speech for converting audio to text, and Sound Analysis for identifying sounds in audio. Core ML itself builds on top of low-level primitives like Accelerate and BNNS, as well as Metal Performance Shaders.

A block diagram of the machine learning stack. The top layer is a single block labeled "Your app," which spans the entire width of the block diagram. The second layer has four blocks labeled "Vision," "Natural Language," "Speech," and "Sound Analysis." The third layer is labeled "Core ML," which also spans the entire width. The fourth and final layer has two blocks, "Accelerate and BNNS" and "Metal Performance Shaders."

## Topics

### Core ML models
- [Getting a Core ML Model](https://developer.apple.com/documentation/coreml/getting_a_core_ml_model) - Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](https://developer.apple.com/documentation/coreml/updating_a_model_file_to_a_model_package) - Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/coreml/integrating_a_core_ml_model_into_your_app) - Add a simple model to an app, pass input data to the model, and process the model's predictions.
- **MLModel** - An encapsulation of all the details of your machine learning model.
- [Model Customization](https://developer.apple.com/documentation/coreml/model_customization) - Expand and modify your model with new layers.
- [Model Personalization](https://developer.apple.com/documentation/coreml/model_personalization) - Update your model to adapt to new data.

### Model inputs and outputs
- [Making Predictions with a Sequence of Inputs](https://developer.apple.com/documentation/coreml/making_predictions_with_a_sequence_of_inputs) - Integrate a recurrent neural network model to process sequences of inputs.
- **MLFeatureValue** - A generic wrapper around an underlying value and the value's type.
- **MLSendableFeatureValue** - A sendable feature value.
- **MLFeatureProvider** - An interface that represents a collection of values for either a model's input or its output.
- **MLDictionaryFeatureProvider** - A convenience wrapper for the given dictionary of data.
- **MLBatchProvider** - An interface that represents a collection of feature providers.
- **MLArrayBatchProvider** - A convenience wrapper for batches of feature providers.
- **MLModelAsset** - An abstraction of a compiled Core ML model asset.

### App integration
- [Downloading and Compiling a Model on the User's Device](https://developer.apple.com/documentation/coreml/downloading_and_compiling_a_model_on_the_user_s_device) - Install Core ML models on the user's device dynamically at runtime.
- [Model Integration Samples](https://developer.apple.com/documentation/coreml/model_integration_samples) - Integrate tabular, image, and text classification models into your app.

### Model encryption
- [Generating a Model Encryption Key](https://developer.apple.com/documentation/coreml/generating_a_model_encryption_key) - Create a model encryption key to encrypt a compiled model or model archive.
- [Encrypting a Model in Your App](https://developer.apple.com/documentation/coreml/encrypting_a_model_in_your_app) - Encrypt your app's built-in model at compile time by adding a compiler flag.

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
- **Code** - Information about a Core ML model error.
- **MLModelErrorDomain** - The domain for Core ML errors.

### Model deployments
- **MLModelCollection** - A set of Core ML models from a model deployment. (Deprecated)

### Reference
- [CoreML Enumerations](https://developer.apple.com/documentation/coreml/coreml_enumerations)

### Functions
- **pointwiseMax(_:_:)** - Computes the element-wise maximum of two values. (Beta)
- **pointwiseMin(_:_:)** - Computes the element-wise minimum of two values. (Beta)

### Enumerations
- **MLShapedArrayBufferLayout** - Buffer layout enum

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreML)*