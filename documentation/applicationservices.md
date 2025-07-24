# Application Services

Perform common application tasks.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.0+

## Overview

This collection of documents provides the API reference for the Application Services framework, which includes several services that are essential to Carbon applications. The Application Services framework also includes support for a number of legacy technologies—such as QuickDraw and the Font Manager—that have been superseded with newer technologies like Quartz 2D and ATSUI.

## Topics

### Managers
- **Apple Event Manager**
- **ColorSync Manager**
- **Speech Synthesis Manager**

### Reference
- **Carbon Accessibility**
- **Core Printing**

### Headers
- **AXActionConstants.h** - Many UIElements have a set of actions that they can perform. Actions are designed to be simple. Actions roughly correspond to things you could do with a single click of the mouse on the UIElement. Buttons and menu items, for example, have a single action: push or pick, respectively. A scroll bar has several actions: page up, page down, up one line, down one line.
- **AXAttributeConstants.h**
- **AXError.h** - These error codes can be returned from the accessibility functions defined in AXUIElement.h.
- **AXNotificationConstants.h**
- **AXRoleConstants.h**
- **AXTextAttributedString.h** - This header file contains definitions of constants used with accessibility objects that represent attributed strings. An attributed string is an association of a range of characters and their attributes, such as color and font. If an accessibility object represents an attributed string, the value of its kAXParameterizedAttributeStringAttribute attribute is an attributed string object (a CFAttributedStringRef or an NSAttributedString) that uses the constants defined in this header file to define its attributes.
- **AXUIElement.h**
- **AXValue.h** - This header contains functions and data types for working with AXValueType wrappers.
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