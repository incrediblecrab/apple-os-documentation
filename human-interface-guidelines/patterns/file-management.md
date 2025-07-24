# File management

Some apps can support documents and files that people expect to manage throughout the system.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

Document-based apps — such as Pages, Keynote, Photos, and Preview — help people create, edit, and save documents and files, often providing customized ways for people to browse for content they want to open in the app.

People also expect to browse documents without first opening a document-based app. On a Mac, for example, people use the Finder to access the macOS file system; on iPhone, iPad, and Apple Vision Pro, people use the Files app to manage the documents and files on their device. In watchOS and tvOS, people don't typically create, edit, or manage documents, so these systems don't provide a document-browsing interface.

## Topics

### Creating and opening files

- **Use app menus and keyboard shortcuts** - Give people convenient ways to create and open documents. In iPadOS and macOS, people expect to create new documents or open existing ones using familiar menu commands. When you provide commands like New or Open, iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard, and macOS presents them in the menu bar File menu. Regardless of the availability of keyboard shortcuts, include an Add (+) button to help people create a new document. In a macOS app, you put the add action in the File menu (for guidance, see File menu).

- **Support platform file system understanding** - If your app requires a custom file browser, support people's understanding of the platform's file system. People who are familiar with the Finder and Files apps already understand the basic layout of their device's file system. Although you might want to show the most relevant part of the file system when your custom file browser opens — for example, a Documents or iCloud folder or the most recently selected location — let people use your browser to view the rest of the file system if they want.

### Saving work

- **Preserve work automatically** - Help people be confident that their work is always preserved unless they cancel or delete it. In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they're editing and when they close a file or switch to another app.

- **Hide file extensions by default** - But let people view them if they choose. Be sure to reflect the current choice in all the save or open interfaces you display.

### Quick Look previews

Quick Look helps you create previews of the files your app handles so that people can view them within your app and in some cases interact with them. For example, you can use Quick Look to let people listen to a preview of an audio file, add markup to a photo's preview, or rotate and scale a 3D file preview to examine it in different ways.

- **Use Quick Look for unsupported files** - Use a Quick Look viewer to let people preview a file even when your app can't open it. If your app lets people attach or otherwise interact with files that it doesn't support, implementing a Quick Look viewer lets people preview those files without leaving your app.

- **Consider implementing a Quick Look generator** - If your app produces custom file types, a Quick Look generator lets other apps — including the Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.

### Platform considerations

Not supported in tvOS or watchOS.

**iOS, iPadOS**

**Document launcher**

Starting in iOS 18 and iPadOS 18, document-based apps can use the system's document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app's theme, while making it easy for people to create new documents. For developer guidance, see DocumentGroupLaunchScene.

The document launcher consists of three main parts:

- A title card that displays the app title and two app-specific buttons
- A background image that appears behind the title card and additional images — called accessories — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card's primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser's toolbar.

- **Assign the title card's buttons to your app's most important functions** - The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.

- **Provide a distinct background** - Create a background that's clearly distinct from the accessories and title card. You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

- **Be mindful of accessory placement** - You can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

- **Use animation sparingly** - Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app's content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see Motion.

**File provider app extension**

If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app's documents. For developer guidance, see File Provider. An app extension is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see App extensions.

- **Display only appropriate documents** - When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context. For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

- **Let people select a destination** - Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy when exporting and moving documents. You could also provide a way to add new subdirectories.

- **Avoid including a custom top toolbar** - Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see Adding a document browser to your app.

**macOS**

**Custom file management**

People have strong associations with the familiar file browsing experience of the Finder and most document-based apps. Use the default file browser unless you have an important reason to create a custom one.

- **Make custom file-opening interfaces convenient** - People might appreciate an "open recent" action in addition to the simple "open" action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file's contents into the current document, you might change the title to Insert.

- **Provide a save interface** - Let people change a file's name, format, or location. By default, a new document's title is "Untitled" until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

- **Consider extending the Save dialog functionality** - If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

**Finder Sync extensions**

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see Finder Sync.

For example, you can use a Finder Sync extension to:

- Display badges in the Finder to indicate the sync status of items
- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- Provide custom toolbar buttons that perform global actions, like initiating a sync operation

**Autosaving considerations**

- **Help people avoid losing work** - If they turn off autosaving, help people avoid losing work. People can turn off autosaving by selecting the "Ask to keep changes when closing documents" toggle in Desktop & Dock settings. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.

- **Show unsaved changes when autosaving is off** - Make sure people know when a document has unsaved changes. To show that there are unsaved changes, display a dot on the document window's close button and next to the document's name in your app's Window menu. When autosaving is on, showing a dot in these locations is confusing, because it implies that people need to take action to avoid losing their work. Regardless of autosave status, you can append "Edited" to the document's title in the title bar, but be sure to remove this suffix as soon as autosave occurs or when people explicitly save their work.

**visionOS**  
No additional considerations.

### Related

- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- [Printing](https://developer.apple.com/design/human-interface-guidelines/printing)

### Developer documentation

- [Documents — SwiftUI](https://developer.apple.com/documentation/swiftui/documents)

### Videos

- [Build document-based apps in SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10029)

## Changelog

### June 10, 2024
- Added guidelines for using the document launcher in iOS and iPadOS.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/file-management)*