# Image Playground

Present a system interface to generate images based on descriptive information.

**Platforms:** iOS 18.1+ | iPadOS 18.1+ | Mac Catalyst 18.1+ | macOS 15.1+ | visionOS 2.4+

## Overview

Use the ImagePlayground framework to generate custom images using system-supported styles. To generate images, you specify a text description of what you want, an optional image, and the style you want the image to adopt. Use that information to present a system sheet from your SwiftUI view, or present a system view controller from your UIKit or AppKit interface. The system interface manages all interactions with the person, and upon success delivers an image for you to incorporate into your content. You can also use a programmatic interface to generate images without interactions.

## Topics

### SwiftUI presentation
- **imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.
- **imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.
- **imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)** - Presents the system sheet to create images from the specified input.

### UIKit and AppKit presentation
- **ImagePlaygroundViewController** - Displays a standard system interface to generate images from the provided input.

### Programmatic creation
- **ImageCreator** - Generates images programmatically from the description and style information you specify.

### Platform support
- **ImagePlaygroundConcept** - Text elements that specify the content to include in the image.
- **ImagePlaygroundStyle** - Style options that determine the appearance of generated images.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImagePlayground)*