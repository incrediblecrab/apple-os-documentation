# OpenGL ES

Create 3D and 2D graphics effects with this compact, efficient subset of OpenGL.

**Platforms:** iOS 2.0–12.0 (Deprecated) | iPadOS 2.0–12.0 (Deprecated) | tvOS 9.0–12.0 (Deprecated) | visionOS 1.0–1.0 (Deprecated)

## Overview

OpenGL ES provides a C-based interface for hardware-accelerated 2D and 3D graphics rendering. The OpenGL ES framework (OpenGLES.framework) in iOS provides implementations of versions 1.1, 2.0, and 3.0 of the OpenGL ES specification.

This collection of documents describes the platform-specific APIs for OpenGL ES on iOS devices, also known as EAGL. EAGL provides graphics contexts that encapsulate all OpenGL ES state and the ability to configure a Core Animation layer to be the destination for OpenGL ES drawing commands. EAGL also allows OpenGL ES objects, such as textures, renderbuffers, and framebuffers, to be shared between two or more graphics contexts.

The Khronos Group maintains the OpenGL ES specifications and references for the cross-platform OpenGL ES APIs:

OpenGL ES API Registry is the official repository of OpenGL ES specification and extension documents provided by the Khronos Group.

For a complete reference to the OpenGL ES APIs and OpenGL ES Shading Language, see the collection for the version of OpenGL ES you plan to use:

- OpenGL ES 1.1 Reference Pages
- OpenGL ES 2.0 Reference Pages
- OpenGL ES 3.0 Reference Pages

## Topics

### Classes
- **EAGLContext** - An EAGLContext object manages an OpenGL ES rendering context—the state information, commands, and resources needed to draw using OpenGL ES. To execute OpenGL ES commands, you need a current rendering context.
- **EAGLSharegroup** - An EAGLSharegroup object manages OpenGL ES resources associated with one or more EAGLContext objects. It is created when an EAGLContext object is initialized and disposed of when the last EAGLContext object that references it is released. As an opaque object, there is no developer accessible API.

### Protocols
- **EAGLDrawable** - iOS objects that implement the EAGLDrawable protocol can be used as a rendering surface and displayed to the screen by an EAGLContext object. In iOS 2.0, this protocol is implemented only by the CAEAGLLayer class, but in the future other classes may choose to implement the protocol. The EAGLDrawable protocol is not intended to be implemented by objects outside of the iOS.

### Reference
- **EAGL Functions** - This document describes the functions in the OpenGL ES framework.
- **OpenGL ES Enumerations**
- **OpenGL ES Constants**
- **OpenGL ES Functions**
- **OpenGL ES Data Types**

### Variables
- **GL_SAMPLER_2D_SHADOW**
- **GL_TEXTURE_ENV_COLOR**
- **GL_TEXTURE_ENV_MODE**
- **GL_TIMEOUT_IGNORED**

### Functions
- **glFramebufferTextureLayer**

### See Also

#### Related Documentation
- **OpenGL ES Programming Guide**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/OpenGLES)*