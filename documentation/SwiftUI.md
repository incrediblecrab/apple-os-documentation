# SwiftUI

Declare the user interface and behavior for your app on every platform.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

SwiftUI provides views, controls, and layout structures for declaring your app's user interface. The framework provides event handlers for delivering taps, gestures, and other types of input to your app, and tools to manage the flow of data from your app's models down to the views and controls that users see and interact with.

For the SwiftUI app life cycle, use the [`App`](https://developer.apple.com/documentation/swiftui/app) protocol and populate it with scenes. This protocol requires iOS/iPadOS/Mac Catalyst/tvOS 14+, macOS 11+, watchOS 7+, or visionOS 1+; it did not ship at every original framework minimum. Create custom views conforming to **View** and compose them with text, images, shapes, stacks, and lists. View modifiers customize rendering and interaction, while platform-aware controls allow substantial code sharing without making every API available everywhere.

You can integrate SwiftUI views with objects from the UIKit, AppKit, and WatchKit frameworks to take further advantage of platform-specific functionality. You can also customize accessibility support in SwiftUI, and localize your app's interface for different languages, countries, or cultural regions.

## Featured Samples

- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass) - System-provided and custom Liquid Glass.
- [Destination Video](https://developer.apple.com/documentation/visionos/destination-video) - Multiplatform media browsing and playback.
- [BOT-anist](https://developer.apple.com/documentation/visionos/bot-anist) - A shared iOS/iPadOS/macOS/visionOS app with platform-specific windows and volumes.
- [Building a document-based app with SwiftUI](https://developer.apple.com/documentation/swiftui/building-a-document-based-app-with-swiftui) - Document creation, saving, and opening.

## OS 27 migration

The following changes are documented in the September 2026 betas; they do not raise SwiftUI's framework minimums above.

### State initialization in Xcode 27

Xcode 27 implements [`@State` with a macro](https://developer.apple.com/documentation/swiftui/state()). A declaration such as `@State private var model = Model()` no longer repeatedly evaluates its initial-value expression when SwiftUI recreates the view value. This behavior back-deploys to iOS/iPadOS/Mac Catalyst 17, macOS 14, tvOS 17, watchOS 10, and visionOS 1 and later, rather than requiring an OS 27 runtime.

Audit custom initializers when rebuilding:

- Choose either a declaration default or an initializer assignment. Assigning again after a declaration default does not replace the managed initial value; that behavior is not new, but some formerly accepted cases now fail to compile.
- If initialization needs an argument, omit the declaration default and assign the property explicitly.
- Extensions that called the synthesized private memberwise initializer must initialize members explicitly; the macro disables that synthesized initializer.
- Add explicit generic type information where inference fails. Composing `@State` with another property wrapper or macro is unsupported.

```swift
import SwiftUI

struct DraftTitle: View {
    @State private var title: String

    init(initialTitle: String) {
        self.title = initialTitle
    }

    var body: some View {
        TextField("Title", text: $title)
    }
}
```

The argument seeds state; later parent-view updates are not a way to overwrite state for the same view identity. Use a binding when the parent owns the value.

### Network images

[`AsyncImage`](https://developer.apple.com/documentation/swiftui/asyncimage) supports HTTP caching on OS 27. Standard server headers, request cache policy, and session configuration govern reuse; this is not permanent offline storage. New request-based initializers include [`init(request:scale:content:placeholder:)`](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:content:placeholder:)) and [`init(request:scale:transaction:content:)`](https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:transaction:content:)). [`asyncImageURLSession(_:)`](https://developer.apple.com/documentation/swiftui/view/asyncimageurlsession(_:)) supplies the session for descendant image views.

Those additions require version 27 across the listed SwiftUI platforms. `AsyncImage` itself remains available from iOS/iPadOS/Mac Catalyst/tvOS 15, macOS 12, watchOS 8, and visionOS 1. Test expiration, revalidation, failures, and any custom `URLCache` configuration. See [Foundation](Foundation.md).

### URL-based documents

On iOS, iPadOS, Mac Catalyst, macOS, and visionOS 27+, use [`ReadableDocument`](https://developer.apple.com/documentation/swiftui/readabledocument) for read-only documents or [`Document`](https://developer.apple.com/documentation/swiftui/document), which also adopts [`WritableDocument`](https://developer.apple.com/documentation/swiftui/writabledocument), for editing. These reference-type models support asynchronous URL-based I/O and progress. The current notes deprecate `FileDocument` and `ReferenceFileDocument`, not remove them. The latter's [per-platform metadata](https://developer.apple.com/documentation/swiftui/referencefiledocument) still lacks a visionOS deprecation version, unlike its iOS/iPadOS/Mac Catalyst/macOS entries; don't infer a removal or uniform warning across platforms.

- [`DocumentGroup`](https://developer.apple.com/documentation/swiftui/documentgroup) has new factories and launch/customization options, including editing-only flows.
- [`DocumentReader`](https://developer.apple.com/documentation/swiftui/documentreader) and [`DocumentWriter`](https://developer.apple.com/documentation/swiftui/documentwriter) define asynchronous reading and writing operations. Match the `@concurrent` requirements for [`read(from:progress:)`](https://developer.apple.com/documentation/swiftui/documentreader/read(from:progress:)) and [`write(snapshot:to:previous:progress:)`](https://developer.apple.com/documentation/swiftui/documentwriter/write(snapshot:to:previous:progress:)), rather than earlier-beta `nonisolated` declarations. The writer's formal declaration uses `snapshot:` even though some current prose and examples still say `content:`.
- [`URLDocumentConfiguration`](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration) is an observable, main-actor-isolated reference, **not `Sendable`**. Document factories are also main-actor isolated; do not capture the configuration in unrelated sendable work.
- Register undo actions for user edits so autosave can observe them. When migrating `FileWrapperDocumentWriter`, accept its second `previous` argument to reuse unchanged package content.

Follow [Updating your document-based app](https://developer.apple.com/documentation/swiftui/updating-your-document-based-app). The beta notes still list document progress not appearing as a **known issue**, not a permanent API limitation.

### Layout, input, and toolbars

- [`GeometryProxy.concentricCornerRadii`](https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii) and [`concentricCornerRadii(in:)`](https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii(in:)) return optional corner geometry for custom layout/drawing on OS 27; handle `nil` when there is no suitable container shape. The latter accepts a `CGRect` in the view's local coordinate space.
- [`textInputBorderShape(_:)`](https://developer.apple.com/documentation/swiftui/view/textinputbordershape(_:)) customizes text-input borders on OS 27. Prefer `.textFieldStyle(.bordered)` over the soft-deprecated `.squareBorder` and `.roundedBorder` styles.
- Rebuilding for iOS/iPadOS 27 gives selectable `Text` the system selection gestures. Review competing custom gestures; use `highPriorityGesture` only when the custom interaction should win. Selectable text also supports `TextRenderer` in apps built with the iOS/macOS 27 SDKs.
- [`toolbarMinimizationBehavior(_:for:)`](https://developer.apple.com/documentation/swiftui/view/toolbarminimizationbehavior(_:for:)) replaces the earlier-beta `toolbarMinimizeBehavior` spelling; its supported placement is `.navigationBar`. Review safe-area changes as bars minimize.
- [`ToolbarOverflowMenu`](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) places secondary actions in overflow on iOS/iPadOS/Mac Catalyst/visionOS 27+. [`visibilityPriority(_:)`](https://developer.apple.com/documentation/swiftui/toolbarcontent/visibilitypriority(_:)) keeps higher-priority toolbar items visible longer; it is available from macOS 26.1 and from 27 on the other listed platforms. The new `.statusBar` placement supports preferred color scheme and visibility.
- [`TabsPickerStyle`](https://developer.apple.com/documentation/swiftui/tabspickerstyle) gives navigation pickers tab semantics for VoiceOver on its supported 27 platforms (not watchOS). In iOS/iPadOS 27 SDK builds, keep `TabView` selection on a visible, available tab to avoid a crash.
- Menu icons have new visibility defaults on iPadOS/macOS 27. Use `.labelStyle(.titleAndIcon)` when an icon is needed to identify content, guided by the [menu HIG](https://developer.apple.com/design/human-interface-guidelines/menus).

### Integration and design

[`UIHostingSceneDelegate`](https://developer.apple.com/documentation/swiftui/uihostingscenedelegate) bridges SwiftUI scenes into UIKit (iOS/iPadOS/Mac Catalyst/visionOS 26+, tvOS 27+); [`NSHostingSceneRepresentation`](https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation) provides the AppKit bridge on macOS 26+. UIKit hosts must meet the [scene-lifecycle requirement](UIKit.md#os-27-migration).

Liquid Glass APIs belong to `SwiftUI`, not a separate import. [`glassEffect(_:in:)`](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) and [`GlassEffectContainer`](https://developer.apple.com/documentation/swiftui/glasseffectcontainer) list iOS/iPadOS/Mac Catalyst/macOS/tvOS/watchOS 26+, **not visionOS**. [`backgroundExtensionEffect()`](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()) also supports visionOS 26. For visionOS glass, use its own APIs, such as [`glassBackgroundEffect(in:displayMode:)`](https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:)), available from visionOS 1.

Use standard controls first and follow [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass). Test Reduce Transparency, Increase Contrast, text sizing, and different backgrounds rather than assuming a particular material rendering. See [Bundle Resources](BundleResources.md#ui-design-compatibility) for the exact build-target rules for `UIDesignRequiresCompatibility`.

Sources: [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui), [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), and [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes). For testing tools, see [Xcode](Xcode.md) and [XCUIAutomation](XCUIAutomation.md).

## Topics

### Essentials
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) - Find out how to bring the new material to your app
- [Develop in Swift](https://developer.apple.com/tutorials/develop-in-swift) - Introductory Swift and Xcode app-development tutorials.
- [Exploring SwiftUI Sample Apps](https://developer.apple.com/tutorials/sample-apps) - Sample projects covering user interfaces, interactions, and data flow.
- [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui) - Learn about important changes to SwiftUI
- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass) - Enhance your app experience with system-provided and custom Liquid Glass

### App Structure
- **App organization** - Define the entry point and top-level structure of your app
- **Scenes** - Declare the user interface groupings that make up the parts of your app
- **Windows** - Display user interface content in a window or a collection of windows
- **Immersive spaces** - Display unbounded content in a person's surroundings
- **Documents** - Enable people to open and manage documents
- **Navigation** - Enable people to move between different parts of your app's view hierarchy within a scene
- **Modal presentations** - Present content in a separate view that offers focused interaction
- **Toolbars** - Provide immediate access to frequently used commands and controls
- **Search** - Enable people to search for text or other content within your app
- **App extensions** - Extend your app's basic functionality to other parts of the system, like by adding a Widget

### Data and Storage
- **Model data** - Manage the data that your app uses to drive its interface
- **Environment values** - Share data throughout a view hierarchy using the environment
- **Preferences** - Indicate configuration preferences from views to their container views
- **Persistent storage** - Store data for use across sessions of your app

### Views
- **View fundamentals** - Define the visual elements of your app using a hierarchy of views
- **View configuration** - Adjust the characteristics of views in a hierarchy
- **View styles** - Apply built-in and custom appearances and behaviors to different types of views
- **Animations** - Create smooth visual updates in response to state changes
- **Text input and output** - Display formatted text and get text input from the user
- **Images** - Add images and symbols to your app's user interface
- **Controls and indicators** - Display values and get user selections
- **Menus and commands** - Provide space-efficient, context-dependent access to commands and controls
- **Shapes** - Trace and fill built-in and custom shapes with a color, gradient, or other pattern
- **Drawing and graphics** - Enhance your views with graphical effects and customized drawings

### View Layout
- **Layout fundamentals** - Arrange views inside built-in layout containers like stacks and grids
- **Layout adjustments** - Make fine adjustments to alignment, spacing, padding, and other layout parameters
- **Custom layout** - Place views in custom arrangements and create animated transitions between layout types
- **Lists** - Display a structured, scrollable column of information
- **Tables** - Display selectable, sortable data arranged in rows and columns
- **View groupings** - Present views in different kinds of purpose-driven containers, like forms or control groups
- **Scroll views** - Enable people to scroll to content that doesn't fit in the current display

### Event Handling
- **Gestures** - Define interactions from taps, clicks, and swipes to fine-grained gestures
- **Input events** - Respond to input from a hardware device, like a keyboard or a Touch Bar
- **Clipboard** - Enable people to move or duplicate items by issuing Copy and Paste commands
- **Drag and drop** - Enable people to move or duplicate items by dragging them from one location to another
- **Focus** - Identify and control which visible object responds to user interaction
- **System events** - React to system events, like opening a URL

### Accessibility
- **Accessibility fundamentals** - Make your SwiftUI apps accessible to everyone, including people with disabilities
- **Accessible appearance** - Enhance the legibility of content in your app's interface
- **Accessible controls** - Improve access to actions that your app can undertake
- **Accessible descriptions** - Describe interface elements to help people understand what they represent
- **Accessible navigation** - Enable users to navigate to specific user interface elements using rotors

### Framework Integration
- **AppKit integration** - Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app
- **UIKit integration** - Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app
- **WatchKit integration** - Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app
- **Technology-specific views** - Use SwiftUI views that other Apple frameworks provide

### Tool Support
- **Previews in Xcode** - Generate dynamic, interactive previews of your custom views
- **Xcode library customization** - Expose custom views and modifiers in the Xcode library
- **Performance analysis** - Measure and improve your app's responsiveness

### Web Content and Rich Text (iOS 26 generation)
- [WebKit `WebView`](https://developer.apple.com/documentation/webkit/webview-swift.struct) and [`WebPage`](https://developer.apple.com/documentation/webkit/webpage) - WebKit types for displaying and managing web content in SwiftUI; import `WebKit` as well as `SwiftUI`.
- [Rich text `TextEditor`](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:)-11r0a) - Edits `AttributedString` with optional attributed-text selection on iOS/iPadOS/Mac Catalyst/macOS/visionOS 26+. It is a SwiftUI control, not a WebKit API.

### Protocols
- [`RoundedRectangularShape`](https://developer.apple.com/documentation/swiftui/roundedrectangularshape) - Refines `InsettableShape` for rounded rectangles; 26+ on the listed SwiftUI platforms.
- [`SliderTickContent`](https://developer.apple.com/documentation/swiftui/slidertickcontent) - Content for a `SliderTickBuilder`; 26+ on iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS, not tvOS.

### Structures
- [`AnyCompositorContent`](https://developer.apple.com/documentation/swiftui/anycompositorcontent) - Type-erased compositor content for macOS and visionOS 26+.
- [`ConcentricRectangle`](https://developer.apple.com/documentation/swiftui/concentricrectangle) - Resolves a shape concentric with its container; 26+.
- [`RectangleCornerInsets`](https://developer.apple.com/documentation/swiftui/rectanglecornerinsets) - Insets at the corners of a rectangle; 26+.
- [`RoundedRectangularShapeCorners`](https://developer.apple.com/documentation/swiftui/roundedrectangularshapecorners) - Corner styles for a rounded rectangular shape; 26+.
- [`SliderTick`](https://developer.apple.com/documentation/swiftui/slidertick) - Slider tick content, with the same non-tvOS 26+ platform set as `SliderTickContent`.

### Xcode 26 Features
- **`#Playground` blocks** - Interactive code exploration in Xcode's preview panel. See [Xcode](Xcode.md) for toolchain-specific playground guidance.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SwiftUI)*
