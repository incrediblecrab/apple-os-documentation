# TVML

Use Apple TV Markup Language to create individual pages inside of a client-server app.

**Deprecated:** TVML is deprecated in tvOS 18 and later. Instead, develop apps for tvOS with SwiftUI or UIKit.

## Overview

Every page in a client-server app is built on an Apple TV Markup Language (TVML) template. TVML templates define what elements can be used and in what order. Each template is designed to display information in a specific way. For example, **loadingTemplate** shows a spinner and a quick description of what is happening, while **ratingTemplate** shows the rating for a product. You create a new TVML file that contains a single template for each page in a client-server app. Each template page occupies the entire TV screen.

Each template page uses compound and simple elements. Compound elements contain other elements, while simple elements are single lines of TVML. Elements contain the information and images that are displayed on the screen.

Every template has a default presentation theme associated with it. You can set a specific theme for your app setting **UIUserInterfaceStyle** in the info.plist file. Themes provide a consistent look inside of a template.

You control the flow of a client-server app through a JavaScript file that is called by your binary app. Your JavaScript file needs to be able to load TVML pages and respond to user input. For more information on available JavaScript APIs, see **TVMLKit JS**.

## Topics

### Full-Page Templates
- **alertTemplate** - Displays important information to the user.
- **catalogTemplate** - Displays groups of items along one side of a page and images of a group's contents on the other side.
- **compilationTemplate** - Displays information about a single media item and its components.
- **descriptiveAlertTemplate** - Displays large amounts of important information to the user.
- **divTemplate** - Provides the ability to create pages that don't conform to a layout defined by another template.
- **formTemplate** - Provides the ability to gather information from the user.
- **listTemplate** - Displays a list of items along one side of a page and the corresponding image on the other side.
- **loadingTemplate** - Displays a spinner and description on the screen.
- **mainTemplate** - Displays user options for a media item.
- **menuBarTemplate** - Creates a page with items along the top and related information below.
- **oneupTemplate** - Creates a page that allows users to navigate between full-screen images.
- **paradeTemplate** - Displays a groups of items along one side of a page and scrolling images on the other side.
- **productBundleTemplate** - Displays information for a group of related media items.
- **productTemplate** - Displays detailed information about a single product.
- **ratingTemplate** - Displays a rating for an item.
- **searchTemplate** - Searches for a media item based on user input.
- **showcaseTemplate** - Displays images the user can navigate between.
- **stackTemplate** - Displays groups of products.
- [Displaying a Product or Bundle in a Full-Page Template](https://developer.apple.com/documentation/tvml/displaying_a_product_or_bundle_in_a_full-page_template) - Specify scrollable and fixed regions in a product page.

### Compound Elements
Compound elements are multiple-line TVML elements that encapsulate other compound or simple TVML elements.

#### Background Elements
Control background images and media items that play in the background.

#### Banner and Header Elements
Provide initial descriptive information for other elements.

#### Information Elements
Group and display content in the form best suited for the information.

#### Layout Elements
Organize and display multiple elements in a structured layout.

#### Lockup Elements
Combine several elements so that they can be treated as a single element.

### Simple Elements
Simple elements often don't contain other elements and typically fit on one line.

#### Display Elements
Display a visual element, such as an image, badge, or progress overlay.

#### Multimedia Elements
Provide the user the ability to stream audio and search for information stored on a server.

#### Text Elements
Display text onscreen.

### Styles
Customize TVML elements using the TVML styles provided by Apple. Usage of these styles is optional, and you can create great client-server apps without ever changing the default look of an element.

#### Color Styles
Provide the ability to customize an element's color.

#### Text Styles
Change the text characteristics for an element.

#### Element Shaping
Modify the size and shape of an element.

#### Element Alignment and Spacing
Modify the alignment and spacing between elements.

#### Style Properties
- **tv-placeholder** - Sets a default image for an img or monogram element.
- **tv-rating-style** - Sets the displayed image for rating a product.
- **tv-transition** - Specifies how an element transitions on and off the screen.
- **tv-text-highlight-style** - Specifies how an element looks when it comes into focus.
- **tv-scrollable-bounds-inset** - Creates an unscrollable region of a specified size at the top and bottom of the stack template.

### Attributes
Customize how TVML elements look and respond to user inputs by using attributes. Except where noted, attributes override the styles set for an element.

#### Image Attributes
Retrieve images from a server and specify how they fit into an element.

#### Text Attributes
Modify how text is displayed, entered, and laid out.

#### Focus Attributes
Define how an element acts when it comes into focus.

#### Binding and DOM Manipulation
Implement binding and impove DOM manipulation options.

#### Inline Playback
Set when and how inline playback is initiated.

#### Alignment, Scrolling, and Coloring
Align elements within a shelf, set how your app reacts to scrolling, and set the overall color scheme for your app.

### Queries
Use queries inside of a style element to define different values for the same style in a single class.

#### Media Queries
Change the look and layout of a page based on the user's preferences.

#### Data Binding Queries
Compare a value from a JSON file to another value.

### Resource Icons
Access Apple-provided icons for buttons, media item ratings, and general usage.
- [Adding Resource Icons](https://developer.apple.com/documentation/tvml/adding_resource_icons) - Add Apple-provided icons to buttons and as independent images.

#### Button Icons
Icons that indicate the function of a button.

#### Movie Rating Icons (United States)
Icons that pertain to United States movie ratings.

#### Television Rating Icons (United States)
Icons that pertain to United States television ratings.

#### Rating Icons (New Zealand)
Icons that pertain to New Zealand movie ratings.

#### Rating Icons (United Kingdom)
Icons that pertain to United Kingdom movie ratings.

#### Rating Icons (Brazil)
Icons that pertain to Brazil movie ratings.

#### Rotten Tomatoes Rating Icons
Icons pertaining to the Rotten Tomatoes rating system.

#### Miscellaneous Icons
Miscellaneous icons that don't fall into a specific category.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVML)*