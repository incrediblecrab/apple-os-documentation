# ColorSync

Reproduce colors accurately across a range of input, output, and display devices.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Availability and scope

The framework's platform list is not a guarantee for every API. For example, [`ColorSyncCMM`](https://developer.apple.com/documentation/colorsync/colorsynccmm), a color-management-module handle, lists Mac Catalyst and macOS, while [`ColorSyncMutableProfile`](https://developer.apple.com/documentation/colorsync/colorsyncmutableprofile) has the broader platform coverage above. Check the selected profile, transform, or CMM operation's own availability.

## Topics

### Reference
- **ColorSync Constants**
- **ColorSync Functions**

### Classes
- **ColorSyncCMM**
- **ColorSyncMutableProfile**
- **ColorSyncProfile**
- **ColorSyncTransform**

### Structures
- **ColorSyncAlphaInfo**
- **ColorSyncDataDepth**
- **ColorSyncMD5**

### Variables
- **kColorSyncAlphaNone**
- **kColorSyncTransformUseITU709OETF**

### Type Aliases
- **CMMApplyTransformProc**
- **CMMCreateTransformPropertyProc**
- **CMMInitializeLinkProfileProc**
- **CMMInitializeTransformProc**
- **ColorSyncCMMIterateCallback**
- **ColorSyncDataLayout**
- **ColorSyncDeviceProfileIterateCallback**
- **ColorSyncProfileIterateCallback**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ColorSync)*
