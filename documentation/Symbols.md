# Symbols

Apply universal animations to symbol-based images.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

The Symbols framework provides access to symbol effects you can use to animate SF Symbols in your AppKit, UIKit, and SwiftUI apps. These animations exhibit different behaviors:

- **Discrete** - An effect that runs from start to finish
- **Indefinite** - An effect that lasts until you remove or disable it
- **Transition** - An effect that animates a symbol in or out of visibility
- **Content Transition** - An effect that replaces one symbol with another symbol, or with a different configuration of itself

A symbol effect can exhibit multiple types of behavior. For instance, you can add a pulse effect with an option to occur a finite number of times — a discrete behavior. You can also add a pulse effect with an option to loop forever — an indefinite behavior.

```swift
// Add an effect in SwiftUI.
Image(systemName: "globe")
    // Add effect with discrete behavior to image view.
    .symbolEffect(.pulse, options: .repeat(3))

Image(systemName: "globe")
    // Add effect with indefinite behavior to image view.
    .symbolEffect(.pulse)
```

You can apply universal animation effects to symbol-based images that you display in image views. The Symbols framework provides a consistent set of effects to use regardless of your UI framework or language choices.

Consider a SwiftUI app that displays a variable color effect on a Wi-Fi symbol while the system searches for Wi-Fi networks.

```swift
// Add an effect in SwiftUI.
Image(systemName: "wifi")
    .symbolEffect(.variableColor.reversing)
```

Now consider an AppKit or UIKit version of the app. You can apply the same effect to animate the search for Wi-Fi networks.

```swift
// Add an effect in AppKit and UIKit.
imageView.addSymbolEffect(.variableColor.reversing)
```

## Topics

### Symbol Effects
- **appear** - An animation that makes the layers of a symbol-based image appear separately or as a whole
- **bounce** - An animation that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole
- **disappear** - An animation that makes the layers of a symbol-based image disappear separately or as a whole
- **pulse** - An animation that fades the opacity of some or all layers in a symbol-based image
- **scale** - An animation that scales the layers in a symbol-based image separately or as a whole
- **variableColor** - An animation that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence

### Symbol Content Transitions
- **replace** - An animation that replaces the layers of one symbol-based image with those of another
- **automatic** - A transition that applies the default animation to a symbol-based image in a context-sensitive manner

### Symbol Effect Types
- **AppearSymbolEffect** - A type that makes the layers of a symbol-based image appear separately or as a whole
- **AutomaticSymbolEffect** - A type that applies the default animation to a symbol-based image in a context-sensitive manner
- **BounceSymbolEffect** - A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole
- **DisappearSymbolEffect** - A type that makes the layers of a symbol-based image disappear separately or as a whole
- **PulseSymbolEffect** - A type that fades the opacity of some or all layers in a symbol-based image
- **ReplaceSymbolEffect** - A type that replaces the layers of one symbol-based image with those of another
- **ScaleSymbolEffect** - A type that scales the layers in a symbol-based image separately or as a whole
- **VariableColorSymbolEffect** - A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence
- **BreatheSymbolEffect**
- **RotateSymbolEffect**
- **WiggleSymbolEffect**

### Symbol Effect Options
- **SymbolEffectOptions** - Options that configure how effects apply to symbol-based images

### Symbol Effect Protocols
- **SymbolEffect** - A presentation effect that you apply to a symbol-based image
- **DiscreteSymbolEffect** - An effect that performs a transient animation
- **IndefiniteSymbolEffect** - An animation that continually affects a symbol until it's disabled or removed
- **ContentTransitionSymbolEffect** - An effect that animates between symbols or different configurations of the same symbol
- **TransitionSymbolEffect** - An effect that animates a symbol in or out

### Structures
- **DrawOffSymbolEffect** - A symbol effect that applies the DrawOff animation to symbol images
- **DrawOnSymbolEffect** - A symbol effect that applies the DrawOn animation to symbol images

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Symbols)*