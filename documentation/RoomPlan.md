# RoomPlan

Create a 3D model of a room by interactively guiding people to scan their physical environment using a device's camera.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+

## Overview

Use RoomPlan to create a 3D model of an interior room. The framework uses a device's sensors, trained ML models, and RealityKit's rendering capabilities to capture the physical surroundings of an interior room. For example, the framework inspects a device's camera feed and LiDAR readings to identify walls, windows, openings, and doors. RoomPlan also recognizes room features, furniture, and appliances, such as a fireplace, bed, or refrigerator, and provides that information to the app.

To begin a capture, the app presents a view (RoomCaptureView) that the user looks through to see their room in AR. The view displays virtual cues as they move around the room:

- Real-time graphic overlays display on top of physical structures in the room to convey scanning progress.
- If the framework requires a specific kind of device movement or perspective to complete the capture, the UI displays instructions that explain how to position the device.

When the app determines that the current scan is complete, the view displays a small-scale version of the scanned room for the user to approve.

Alternatively, your app can display custom graphics during the scanning process by creating and using a scan session object (RoomCaptureSession) directly.

### Access the captured results

The framework outputs a scan as parametric data, which makes it easy for your app to modify the scanned room's individual components. RoomPlan also provides the results in various Universal Scene Description (USD) formats. With these assets, your app can implement custom features, such as the following:

- Estimate the size of particular areas of a room.
- Preview virtual furniture from a catalog in a variety of styles and positions.
- Integrate a version of a scanned room or structure in a 3D game.

### Process scan results on macOS with Mac Catalyst

Mac apps built with Mac Catalyst can access CapturedRoom and CapturedStructure and can perform encoding, decoding, and exporting. Environment scanning relies on a camera, LiDAR, and other sensors that support augmented reality on iOS and iPad OS devices. However, macOS apps built with Mac Catalyst can process the results of room-capture sessions performed on those devices. RoomPlan ignores all capture-session-related calls on macOS apps built with Mac Catalyst.

## Topics

### Essentials
- [Create a 3D model of an interior room by guiding the user through an AR experience](https://developer.apple.com/documentation/roomplan/create_a_3d_model_of_an_interior_room_by_guiding_the_user_through_an_ar_experience) - Highlight physical structures and display text that guides a user to scan the shape of their physical environment using a framework-provided view.

### User Interface
- **RoomCaptureView** - A view that enables the user to scan their room with the device's camera.
- **RoomCaptureViewDelegate** - A specification to post-process the results of a scan.

### Scanning Protocol
- **RoomCaptureSession** - An object that manages the room-scanning process.
- **RoomCaptureSessionDelegate** - A specification of important events in the room-scanning process.

### Captured Data
- [Merging multiple scans into a single structure](https://developer.apple.com/documentation/roomplan/merging_multiple_scans_into_a_single_structure) - Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [Scanning the rooms of a single structure](https://developer.apple.com/documentation/roomplan/scanning_the_rooms_of_a_single_structure) - Create an AR experience that enables people to scan a building that contains multiple rooms.
- **CapturedRoom** - A structure that provides the key details of a scanned room.
- **CapturedStructure** - An object that holds the results of the merger of multiple capture sessions.
- **CapturedRoomData** - An opaque object that holds the raw results of a scan.

### Captured Object Attributes
- Determine details about the objects and surfaces that the framework identifies in a scan.

### 3D Asset Output
- [Providing custom models for captured rooms and structure exports](https://developer.apple.com/documentation/roomplan/providing_custom_models_for_captured_rooms_and_structure_exports) - Enhance the look of an exported 3D model by substituting object bounding boxes with detailed 3D renditions.
- **RoomBuilder** - An object that generates a 3D asset from room-capture data.
- **StructureBuilder** - An object that combines multiple scan sessions into a single captured result.
- **USDExportOptions** - Options that determine the underlying data format of a scan export.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RoomPlan)*