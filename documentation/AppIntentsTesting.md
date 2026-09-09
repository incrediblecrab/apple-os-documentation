# App Intents Testing

Test registered intents, entities, queries, and their integration with system services.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

## Overview

App Intents Testing exercises [App Intents](AppIntents.md) **out-of-process**, through the infrastructure used by Siri and Shortcuts. Tests look up registered definitions by name instead of importing the app's Swift types. This catches problems that a direct call to an intent's `perform()` method can miss, including discovery, parameter transfer, and query resolution.

Use an **XCTest UI testing bundle**, not a unit test target. The app must be running, and the test target must use the app's code-signing team. An OS availability declaration is not a guarantee of UI-testing support on every destination; [XCUIAutomation](XCUIAutomation.md) still documents a limitation for apps built with the native visionOS SDK.

## Topics

### Set up and execute

- [Testing your App Intents code](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code.md) — Create a UI testing target, launch the app with `XCUIApplication`, and configure a known test state.
- [`IntentDefinitions`](https://developer.apple.com/documentation/appintentstesting/intentdefinitions.md) — Initialize with the app's bundle identifier; look up `intents`, `entities`, `enums`, and queries.
- [`AnyAppIntent.run()`](https://developer.apple.com/documentation/appintentstesting/anyappintent/run().md) — Execute a type-erased intent inside the app.
- [`ResolvedIntentResult`](https://developer.apple.com/documentation/appintentstesting/resolvedintentresult.md) — Inspect returned values and their dynamically resolved properties; resolution can throw.

### Queries and data transfer

- [`AnyAppEntity`](https://developer.apple.com/documentation/appintentstesting/anyappentity.md) and [`AnyEntityQuery`](https://developer.apple.com/documentation/appintentstesting/anyentityquery.md) — Work with entity references without linking app types.
- [`AppEntityDefinition.entities(matching:)`](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/entities(matching:).md) — Check name-based resolution, including empty and ambiguous results.
- [`AppEntityDefinition.makeReference(identifier:)`](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/makereference(identifier:).md) — Supply a known entity identifier to another intent.
- [`ResolvedValueQueryResult`](https://developer.apple.com/documentation/appintentstesting/resolvedvaluequeryresult.md) — Inspect intent-value-query output.
- [Transferable testing](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code.md) — Exercise entity export and reimport, then chain an output entity into another intent.

### Spotlight and onscreen context

- [`AppEntityDefinition.spotlightQuery(_:)`](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/spotlightquery(_:).md) — Verify indexed entities; a `nil` query requests all indexed entities of that type. This member declares iOS, iPadOS, Mac Catalyst, macOS, and visionOS 27.0+, not tvOS or watchOS.
- [`AppEntityDefinition.viewAnnotations()`](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/viewannotations().md) — Inspect annotations after navigating to the relevant screen.
- [`ViewAnnotation`](https://developer.apple.com/documentation/appintentstesting/viewannotation.md) — Check the returned entity and `isSelected` state.

## Validation and beta limitations

Seed deterministic data, test success and failure, then reset it between cases. Cover stale identifiers, missing entities, denied authorization, offline services, and renamed intent definitions. Keep setup-only intents behind a debug compilation condition; `isDiscoverable = false` alone is not access control.

The beta adoption article uses singular `intent` in one example, while the symbol reference documents **`IntentDefinitions.intents`**. The `makeReference(identifier:)` page also has an example that incorrectly says `reference(identifier:)`; follow the declaration and the adoption article's `makeReference` spelling. Compile tests with the selected SDK. Framework tests verify the integration code path, not every possible Siri utterance or deployment-region configuration.

See the [App Intents migration recipe](../guides/app-intents-migration.md), [XCTest](XCTest.md), [Core Spotlight](CoreSpotlight.md), and [Evaluations](Evaluations.md) for adjacent validation.

*Sources: [App Intents Testing](https://developer.apple.com/documentation/appintentstesting.md), [testing workflow](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code.md).*
