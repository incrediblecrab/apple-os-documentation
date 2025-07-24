# JavaScriptCore

Evaluate JavaScript programs from within an app, and support JavaScript scripting of your app.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 13.0+ | macOS 10.5+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The JavaScriptCore framework provides the ability to evaluate JavaScript programs from within Swift, Objective-C, and C-based apps. You can use also use JavaScriptCore to insert custom objects into the JavaScript environment.

## Topics

### Execution Environment
- **JSVirtualMachine** - A self-contained environment for JavaScript execution.
- **JSContext** - A JavaScript execution environment.

### JavaScript Code
- **JSValue** - A JavaScript value.
- **JSManagedValue** - A JavaScript value with conditional retain behavior to provide automatic memory management.

### Native Code
- **JSExport** - The protocol for exporting Objective-C objects to JavaScript.

### C API
- **C JavaScriptCore API** - Browse the alternative C-based APIs for JavaScriptCore.

### Reference
- **JavaScriptCore Constants**

### Variables
- **kJSTypeBigInt** - A JavaScript BigInt type.

### Functions
- **JSBigIntCreateWithDouble** - Creates a JavaScript BigInt value from a double.
- **JSBigIntCreateWithInt64** - Creates a JavaScript BigInt value from an Int64.
- **JSBigIntCreateWithString** - Creates a JavaScript BigInt value from a string.
- **JSBigIntCreateWithUInt64** - Creates a JavaScript BigInt value from a UInt64.
- **JSValueCompare** - Compares two JavaScript values.
- **JSValueCompareDouble** - Compares a JavaScript value with a double.
- **JSValueCompareInt64** - Compares a JavaScript value with an Int64.
- **JSValueCompareUInt64** - Compares a JavaScript value with a UInt64.
- **JSValueIsBigInt** - Determines if a JavaScript value is a BigInt.
- **JSValueToInt32** - Converts a JavaScript value to an Int32.
- **JSValueToInt64** - Converts a JavaScript value to an Int64.
- **JSValueToUInt32** - Converts a JavaScript value to a UInt32.
- **JSValueToUInt64** - Converts a JavaScript value to a UInt64.

### Enumerations
- **JSRelationCondition** - Represents the result of a JavaScript value comparison.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/JavaScriptCore)*