# Create ML Components

Create more customizable machine learning models in your app.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 11.0+

## Overview

Create ML Components is a fundamental technology that exposes the underpinnings of monolithic tasks. You're in full control and can create custom pipelines for greater flexibility.

Use components to configure your machine learning tasks with a detailed level of granularity. Choose a specific classifier for images, video, or tabular data.

## Topics

### Image Components
- [Augmenting images to expand your training data](https://developer.apple.com/documentation/createmlcomponents/augmenting_images_to_expand_your_training_data) - Improve your model by using transformed versions of your training images.
- [Creating a multi-label image classifier](https://developer.apple.com/documentation/createmlcomponents/creating_a_multi-label_image_classifier) - Train a machine learning model to assign multiple labels to an image.
- **ImageReader** - An image file reader.
- **ImageFeatureExtractor** - A transformer that takes an image and outputs image features.
- **ImageCropper** - An image crop transformer.
- **ImageScaler** - An image scaling transformer.
- **ImageFeaturePrint** - ImageFeaturePrint image feature extractor.
- **ImageBlur** - An image blurring transformer.
- **ImageColorTransformer** - An image color transformer.
- **ImageExposureAdjuster** - An image exposure adjusting transformer.
- **ImageFlipper** - An image flipper transformer.
- **ImageRotator** - An image rotating transformer.
- **RandomImageNoiseGenerator** - A transformer that adds random noise to an image.
- **MLModelImageFeatureExtractor** - An image feature extractor provided by an MLModel.

### Pose Components
- [Counting human body action repetitions in a live video feed](https://developer.apple.com/documentation/createmlcomponents/counting_human_body_action_repetitions_in_a_live_video_feed) - Use Create ML Components to analyze a series of video frames and count a person's repetitive or periodic body movements.
- **Pose** - A pose that contains joint keypoints from a person, a hand, or a combination.
- **JointKey** - A key that uniquely identifies a joint.
- **JointPoint** - A joint in a pose that contains a location and scoring information.
- **PoseSelector** - A transformer that selects one pose from an array of poses.
- **PoseSelectionStrategy** - Pose selection strategy.
- **JointsSelector** - Joints selector from a pose.
- **HumanBodyPoseExtractor** - The human body pose image feature extractor.
- **HumanHandPoseExtractor** - The human hand pose image feature extractor.
- **HumanBodyActionCounter** - A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.
- **HumanBodyActionPeriodPredictor** - A human body action period predictor transformer that takes window of poses and produces a window of predictions.

### Audio Components
- **AudioReader** - An audio file reader.
- **AudioFeaturePrint** - A stream transformer that extracts audio features from audio buffers.
- **AudioConvertingTransformer** - A transformer for audio conversion.

### Time-based Components
- [Creating a time-series classifier](https://developer.apple.com/documentation/createmlcomponents/creating_a_time-series_classifier) - Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](https://developer.apple.com/documentation/createmlcomponents/creating_a_time-series_forecaster) - Forecast future data points by training a machine learning model using historical data.
- **DateFeatures** - A set of date and time features.
- **DateFeatureExtractor** - A time and date feature extractor.
- **LinearTimeSeriesForecaster** - A time-series forecasting estimator.
- **LinearTimeSeriesForecasterConfiguration** - The configuration for a linear time-series forecaster.
- **TimeSeriesForecasterBatches** - A sequence of forecaster batches on a time series shaped array.
- **TimeSeriesForecasterAnnotatedWindows** - A sequence of forecasting windows on a time series shaped array.
- **TemporalFeature** - A temporal feature contains a segment identifier and a feature value.
- **TemporalSequence** - Async sequence for temporal features.
- **TemporalSegmentIdentifier** - Uniquely identifiers a segment of a temporal sequence.
- **SlidingWindows** - A sequence of windows on a time series shaped array.
- **SlidingWindowTransformer** - A temporal transformer that groups input elements.
- **Downsampler** - A temporal transformer that down samples the input stream.
- **VideoReader** - A video file reader.
- **TemporalFileSegment** - A URL and a time range identifying a specific segment of a time-based (temporal) file.
- **AnyTemporalIterator** - A type-erased async iterator.
- **AnyTemporalSequence** - A type-erased temporal sequence.
- **PreprocessedFeatureSequence** - An asynchronous sequence of eagerly stored temporal features.

### Object Detection Components
- **DetectedObject** - An item in a detection result.
- **ObjectDetectionAnnotation** - An object detection annotation.
- **ObjectDetectionMetrics** - Metrics for object detection model.

### Tabular Components
- **TabularTransformer** - A tabular transformer that transforms a data frame.
- **TabularEstimator** - A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- **SupervisedTabularEstimator** - A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- **ColumnSelector** - An operation that applies an estimator to a selection of columns.
- **ColumnSelectorTransformer** - A transformer that applies a base transformer to specific columns in a data frame.
- **ColumnSelection** - A selection of columns from a data frame.
- **ColumnConcatenator** - A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.
- **PreprocessingSupervisedTabularEstimator** - A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- **PreprocessingTabularEstimator** - An estimator that composes a preprocessing transformer and an estimator.
- **PreprocessingUpdatableSupervisedTabularEstimator** - An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- **PreprocessingUpdatableTabularEstimator** - An updatable estimator that composes a preprocessing transformer and an updatable estimator.

### Protocols
- **Transformer** - A transformer that takes an input and produces an output.
- **TemporalTransformer** - A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output sequence.
- **RandomTransformer** - A transformer that takes an input and a random number generator and produces a randomized output.
- **Estimator** - An estimator that creates a transformer by fitting to a data set.
- **TemporalEstimator** - An estimator that creates a transformer by fitting to a sequence of temporal features.
- **SupervisedEstimator** - An estimator that creates a transformer by fitting to a data set. (Deprecated)
- **SupervisedTemporalEstimator** - An estimator that creates a transformer by fitting to a sequence of annotated temporal features. (Deprecated)
- **UpdatableEstimator** - An estimator that can be incrementally updated.
- **UpdatableSupervisedEstimator** - A supervised estimator that can be incrementally updated.
- **UpdatableSupervisedTemporalEstimator** - A supervised temporal estimator that can be incrementally updated. (Deprecated)
- **UpdatableSupervisedTabularEstimator** - A supervised tabular estimator that can be incrementally updated.
- **UpdatableTemporalEstimator** - A temporal estimator that can be incrementally updated. (Deprecated)
- **UpdatableTabularEstimator** - A tabular estimator that can be incrementally updated.

### Core ML Adaptors
- **MLModelTransformerAdaptor** - A transformer that uses a Core ML model.
- **MLModelClassifierAdaptor** - A transformer that uses a Core ML model as a classifier.
- **MLModelRegressorAdaptor** - A transformer that uses a Core ML model as a regressor.
- **ModelMetadata** - User info keys that specify useful information about a model.

### Annotations
- **AnnotatedFiles** - An annotated files collection.
- **AnnotatedBatch** - A batch of annotated examples for fitting a supervised estimator.
- **AnnotatedFeature** - An annotated example for fitting a supervised estimator.
- **AnnotatedFeatureProvider** - An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- **AnnotatedPrediction** - An annotated prediction.
- **DataFrameTemporalAnnotationParameters** - Annotation parameters for the dataframe containing temporal annotations.

### Augmentations
- **ApplyEachRandomly** - Applies each transformer randomly given a probability.
- **ApplyRandomly** - Randomly applies the transformer with the given probability.
- **AugmentationBuilder** - A series of augmentations.
- **AugmentationSequence** - An async sequence of augmented elements.
- **Augmenter** - An augmenter.
- **ChooseRandomly** - Apply single transformation randomly chosen from a list of transformers.
- **RandomImageCropper** - Crops an image at a random location.
- **ShuffleRandomly** - Apply transformations in a random order.
- **UniformRandomFloatingPointParameter** - Applies the transformer with a randomly generated input parameter.
- **UniformRandomIntegerParameter** - Applies the transformer with a randomly generated input parameter.
- **UpsampledAugmentationSequence** - An async sequence of augmented elements.

### Event Handling
- **Event** - Maintains the status of the pipeline.
- **EventHandler** - A closure to handle processing events.
- **MetricsKey** - A key that uniquely identifies a metric.

### Scalers
- **StandardScaler** - An estimator that standardizes the input by removing the mean and scaling to unit variance.
- **MaxAbsScaler** - An estimator that scales the input values so that the maximum absolute value is 1.0.
- **MinMaxScaler** - An estimator that scales the input values so that they all lie in a closed range.
- **NormalizationScaler** - An estimator that normalizes the input values using a normalization strategy.
- **RobustScaler** - An estimator that scales the input using statistics that are robust to outliers.

### Preprocessors
- **LinearTransformer** - A transformer that runs an input through a scale and offset.
- **ImputeTransformer** - A transformer that replaces missing values with a pre-defined value.
- **OneHotEncoder** - An estimator that encodes categorical values to an integer array.
- **OrdinalEncoder** - An ordinal encoder estimator encodes categorical values to ordinal integer values.
- **NumericImputer** - An estimator that replaces missing values in the numeric input.
- **Reshaper** - A transformer that reshapes a shaped array.
- **CategoricalImputer** - An estimator that replaces missing values in the categorical input.
- **OptionalUnwrapper** - A transformer that unwraps optional elements and throws when encountering missing values.

### Regressors
- **Regressor** - A transformer that predicts a float value.
- **LinearRegressor** - A linear regressor.
- **LinearRegressorModel** - A trained linear regressor model.
- **MultivariateLinearRegressor** - A multivariate linear regressor.
- **MultivariateLinearRegressorConfiguration** - A linear regressor configuration.
- **Model** - A trained multivariate linear regressor model.
- **FullyConnectedNetworkRegressor** - A regressor that uses a fully connected network.
- **FullyConnectedNetworkRegressorModel** - A regressor model that uses a fully connected network.
- **BoostedTreeRegressor** - A gradient boosted decision tree regressor.
- **TreeRegressorModel** - A trained tree regressor model.
- **OptimizationStrategy** - A linear optimization strategy.

### Serializers
- **EstimatorDecoder** - A type that can decode values from a model representation.
- **EstimatorEncoder** - A type that can encode values into a model representation.

### Classifiers
- **Classifier** - An estimator that predicts classification probabilities.
- **LogisticRegressionClassifier** - A logistic regression classifier.
- **LogisticRegressionClassifierModel** - A trained logistic regression classifier model.
- **BoostedTreeClassifier** - A gradient boosted decision tree classifier.
- **BoostedTreeConfiguration** - A boosted tree configuration.
- **FullyConnectedNetworkClassifier** - A classifier that uses a fully connected network.
- **FullyConnectedNetworkClassifierModel** - A classifier model that uses a fully connected network.
- **FullyConnectedNetworkMultiLabelClassifier** - A classifier that uses a multi-label fully-connected network.
- **FullyConnectedNetworkMultiLabelClassifierModel** - A multi-label classifier model that uses a fully-connected network.
- **FullyConnectedNetworkConfiguration** - A fully connected network configuration.
- **TreeClassifierModel** - A trained tree classifier model.
- **TimeSeriesClassifier**
- **TimeSeriesClassifierConfiguration** - The configuration for a time-series classifier.

### Metrics
- **Classification** - An item in a classification result.
- **ClassificationDistribution** - A classification distribution that contains a probability for each classification label.
- **ClassificationMetrics** - Classification metrics.
- **MultiLabelClassificationMetrics** - Multi-label classification metrics.
- **rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T** - Computes the root mean squared error between predicted and ground truth values.
- **rootMeanSquaredError<T>(some Collection, some Collection) -> T** - Computes the root mean squared error between predicted and ground truth values.
- **maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T** - Computes the maximum absolute error between predicted and ground truth values.
- **maximumAbsoluteError<T>(some Collection, some Collection) -> T** - Computes the maximum absolute error between predicted and ground truth values.
- **meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T** - Computes the mean absolute error between predicted and ground truth values.
- **meanAbsoluteError<T>(some Collection, some Collection) -> T** - Computes the mean absolute error between predicted and ground truth values.
- **meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T** - Computes the mean absolute percentage error between predicted and ground truth values.
- **meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T** - Computes the root mean squared error between predicted and ground truth values.
- **meanSquaredError<T>(some Collection, some Collection) -> T** - Computes the mean squared error between predicted and ground truth values.

### Transformer Adaptors
- **TransformerToEstimatorAdaptor** - An estimator that always returns a predefined transformer.
- **TransformerToTemporalAdaptor** - A temporal transformer that applies a regular transformer to each value of a temporal sequence. (Deprecated)
- **TransformerToUpdatableEstimatorAdaptor** - An updatable estimator that always returns a predefined transformer.

### Updatable Adaptors
- **UpdatableEstimatorToTemporalAdaptor** - An updatable temporal estimator wrapping an updatable estimator. (Deprecated)
- **UpdatableEstimatorToSupervisedAdaptor** - An adaptor that exposes an updatable estimator as an updatable supervised estimator.
- **UpdatableSupervisedEstimatorToTemporalAdaptor** - An updatable supervised temporal estimator wrapping an updatable supervised estimator. (Deprecated)
- **UpdatableTemporalEstimatorToSupervisedAdaptor** - An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator. (Deprecated)

### Estimator Adaptors
- **EstimatorToSupervisedAdaptor** - An adaptor that exposes an estimator as a supervised estimator.
- **EstimatorToTemporalAdaptor** - A temporal estimator wrapping an estimator. (Deprecated)
- **SupervisedEstimatorToTemporalAdaptor** - A supervised temporal estimator wrapping a supervised estimator. (Deprecated)

### Tabular Adaptors
- **TabularEstimatorToSupervisedAdaptor** - An adaptor that exposes a tabular estimator as a tabular supervised estimator.
- **TabularTransformerToEstimatorAdaptor** - A tabular estimator that always returns a predefined tabular transformer.
- **TabularTransformerToUpdatableEstimatorAdaptor** - An updatable tabular estimator that always returns a predefined transformer.
- **UpdatableTabularEstimatorToSupervisedAdaptor** - An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.

### Temporal Adaptors
- **TemporalAdaptor** - A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- **TemporalTransformerToEstimatorAdaptor** - A temporal estimator that always returns a predefined temporal transformer. (Deprecated)
- **TemporalEstimatorToSupervisedAdaptor** - An adaptor that exposes a temporal estimator as a supervised temporal estimator. (Deprecated)
- **TemporalTransformerToUpdatableEstimatorAdaptor** - A temporal estimator that always returns a predefined temporal transformer. (Deprecated)

### Composition with Preprocessing
- **PreprocessingEstimator** - An estimator that composes a preprocessing transformer and an estimator.
- **PreprocessingTemporalEstimator** - A temporal estimator that composes a preprocessing transformer and a temporal estimator. (Deprecated)
- **PreprocessingSupervisedEstimator** - A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- **PreprocessingSupervisedTemporalEstimator** - A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator. (Deprecated)
- **PreprocessingUpdatableEstimator** - An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- **PreprocessingUpdatableTemporalEstimator** - An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator. (Deprecated)
- **PreprocessingUpdatableSupervisedEstimator** - An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- **PreprocessingUpdatableSupervisedTemporalEstimator** - An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator. (Deprecated)

### Composition
- **ComposedTransformer** - A transformer that composes two transformers by applying them one after the other.
- **ComposedTemporalTransformer** - A temporal transformer that composes two temporal transformers by applying them one after the other.
- **ComposedTabularTransformer** - A transformer that composes two tabular transformers by applying them one after the other.

### Errors
- **AudioPreprocessingError** - Audio preprocessing errors.
- **AudioReaderError** - Audio reader errors.
- **CompatibilityError** - A compatibility error.
- **ConcatenationError** - Errors thrown when concatenating numeric values.
- **DatasetError** - Dataset processing errors.
- **EstimatorEncodingError** - An estimator encoding error.
- **ModelCompatibilityError** - Errors related to CoreML model compatibility.
- **ModelUpdateError** - An updatable model error.
- **OptimizationError** - An optimization error.
- **PipelineDataError** - Errors related to pipeline data affinity problems.
- **SerializationError** - A serialization error.
- **TabularPipelineDataError** - Errors related to tabular pipeline data affinity problems.
- **VideoReaderError** - Video loader errors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CreateMLComponents)*