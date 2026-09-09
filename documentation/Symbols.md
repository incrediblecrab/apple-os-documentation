# Symbols

Animate symbol-based images with shared effect types.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

The Symbols framework provides effects for [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) in AppKit, UIKit, and SwiftUI. An effect's supported behaviors determine how to apply it:

- **Discrete** - An effect that runs from start to finish
- **Indefinite** - An effect that lasts until you remove or disable it
- **Transition** - An effect that animates a symbol in or out of visibility
- **Content Transition** - An effect that replaces one symbol with another symbol, or with a different configuration of itself

A type can support more than one behavior. In SwiftUI, use the [`value:` overload](https://developer.apple.com/documentation/swiftui/view/symboleffect(_:options:value:)) to trigger a discrete effect when an `Equatable` value changes. Use [`isActive:`](https://developer.apple.com/documentation/swiftui/view/symboleffect(_:options:isactive:)) to control an indefinite effect. Specifying a repeat count alone doesn't select the discrete overload.

```swift
import SwiftUI
import Symbols

struct PulseExample: View {
    @State private var pulseTrigger = 0
    @State private var isPulsing = true

    var body: some View {
        VStack {
            Button("Pulse") {
                pulseTrigger += 1
            }
            Image(systemName: "globe")
                .symbolEffect(.pulse, value: pulseTrigger)

            Toggle("Keep pulsing", isOn: $isPulsing)
            Image(systemName: "globe")
                .symbolEffect(.pulse, isActive: isPulsing)
        }
    }
}
```

Not every symbol has the same animation data. Variable-color effects require variable-color layers, and draw effects animate portions carrying draw data. These effects aren't general animations for arbitrary bitmap images.

This view visualizes an app-supplied activity flag; it doesn't discover or connect to Wi-Fi networks:

```swift
import SwiftUI
import Symbols

struct SearchIndicator: View {
    var isSearching: Bool

    var body: some View {
        Image(systemName: "wifi")
            .symbolEffect(.variableColor.reversing, isActive: isSearching)
    }
}
```

In a main-actor AppKit or UIKit context, `imageView` below is an `NSImageView` or `UIImageView` containing a symbol image. Native discrete effects start when added, unlike SwiftUI's value-triggered overload:

```swift
imageView.addSymbolEffect(.variableColor.reversing)
```

### Later effects and repetition options

`BreatheSymbolEffect`, `RotateSymbolEffect`, and `WiggleSymbolEffect` require iOS/iPadOS/Mac Catalyst/tvOS 18, macOS 15, visionOS 2, or watchOS 11. `DrawOnSymbolEffect` and `DrawOffSymbolEffect` require the 26 generation on all seven platforms; they aren't OS 27-only.

The integer-count [`SymbolEffectOptions.repeat(_:)`](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeat(_:)-33816) is deprecated in the 27 generation. The [`RepeatBehavior` overload](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeat(_:)-3klm2) is the newer form, available from the 18/macOS 15/visionOS 2/watchOS 11 generation. Keep availability checks for apps supporting the framework's original minimum. Repetition options express a preferred behavior, not a guarantee that every animation is rendered.

## Topics

### Symbol Effects
- [`appear`](https://developer.apple.com/documentation/symbols/symboleffect/appear) - Makes symbol layers appear individually or together.
- [`bounce`](https://developer.apple.com/documentation/symbols/symboleffect/bounce) - Applies a transient scaling animation.
- [`disappear`](https://developer.apple.com/documentation/symbols/symboleffect/disappear) - Makes layers disappear individually or together.
- [`pulse`](https://developer.apple.com/documentation/symbols/symboleffect/pulse) - Varies the opacity of participating layers.
- [`scale`](https://developer.apple.com/documentation/symbols/symboleffect/scale) - Scales layers individually or together.
- [`variableColor`](https://developer.apple.com/documentation/symbols/symboleffect/variablecolor) - Animates the opacity of variable-color layers.

### Symbol Content Transitions
- [`replace`](https://developer.apple.com/documentation/symbols/symboleffect/replace) - Transitions between symbols or configurations.
- [`automatic`](https://developer.apple.com/documentation/symbols/symboleffect/automatic) - Uses the context's default symbol transition.

### Symbol Effect Types
- [`AppearSymbolEffect`](https://developer.apple.com/documentation/symbols/appearsymboleffect) - Appearance behavior.
- [`AutomaticSymbolEffect`](https://developer.apple.com/documentation/symbols/automaticsymboleffect) - Context-sensitive transition behavior.
- [`BounceSymbolEffect`](https://developer.apple.com/documentation/symbols/bouncesymboleffect) - Transient bounce behavior.
- [`DisappearSymbolEffect`](https://developer.apple.com/documentation/symbols/disappearsymboleffect) - Disappearance behavior.
- [`PulseSymbolEffect`](https://developer.apple.com/documentation/symbols/pulsesymboleffect) - Layer-opacity pulsing.
- [`ReplaceSymbolEffect`](https://developer.apple.com/documentation/symbols/replacesymboleffect) - Symbol replacement behavior.
- [`ScaleSymbolEffect`](https://developer.apple.com/documentation/symbols/scalesymboleffect) - Layer-scaling behavior.
- [`VariableColorSymbolEffect`](https://developer.apple.com/documentation/symbols/variablecolorsymboleffect) - Cumulative or iterative variable-layer animation.
- [`BreatheSymbolEffect`](https://developer.apple.com/documentation/symbols/breathesymboleffect)
- [`RotateSymbolEffect`](https://developer.apple.com/documentation/symbols/rotatesymboleffect)
- [`WiggleSymbolEffect`](https://developer.apple.com/documentation/symbols/wigglesymboleffect)

### Symbol Effect Options
- [`SymbolEffectOptions`](https://developer.apple.com/documentation/symbols/symboleffectoptions) - Configures repetition, speed, and other effect preferences.

### Symbol Effect Protocols
- [`SymbolEffect`](https://developer.apple.com/documentation/symbols/symboleffect) - The base effect protocol.
- [`DiscreteSymbolEffect`](https://developer.apple.com/documentation/symbols/discretesymboleffect) - Marks transient animation behavior.
- [`IndefiniteSymbolEffect`](https://developer.apple.com/documentation/symbols/indefinitesymboleffect) - Marks behavior controlled by activation and removal.
- [`ContentTransitionSymbolEffect`](https://developer.apple.com/documentation/symbols/contenttransitionsymboleffect) - Marks transitions between symbols or configurations.
- [`TransitionSymbolEffect`](https://developer.apple.com/documentation/symbols/transitionsymboleffect) - Marks appearance/disappearance transitions.

### Structures
- [`DrawOffSymbolEffect`](https://developer.apple.com/documentation/symbols/drawoffsymboleffect) - Hides a symbol using its draw data.
- [`DrawOnSymbolEffect`](https://developer.apple.com/documentation/symbols/drawonsymboleffect) - Reveals a symbol using its draw data.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Symbols)*
