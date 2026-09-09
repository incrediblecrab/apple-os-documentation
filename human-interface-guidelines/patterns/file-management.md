# File management

Some apps can support documents and files that people expect to manage throughout the system.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Document-based apps — such as Pages, Keynote, Photos, and Preview — help people create, edit, and save documents and files, often providing customized ways for people to browse for content they want to open in the app.

People also expect to browse documents without first opening a document-based app. On a Mac, for example, people use the Finder to access the macOS file system; on iPhone, iPad, and Apple Vision Pro, people use the Files app to manage the documents and files on their device. In watchOS and tvOS, people don't typically create, edit, or manage documents, so these systems don't provide a document-browsing interface.

## Topics

### Creating and opening files

- **Use app menus and keyboard shortcuts** - Give people convenient ways to create and open documents. In iPadOS and macOS, people expect to create new documents or open existing ones using familiar menu commands. When you provide commands like New or Open, iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard, and macOS presents them in the menu bar File menu. Regardless of the availability of keyboard shortcuts, include an Add (+) button to help people create a new document. In a macOS app, you put the add action in the File menu (for guidance, see File menu).

- **Support platform file system understanding** - Prefer familiar Finder or Files browsing conventions. A custom browser can start in a relevant folder or the last selected location, but should let people navigate other accessible locations. Respect sandbox and permission boundaries; this isn't a promise of unrestricted access to the device's entire file system.

### Saving work

- **Preserve work automatically** - Help people be confident that their work is always preserved unless they cancel or delete it. In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they're editing and when they close a file or switch to another app.

- **Hide file extensions by default** - But let people view them if they choose. Be sure to reflect the current choice in all the save or open interfaces you display.

### Quick Look previews

Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them. For example, you can use Quick Look to let people listen to a preview of an audio file, add markup to a photo's preview, or rotate and scale a 3D file preview to examine it in different ways.

- **Use Quick Look for formats it can preview even when your app can't edit them** - For example, people can inspect a supported attachment without leaving your app. Handle unavailable previews gracefully; supported file types and interactions can differ by platform and OS release.

- **Provide previews or thumbnails for custom file types** - A [Quick Look preview extension](https://developer.apple.com/documentation/quicklook) can render your format for previewing, while a [Thumbnail Extension](https://developer.apple.com/documentation/quicklookthumbnailing) supplies miniature representations. These help system surfaces and other apps present your documents; use the extension mechanism appropriate to the target platform rather than assuming legacy Mac generators are universal.

### Platform considerations

tvOS and watchOS don't ordinarily offer a general-purpose document browser. This is a difference in user-facing experience, not a statement that apps on those platforms can't manage files.

#### iOS, iPadOS

##### Document launcher

Starting in iOS 18 and iPadOS 18, document-based apps can use the system's document launcher to give people a consistent, highly graphical way to browse, open, and create files. In this mobile presentation, the launcher highlights your app's theme while keeping document creation accessible. [DocumentGroupLaunchScene](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene) also lists Mac Catalyst 18 and visionOS 2 availability; this HIG section describes the iOS and iPadOS design.

The HIG describes three main regions:

- A title card that displays the app title and prominent app-specific actions
- A background image that appears behind the title card and additional images — called accessories — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize the title, actions, background, accessories, and supported browser controls. Without a custom title or actions builder, `DocumentGroupLaunchScene` uses the app name and a default Create Document action. The HIG's primary-and-secondary-button composition is guidance, not a requirement to supply exactly two buttons.

- **Assign the title card's buttons to your app's most important functions** - A primary action can create a document, with a secondary action offering options such as choosing a template. Use labels that accurately describe your own app's behavior.

- **Provide a distinct background** - Create a background that's clearly distinct from the accessories and title card. You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

- **Be mindful of accessory placement** - You can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

- **Use animation sparingly** - Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app's content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see Motion.

##### File provider app extension

Use a [File Provider extension](https://developer.apple.com/documentation/fileprovider) when your app supplies and synchronizes documents from remote storage. The extension integrates those documents with system browsing; it isn't synonymous with a custom document-picker screen. Sharing only local documents doesn't require a File Provider extension. The framework documents the appropriate document-browser or file-sharing configuration for that case.

- **Make document eligibility clear** - Configure the browser or picker for the content types your app can accept, and expose useful file metadata such as modification dates, sizes, and local or remote status. A PDF editor should let people select supported PDFs rather than implying it can open every supplied format.

- **Let people select a destination** - Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy when exporting and moving documents. You could also provide a way to add new subdirectories.

- **Avoid duplicating system browsing controls** - When adding custom UI to a system-hosted document workflow, don't add a competing top toolbar. This doesn't mean every modern File Provider extension supplies its own modal browsing interface.

Your app can also let people browse and open files from other apps. See [Adding a document browser to your app](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app). A `UIDocumentBrowserViewController` belongs at the root of the app's view hierarchy; use a document picker when presenting document selection from elsewhere.

#### macOS

##### Custom file management

People have strong associations with the familiar file browsing experience of the Finder and most document-based apps. Use the default file browser unless you have an important reason to create a custom one.

- **Make custom file-opening interfaces convenient** - People might appreciate an "open recent" action in addition to the simple "open" action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file's contents into the current document, you might change the title to Insert.

- **Provide a save interface** - Let people change a file's name, format, or location. By default, a new document's title is "Untitled" until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

- **Consider extending the Save dialog functionality** - If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

##### Finder Sync extensions

If your app syncs local and remote files, you can create a [Finder Sync](https://developer.apple.com/documentation/findersync) app extension to express synchronization status and controls within the Finder. Finder Sync customizes that interface; your app or file-provider implementation remains responsible for synchronization itself.

For example, you can use a Finder Sync extension to:

- Display badges in the Finder to indicate the sync status of items
- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- Provide custom toolbar buttons that perform global actions, like initiating a sync operation

##### Autosaving considerations

- **Respect save-confirmation preferences without losing work** - In [Desktop & Dock settings](https://support.apple.com/guide/mac-help/change-desktop-dock-settings-mchlp1119/26/mac/26), "Ask to keep changes when closing documents" controls whether people are asked about unsaved changes at close. Don't describe it as a universal switch that disables every form of autosaving. Use the document framework's save and close lifecycle to preserve work and request confirmation when needed.

- **Represent unsaved work accurately** - In workflows that require saving, the HIG recommends a dot on the close button and beside the document in the Window menu. Avoid stale indicators that imply already-preserved work still needs a save. Keep the document framework's edited state, title treatment, and save behavior consistent rather than manually leaving an "Edited" suffix after saving.

#### visionOS

No additional considerations.

### Related

- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- [Printing](https://developer.apple.com/design/human-interface-guidelines/printing)

### Developer documentation

- [Documents — SwiftUI](https://developer.apple.com/documentation/swiftui/documents)

### Videos

- [Build document-based apps in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10039)

## Changelog

These dates describe Apple's HIG article history.

### June 10, 2024
- Added guidelines for using the document launcher in iOS and iPadOS.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/file-management)*
