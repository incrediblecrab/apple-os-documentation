# Force Feedback

Control force feedback devices attached to the system. Develop plug-ins that enable communication with force feedback hardware.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.2+

## Overview

The Force Feedback framework contains the public interfaces to the Force Feedback implementation in macOS, including an API that supports the development of Force Feedback plug-ins.

## Topics

### Reference
- **ForceFeedback.h** - Public Interfaces to the Force Feedback implementation in macOS.
- **ForceFeedbackConstants.h** - Constants used in the public interfaces to the Force Feedback implementation in macOS.
- **IOForceFeedbackLib.h** - Public Interfaces and constants used to develop Force Feedback plugIns.
- **ForceFeedback Structures**
- **ForceFeedback Enumerations**
- **ForceFeedback Constants**
- **ForceFeedback Data Types**

### Variables
- **var kFFAPIMajorRev: Int**
- **var kFFAPIMinorAndBugRev: Int**
- **var kFFAPINonRelRev: Int**
- **var kFFAPIStage: Int**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ForceFeedback)*