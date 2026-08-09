# xcselect

Access the path of the macOS SDK available on the host system.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.15+

## Overview

The system provides xcselect_host_sdk_path, a function to locate the path to a macOS SDK version for building executables, libraries, and other content that runs on the local Mac. If you don't use Xcode build tools, you can use this function to get the macOS SDK version you need.

Note

The xcselect framework is not available in Swift.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/xcselect)*
