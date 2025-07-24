# Maps

A map displays outdoor or indoor geographical data in your app or on your website.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation. A map can also include annotations and overlays and show routing information, and you can configure it to use a standard graphical view, a satellite image-based view, or a view that's a hybrid of both.

## Topics

### Best Practices

- **Make your map interactive** - People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements that obscure the map can interfere with people's expectations for how maps behave.

- **Pick a map emphasis style that suits the needs of your app** - The default style presents a version of the map with fully saturated colors, and is a good option for most standard map applications. The muted style presents a desaturated version of the map and is great if you have a lot of information-rich content that you want to stand out against the map.

- **Help people find places in your map** - Consider offering a search feature combined with a way to filter locations by category.

- **Clearly identify elements that people select** - When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.

- **Cluster overlapping points of interest to improve map legibility** - A cluster uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.

- **Help people see the Apple logo and legal link** - It's fine when parts of your interface temporarily cover the logo and link, but don't cover these elements all the time. Use adequate padding to separate the logo and link from the map boundaries and your custom controls.

### Custom Information

- **Use annotations that match the visual style of your app** - Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app.

- **Consider making standard map features independently selectable** - When you support selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add.

- **Use overlays to define map areas with a specific relationship to your content** - Above roads places the overlay above roads but below buildings and trees. Above labels places the overlay above both roads and labels, hiding everything beneath it.

- **Make sure there's enough contrast between custom controls and the map** - Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its contrast with the controls atop it.

### Place Cards

Place cards display rich place information in your app or website, such as operating hours, phone numbers, addresses, and more.

- **Consider your map presentation when choosing a style** - The full callout style place card offers people the richest experience, but choose a place card style that fits in the context of your map.

- **Make sure your place card looks great on different devices and window sizes** - If you choose to specify a style, ensure that the content in your place card remains viewable on different devices and as window sizes change.

- **Avoid duplicating information** - Consider what information you already display in your app or website when you choose a place card style.

- **Keep the location on your map visible when displaying a place card** - This helps people maintain a sense of where the location is on your map while getting detailed place information.

- **Use location-related cues in surrounding content** - Help communicate that people can open a place card by displaying place names and addresses alongside a button for more details.

### Indoor Maps

Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest.

- **Adjust map detail based on the zoom level** - Show large areas like rooms and buildings at all zoom levels, then progressively add more detailed features and labels as the map is zoomed in.

- **Use distinctive styling to differentiate the features of your map** - Using color along with icons can help distinguish different types of areas, stores, and services.

- **Offer a floor picker if your venue includes multiple levels** - A floor picker lets people quickly jump between floors. Keep floor numbers concise for simplicity.

- **Include surrounding areas to provide context** - Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map.

- **Consider supporting navigation between your venue and nearby transit points** - Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, and garages.

- **Limit scrolling outside of your venue** - This can help people avoid getting lost when they swipe too hard on your map.

- **Design an indoor map that feels like a natural extension of your app** - Don't try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app.

### Platform Considerations

**watchOS**  
- On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime.
- The displayed region isn't interactive; tapping it opens the Maps app on Apple Watch.
- You can add up to five annotations to a map to highlight points of interest or other relevant information.
- Fit the map interface element to the screen and show the smallest region that encompasses the points of interest.

### Developer Documentation

- [MapKit](https://developer.apple.com/documentation/mapkit) - MapKit
- [MapKit JS](https://developer.apple.com/documentation/mapkitjs) - MapKit JS
- [Indoor Mapping Data Format](https://developer.apple.com/documentation/mapkit/indoor_mapping_data_format) - Indoor mapping

## Changelog

### December 18, 2024
- Added guidance for place cards and included additional artwork.

### September 12, 2023
- Added artwork.

### September 23, 2022
- Added guidelines for presenting custom information, refined best practices, and consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/maps)*