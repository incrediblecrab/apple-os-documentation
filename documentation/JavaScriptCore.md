# JavaScriptCore

Evaluate JavaScript programs from within an app, and support JavaScript scripting of your app.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.1+ | macOS 10.5+ (C API), 10.9+ (bridge classes) | tvOS 9.0+ | visionOS 1.0+

## Overview

JavaScriptCore evaluates scripts and exchanges values between JavaScript and native code. Swift and Objective-C apps can use its object bridge; C-based apps can use the C API. The older bridge-class declarations, rather than the framework catalog's iOS 16 aggregate, establish the baseline above. Newer functions have separate requirements.

## Runtime boundaries and Safari 27

[`JSContext`](https://developer.apple.com/documentation/javascriptcore/jscontext) and [`JSVirtualMachine`](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine) provide an embedded JavaScript runtime, not a browser DOM, CSS engine, or Safari extension host. Use [WebKit](WebKit.md) for webpage integration.

The [Safari 27 WebKit announcement](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/) documents a module-loader rewrite that fixes top-level-await ordering and support for WebAssembly JavaScript Promise Integration (JSPI). Do not infer that installing Safari 27 adds every browser capability to an app's `JSContext` on an older OS. Test the actual embedded runtime and the JavaScript APIs your scripts require.

For browser-side Wasm, detect **both** `WebAssembly.Suspending` and `WebAssembly.promising` before selecting a JSPI build. Keep a compatible asynchronous fallback; JSPI does not permit blocking the UI thread for synchronous network access. See the [Safari migration guide](../guides/safari27-migration.md#javascript-wasm-and-announcements).

## Topics

### Execution Environment
- [`JSVirtualMachine`](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine) - Owns execution resources and can contain multiple contexts. Calls are thread-safe but serialize within a virtual machine; use separate machines for concurrent JavaScript execution.
- [`JSContext`](https://developer.apple.com/documentation/javascriptcore/jscontext) - Holds a script environment and exposes evaluation and native bridging. Values can cross contexts in the same virtual machine, but not between different virtual machines.

### JavaScript Code
- [`JSValue`](https://developer.apple.com/documentation/javascriptcore/jsvalue) - Wraps a JavaScript value and strongly retains its context. Storing one in an exported native object can create a retain cycle.
- [`JSManagedValue`](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue) - Supports conditional retention. Report native ownership with the virtual machine's `addManagedReference(_:withOwner:)` and remove that relationship when appropriate. Without reachability through JavaScript or a reported, reachable native ownership chain, its `value` can become `nil`.

These four bridge classes date to iOS/iPadOS 7 and macOS 10.9, with Mac Catalyst 13.1, tvOS 9, and visionOS 1 declarations.

### Native Code
- [`JSExport`](https://developer.apple.com/documentation/javascriptcore/jsexport) - Define a protocol inheriting from `JSExport` to select the Objective-C-visible methods and properties exposed to JavaScript. Native class members are not all exported automatically.

The current `JSExport` catalog carries different aggregate availability labels from the bridge classes. Its [public header](https://github.com/WebKit/WebKit/blob/main/Source/JavaScriptCore/API/JSExport.h) does not annotate a separate introduction; do not use that catalog's iOS 16 label to date all JavaScriptCore bridging.

### C API
- [C JavaScriptCore API](https://developer.apple.com/documentation/javascriptcore/c-javascriptcore-api) - Context, value, object, string, and garbage-collection interfaces for C callers.

### Reference
- [JavaScriptCore Constants](https://developer.apple.com/documentation/javascriptcore/javascriptcore-constants) - BigInt typed-array constants and native export macros.

### Variables
- [`kJSTypeBigInt`](https://developer.apple.com/documentation/javascriptcore/kjstypebigint) - A `JSType` value identifying a BigInt primitive.

### Functions

The BigInt constant, comparison-result enum, and functions listed here have **iOS/iPadOS/Mac Catalyst 18+, macOS 15+, and visionOS 2+** reference declarations. They are not OS 27 introductions. Their current DocC pages also show tvOS 9, whereas the [public C header](https://github.com/WebKit/WebKit/blob/main/Source/JavaScriptCore/API/JSValueRef.h) supplies macOS/iOS annotations without a separate tvOS introduction. This page does not treat that tvOS catalog label as proof these newer functions run on tvOS 9.

- [`JSBigIntCreateWithDouble`](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithdouble(_:_:_:)) - Creates a BigInt from an integer-valued double; a noninteger produces an exception.
- [`JSBigIntCreateWithInt64`](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithint64(_:_:_:)) - Creates a BigInt from a signed 64-bit integer.
- [`JSBigIntCreateWithString`](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithstring(_:_:_:)) - Parses a `JSStringRef` using JavaScript's `BigInt(string)` semantics; malformed input can fail.
- [`JSBigIntCreateWithUInt64`](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithuint64(_:_:_:)) - Creates a BigInt from an unsigned 64-bit integer.
- [`JSValueCompare`](https://developer.apple.com/documentation/javascriptcore/jsvaluecompare(_:_:_:_:)) - Uses JavaScript `==`, `<`, and `>` semantics, including coercion, rather than strict identity.
- [`JSValueCompareDouble`](https://developer.apple.com/documentation/javascriptcore/jsvaluecomparedouble(_:_:_:_:)), [`JSValueCompareInt64`](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareint64(_:_:_:_:)), and [`JSValueCompareUInt64`](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareuint64(_:_:_:_:)) - Compare a JavaScript value with the specified native numeric type.
- [`JSValueIsBigInt`](https://developer.apple.com/documentation/javascriptcore/jsvalueisbigint(_:_:)) - Tests the value's type without converting it.
- [`JSValueToInt32`](https://developer.apple.com/documentation/javascriptcore/jsvaluetoint32(_:_:_:)), [`JSValueToInt64`](https://developer.apple.com/documentation/javascriptcore/jsvaluetoint64(_:_:_:)), [`JSValueToUInt32`](https://developer.apple.com/documentation/javascriptcore/jsvaluetouint32(_:_:_:)), and [`JSValueToUInt64`](https://developer.apple.com/documentation/javascriptcore/jsvaluetouint64(_:_:_:)) - Apply JavaScript integer-conversion rules; BigInts are truncated to the destination width, not range-checked lossless conversions.

Initialize the C exception output to `NULL` before each fallible call and inspect it afterward. Integer conversions return `0` on an exception, but zero is also a valid result. BigInt creation documents `NULL` on failure even though the rendered Swift signature uses a nonoptional `JSValueRef`; do not use a result after a reported exception.

### Enumerations
- [`JSRelationCondition`](https://developer.apple.com/documentation/javascriptcore/jsrelationcondition) - The comparison result. `kJSRelationConditionUndefined` can indicate an exception or an unordered comparison involving `NaN`, so also inspect the exception output.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/JavaScriptCore)*
