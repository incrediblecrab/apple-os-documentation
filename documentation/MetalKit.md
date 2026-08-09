# MetalKit

Build Metal apps quicker and easier using a common set of utility classes.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | tvOS 9.0+ | visionOS 1.0+

## Topics

### View Management
Display your Metal content with a view that manages much of the setup for you.
- **MTKView** - A specialized view that creates, configures, and displays Metal objects.
- **MTKViewDelegate** - Methods for responding to a MetalKit view's drawing and resizing events.

### Texture Loading
Load textures into your Metal app from a variety of sources.
- **MTKTextureLoader** - An object that creates textures from existing data in common image formats.

### Model Handling
Handle Model I/O assets using a Metal-specific interface.
- **MTKMesh** - A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- **MTKMeshBuffer** - A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- **MTKMeshBufferAllocator** - An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- **MTKSubmesh** - A container for the index data of a Model I/O submesh, suitable for use in a Metal app.

### Conversion Functions
Convert between Metal and Model I/O vertex representations.

### Model Errors
Learn about errors thrown by model handling methods.

### Reference
- **MetalKit Functions** - The MetalKit framework defines helper functions that are used to efficiently interface with the Metal and Model I/O frameworks.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetalKit)*