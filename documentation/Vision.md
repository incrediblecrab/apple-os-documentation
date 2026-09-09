# Vision

Apply computer vision algorithms to perform a variety of tasks on input images and videos.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+ | macOS 10.13+ | tvOS 11.0+ | visionOS 1.0+ | watchOS 27.0+ (selected APIs)

The older minimums above describe the [`VNRequest`](https://developer.apple.com/documentation/vision/vnrequest.md) family. Swift-only requests and OS 27 model tools have later, per-symbol requirements; the framework baseline does not make every API available on every listed platform.

## Overview

The Vision framework combines machine learning technologies and Swift's concurrency features to perform computer vision tasks in your app. Use the Vision framework to analyze images for a variety of purposes:

- Tracking human and animal body poses or the trajectory of an object
- Recognizing text in multiple languages; Apple's current overview lists 26 languages, and [`supportedRecognitionLanguages`](https://developer.apple.com/documentation/vision/recognizetextrequest/supportedrecognitionlanguages.md) reports those supported by a particular text request
- Detecting faces and face landmarks, such as eyes, nose, and mouth
- Performing hand tracking to enable new device interactions
- Calculating aesthetic quality scores to help rank images or select video thumbnails

To begin using the Swift API, create a request for the type of analysis you want to do. These requests conform to the VisionRequest protocol. Perform the request to obtain observations with the analysis results. The current request catalog offers more than 25 analysis requests. Vision also allows the use of custom Core ML models for tasks like classification or object detection.

**Note:** Starting in iOS 18.0, the Vision framework provides a new Swift-only API. See Original Objective-C and Swift API to view the original API.

## OS 27 model tools

[`OCRTool`](https://developer.apple.com/documentation/vision/ocrtool.md) and [`BarcodeReaderTool`](https://developer.apple.com/documentation/vision/barcodereadertool.md) conform to Foundation Models' `Tool` protocol. Add the appropriate tool to a model session and supply image attachments as described in [multimodal prompting](https://developer.apple.com/documentation/foundationmodels/analyzing-images-with-multimodal-prompting.md).

The OCR tool lists iOS, iPadOS, macOS, and visionOS 27.0+; the barcode tool additionally lists watchOS 27.0+. These symbol lists do not enumerate tvOS or Mac Catalyst. Do not extend the framework's older minimums to these new tools or assume that every model supports image input.

Neither `OCRTool` nor `BarcodeReaderTool` is available in Simulator. Validate these model-tool integrations on a supported physical device and handle unavailable models or unsupported image input.

[Visual Intelligence](VisualIntelligence.md) system search and [Media Intelligence](MediaIntelligence.md) face grouping/video highlights are separate integrations. See [App Intents](AppIntents.md) for system content discovery and [Evaluations](Evaluations.md) for model/tool quality checks.

## Topics

### Still-image analysis
- [Classifying images for categorization and search](https://developer.apple.com/documentation/vision/classifying-images-for-categorization-and-search.md) - Analyze and label images using a Vision classification request.
- **ClassifyImageRequest** - A request to classify an image.
- **ImageProcessingRequest** - A type for image-analysis requests that focus on a specific part of an image.
- **ImageRequestHandler** - An object that processes one or more image-analysis requests pertaining to a single image.
- **VisionRequest** - A type for image-analysis requests.
- **VisionObservation** - A type for objects produced by image-analysis requests.
- **DetectLensSmudgeRequest** - A request that detects a smudge on a lens from an image or video frame capture.
- **SmudgeObservation** - An observation that provides an overall score of the presence of a smudge in an image or video frame capture.

### Image sequence analysis
- **GeneratePersonSegmentationRequest** - A request that produces a matte image for a person it finds in the input image.
- **GeneratePersonInstanceMaskRequest** - A request that produces a mask of individual people it finds in the input image.
- **DetectDocumentSegmentationRequest** - A request that detects rectangular regions that contain text in the input image.
- **StatefulRequest** - The protocol for a type that builds evidence of a condition over time.

### Image aesthetics analysis
- [Generating high-quality thumbnails from videos](https://developer.apple.com/documentation/vision/generating-thumbnails-from-videos.md) - Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.
- **CalculateImageAestheticsScoresRequest** - A request that analyzes an image for aesthetically pleasing attributes.

### Saliency analysis
- **GenerateAttentionBasedSaliencyImageRequest** - An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- **GenerateObjectnessBasedSaliencyImageRequest** - A request that generates a heat map that identifies the parts of an image most likely to represent objects.

### Object tracking
- **TrackObjectRequest** - An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- **TrackRectangleRequest** - An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.

### Face and body detection
- [Analyzing a selfie and visualizing its content](https://developer.apple.com/documentation/vision/analyzing-a-selfie-and-visualizing-its-content.md) - Calculate face-capture quality and visualize facial features for a collection of images using the Vision framework.
- **DetectFaceRectanglesRequest** - A request that finds faces within an image.
- **DetectFaceLandmarksRequest** - An image-analysis request that finds facial features like eyes and mouth in an image.
- **DetectFaceCaptureQualityRequest** - A request that produces a floating-point number that represents the capture quality of a face in a photo.
- **DetectHumanRectanglesRequest** - A request that finds rectangular regions that contain people in an image.

### Body and hand pose detection
- **DetectHumanBodyPoseRequest** - A request that detects a human body pose.
- **DetectHumanHandPoseRequest** - A request that detects a human hand pose.
- **PoseProviding** - An observation that provides a collection of joints that make up a pose.
- **Chirality** - The hand sidedness of a pose.
- **Joint** - A pose joint represented as a normalized point in an image, along with a label and a confidence value.

### 3D body pose detection
- **DetectHumanBodyPose3DRequest** - A request that detects points on human bodies in 3D space, relative to the camera.
- **Joint3D** - An object that represents a body pose joint in 3D space.

### Text detection
- [Recognizing tables within a document](https://developer.apple.com/documentation/vision/recognize-tables-within-a-document.md) - Scan a document containing a table and extract its content in a structured form.
- [Locating and displaying recognized text](https://developer.apple.com/documentation/vision/locating-and-displaying-recognized-text.md) - Perform text recognition on a photo using the Vision framework's text-recognition request.
- **RecognizeDocumentsRequest** - An image-analysis request to scan an image of a document and provide information about its structure.
- **DocumentObservation** - Information about the sections of content that an image-analysis request detects in a document.
- **DetectTextRectanglesRequest** - An image-analysis request that finds regions of visible text in an image.
- **RecognizeTextRequest** - An image-analysis request that recognizes text in an image.

### Barcode detection
- **DetectBarcodesRequest** - A request that detects barcodes in an image.

### Trajectory, contour, and horizon detection
- **DetectTrajectoriesRequest** - A request that detects the trajectories of shapes moving along a parabolic path.
- **DetectContoursRequest** - A request that detects the contours of the edges of an image.
- **DetectHorizonRequest** - An image-analysis request that determines the horizon angle in an image.

### Animal detection
- **DetectAnimalBodyPoseRequest** - A request that detects an animal body pose.
- **RecognizeAnimalsRequest** - A request that recognizes animals in an image.

### Optical flow and rectangle detection
- **TrackOpticalFlowRequest** - A request that determines the direction change of vectors for each pixel from a previous to current image.
- **DetectRectanglesRequest** - An image-analysis request that finds projected rectangular regions in an image.

### Image alignment
- **TrackTranslationalImageRegistrationRequest** - An image-analysis request that you track over time to determine the affine transform necessary to align the content of two images.
- **TrackHomographicImageRegistrationRequest** - An image-analysis request that you track over time to determine the perspective warp matrix necessary to align the content of two images.
- **TargetedRequest** - A type for analyzing two images together.

### Image feature print and background removal
- **GenerateImageFeaturePrintRequest** - An image-based request to generate feature prints from an image.
- **GenerateForegroundInstanceMaskRequest** - A request that generates an instance mask of noticeable objects to separate from the background.

### Machine learning image analysis
- **CoreMLRequest** - An image-analysis request that uses a Core ML model to process images.
- **CoreMLFeatureValueObservation** - An object that represents a collection of key-value information that a Core ML image-analysis request produces.
- **ClassificationObservation** - An object that represents classification information that an image-analysis request produces.
- **PixelBufferObservation** - An object that represents an image that an image-analysis request produces.

### Image locations and regions
- **NormalizedPoint** - A point in a 2D coordinate system.
- **NormalizedRect** - The location and dimensions of a rectangle.
- **NormalizedRegion** - A polygon composed of normalized points.
- **NormalizedCircle** - The center point and radius of a 2D circle.
- **BoundingBoxProviding** - A protocol for objects that have a bounding box.
- **BoundingRegionProviding** - A protocol for objects that have a defined boundary in an image.
- **QuadrilateralProviding** - A protocol for objects that have a bounding quadrilateral.
- **CoordinateOrigin** - The origin of a coordinate system relative to an image.

### Request Handlers
- **ImageRequestHandler** - An object that processes one or more image-analysis requests pertaining to a single image.
- **TargetedImageRequestHandler** - An object that performs image-analysis requests on two images.

### Utilities
- **ComputeStage** - Types that represent the compute stage.
- **VideoProcessor** - An object that performs offline analysis of video content.

### Errors
- **VisionError** - The errors that the framework produces.

### Legacy API
- [Original Objective-C and Swift API](https://developer.apple.com/documentation/vision/original-objective-c-and-swift-api.md)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Vision)*
