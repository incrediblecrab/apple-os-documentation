# Drag and drop

Using drag and drop, people can move or duplicate selected photos, text, and other content by dragging the selection from one location to another.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

To perform drag and drop, people select content in one location, called the source, and drop it in another, called the destination. These locations can be in the same container — like a text view — or in different containers, like text views on opposite sides of a split view, or even in different apps.

The operation depends on the platform, content, and agreement between source and destination. Moving within a container and copying between containers are useful defaults, not a universal rule for every drag. UIKit permits a move only within the same app and requires copying data shared with another app; its delegates still implement the actual insertion and removal. AppKit exposes operation masks for different dragging contexts, so don't generalize UIKit's cross-app rule to every Mac operation.

People use different interactions to perform drag and drop depending on platform. For example:

- In visionOS, people pinch and hold a virtual object while dragging it to a new location in any direction, including along the z-axis.
- iOS and iPadOS support drag and drop through gestures on the touchscreen, interactions with a pointing device, and through full keyboard-access mode.
- Universal Control lets people drag content between their Mac and iPad.
- On a Mac, people can interact with a pointing device, use full keyboard access mode, or use VoiceOver to perform drag and drop.

## Topics

### Best practices

- **Support drag and drop throughout your app** - Most people are familiar with drag and drop and they often try it everywhere. When you use system-provided components — such as text fields and text views — you get built-in support for drag and drop.

- **Offer alternative ways to accomplish drag-and-drop actions** - Sometimes, drag-and-drop operations are inconvenient or impossible for people to perform, so it's important to provide other ways to do the same things. For example, you can include menu commands that people can use to copy an item and move it to another location. In iOS and iPadOS, you can use accessibility APIs to identify sources and destinations so that people can use assistive technologies to drag and drop in your app (for developer guidance, see accessibilityDragSourceDescriptors and accessibilityDropPointDescriptors).

- **Determine when dragging and dropping content results in a move or a copy** - In general, a move makes sense when the source and destination containers are the same — such as dragging text from one location to another within a document — and a copy makes sense when they're different, like dragging an image from one document to another. Before you change these defaults, consider the behavior that most people expect and prefer the one that is least likely to result in frustration or data loss.

- **Support multi-item drag and drop when appropriate** - Let people move a selected group instead of handling every item separately. On iPad, supported interactions can add items to a drag already in progress. Don't assume that touch-based gathering or multiple simultaneous drag activities work identically on a Mac.

- **Prefer letting people undo a drag-and-drop operation** - Sometimes, people inadvertently drop content in the wrong destination, so they appreciate being able to undo the action and return to their previous state. You might also be able to help people avoid mistakes by asking for confirmation before completing a drag-and-drop operation that can't be undone. In macOS, for example, the Finder asks for confirmation when people drag a file into a write-only folder because they won't be able to open the folder and remove the dropped item. If a drop starts a sharing operation, provide a way to stop or reverse it when the service supports that; don't imply that already-delivered copies can always be recalled.

- **Offer multiple versions of dragged content** - By providing multiple alternatives ordered from highest to lowest fidelity, the destination can choose the highest quality version it can accept. For example, if people can drag a line drawing they created in your app, you could offer a PDF vector representation, a lossless PNG image with transparency, and a lossy JPEG image without transparency, in that order. Another example is an app that uses rich, complicated objects, like charts. This app might offer the native chart object followed by a simpler version — like an image of the chart — for destinations that don't support chart objects.

- **Consider supporting spring loading** - Spring loading lets people activate supporting controls while holding dragged content over them, making another view or destination accessible without ending the drag. Activation depends on the platform, input device, and preferences: for example, a supported Force Touch trackpad can offer pressure-based activation, while supported iPad controls can respond to hovering dragged content.

### Providing feedback

Drag and drop is a dynamic process that can result in multiple outcomes. To help people feel in control of the process, provide clear and continuous feedback throughout.

- **Display the drag preview promptly** - The HIG describes showing feedback after approximately three points of selection movement. Treat that as design guidance, not a universal gesture-recognition constant for touch, pointer, and spatial input. Use the platform's drag lifecycle and previews; a translucent representation can distinguish the dragged content while keeping destinations visible.

- **Modify the drag image to help predict results** - If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation. For example, when dragging a photo into a document, the drag image could expand to show the default size of the photo in the document. You can also use drag flocking to visually group multiple drag items — letting people confirm that they haven't missed an item they want to drag — and then ungroup the items when people drop them. Although changing the drag image can provide valuable feedback, avoid creating a distracting experience in which the drag image is constantly and radically changing.

- **Show whether a destination can accept content** - For example, you might display an insertion point or highlight a containing view only when the destination can accept a dragged item, and show no visual feedback — or an explicit "not allowed" image, like the circle.slash from SF Symbols — when it can't. Display highlighting or other visual cues only while the content is positioned above the destination, removing the visual feedback when people drag the content away. When there are multiple possible destinations, provide visual cues that help people identify one at a time.

- **Provide feedback for invalid drops** - When people drop an item on an invalid destination, or when dropping fails, provide visual feedback. For example, the item can move back from its current location to its source (if the source is still visible) or it can scale up and fade out to give the impression of the item evaporating instead of landing successfully.

### Accepting drops

- **Scroll the contents when necessary** - When people drag an item within a scrolling container that has a lot of content, the content can automatically scroll as people move the item over it. This behavior makes it easy for people to find the right place to drop the item, but if they continue the drag operation outside of the container, automatic scrolling is no longer necessary. System-provided text views and text fields behave this way by default.

- **Pick the richest version of dropped content** - When there's a choice, pick the richest version of dropped content your app can accept. For example, if people drag a chart object from another app, the drag operation might offer both the rich, native chart object and a simple image of it. If your app supports charts, extract and display the native chart object; if it doesn't, use the image instead.

- **Extract only the relevant portion** - For example, when people drag a contact to a recipient field in an email, Mail displays only the name and email address, not the contact's address information.

- **Honor supported modifier-key behavior at drop time** - Where Option requests a copy, evaluate the final modifier state rather than only the state at drag start. Advertise and perform only operations that the source and destination allow; a modifier doesn't make an unsupported copy or move valid.

- **Provide feedback for time-consuming transfers** - For example, you might display a progress indicator to help people estimate how long the transfer will take. In collections, lists, and tables, you might also display a placeholder at the drop location so people know where to find the content after it finishes transferring. The system can display an alert when a time-consuming transfer occurs between apps.

- **Provide feedback when drops initiate tasks** - If people drop content onto a control that initiates a task — such as printing — show people that the task has begun and keep them informed of its progress.

- **Apply appropriate styling to dropped text** - When the source and destination both support the same text styles, make sure dropped text maintains its original font, typeface, size, and other attributes. Otherwise, apply the destination's style to dropped text.

- **Maintain selection state after a drop** - People expect the content they drop to remain selected so they can immediately act on it. When the source and destination are the same container, the content disappears from its original location when the drag operation performs a move. When a drag operation within the same container performs a copy, remove the selection state from the content that remains in the original location. When people drag selected content to a different container, deselect the content in the source.

### Platform considerations

Not supported in tvOS or watchOS.

**iOS, iPadOS**  
Let people perform multiple simultaneous drag activities. In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional app icons before dropping all of them in a different Home Screen or in a folder. To support this interaction, you need to let people add items during a drag — providing visual feedback through flocking — and accept multiple, simultaneous drops.

**macOS**  
- Consider letting people drag content from your app into the Finder. When you support this, be sure to present the content in a format your app can open later. For example, Calendar lets people drag an event to the Finder as an .ics file that can be shared or reopened. Text can also be represented by a clipping file that people later drag into a compatible destination. A clipping is separate from the Clipboard; don't imply that the system automatically deletes it after the drag.

- Let people drag selected content from an inactive window without first making the window active. Selected content in an inactive window is known as a background selection and has a different appearance from selected content in the active window. In general, people expect to drag a background selection to the active window without bringing the inactive window forward.

- When possible, let people drag individual items from an inactive window without affecting an existing background selection. For example, people can drag an unselected file from an inactive Finder window without deselecting any of the window's selected files.

- Consider displaying a badge during multi-item drag operations. A badge is a small filled oval containing a number you can use to indicate the number of items people are dragging. If a destination can accept only a subset of dragged items, update the badge to show the new number.

- Consider changing the pointer appearance to indicate what will happen when people drop content. In addition to using the copy pointer, you might want to use the drag link, disappearing item, and operation not allowed pointers, depending on the situation. For guidance, see Pointers.

- As much as possible, let people select and drag content with a single motion. Unless people are selecting multiple items, they appreciate it when they don't have to pause between making a selection and starting the drag operation.

**visionOS**  
When appropriate, support opening content dropped into empty space. Associate a user activity with draggable content and configure the app to handle that activity and activate the appropriate scene. The HIG illustrates URLs opening in Safari and supported files opening in Quick Look; these are examples, not a promise that any dropped payload launches your app. See [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity).

### Related

- [Universal Control](https://support.apple.com/en-us/102459)

### Developer documentation

- [Drag and drop — UIKit](https://developer.apple.com/documentation/uikit/drag-and-drop)
- [UIDropOperation.move](https://developer.apple.com/documentation/uikit/uidropoperation/move) - Same-app restriction and delegate responsibilities
- [Drag and Drop — AppKit](https://developer.apple.com/documentation/appkit/drag-and-drop)
- [NSDraggingSource operation mask](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:sourceoperationmaskfor:)) - Permitted operations by dragging context
- [File Provider](https://developer.apple.com/documentation/fileprovider)

### Videos

- [What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059)
- [SwiftUI on the Mac: The finishing touches](https://developer.apple.com/videos/play/wwdc2021/10289)
- [Designed for iPad](https://developer.apple.com/videos/play/wwdc2020/10206)

## Changelog

These dates describe Apple's HIG article history.

### October 24, 2023
- Added artwork.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)*
