# GLKit

Speed up OpenGL ES or OpenGL app development. Use math libraries, background texture loading, pre-created shader effects, and a standard view and view controller to implement your rendering loop.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | macOS 10.8+ | tvOS 9.0+

## Overview

The GLKit framework provides functions and classes that reduce the effort required to create new shader-based apps or to port existing apps that rely on fixed-function vertex or fragment processing provided by earlier versions of OpenGL ES or OpenGL.

### GLKit Features

GLKit provides functionality in four key areas:

- **Texture loading** allows your app to easily load textures from a variety of sources. Textures can even be loaded asynchronously in the background with just a few lines of code. For more information, see GLKTextureLoader.

- **Math libraries** provide commonly used vector, quaternion and matrix operations. These implementations are optimized to provide great performance.

- **Effects** provide standard implementations of common shader effects. You configure the effect and the associated vertex data; the effect creates and loads an appropriate shader. GLKit includes three effects: The GLKBaseEffect class implements a critical subset of the OpenGL ES 1.1 shading and lighting model, the GLKReflectionMapEffect class extends the base effect to include reflection mapping support, and the GLKSkyboxEffect class provides an implementation of a skybox effect.

- **Views and View Controllers** provide a standard implementation of an OpenGL ES view and a corresponding view controller. This reduces the amount of code needed to create an iOS app that use OpenGL ES. For more information, see GLKView and GLKViewController.

On iOS, GLKit requires an OpenGL ES 2.0 context. In macOS, GLKit requires an OpenGL context that supports the OpenGL 3.2 Core Profile.

## Topics

### Texture Loading
- **GLKTextureInfo** - Information about OpenGL textures created by the GLKTextureLoader class. (Deprecated)
- **GLKTextureLoader** - A utility class that simplifies loading OpenGL or OpenGL ES texture datas from a variety of image file formats. (Deprecated)

### OpenGL ES View Rendering
- **GLKView** - A default implementation for views that draw their content using OpenGL ES. (Deprecated)
- **GLKViewDelegate** - Drawing callback methods for use with a GLKView object.
- **GLKViewController** - A view controller that manages an OpenGL ES rendering loop. (Deprecated)
- **GLKViewControllerDelegate** - Rendering loop callback methods for use with a GLKViewController object.

### Mesh Data Management
- **GLKMesh** (Deprecated)
- **GLKMeshBuffer** (Deprecated)
- **GLKMeshBufferAllocator** (Deprecated)
- **GLKSubmesh** (Deprecated)

### Shader-Based Rendering Effects
- **GLKNamedEffect** - A standard interface for objects that provide shader-based OpenGL rendering effects.
- **GLKBaseEffect** - A simple lighting and shading system for use in shader-based OpenGL rendering. (Deprecated)
- **GLKReflectionMapEffect** - A lighting and shading system that supports reflection mapping for use in shader-based OpenGL rendering. (Deprecated)
- **GLKSkyboxEffect** - A simple skybox visual effect for use in shader-based OpenGL rendering. (Deprecated)

### Rendering Effect Parameters
- **GLKEffectProperty** - The abstract superclass for configuration information used in GLKit rendering effects. (Deprecated)
- **GLKEffectPropertyFog** - Fog drawing information for use in GLKit rendering effects. (Deprecated)
- **GLKEffectPropertyLight** - Lighting information for use in GLKit rendering effects. (Deprecated)
- **GLKEffectPropertyTexture** - Texture drawing parameters for use in GLKit rendering effects. (Deprecated)
- **GLKEffectPropertyMaterial** - Surface appearance properties for use in GLKit rendering effects. (Deprecated)
- **GLKEffectPropertyTransform** - Coordinate transform information for use in GLKit rendering effects. (Deprecated)
- **GLKit Effects Constants**

### Math Utilities
- **GLKMatrixStack** - An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- **GLKMatrix3**
- **GLKMatrix4**
- **GLKVector2**
- **GLKVector3**
- **GLKVector4**
- **GLKQuaternion**
- **GLKit Math Utilities**

### Reference
- **GLKit Structures**
- **GLKit Enumerations**
- **GLKit Constants**
- **GLKit Functions**
- **GLKit Data Types**

### See Also
- **Related Documentation**
- [OpenGL Programming Guide for Mac](https://developer.apple.com/documentation/opengl_programming_guide_for_mac)
- [OpenGL ES Programming Guide](https://developer.apple.com/documentation/opengles_programming_guide)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GLKit)*