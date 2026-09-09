# Application Services

Perform common application tasks.

**Catalog platform annotations:** Mac Catalyst 13.0+ | macOS 10.0+. These are not uniform minimums or current-platform support guarantees for every legacy header and symbol below.

## Overview

Application Services is a reference catalog for low-level application services, including accessibility, color management, printing, and older Carbon interfaces. Check the individual API's availability and deprecation annotations rather than assuming every historical manager is appropriate for new applications.

For current 2D drawing and text-layout work, consult [Core Graphics](https://developer.apple.com/documentation/coregraphics) and [Core Text](https://developer.apple.com/documentation/coretext). The older catalog's discussion of QuickDraw, Font Manager, and ATSUI is historical context, not a recommendation to adopt those interfaces or evidence of a particular removal date.

## Topics

### Managers
- [Apple Event Manager](https://developer.apple.com/documentation/applicationservices/apple_event_manager)
- [ColorSync Manager](https://developer.apple.com/documentation/applicationservices/colorsync_manager)
- [Speech Synthesis Manager](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)

### Reference
- [Carbon Accessibility](https://developer.apple.com/documentation/applicationservices/carbon_accessibility)
- [Core Printing](https://developer.apple.com/documentation/applicationservices/core_printing)

### Headers
- **AXActionConstants.h** - Many UIElements have a set of actions that they can perform. Actions are designed to be simple. Actions roughly correspond to things you could do with a single click of the mouse on the UIElement. Buttons and menu items, for example, have a single action: push or pick, respectively. A scroll bar has several actions: page up, page down, up one line, down one line.
- **AXAttributeConstants.h**
- **AXError.h** - These error codes can be returned from the accessibility functions defined in AXUIElement.h.
- **AXNotificationConstants.h**
- **AXRoleConstants.h**
- [**AXTextAttributedString.h**](https://developer.apple.com/documentation/applicationservices/axtextattributedstring_h) - Constants used by accessibility attributed strings, associating character ranges with attributes such as color, font, and underlining.
- **AXUIElement.h**
- [**AXValue.h**](https://developer.apple.com/documentation/applicationservices/axvalue_h) - The `AXValue`/`AXValueType` types and functions that create, identify, and extract wrapped values.
- **AXValueConstants.h**
- **UniversalAccess.h** - This header file contains functions that give applications the ability to control the zoom focus. Using these functions, an application can tell the macOS Universal Access zoom feature what part of its user interface needs focus.

### ApplicationServices Types
- **ApplicationServices Structures**
- **ApplicationServices Enumerations**
- **ApplicationServices Constants**
- **ApplicationServices Functions**
- **ApplicationServices Data Types**

### Classes
- **ColorSyncCMM**
- **ColorSyncMutableProfile**
- **ColorSyncProfile**
- **ColorSyncTransform**
- **HIMutableShape**
- **HIShape**
- **Pasteboard**
- **Translation**
- **AXTextMarker**
- **AXTextMarkerRange**

### Protocols
- **PDEPanel**
- **PDEPlugIn**
- **PDEPlugInCallbackProtocol**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/applicationservices)*
