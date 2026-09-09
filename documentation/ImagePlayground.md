# Image Playground

Present a system interface to generate images based on descriptive information.

**Platforms:** iOS 18.1+ | iPadOS 18.1+ | Mac Catalyst 18.1+ | macOS 15.1+ | visionOS 2.4+

## Overview

Use the ImagePlayground framework to generate custom images using system-supported styles. To generate images, you specify a text description of what you want, an optional image, and the style you want the image to adopt. Use that information to present a system sheet from your SwiftUI view, or present a system view controller from your UIKit or AppKit interface. The system interface manages all interactions with the person, and upon success delivers an image for you to incorporate into your content. The older programmatic `ImageCreator` interface is deprecated in OS 27; Apple recommends the system presentation APIs instead.

## Topics

### SwiftUI presentation
- **imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.
- **imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.
- **imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.

### UIKit and AppKit presentation
- **ImagePlaygroundViewController** - Displays a standard system interface to generate images from the provided input.

### Programmatic creation
- [ImageCreator](https://developer.apple.com/documentation/imageplayground/imagecreator.md) - Generates images programmatically on supported devices. Introduced in iOS/iPadOS/Mac Catalyst 18.4, macOS 15.4, and visionOS 2.4; deprecated at version 27.0 on those platforms in favor of `ImagePlaygroundViewController` or `imagePlaygroundSheet`.

### Platform support
- **ImagePlaygroundConcept** - Text elements that specify the content to include in the image.
- **ImagePlaygroundStyle** - Style options that determine the appearance of generated images.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImagePlayground)*
