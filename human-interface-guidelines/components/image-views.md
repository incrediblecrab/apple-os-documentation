# Image Views

An image view displays a single image — or in some cases, an animated sequence of images — on a transparent or opaque background.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Within an image view, you can stretch, scale, size to fit, or pin the image to a specific location. Image views are typically not interactive.

## Topics

### Best Practices

- **Use an image view when the primary purpose of the view is simply to display an image** - In rare cases where you might want an image to be interactive, configure a system-provided button to display the image instead of adding button behaviors to an image view.
- **Consider using a symbol or interface icon instead of an image view for icons** - SF Symbols provides a large library of streamlined, vector-based images that you can render with various colors and opacities. An icon (also called a glyph or template image) is typically a bitmap image in which the nontransparent pixels can receive color. Both symbols and interface icons can use the accent colors people choose.

### Content

- **An image view can contain rich image data in various formats** - Supports PNG, JPEG, and PDF. For more guidance, see [Images](https://developer.apple.com/design/human-interface-guidelines/images).
- **Take care when overlaying text on images** - Compositing text on top of images can decrease both the clarity of the image and the legibility of the text. To help improve the results, ensure the text contrasts well with the image, and consider ways to make the text object stand out, like adding a text shadow or background layer.
- **Aim to use a consistent size for all images in an animated sequence** - When you prescale images to fit the view, the system doesn't have to perform any scaling. In cases where the system must do the scaling, performance is generally better when all images are the same size and shape.

### Platform Considerations

**iOS and iPadOS**  
No additional considerations for iOS or iPadOS.

**macOS**  
- If your app needs an editable image view, use an image well. An image well is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.
- Use an image button instead of an image view to make a clickable image. An image button contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.

**tvOS**  
Many tvOS images combine multiple layers with transparency to create a feeling of depth. For guidance, see Layered images.

**visionOS**  
- You can add the appearance of depth to image views in a standard window to give your content more visual substance and improve the experience when people view it from an angle. If you display 3D content in a standard window, the system clips it when it extends too far from the window's surface; for guidance, see Windows.
- If you want to display true 3D content, use a volume; for guidance, see visionOS volumes.

**watchOS**  
Use SwiftUI to create animations when possible. Alternatively, you can use WatchKit to animate a sequence of images within an image element if necessary. For developer guidance, see WKImageAnimatable.

### Related Components

- [Images](https://developer.apple.com/design/human-interface-guidelines/images)
- [Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells)
- [Image buttons](https://developer.apple.com/design/human-interface-guidelines/image-buttons)
- [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)

### Developer Documentation

- [Image](https://developer.apple.com/documentation/swiftui/image) - SwiftUI
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) - UIKit
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) - AppKit

### Videos

- [Support HDR images in your app](https://developer.apple.com/videos/play/wwdc2023/10053/)
- [Add rich graphics to your SwiftUI app](https://developer.apple.com/videos/play/wwdc2023/10080/)

## Changelog

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/image-views)*