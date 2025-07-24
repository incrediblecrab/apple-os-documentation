# Action Sheets

An action sheet is a modal view that presents choices related to an action people initiate.

**Platforms:** iOS | iPadOS | tvOS | watchOS

## Overview

When you use SwiftUI, you can offer action sheet functionality in all platforms by specifying a presentation modifier for a confirmation dialog. If you use UIKit, you use the UIAlertController.Style.actionSheet to display an action sheet in iOS, iPadOS, and tvOS.

## Topics

### Best Practices

- **Use action sheets for intentional actions** - Offer choices related to an intentional action, not for alerts about problems or unexpected situations.
- **Use sparingly** - Action sheets interrupt the current task, so avoid overusing them.
- **Keep titles short** - Aim for single-line titles that are easy to read quickly.
- **Provide messages only when necessary** - The title and context usually provide sufficient information.
- **Include Cancel button for destructive actions** - Place at bottom of sheet (or upper-left in watchOS).
- **Make destructive choices prominent** - Use destructive style and place at top of the sheet.

### Platform Considerations

**iOS, iPadOS**  
- Use action sheets instead of menus for action-related choices
- Avoid scrolling action sheets
- Limit the number of buttons to prevent complexity

**watchOS**  
- System style includes title, optional message, Cancel button, and additional buttons
- Three button styles available: Default, Destructive, and Cancel
- Limit to four buttons maximum (including Cancel)
- Cancel button is required

**macOS, tvOS**  
No additional platform-specific considerations.

**visionOS**  
Not supported.

### Related Components

- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) - General principles for modal interfaces
- [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) - Related modal presentation style
- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) - For unexpected situations requiring attention

### Developer Documentation

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)) - SwiftUI
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) - UIKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/action-sheets)*