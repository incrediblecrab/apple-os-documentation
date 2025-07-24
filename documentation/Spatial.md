# Spatial

Create and manipulate 3D mathematical primitives.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

The Spatial module is a lightweight 3D mathematical library that provides a simple API for working with 3D primitives. Much of its functionality is similar to the 2D geometry support in Core Graphics, but in three dimensions.

## Topics

### Data structures
- **Vector3D** - A three-element vector.
- **Vector3DFloat** - A single-precision structure that defines a three-element vector.
- **Axis3D** - Constants that describe an axis. *(Beta)*

### 2D primitives
- **Angle2D** - A geometric angle with a value you access in either radians or degrees.
- **Angle2DFloat** - A single-precision geometric angle whose value you access in either radians or degrees. *(Beta)*

### 3D primitives
- **Point3D** - A point in a 3D coordinate system.
- **Point3DFloat** - A single-precision structure that contains a point in a three-dimensional coordinate system. *(Beta)*
- **Size3D** - A size that describes width, height, and depth in a 3D coordinate system.
- **Size3DFloat** - A single-precision structure that contains width, height, and depth values. *(Beta)*
- **Rect3D** - A rectangle in a 3D coordinate system.
- **Rect3DFloat** - A single-precision structure that contains the location and dimensions of a 3D rectangle. *(Beta)*
- **Rotation3D** - A rotation in three dimensions.
- **Rotation3DFloat** - A single-precision structure that represents a rotation in three dimensions. *(Beta)*
- **RotationAxis3D** - A 3D rotation axis.
- **RotationAxis3DFloat** - A 3D axis. *(Beta)*
- **Pose3D** - A structure that contains a 3D position and a 3D rotation.
- **Pose3DFloat** - A single-precision structure that contains a position and rotation. *(Beta)*
- **ScaledPose3D** - A structure that contains a position, rotation, and scale.
- **ScaledPose3DFloat** - A structure that contains a position, rotation, and scale.
- **SphericalCoordinates3D** - A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- **SphericalCoordinates3DFloat** - A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order. *(Beta)*
- **Ray3D** - A ray in a 3D coordinate system.
- **Ray3DFloat** - A single-precision structure that contains the origin and direction of a 3D ray. *(Beta)*

### Affine and projective transforms
- **AffineTransform3D** - A 3D affine transformation matrix.
- **AffineTransform3DFloat** - *(Beta)*
- **ProjectiveTransform3D** - A 3D projective transformation matrix.
- **ProjectiveTransform3DFloat** - A single-precision 3D projective transformation matrix. *(Beta)*

### Converting between coordinate spaces
- **CoordinateSpace3D** - A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- **CoordinateSpace3DFloat**
- **CoordinateSpaceValue3D** - An opaque value which can be resolved to a concrete value in a CoordinateSpace3D.
- **ProjectiveTransformable3D**
- **ProjectiveTransformable3DFloat**
- **WorldReferenceCoordinateSpace** - A coordinate space that represents a world reference point.

### Applying trigonometric functions
- **cos(Angle2D)** - Returns Double
- **cos(Angle2DFloat)** - Returns Float
- **cosh(Angle2D)** - Returns Double
- **cosh(Angle2DFloat)** - Returns Float
- **sin(Angle2DFloat)** - Returns Float
- **sin(Angle2D)** - Returns Double
- **sinh(Angle2D)** - Returns Double
- **sinh(Angle2DFloat)** - Returns Float
- **tan(Angle2D)** - Returns Double
- **tan(Angle2DFloat)** - Returns Float
- **tanh(Angle2D)** - Returns Double
- **tanh(Angle2DFloat)** - Returns Float

### Protocols
- **Primitive3D** - A set of methods common to Spatial primitives.
- **Rotatable3D** - A set of methods that defines the interface to rotate Spatial entities.
- **Scalable3D** - A set of methods that defines the interface to scale Spatial entities.
- **Shearable3D** - A set of methods that defines the interface to shear Spatial entities.
- **Translatable3D** - A set of methods that defines the interface to translate Spatial entities.
- **Volumetric** - A set of methods for working with Spatial primitives with volume.
- **ClampableWithinRectProtocol** - A set of methods that defines the interface for Spatial entities that can be clamped to a volume.
- **Primitive3DProtocol** - A set of methods common to Spatial primitives.
- **Rotatable3DProtocol** - A set of methods that defines the interface for Spatial entities that can rotate.
- **Scalable3DProtocol** - A set of methods that defines the interface for Spatial entities that can scale.
- **Shearable3DProtocol** - A set of methods that defines the interface for Spatial entities that can shear.
- **SpatialTypeProtocol**
- **Transform3DProtocol** - A set of methods that are common to transforms.
- **Translatable3DProtocol** - A set of methods that defines the interface for Spatial entities that can translate.
- **VolumetricProtocol** - A set of methods for working with Spatial primitives with volume.

### Structures
- **EulerAnglesFloat** - *(Beta)*

### Enumerations
- **AxisWithFactorsFloat** - The axis of a shear transform.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Spatial)*