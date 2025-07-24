# Create ML

Create machine learning models for use in your app.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 10.14+ | tvOS 16.0+ | visionOS 1.0+

## Overview

Use Create ML with familiar tools like Swift and macOS playgrounds to create and train custom machine learning models on your Mac. You can train models to perform tasks like recognizing images, extracting meaning from text, or finding relationships between numerical values.

You train a model to recognize patterns by showing it representative samples. For example, you can train a model to recognize dogs by showing it lots of images of different dogs. After you've trained the model, you test it out on data it hasn't seen before, and evaluate how well it performed the task. When the model is performing well enough, you're ready to integrate it into your app using Core ML.

Create ML leverages the machine learning infrastructure built in to Apple products like Photos and Siri. This means your image classification and natural language models are smaller and take much less time to train.

## Topics

### Image Models
- [Creating an Image Classifier Model](https://developer.apple.com/documentation/createml/creating_an_image_classifier_model) - Train a machine learning model to classify images, and add it to your Core ML app.
- **MLImageClassifier** - A model you train to classify images.
- **MLObjectDetector** - A model you train to classify one or more objects within an image.
- **MLHandPoseClassifier** - A task that creates a hand pose classification model by training with images of people's hands that you provide.

### Video Models
- [Creating an Action Classifier Model](https://developer.apple.com/documentation/createml/creating_an_action_classifier_model) - Train a machine learning model to recognize a person's body movements.
- [Detecting Human Actions in a Live Video Feed](https://developer.apple.com/documentation/createml/detecting_human_actions_in_a_live_video_feed) - Identify body movements by sending a person's pose data from a series of video frames to an action-classification model.
- **MLActionClassifier** - A model you train with videos to classify a person's body movements.
- **MLHandActionClassifier** - A task that creates a hand action classification model by training with videos of people's hand movements that you provide.
- **MLStyleTransfer** - A model you train to apply an image's style to other images or videos.

### Text Models
- [Creating a text classifier model](https://developer.apple.com/documentation/createml/creating_a_text_classifier_model) - Train a machine learning model to classify natural language text.
- [Creating a word tagger model](https://developer.apple.com/documentation/createml/creating_a_word_tagger_model) - Train a machine learning model to tag individual words in natural language text.
- **MLTextClassifier** - A model you train to classify natural language text.
- **MLWordTagger** - A word-tagging model you train to classify natural language text at the word level.
- **MLGazetteer** - A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- **MLWordEmbedding** - A map of strings in a vector space that enable your app to find similar strings by looking at a string's neighbors.

### Sound Models
- **MLSoundClassifier** - A machine learning model you train with audio files to recognize and identify sounds on a device.

### Motion Models
- **MLActivityClassifier** - A model you train to classify motion sensor data.

### Tabular Models
Model types for general tasks, such as labeling, estimating, or finding similarities. The models learn from columns of data values in a data table.

- [Creating a Model from Tabular Data](https://developer.apple.com/documentation/createml/creating_a_model_from_tabular_data) - Train a machine learning model by using Core ML to import and manage tabular data.
- **MLClassifier** - A model you train to classify data into discrete categories.
- **MLRegressor** - A model you train to estimate continuous values.
- **MLRecommender** - A model you train to make recommendations based on item similarity, grouping, and, optionally, item ratings.

### Tabular Data
- **MLDataTable** - A table of data for training or evaluating a machine learning model.
- **MLDataValue** - The value of a cell in a data table.

### Data Visualizations
- [Data Visualizations](https://developer.apple.com/documentation/createml/data_visualizations) - Render images of data tables and columns in a playground.

### Model Accuracy
- [Improving Your Model's Accuracy](https://developer.apple.com/documentation/createml/improving_your_model_s_accuracy) - Use metrics to tune the performance of your machine learning model.
- **MLClassifierMetrics** - Metrics you use to evaluate a classifier's performance.
- **MLRegressorMetrics** - Metrics you use to evaluate a regressor's performance.
- **MLWordTaggerMetrics** - Metrics you use to evaluate a word tagger's performance.
- **MLRecommenderMetrics** - Metrics you use to evaluate a recommender's performance.
- **MLObjectDetectorMetrics** - Metrics you use to evaluate an object detector's performance.

### Model Training Control
- **MLJob** - The representation of a model's asynchronous training session you use to monitor the session's progress or terminate its execution.
- **MLTrainingSession** - The current state of a model's asynchronous training session.
- **MLTrainingSessionParameters** - The configuration settings for a training session.
- **MLCheckpoint** - The state of a model's asynchronous training session at a specific point in time during the feature extraction or training phase.

### Supporting Types
Communal types that Create ML uses in all of its model-creation tasks.

- **MLCreateError** - The errors Create ML throws while performing various operations, such as training models, making predictions, writing models to a file system, and so on.
- **MLModelMetadata** - Information about a model that's stored in a Core ML model file.
- **MLSplitStrategy** - Data partitioning approaches, typically for creating a validation dataset from a training dataset.

### Articles
- [Creating a Text Classifier Model](https://developer.apple.com/documentation/createml/creating_a_text_classifier_model) - Train a machine learning model to classify natural language text.
- [Data Visualizations](https://developer.apple.com/documentation/createml/data_visualizations) - Render images of data tables and columns in a playground.
- [Gathering Training Videos for an Action Classifier](https://developer.apple.com/documentation/createml/gathering_training_videos_for_an_action_classifier) - Collect quality example videos that effectively train action classifiers.
- [Option Set Support](https://developer.apple.com/documentation/createml/option_set_support) - Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.

### Enumerations
- **MLBoundingBoxAnchor** - A location within a bounding box that an annotation's coordinates use as their reference point.
- **MLBoundingBoxCoordinatesOrigin** - The location within an image that an annotation's coordinates use as their origin.
- **MLBoundingBoxUnits** - The units a bounding box annotation uses to define its position and size.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CreateML)*