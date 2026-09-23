# Sample Code Library

Apple's sample library is a collection of separate projects, not one SDK or package with a universal platform minimum. Use a project's own README, availability, and license before adopting its code.

## Overview

The September 8, 2026 catalog includes WWDC26 examples alongside maintained and historical samples. A conference grouping identifies a selection of projects; it does not prove that every API in those projects was introduced that year.

This repository includes the [Landmarks Liquid Glass sample](../os26-liquid-glass-example/README.md). It remains an OS 26-minimum iOS, iPadOS, and macOS app rather than a showcase target for every OS 27 framework.

## Topics

### Intelligence and system integration

- [Origami: Crafting a dynamic tutorial for Apple Intelligence](https://developer.apple.com/documentation/foundationmodels/origami-crafting-a-dynamic-tutorial-for-apple-intelligence) connects an interactive feature to Foundation Models.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](https://developer.apple.com/documentation/evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature) provides an evaluation-focused project rather than a substitute for all unit testing.
- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences) is a starting point for actions and entities.

### UI, spatial, and media

- [Manipulating models with RealityKit](https://developer.apple.com/documentation/realitykit/manipulating-models-with-realitykit) demonstrates spatial model interaction.
- [Building a handwriting recognition experience with PencilKit](https://developer.apple.com/documentation/pencilkit/building-a-handwriting-recognition-experience-with-pencilkit)
  covers a concrete handwriting workflow. Its project instructions require a physical device with Apple Pencil.
- [Building a cross-platform web browser](https://developer.apple.com/documentation/webkit/building-a-cross-platform-web-browser) connects native app structure to web content.
- [Creating visuals with Music Understanding analysis results](https://developer.apple.com/documentation/musicunderstanding/create-visuals-using-musicunderstanding-analysis-results) is a specialized media-analysis example.

### Data, commerce, and diagnostics

- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/coredata/adopting-swiftdata-for-a-core-data-app) illustrates a persistence transition.
- [Implementing a store using StoreKit](https://developer.apple.com/documentation/storekit/implementing-a-store-in-your-app-using-the-storekit-api) covers an in-app commerce integration.
- [Track performance by app state using MetricKit](https://developer.apple.com/documentation/metrickit/track-performance-by-app-state-using-metrickit) links diagnostics to application state. The sample requires a physical device for MetricKit report delivery.

## Using a sample responsibly

Check the selected Xcode, SDK, deployment target, destination, account capabilities, and data dependencies separately. Keep beta-specific behavior qualified and reproduce the relevant failure or permission-denied path before copying an integration.

Sample code is instructional: a successful build is not a production-readiness, security, accessibility, or licensing certification. Apple sample licenses can exclude photographs or other accompanying material. The local Landmarks [asset manifest](../metadata/assets.json) preserves those distinctions.

This is a curated entry point, not a duplicate of the full upstream project inventory.

*Source: [Apple Sample Code Library](https://developer.apple.com/documentation/samplecode)*
