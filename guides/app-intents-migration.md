# Migrate a custom SiriKit shortcut without breaking existing users

Move one custom intent to App Intents, preserve its identity and data, and verify both legacy shortcuts and new system integrations.

## Prerequisites and availability

- Inventory the custom intent class name, parameters, entity identifiers, donations, saved shortcuts, extension targets, and underlying action implementation.
- Establish a passing legacy flow before changing it. [SiriKit](../documentation/SiriKit.md) still provides legacy support for most existing Siri interactions, Shortcuts actions, and widget configuration. Apple recommends App Intents for modern integration; it has not made a blanket framework-removal announcement.
- [App Intents](../documentation/AppIntents.md) begins at iOS/iPadOS 16, Mac Catalyst 16, macOS 13, tvOS 16, watchOS 9, and visionOS 1. Keep legacy paths for earlier deployment targets.
- This custom-intent recipe uses [`CustomIntentMigratedAppIntent`](https://developer.apple.com/documentation/appintents/customintentmigratedappintent.md), available at iOS/iPadOS/Mac Catalyst/tvOS 16, macOS 13, watchOS 9, and visionOS 1.0. Versioned DocC metadata confirms Catalyst 16; the visionOS 1.0 API availability was checked with the installed XRSimulator 26.5 SDK.
- [App Intents Testing](../documentation/AppIntentsTesting.md) requires OS 27 APIs and an **XCTest UI testing bundle**. Use Xcode 27 (`27A266a`) on an Apple silicon Mac running macOS Tahoe 26.6 or later for this workflow.

## 1. Share the action implementation

Keep the business operation in code shared by the app and relevant extension targets. Both the old handler and the new intent should call this implementation rather than duplicating validation and side effects.

Write deterministic tests for the operation's authorization, persistence, errors, and repeat execution. A Siri entry point must not bypass checks that the in-app action requires.

## 2. Convert and preserve identity

For a custom `.intentdefinition`, use Xcode's **Convert to AppIntents** workflow described in [Soup Chef's migration sample](https://developer.apple.com/documentation/sirikit/soup-chef-with-app-intents-migrating-custom-intents.md). Review generated types rather than assuming conversion completes the migration.

Adopt `CustomIntentMigratedAppIntent` and preserve [`intentClassName`](https://developer.apple.com/documentation/appintents/customintentmigratedappintent/intentclassname.md), the original SiriKit intent class name. This mapping lets existing shortcuts and donations continue to resolve to the replacement.

This protocol is for **custom** SiriKit intents. System-defined SiriKit domains are not all interchangeable with a converted custom intent. For audio search and playback, consult [Media Intents](../documentation/MediaIntents.md) and its domain-specific adoption workflow.

## 3. Resolve parameters and implement the action

- Define data as `AppEntity` values with stable identifiers, display representations, and queries; use `AppEnum` for bounded choices.
- Resolve identifiers to current, authorized records. Return an empty result for a genuinely missing record rather than fabricating an entity.
- Implement [`AppIntent.perform()`](https://developer.apple.com/documentation/appintents/appintent/perform().md) to validate the resolved inputs, perform confirmation where needed, invoke the shared operation, and return the documented result.
- Choose the intent's [`authenticationPolicy`](https://developer.apple.com/documentation/appintents/appintent/authenticationpolicy.md) explicitly when authentication is required. Its default is `alwaysAllowed`, including on a locked device; retain application-level authorization checks.
- Configure `AppShortcutsProvider` and localized metadata for useful discoverability. Test existing saved shortcuts, not only newly created ones.

Errors, cancellation, denied authorization, or a lost network connection must not return a success result. Prevent duplicated side effects if an operation is retried; only report completion after the underlying action has completed.

## 4. Add discoverability and context deliberately

Follow the canonical [App Intents integration steps](../documentation/AppIntents.md#os-27-integration):

1. Apply the matching app schema where one exists.
2. Index relevant entities through [Core Spotlight](../documentation/CoreSpotlight.md). Schema adoption alone does not populate the index.
3. Provide transferable representations where another app needs the content.
4. Associate visible content with the correct entity and keep selection/bounds current.

For custom SwiftUI drawing, [`appEntityUIElements(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityuielements(_:).md) supplies `AppEntityUIElement` values. This is **not new in OS 27**: its documented minimums are iOS/iPadOS/Mac Catalyst/tvOS 18.4, macOS 15.4, watchOS 11.4, and visionOS 2.4. Standard views can use [`appEntityIdentifier(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(_:).md) at the same minimums. Guard both appropriately; the framework's earlier baseline does not cover these modifiers.

API availability does not guarantee that every Siri feature is enabled for a person's device, language, or region. Preserve direct in-app navigation and action controls.

## 5. Verify through the real intent infrastructure

In a UI testing target signed with the app's team:

1. Launch the app with `XCUIApplication` and establish deterministic test data.
2. Create `IntentDefinitions(bundleIdentifier:)`.
3. Look up the registered name through **`definitions.intents`**, construct parameters with `makeIntent`, call `run()`, and inspect the `ResolvedIntentResult`.
4. Test entity lookup by identifier and name, then pass an output entity into a second intent.
5. Query `spotlightQuery(_:)` after indexing, changes, and deletion on its supported iOS/iPadOS/Mac Catalyst/macOS/visionOS 27 destinations; this method does not list tvOS or watchOS.
6. Navigate to the relevant screen and inspect `viewAnnotations()`, including `entity` and `isSelected`.
7. Verify failures: stale identifiers, ambiguous input, denied access, offline services, cancellation, and missing definitions.

The [App Intents Testing reference](../documentation/AppIntentsTesting.md) links the exact APIs and records a singular/plural typo in one article example. Use the symbol reference's plural `intents` member.

Keep setup-only intents out of release builds with a debug compilation condition. Hiding an intent with `isDiscoverable = false` is not access control.

## 6. Roll out without deleting the fallback prematurely

Run the saved-shortcut migration on an upgraded installation, compare it with a fresh install, and test the oldest supported OS. Use [XCTest](../documentation/XCTest.md)/[XCUIAutomation](../documentation/XCUIAutomation.md) for visible app behavior in addition to intent tests. Native visionOS UI automation has a documented limitation; do not count an unrun destination as passing.

Remove a legacy path only after its supported users and shortcuts have a verified replacement—not because of an invented SiriKit removal deadline.

## Sources

- [SiriKit's current legacy-support statement](https://developer.apple.com/documentation/sirikit.md)
- [App Intents](https://developer.apple.com/documentation/appintents.md)
- [Custom intent migration sample](https://developer.apple.com/documentation/sirikit/soup-chef-with-app-intents-migrating-custom-intents.md)
- [CustomIntentMigratedAppIntent](https://developer.apple.com/documentation/appintents/customintentmigratedappintent.md)
- [Providing contextual cues](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri.md)
- [Testing your App Intents code](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code.md)
