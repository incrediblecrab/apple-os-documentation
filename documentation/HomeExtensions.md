# HomeExtensions

Provide accessory settings, configuration views, and help content that the Home app shows for accessories you manufacture.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ on the framework's symbol pages; the `com.apple.developer.home` entitlement and the `EXAppExtensionAttributes` and `NSHomeExtensionManufacturer` keys list iOS and iPadOS 27.2+ only

**Status:** Reviewed November 1, 2026. Apple's framework page says Home Extensions is available at compile time only and that its functionality will come at a later date; Apple gives no date. The framework page itself lists no availability. The entitlement and keys are documented from the iOS & iPadOS 27.2 SDK, which ships with Xcode 27.2.

## Overview

An accessory manufacturer adds a Home extension to its app. The Home app then hosts the extension's content when a person sets up, controls, or configures that manufacturer's accessories: settings that the Home app displays, custom SwiftUI views for configuration, help guides, and troubleshooting content.

The extension's entry point is a type that adopts `HomeExtension` and is marked `@main`. Its `body` returns the framework's content types: `HomeAccessoryConfiguration`, `HomeAccessorySettings`, `HomeAccessoryHelpGuide`, and `HomeAccessoryTroubleshooting`. Apple says not to add your own `HomeContent` conformances.

While the extension runs, `HomeContext` is in the SwiftUI environment (`@Environment(\.homeContext)`). It carries the home and accessory the person selected, both optional and typed as [HomeKit](HomeKit.md) `HMHome` and `HMAccessory`, plus the navigator, a metadata dictionary, `dismiss()`, and `reportConfigurationComplete()`, which tells the Home app that the accessory's configuration is finished. `HomeNavigator.push(_:title:)` pushes a page onto the Home app's navigation stack.

## Project setup

Xcode's Home Extension target template (File > New > Target) sets up the target. To configure a project by hand:

- Add the Boolean `com.apple.developer.home` entitlement to the app extension.
- Add an `EXAppExtensionAttributes` dictionary to the extension's information property list, with `EXExtensionPointIdentifier` set to `com.apple.Home.HomeExtension`.
- Add `NSHomeExtensionManufacturer`, a string holding the accessory manufacturer's name. Apple's framework page says to add it to the app; the key's own reference says to include it in the Home app extension's information property list and marks it optional.

The Home entitlement doesn't stand in for accessory access. An extension that communicates with HomeKit or [Matter](Matter.md) accessories also needs the matching entitlements, such as `com.apple.developer.homekit` and `com.apple.developer.matter.allow-setup-payload`.

## Accessory settings

Settings that the Home app displays come from three types you write:

- A container adopting `HomeAccessorySettingsContainer` declares one property per setting, each with one of the setting property wrappers (toggle, range, enumeration, text field, or information), and lists the projected values in `availableSettings` in display order.
- A provider adopting `HomeAccessorySettingsProvider` reads the accessory into a new container in `settings(context:for:)` and applies a person's edits in `settingsDidChange(changes:context:for:)`. The provider keeps no setting values itself.
- A context adopting `HomeAccessorySettingsContext` holds what the provider needs to reach the accessory, such as a web service client or a Matter handle; the framework passes it on every call. A provider with no such needs uses an empty context type.

`HomeAccessorySettings` combines a provider, its context, and a filter closure that decides which accessories the settings apply to. Apple's provider guidance:

- The framework calls `settings(context:for:)` when the settings appear and again after every change, so keep it fast and build a new container each time instead of caching one.
- `settingsDidChange(changes:context:for:)` receives new values keyed by setting identifier: `Bool` for a toggle, `NSNumber` for a range, and `String` for an enumeration's raw value or a text field. Information settings are read-only and never appear there. Write only the settings you receive.
- Finish the device write before returning, because the framework reads the settings again immediately afterward.
- Return `nil` for any value you can't read reliably.
- Labels, `isEnabled`, and `isHidden` belong to each snapshot, so set them every time. Assigning a plain string label clears `detailedLabel`; assign both to keep it.
- Keep setting identifiers unique across all providers. The framework routes each change to the provider that owns the identifier.

## Configuration and support content

`HomeAccessoryConfiguration` pairs a `HomeContentID` with a SwiftUI view and an optional filter closure that decides which accessories the content applies to; `hidesNavigationTitleInLandscape(_:)` controls the Home app's title and app icon in landscape. `HomeAccessoryHelpGuide` takes the same identifier, view, and filter; `HomeAccessoryTroubleshooting` takes a view and a filter without an identifier. Both can add a button for contacting the manufacturer with `contactAccessoryManufacturerLink()`.

## Topics

### Essentials
- [HomeExtension](https://developer.apple.com/documentation/homeextensions/homeextension) - The extension's `@main` entry point; its `body` supplies the content.
- [HomeContext](https://developer.apple.com/documentation/homeextensions/homecontext) - The selected home and accessory, navigation, metadata, dismissal, and configuration completion.
- [HomeNavigator](https://developer.apple.com/documentation/homeextensions/homenavigator) - Pushes pages onto the Home app's navigation stack.

### Displaying accessory configuration
- [HomeAccessorySettingsProvider](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider) - Reads an accessory's settings into a snapshot and writes a person's changes back.
- [HomeAccessorySettingsContainer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingscontainer) - A snapshot type with one property per setting.
- [AnyHomeAccessorySettingsContainer](https://developer.apple.com/documentation/homeextensions/anyhomeaccessorysettingscontainer) - A type-erasing wrapper for a settings container; Apple's page has no abstract.
- [HomeAccessorySettingsContext](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingscontext) - Resources the provider uses to communicate with the accessory.
- [HomeAccessorySettings](https://developer.apple.com/documentation/homeextensions/homeaccessorysettings) - Settings content backed by a provider and context.
- [HomeAccessoryConfiguration](https://developer.apple.com/documentation/homeextensions/homeaccessoryconfiguration) - A custom SwiftUI configuration view.

### Defining accessory settings
- [HomeAccessorySetting](https://developer.apple.com/documentation/homeextensions/homeaccessorysetting) - The protocol behind every setting; use the property wrappers instead of adopting it.
- [HomeAccessorySettingLabel](https://developer.apple.com/documentation/homeextensions/homeaccessorysettinglabel) - Display text for a setting or option.
- [HomeAccessoryEnumSetting](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsetting) - A choice among several options.
- [HomeAccessoryEnumSettingConstant](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsettingconstant) - A type whose cases are an enumeration setting's options.
- [HomeAccessoryInformationSetting](https://developer.apple.com/documentation/homeextensions/homeaccessoryinformationsetting) - A read-only label and value.
- [HomeAccessoryRangeSetting](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting) - A numeric value within a range.
- [HomeAccessoryRangeSettingDescriptor](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesettingdescriptor) - The bounds of a range setting.
- [HomeAccessoryTextFieldSetting](https://developer.apple.com/documentation/homeextensions/homeaccessorytextfieldsetting) - One line of editable text.
- [HomeAccessoryToggleSetting](https://developer.apple.com/documentation/homeextensions/homeaccessorytogglesetting) - An on/off choice.

### Guides and troubleshooting content
- [HomeContent](https://developer.apple.com/documentation/homeextensions/homecontent) - The content protocol; use the framework's conforming types.
- [HomeContentID](https://developer.apple.com/documentation/homeextensions/homecontentid) - Identifies a piece of extension content.
- [HomeAccessoryHelpGuide](https://developer.apple.com/documentation/homeextensions/homeaccessoryhelpguide) - Help on one topic for an accessory.
- [HomeAccessoryTroubleshooting](https://developer.apple.com/documentation/homeextensions/homeaccessorytroubleshooting) - Content that helps people fix accessory problems.
- [GuideStepHostViewController](https://developer.apple.com/documentation/homeextensions/guidestephostviewcontroller) - A `UIViewController` subclass; Apple's page gives no abstract or availability.

### Configuration keys
- [com.apple.developer.home](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.home) - Boolean entitlement for a Home app extension; iOS and iPadOS 27.2+.
- [EXAppExtensionAttributes](https://developer.apple.com/documentation/bundleresources/information-property-list/exappextensionattributes) - Extension attributes dictionary that requires `EXExtensionPointIdentifier`; iOS and iPadOS 27.2+.
- [NSHomeExtensionManufacturer](https://developer.apple.com/documentation/bundleresources/information-property-list/nshomeextensionmanufacturer) - Optional manufacturer-name string; iOS and iPadOS 27.2+.

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/homeextensions)
- [Compile-time-only notice and target setup](https://developer.apple.com/documentation/homeextensions.md)
- [Settings provider guidance](https://developer.apple.com/documentation/homeextensions/homeaccessorysettingsprovider)
- [Home entitlement and related accessory entitlements](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.home)
- [NSHomeExtensionManufacturer key](https://developer.apple.com/documentation/bundleresources/information-property-list/nshomeextensionmanufacturer)
- [iOS & iPadOS 27.2 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)
