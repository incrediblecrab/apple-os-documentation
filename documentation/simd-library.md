# simd

Perform computations on small vectors and matrices.

## Overview

simd provides types and functions for small vector and matrix computations. The types include integer and floating-point vectors and matrices, and the functions provide basic arithmetic operations, element-wise mathematical operations, and geometric and linear algebra operations.

simd supports vectors containing up to 16 elements (for single-precision values) or 8 elements (for double-precision values), and matrices up to 4 x 4 elements in size. Other frameworks, such as **vForce**, allow you to work with larger vectors.

## Topics

### Boolean Scalar Data Type
- **simd_bool** - A Boolean scalar value.

### Signed Integer Vectors

#### 8-Bit Signed Integer Vectors
Perform operations on vectors that contain signed 8-bit integer elements.

#### 16-Bit Signed Integer Vectors
Perform operations on vectors that contain signed 16-bit integer elements.

#### 32-Bit Signed Integer Vectors
Perform operations on vectors that contain signed 32-bit integer elements.

#### 64-Bit Signed Integer Vectors
Perform operations on vectors that contain signed 64-bit integer elements.

### Unsigned Integer Vectors

#### 8-Bit Unsigned Integer Vectors
Perform operations on vectors that contain unsigned 8-bit integer elements.

#### 16-Bit Unsigned Integer Vectors
Perform operations on vectors that contain unsigned 16-bit integer elements.

#### 32-Bit Unsigned Integer Vectors
Perform operations on vectors that contain unsigned 32-bit integer elements.

#### 64-Bit Unsigned Integer Vectors
Perform operations on vectors that contain unsigned 64-bit integer elements.

### Floating-Point Vectors
- [Working with Vectors](https://developer.apple.com/documentation/accelerate/working_with_vectors) - Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.

#### Half-precision floating-point vectors
Perform operations on vectors that contain half-precision floating-point elements.

#### Single-precision floating-point vectors
Perform operations on vectors that contain single-precision floating-point elements.

#### Double-precision floating-point vectors
Perform operations on vectors that contain double-precision floating-point elements.

### Matrices
- [Working with Matrices](https://developer.apple.com/documentation/accelerate/working_with_matrices) - Solve simultaneous equations and transform points in space.

#### Half-precision floating-point matrices
Perform operations on matrices that contain half-precision floating-point elements.

#### Single-precision floating-point matrices
Perform operations on matrices that contain single-precision floating-point elements.

#### Double-precision floating-point matrices
Perform operations on matrices that contain double-precision floating-point elements.

### Quaternions
- [Working with Quaternions](https://developer.apple.com/documentation/accelerate/working_with_quaternions) - Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](https://developer.apple.com/documentation/accelerate/rotating_a_cube_by_transforming_its_vertices) - Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- **simd_quatf** - A single-precision quaternion.
- **simd_quatd** - A double-precision quaternion.

### Constants
- **SIMD_COMPILER_HAS_REQUIRED_FEATURES**
- **SIMD_LIBRARY_VERSION**

### Macros
- **simd Macros**

### See Also
#### Vectors, Matrices, and Quaternions
- [Working with Vectors](https://developer.apple.com/documentation/accelerate/working_with_vectors) - Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Working with Matrices](https://developer.apple.com/documentation/accelerate/working_with_matrices) - Solve simultaneous equations and transform points in space.
- [Working with Quaternions](https://developer.apple.com/documentation/accelerate/working_with_quaternions) - Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](https://developer.apple.com/documentation/accelerate/rotating_a_cube_by_transforming_its_vertices) - Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- **vForce** - Perform transcendental and trigonometric functions on vectors of any length.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Accelerate/simd-library)*