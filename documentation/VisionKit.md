# VisionKit

Identify and extract information in the environment using the device's camera, or in images that your app displays.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 13.0+ | visionOS 1.0+

## Overview

VisionKit analyzes pixel information and isolates important data such as text of a given language, URLs, street addresses, phone numbers, shipment tracking numbers, flight numbers, dates, times, durations, and barcodes of various formats. The framework provides this analysis to your app through user interfaces your app displays, which enable people to interact with the analyzed data (ImageAnalyzer.AnalysisTypes) and return the data of interest back to your app. In the interfaces, people can highlight, tap to focus, copy and extract data to the clipboard, or invoke a menu option that runs an app-defined action. VisionKit offers the following user interfaces:

**DataScannerViewController** presents a camera pass-through view that enables the user to interact with any of the recognized content types (DataScannerViewController.RecognizedDataType) as seen in the environment, and provides captured information to the app for processing.

The Image Analysis interface (**ImageAnalysisInteraction** on iOS, and **ImageAnalysisOverlayView** on macOS) displays on top of an image and enables people to interact with content types (ImageAnalysisInteraction.InteractionTypes) that the framework recognizes in the image. For example, the Live Text interface enables them to select any text present in the image (textSelection), or invoke a URL (dataDetectors). Also, the text selection UI offers framework-standard buttons for copying selected text, or looking up the subject on the web for more information.

VisionKit's Document Camera view controller (**VNDocumentCameraViewController**) is a camera pass-through experience that enables users to scan physical documents. The user scans the document page by page by tapping a camera interface in the view, which provides your app with the resulting images by page number after the scan completes. With the collection of scanned images, your app can create a digital version of the physical document, such as by exporting the scanned images to PDF.

### Interact with image subjects

In iOS 17 and macOS 14 and later, VisionKit identifies subjects within an image (see ImageAnalysisInteraction.Subject). A subject may be the focal point of a picture, such as an object around which a photograph centers. Or, the framework may identify several objects that it recognizes in an image. VisionKit enables your app to extract, or lift, subjects to a separate image with the background removed, or present a button that gives more information on the subject (visualLookUp).

**Note:** In macOS 14 and later, macOS apps built with Mac Catalyst support the ImageAnalyzer and ImageAnalysisInteraction classes.

## Topics

### Content recognition and interaction in images
- [Enabling Live Text interactions with images](https://developer.apple.com/documentation/visionkit/enabling_live_text_interactions_with_images) - Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- **ImageAnalyzer** - An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- **ImageAnalysis** - An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- **ImageAnalysisInteraction** - An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- **ImageAnalysisInteractionDelegate** - A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- **ImageAnalysisOverlayView** - A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- **ImageAnalysisOverlayViewDelegate** - A delegate that handles image-analysis and user-interaction callbacks for an overlay view.

### Barcode and text scanning through the camera
- [Scanning data with the camera](https://developer.apple.com/documentation/visionkit/scanning_data_with_the_camera) - Enable Live Text data scanning of text and codes that appear in the camera's viewfinder.
- **DataScannerViewController** - An object that scans the camera live video for text, data in text, and machine-readable codes.
- **DataScannerViewControllerDelegate** - A delegate object that responds when people interact with items that the data scanner recognizes.
- **RecognizedItem** - An item that the data scanner recognizes in the camera's live video.

### Document scanning through the camera
- [Structuring Recognized Text on a Document](https://developer.apple.com/documentation/visionkit/structuring_recognized_text_on_a_document) - Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- **VNDocumentCameraViewController** - An object that presents UI for a camera pass-through that helps people scan physical documents.
- **VNDocumentCameraViewControllerDelegate** - A delegate protocol through which the document camera returns its scanned results.
- **VNDocumentCameraScan** - A single document scanned in the document camera.

### Structures
- **CameraRegionView** - CameraRegionView displays a view of a stabilized region of interest within a user's view, and then provide Passthrough camera feed for the selected region. It also allows additional post-processing of the passthrough camera frames. Example of such region of interest could be documents, a user manual, gauges or displays. (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/VisionKit)*