# Swift Charts

Construct and customize charts on every Apple platform.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

Swift Charts combines SwiftUI views with marks, scales, axes, and legends. Use these building blocks to represent data as bars, lines, points, and other visual encodings.

Charts infer scales and axes from their data by default. Override those defaults when your visualization needs a specific domain, labeling scheme, or presentation.

Swift Charts supports localization and accessibility features. You can also override default behavior to customize your charts by using chart modifiers. For example, you can create a dynamic experience by adding animations to your charts.

Charts are content, not navigation chrome. Follow the [material HIG](https://developer.apple.com/design/human-interface-guidelines/materials) rather than adding Liquid Glass behind every plot. Distinguish series with labels, symbols, or line styles as well as color, and preserve legibility with accessibility settings. For custom visualizations, [audio graphs](https://developer.apple.com/documentation/accessibility/audio-graphs) describe the data to VoiceOver. These are design and accessibility responsibilities, not new OS 27 rendering guarantees.

### API generations

- Core 2D charts and the original marks use the framework minimum in the header.
- `SectorMark`, `ChartAxisContent`, `AnnotationOverflowResolution`, and the scrolling types require iOS/iPadOS/Mac Catalyst/tvOS 17, macOS 14, watchOS 10, or visionOS 1.
- The vectorized plots and `VectorizedChartContent` require iOS/iPadOS/Mac Catalyst/tvOS 18, macOS 15, watchOS 11, or visionOS 2.
- `Chart3D`, its content protocol/builder, and `SurfacePlot` require iOS/iPadOS/Mac Catalyst/macOS/visionOS 26. They have no tvOS or watchOS declaration. A mark's older 2D availability doesn't make its 3D initializers available on those older systems.

The updates page dates vectorized plots to June 2024 and 3D charts to June 2025; neither is an OS 27-only addition.

## Topics

### Essentials
- [Swift Charts updates](https://developer.apple.com/documentation/updates/swiftcharts) - Learn about important changes to Swift Charts.

### Charts
- [Creating a chart using Swift Charts](https://developer.apple.com/documentation/charts/creating-a-chart-using-swift-charts) - Combine chart building blocks in SwiftUI.
- [Visualizing your app's data](https://developer.apple.com/documentation/charts/visualizing-your-app-s-data) - Build interactive charts in Apple's sample.
- [`Chart`](https://developer.apple.com/documentation/charts/chart) - The 2D chart view.
- [`ChartContent`](https://developer.apple.com/documentation/charts/chartcontent) - The protocol for content inside a chart.
- [`ChartContentBuilder`](https://developer.apple.com/documentation/charts/chartcontentbuilder) - Composes chart content.
- [`Plot`](https://developer.apple.com/documentation/charts/plot) - Groups chart content into an entity.

### 3D charts
- [`Chart3D`](https://developer.apple.com/documentation/charts/chart3d) - An interactive 3D chart using compatible marks.
- [`Chart3DContent`](https://developer.apple.com/documentation/charts/chart3dcontent) - The protocol for 3D chart content.
- [`Chart3DContentBuilder`](https://developer.apple.com/documentation/charts/chart3dcontentbuilder) - Composes 3D content.
- [`SurfacePlot`](https://developer.apple.com/documentation/charts/surfaceplot) - Samples a function of two variables, `y = f(x, z)`, to produce a surface; it isn't an arbitrary 3D data-collection container.

### Marks
- [`AreaMark`](https://developer.apple.com/documentation/charts/areamark) - Encodes values as regions.
- [`LineMark`](https://developer.apple.com/documentation/charts/linemark) - Connects values with line segments.
- [`PointMark`](https://developer.apple.com/documentation/charts/pointmark) - Encodes values as points.
- [`RectangleMark`](https://developer.apple.com/documentation/charts/rectanglemark) - Encodes ranges as rectangles.
- [`RuleMark`](https://developer.apple.com/documentation/charts/rulemark) - Draws a reference rule.
- [`BarMark`](https://developer.apple.com/documentation/charts/barmark) - Encodes values as bars.
- [`SectorMark`](https://developer.apple.com/documentation/charts/sectormark) - Represents a category's contribution to a total in a pie or donut chart.

### Vectorized plots
- [Creating a data visualization dashboard with Swift Charts](https://developer.apple.com/documentation/charts/creating-a-data-visualization-dashboard-with-swift-charts) - Supply a collection to a vectorized plot instead of constructing each mark separately.
- [`AreaPlot`](https://developer.apple.com/documentation/charts/areaplot) - Plots a collection or function as filled regions.
- [`LinePlot`](https://developer.apple.com/documentation/charts/lineplot) - Plots a collection or function as connected segments.
- [`PointPlot`](https://developer.apple.com/documentation/charts/pointplot) - Vectorized points.
- [`RectanglePlot`](https://developer.apple.com/documentation/charts/rectangleplot) - Vectorized rectangles.
- [`RulePlot`](https://developer.apple.com/documentation/charts/ruleplot) - Vectorized reference rules.
- [`BarPlot`](https://developer.apple.com/documentation/charts/barplot) - Vectorized bars.
- [`SectorPlot`](https://developer.apple.com/documentation/charts/sectorplot) - Vectorized pie or donut sectors.
- [`VectorizedChartContent`](https://developer.apple.com/documentation/charts/vectorizedchartcontent) - A protocol whose primary associated type describes a data element.

### Mark configuration
- [`MarkStackingMethod`](https://developer.apple.com/documentation/charts/markstackingmethod) - Selects how marks stack.
- [`MarkDimension`](https://developer.apple.com/documentation/charts/markdimension) - Describes a mark's width or height.
- [`InterpolationMethod`](https://developer.apple.com/documentation/charts/interpolationmethod) - Selects line or area interpolation.
- [`BasicChartSymbolShape`](https://developer.apple.com/documentation/charts/basicchartsymbolshape) - A built-in plotting shape.
- [`ChartSymbolShape`](https://developer.apple.com/documentation/charts/chartsymbolshape) - The plotting-symbol shape protocol.
- [`AnyChartSymbolShape`](https://developer.apple.com/documentation/charts/anychartsymbolshape) - Type-erases a plotting shape.

### Labeled data
- [`PlottableValue`](https://developer.apple.com/documentation/charts/plottablevalue) - Associates a label with plottable data.
- [`Plottable`](https://developer.apple.com/documentation/charts/plottable) - The protocol for values used by chart encodings.

### Scales
- [`ScaleRange`](https://developer.apple.com/documentation/charts/scalerange) - Configures a scale's output range.
- [`PositionScaleRange`](https://developer.apple.com/documentation/charts/positionscalerange) - Configures a positional range.
- [`PlotDimensionScaleRange`](https://developer.apple.com/documentation/charts/plotdimensionscalerange) - Represents the plot area's width or height.
- [`ScaleDomain`](https://developer.apple.com/documentation/charts/scaledomain) - Configures the input domain.
- [`AutomaticScaleDomain`](https://developer.apple.com/documentation/charts/automaticscaledomain) - Infers a domain from the data.
- [`ScaleType`](https://developer.apple.com/documentation/charts/scaletype) - Selects the scale transformation.

### Axes
- [Customizing axes in Swift Charts](https://developer.apple.com/documentation/charts/customizing-axes-in-swift-charts) - Configure axis appearance and labeling.
- [`ChartAxisContent`](https://developer.apple.com/documentation/charts/chartaxiscontent) - An axis represented as view content.
- [`AxisContent`](https://developer.apple.com/documentation/charts/axiscontent) - The axis-content protocol.
- [`AxisMarks`](https://developer.apple.com/documentation/charts/axismarks) - Groups the visual marks of an axis.
- [`AnyAxisContent`](https://developer.apple.com/documentation/charts/anyaxiscontent) - Type-erases axis content.
- [`AxisContentBuilder`](https://developer.apple.com/documentation/charts/axiscontentbuilder) - Composes axis content.

### Axis marks
- [`AxisMark`](https://developer.apple.com/documentation/charts/axismark) - The axis-mark protocol.
- [`AxisTick`](https://developer.apple.com/documentation/charts/axistick) - Marks a reference value along an axis.
- [`AxisGridLine`](https://developer.apple.com/documentation/charts/axisgridline) - Extends an axis reference through the plot area.
- [`AxisValueLabel`](https://developer.apple.com/documentation/charts/axisvaluelabel) - Labels an axis value.
- [`AxisValue`](https://developer.apple.com/documentation/charts/axisvalue) - Describes the value associated with an axis mark.
- [`AnyAxisMark`](https://developer.apple.com/documentation/charts/anyaxismark) - Type-erases an axis mark.
- [`AxisMarkBuilder`](https://developer.apple.com/documentation/charts/axismarkbuilder) - Composes axis marks.

### Annotations
- [`AnnotationContext`](https://developer.apple.com/documentation/charts/annotationcontext) - Supplies information about the annotated item.
- [`AnnotationPosition`](https://developer.apple.com/documentation/charts/annotationposition) - Selects an annotation's position.
- [`AnnotationOverflowResolution`](https://developer.apple.com/documentation/charts/annotationoverflowresolution)

### Data bins
- [`NumberBins`](https://developer.apple.com/documentation/charts/numberbins) - Groups numeric data into bins.
- [`DateBins`](https://developer.apple.com/documentation/charts/datebins) - Groups dates into bins.
- [`ChartBinRange`](https://developer.apple.com/documentation/charts/chartbinrange) - Represents one bin's range.

### Chart management
- [`ChartPlotContent`](https://developer.apple.com/documentation/charts/chartplotcontent) - Represents the plot area as view content.
- [`ChartProxy`](https://developer.apple.com/documentation/charts/chartproxy) - Accesses scales and plot geometry, including data/coordinate conversion.

### Scrolling
- [`ChartScrollTargetBehavior`](https://developer.apple.com/documentation/charts/chartscrolltargetbehavior) - Customizes chart scroll targets.
- [`ChartScrollTargetBehaviorContext`](https://developer.apple.com/documentation/charts/chartscrolltargetbehaviorcontext) - Supplies context for adjusting a scroll target.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Charts)*
