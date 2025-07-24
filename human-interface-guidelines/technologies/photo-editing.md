# Photo Editing

Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or making other changes.

**Platforms:** iOS | iPadOS | macOS

## Overview

Edits are always saved in the Photos app as new files, safely preserving the original versions.

To access a photo editing extension, a photo must be in edit mode. While in edit mode, tapping the extension icon in the toolbar displays an action menu of available editing extensions. Selecting one displays the extension's interface in a modal view containing a top toolbar. Dismissing this view confirms and saves the edit, or cancels it and returns to the Photos app.

## Topics

### Best Practices

- **Confirm cancellation of edits** - Editing a photo or video can be time consuming. If someone taps the Cancel button, don't immediately discard their changes. Ask them to confirm that they really want to cancel, and inform them that any edits will be lost after cancellation. There's no need to show this confirmation if no edits have been made yet.

- **Don't provide a custom top toolbar** - Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from the content being edited.

- **Let people preview edits** - It's hard to approve an edit if you can't see what it looks like. Let people see the result of their work before closing your extension and returning to the Photos app.

- **Use your app icon for your photo editing extension icon** - This instills confidence that the extension is in fact provided by your app.

### Developer Documentation

- [App extensions](https://developer.apple.com/documentation/appextensions) - App Extensions
- [PhotoKit](https://developer.apple.com/documentation/photokit) - PhotoKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/photo-editing)*