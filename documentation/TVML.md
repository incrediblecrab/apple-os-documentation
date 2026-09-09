# TVML

Use Apple TV Markup Language to create individual pages inside of a client-server app.

**Deprecated:** TVML is deprecated in tvOS 18 and later. Instead, develop apps for tvOS with SwiftUI or UIKit.

This is a legacy content reference, not a statement that TVML was removed in tvOS 18. See [TVMLKit](TVMLKit.md) for the native host and its individual API minima, and [the SwiftUI media-catalog sample](https://developer.apple.com/documentation/swiftui/creating-a-tvos-media-catalog-app-in-swiftui) for migration.

## Overview

In a traditional TVML client-server app, a document uses a template to define a page's allowed elements and layout. For example, `loadingTemplate` supplies a spinner and optional explanatory text, while `ratingTemplate` displays a rating. The full-page templates below provide predefined layouts; native hybrid apps can coordinate TVML documents through `TVDocumentViewController` rather than placing all navigation logic in JavaScript.

Compound elements group other elements; simple elements generally supply individual visual, textual, or media content. This distinction concerns the element's content model, not whether its XML occupies one line or several. Check each element's supported children.

Each template documents its default theme; some follow the system preference and others default to dark. The [`UIUserInterfaceStyle` property-list key](https://developer.apple.com/documentation/bundleresources/information-property-list/uiuserinterfacestyle), available on **tvOS 10+**, controls the app's appearance preference.

The native app launches the TVMLKit JavaScript environment. In the traditional model, that JavaScript loads documents and responds to user input; [TVMLKit JS](tvmljs.md) describes the APIs. TVML is not a general HTML/CSS browser renderer, so new Safari web-platform features do not automatically become TVML features.

## Topics

### Full-Page Templates
- [`alertTemplate`](https://developer.apple.com/documentation/tvml/alerttemplate) - Important information with actions.
- [`catalogTemplate`](https://developer.apple.com/documentation/tvml/catalogtemplate) - Categories beside images of the selected category's contents.
- [`compilationTemplate`](https://developer.apple.com/documentation/tvml/compilationtemplate) - A media item made up of components, such as an album and its tracks.
- [`descriptiveAlertTemplate`](https://developer.apple.com/documentation/tvml/descriptivealerttemplate) - Longer information, such as terms of service, with actions.
- [`divTemplate`](https://developer.apple.com/documentation/tvml/divtemplate) - A layout composed with TVML positioning styles when a predefined template does not fit.
- [`formTemplate`](https://developer.apple.com/documentation/tvml/formtemplate) - Text entry with a keyboard and action buttons.
- [`listTemplate`](https://developer.apple.com/documentation/tvml/listtemplate) - Items from a category beside related item information.
- [`loadingTemplate`](https://developer.apple.com/documentation/tvml/loadingtemplate) - A spinner with optional explanatory text.
- [`mainTemplate`](https://developer.apple.com/documentation/tvml/maintemplate) - Media actions over a background image.
- [`menuBarTemplate`](https://developer.apple.com/documentation/tvml/menubartemplate) - A top menu with related content below.
- [`oneupTemplate`](https://developer.apple.com/documentation/tvml/oneuptemplate) - Full-screen images with navigation between them.
- [`paradeTemplate`](https://developer.apple.com/documentation/tvml/paradetemplate) - Automatically scrolling images associated with the selected category.
- [`productBundleTemplate`](https://developer.apple.com/documentation/tvml/productbundletemplate) - Details and related items for a media bundle.
- [`productTemplate`](https://developer.apple.com/documentation/tvml/producttemplate) - Product details and related content.
- [`ratingTemplate`](https://developer.apple.com/documentation/tvml/ratingtemplate) - A title and rating display.
- [`searchTemplate`](https://developer.apple.com/documentation/tvml/searchtemplate) - Search input and a results area; application code handles the input and supplies results.
- [`showcaseTemplate`](https://developer.apple.com/documentation/tvml/showcasetemplate) - A browsable row of images with descriptions and focus emphasis.
- [`stackTemplate`](https://developer.apple.com/documentation/tvml/stacktemplate) - Vertically arranged groups of products.
- [Displaying a Product or Bundle in a Full-Page Template](https://developer.apple.com/documentation/tvml/displaying-a-product-or-bundle-in-a-full-page-template) - A tvOS 13+ sample for scrollable and fixed product-page regions.

### Compound Elements
Compound elements group supported child elements; XML line wrapping does not determine their type.

#### Background Elements
[Background Elements](https://developer.apple.com/documentation/tvml/background-elements) control background images and media.

#### Banner and Header Elements
[Banner and Header Elements](https://developer.apple.com/documentation/tvml/banner-and-header-elements) introduce content.

#### Information Elements
[Information Elements](https://developer.apple.com/documentation/tvml/information-elements) group descriptive content.

#### Layout Elements
[Layout Elements](https://developer.apple.com/documentation/tvml/layout-elements) arrange child elements.

#### Lockup Elements
[Lockup Elements](https://developer.apple.com/documentation/tvml/lockup-elements) combine content into a single item.

### Simple Elements
Simple elements provide individual pieces of content. Their permitted contents are defined by each element, not by a one-line syntax requirement.

#### Display Elements
[Display Elements](https://developer.apple.com/documentation/tvml/display-elements) include images, badges, and progress visuals.

#### Multimedia Elements
[Multimedia Elements](https://developer.apple.com/documentation/tvml/multimedia-elements) include audio and search-input elements; application code handles input-driven retrieval.

#### Text Elements
[Text Elements](https://developer.apple.com/documentation/tvml/text-elements) display text.

### Styles
Use the supported TVML style properties when an element's default presentation needs customization. Do not assume arbitrary browser CSS is supported.

#### Color Styles
[Color Styles](https://developer.apple.com/documentation/tvml/color-styles) customize colors.

#### Text Styles
[Text Styles](https://developer.apple.com/documentation/tvml/text-styles) control text presentation.

#### Element Shaping
[Element Shaping](https://developer.apple.com/documentation/tvml/element-shaping) controls size and shape.

#### Element Alignment and Spacing
[Element Alignment and Spacing](https://developer.apple.com/documentation/tvml/element-alignment-and-spacing) controls layout.

#### Style Properties
- [`tv-placeholder`](https://developer.apple.com/documentation/tvml/tv-placeholder) - A placeholder image for an `img` or `monogram`.
- [`tv-rating-style`](https://developer.apple.com/documentation/tvml/tv-rating-style) - The image used for a product rating.
- [`tv-transition`](https://developer.apple.com/documentation/tvml/tv-transition) - An element's transition effect.
- [`tv-text-highlight-style`](https://developer.apple.com/documentation/tvml/tv-text-highlight-style) - Label visibility and scrolling when focused.
- [`tv-scrollable-bounds-inset`](https://developer.apple.com/documentation/tvml/tv-scrollable-bounds-inset) - Unscrollable regions at a stack template's top and bottom; using them also changes the automatic content-offset adjustment for peeking.

### Attributes
Customize how TVML elements look and respond to user inputs by using attributes. Except where noted, attributes override the styles set for an element.

#### Image Attributes
[Image Attributes](https://developer.apple.com/documentation/tvml/image-attributes) specify image sources and fitting.

#### Text Attributes
[Text Attributes](https://developer.apple.com/documentation/tvml/text-attributes) control display, entry, and layout.

#### Focus Attributes
[Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) control focus-related behavior.

#### Binding and DOM Manipulation
[Binding and DOM Manipulation](https://developer.apple.com/documentation/tvml/binding-and-dom-manipulation) covers data bindings and document updates.

#### Inline Playback
[Inline Playback](https://developer.apple.com/documentation/tvml/inline-playback) attributes control when and how playback starts.

#### Alignment, Scrolling, and Coloring
[Alignment, Scrolling, and Coloring](https://developer.apple.com/documentation/tvml/alignment-scrolling-and-coloring) covers shelf alignment, scrolling behavior, and color themes.

### Queries
Use queries inside of a style element to define different values for the same style in a single class.

#### Media Queries
[Media Queries](https://developer.apple.com/documentation/tvml/media-queries) adapt layout and presentation to supported preferences.

#### Data Binding Queries
[Data Binding Queries](https://developer.apple.com/documentation/tvml/data-binding-queries) compare values used by data bindings.

### Resource Icons
These are the legacy TVML resource catalogs, not an up-to-date table of regional rating regulations.
- [Adding Resource Icons](https://developer.apple.com/documentation/tvml/adding-resource-icons) - Use built-in icons on buttons or as images.

#### Button Icons
[Button Icons](https://developer.apple.com/documentation/tvml/button-icons) indicate button actions.

#### Movie Rating Icons (United States)
[Movie Rating Icons (United States)](https://developer.apple.com/documentation/tvml/movie-rating-icons-united-states).

#### Television Rating Icons (United States)
[Television Rating Icons (United States)](https://developer.apple.com/documentation/tvml/television-rating-icons-united-states).

#### Rating Icons (New Zealand)
[Rating Icons (New Zealand)](https://developer.apple.com/documentation/tvml/rating-icons-new-zealand).

#### Rating Icons (United Kingdom)
[Rating Icons (United Kingdom)](https://developer.apple.com/documentation/tvml/rating-icons-united-kingdom).

#### Rating Icons (Brazil)
[Rating Icons (Brazil)](https://developer.apple.com/documentation/tvml/rating-icons-brazil).

#### Rotten Tomatoes Rating Icons
[Rotten Tomatoes Rating Icons](https://developer.apple.com/documentation/tvml/rotten-tomatoes-rating-icons).

#### Miscellaneous Icons
[Miscellaneous Icons](https://developer.apple.com/documentation/tvml/miscellaneous-icons).

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVML)*
