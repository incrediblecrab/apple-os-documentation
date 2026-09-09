# ClassKit UI

Present submission controls and assignment status for student documents.

**Platforms:** The SwiftUI controls are available on iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, and visionOS 26.4+. UIKit menu integration excludes macOS; AppKit menu integration is macOS-only. This is a 26.4 addition, not a new OS 27 framework.

## Overview

ClassKit UI connects document submission controls to [ClassKit](ClassKit.md). The controls load assignment information, show submission or withdrawal actions, and update their presentation when the document's submission state changes. Use them instead of maintaining an independent, potentially stale copy of the assignment status.

This framework is for assigned documents. It does not replace ClassKit's activity catalog and progress-reporting APIs, or the server-side [ClassKit Catalog API](ClassKitCatalogAPI.md).

## Prerequisites and authorization

Add the [ClassKit environment entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.classkit-environment) to the app and configure its ClassKit integration. Pass the URL of the assigned document to the control. An ordinary local file does not become a Schoolwork assignment simply because the app displays a submission button.

Check the availability of each UI type when supporting older deployment targets. Do not infer watchOS or tvOS support from the availability of SwiftUI itself.

## Topics

| UI | API | Use |
|---|---|---|
| SwiftUI | [`AssignedDocumentSubmissionButton`](https://developer.apple.com/documentation/classkitui/assigneddocumentsubmissionbutton) | Submit or withdraw a document, with system-managed loading and submission states. |
| SwiftUI | [`AssignedDocumentLabel`](https://developer.apple.com/documentation/classkitui/assigneddocumentlabel) | Display submission status or relevant dates using the `.status` or `.date` role. |
| UIKit | [`AssignedDocumentDeferredMenuElement`](https://developer.apple.com/documentation/classkitui/assigneddocumentdeferredmenuelement) | Load submission actions asynchronously in a menu on iOS, iPadOS, Mac Catalyst, or visionOS 26.4+. |
| AppKit | [`AssignedDocumentMenuItem`](https://developer.apple.com/documentation/classkitui/assigneddocumentmenuitem) | Add submission actions to a macOS 26.4+ menu. |

## Submission lifecycle and failure handling

For SwiftUI, use [`onAssignedDocumentWillSubmit(_:)`](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillsubmit(_:)) to prepare or validate the file. Return `false` when validation fails and explain what the student needs to fix. Use [`onAssignedDocumentDidSubmit(_:)`](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentdidsubmit(_:)) for work that should occur only after a successful submission.

The corresponding withdrawal hooks are [`onAssignedDocumentWillWithdraw(_:)`](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillwithdraw(_:)) and [`onAssignedDocumentDidWithdraw(_:)`](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentdidwithdraw(_:)). UIKit and AppKit menu controls provide lifecycle closures as well.

Keep local document changes safe while the control loads or submits. A tap or successful local validation is not confirmation of submission: do not mark the assignment submitted before its successful completion/state update. Test unavailable assignment data, invalid document contents, and interrupted submissions without discarding the student's work.

## Sources

- [ClassKit UI](https://developer.apple.com/documentation/classkitui)
- [AssignedDocumentSubmissionButton](https://developer.apple.com/documentation/classkitui/assigneddocumentsubmissionbutton)
- [AssignedDocumentLabel](https://developer.apple.com/documentation/classkitui/assigneddocumentlabel)
- [AssignedDocumentDeferredMenuElement](https://developer.apple.com/documentation/classkitui/assigneddocumentdeferredmenuelement)
- [AssignedDocumentMenuItem](https://developer.apple.com/documentation/classkitui/assigneddocumentmenuitem)
