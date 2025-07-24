# Accelerate

Make large-scale mathematical computations and image calculations, optimized for high performance and low energy consumption.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.1+ | macOS 10.3+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Accelerate provides high-performance, energy-efficient computation on the CPU by leveraging its vector-processing capability. The following Accelerate libraries abstract that capability so that code written for them executes appropriate instructions for the processor available at runtime:

### Core Libraries

**BNNS**  
Subroutines for constructing and running neural networks for both training and inference.

**vImage**  
A wide range of image-processing functions, including Core Graphics and Core Video interoperation, format conversion, and image manipulation.

**vDSP**  
Digital signal processing functions, including 1D and 2D fast Fourier transforms, biquadratic filtering, vector and matrix arithmetic, convolution, and type conversion.

**vForce**  
Functions for performing arithmetic and transcendental functions on vectors.

**Sparse Solvers, BLAS, and LAPACK**  
Libraries for performing linear algebra on sparse and dense matrices.

### Related Libraries

Although not part of the Accelerate framework, the following libraries are closely related:

**Apple Archive**  
A framework for performing multithreaded lossless compression of directories, files, and data.

**Compression**  
Algorithms for lossless data compression that support LZFSE, LZ4, LZMA, and ZLIB algorithms.

**simd**  
A module for performing computations on small vectors and matrices.

**Spatial**  
Spatial is a lightweight 3D mathematical library that provides a simple API for working with 3D primitives.

## Topics

### Neural Networks
- [Training a neural network to recognize digits](https://developer.apple.com/documentation/accelerate/training_a_neural_network_to_recognize_digits) - Build a simple neural network and train it to recognize randomly generated numbers.
- **BNNS** - Implement and run neural networks for training and inference.

### Directories, Files, and Data Archives
- [Compressing single files](https://developer.apple.com/documentation/accelerate/compressing_single_files) - Compress a single file and store the result on the file system.
- [Decompressing single files](https://developer.apple.com/documentation/accelerate/decompressing_single_files) - Recreate a single file from a compressed file.
- [Compressing file system directories](https://developer.apple.com/documentation/accelerate/compressing_file_system_directories) - Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](https://developer.apple.com/documentation/accelerate/decompressing_and_extracting_an_archived_directory) - Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](https://developer.apple.com/documentation/accelerate/compressing_and_saving_a_string_to_the_file_system) - Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and Parsing an Archived String](https://developer.apple.com/documentation/accelerate/decompressing_and_parsing_an_archived_string) - Recreate a string from an archive file.

### Compression
- [Compressing and decompressing files with stream compression](https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_files_with_stream_compression) - Perform compression for all files and decompression for files with supported extension types.
- [Compressing and decompressing data with buffer compression](https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_data_with_buffer_compression) - Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [Compressing and decompressing data with input and output filters](https://developer.apple.com/documentation/accelerate/compressing_and_decompressing_data_with_input_and_output_filters) - Compress and decompress streamed or from-memory data, using input and output filters.

### Image Processing Essentials
- [Converting bitmap data between Core Graphics images and vImage buffers](https://developer.apple.com/documentation/accelerate/converting_bitmap_data_between_core_graphics_images_and_vimage_buffers) - Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](https://developer.apple.com/documentation/accelerate/creating_and_populating_buffers_from_core_graphics_images) - Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](https://developer.apple.com/documentation/accelerate/creating_a_core_graphics_image_from_a_vimage_buffer) - Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](https://developer.apple.com/documentation/accelerate/building_a_basic_image-processing_workflow) - Resize an image with vImage.
- [Applying geometric transforms to images](https://developer.apple.com/documentation/accelerate/applying_geometric_transforms_to_images) - Reflect, shear, rotate, and scale image buffers using vImage.
- [Compositing images with alpha blending](https://developer.apple.com/documentation/accelerate/compositing_images_with_alpha_blending) - Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](https://developer.apple.com/documentation/accelerate/compositing_images_with_vimage_blend_modes) - Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](https://developer.apple.com/documentation/accelerate/applying_vimage_operations_to_regions_of_interest) - Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](https://developer.apple.com/documentation/accelerate/optimizing_image-processing_performance) - Improve your app's performance by converting image buffer formats from interleaved to planar.
- **vImage** - Manipulate large images using the CPU's vector processor.

### Signal Processing Essentials
- [Controlling vDSP operations with stride](https://developer.apple.com/documentation/accelerate/controlling_vdsp_operations_with_stride) - Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](https://developer.apple.com/documentation/accelerate/using_linear_interpolation_to_construct_new_data_points) - Fill the gaps in arrays of numerical data using linear interpolation.
- [Using vDSP for vector-based arithmetic](https://developer.apple.com/documentation/accelerate/using_vdsp_for_vector-based_arithmetic) - Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
- [Resampling a signal with decimation](https://developer.apple.com/documentation/accelerate/resampling_a_signal_with_decimation) - Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- **vDSP** - Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.

### Fourier and Cosine Transforms
- [Understanding data packing for Fourier transforms](https://developer.apple.com/documentation/accelerate/understanding_data_packing_for_fourier_transforms) - Format source data for the vDSP Fourier functions, and interpret the results.
- [Finding the component frequencies in a composite sine wave](https://developer.apple.com/documentation/accelerate/finding_the_component_frequencies_in_a_composite_sine_wave) - Use 1D fast Fourier transform to compute the frequency components of a signal.
- [Performing Fourier transforms on interleaved-complex data](https://developer.apple.com/documentation/accelerate/performing_fourier_transforms_on_interleaved-complex_data) - Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [Reducing spectral leakage with windowing](https://developer.apple.com/documentation/accelerate/reducing_spectral_leakage_with_windowing) - Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [Signal extraction from noise](https://developer.apple.com/documentation/accelerate/signal_extraction_from_noise) - Use Accelerate's discrete cosine transform to remove noise from a signal.
- [Performing Fourier Transforms on Multiple Signals](https://developer.apple.com/documentation/accelerate/performing_fourier_transforms_on_multiple_signals) - Use Accelerate's multiple-signal fast Fourier transform (FFT) functions to transform multiple signals with a single function call.
- [Halftone descreening with 2D fast Fourier transform](https://developer.apple.com/documentation/accelerate/halftone_descreening_with_2d_fast_fourier_transform) - Reduce or remove periodic artifacts from images.
- **Fast Fourier transforms** - Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.
- **Discrete Fourier transforms** - Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.
- **Discrete Cosine transforms** - Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.

### Core Video Interoperation
- [Using vImage pixel buffers to generate video effects](https://developer.apple.com/documentation/accelerate/using_vimage_pixel_buffers_to_generate_video_effects) - Render real-time video effects with the vImage Pixel Buffer.
- [Integrating vImage pixel buffers into a Core Image workflow](https://developer.apple.com/documentation/accelerate/integrating_vimage_pixel_buffers_into_a_core_image_workflow) - Share image data between Core Video pixel buffers and vImage buffers to integrate vImage operations into a Core Image workflow.
- [Applying vImage operations to video sample buffers](https://developer.apple.com/documentation/accelerate/applying_vimage_operations_to_video_sample_buffers) - Use the vImage convert-any-to-any functionality to perform real-time image processing of video frames streamed from your device's camera.
- [Improving the quality of quantized images with dithering](https://developer.apple.com/documentation/accelerate/improving_the_quality_of_quantized_images_with_dithering) - Apply dithering to simulate colors that are unavailable in reduced bit depths.
- **Core Video interoperability** - Pass image data between Core Video and vImage.

### Vectors, Matrices, and Quaternions
- [Working with Vectors](https://developer.apple.com/documentation/accelerate/working_with_vectors) - Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Working with Matrices](https://developer.apple.com/documentation/accelerate/working_with_matrices) - Solve simultaneous equations and transform points in space.
- [Working with Quaternions](https://developer.apple.com/documentation/accelerate/working_with_quaternions) - Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](https://developer.apple.com/documentation/accelerate/rotating_a_cube_by_transforming_its_vertices) - Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- **simd** - Perform computations on small vectors and matrices.
- **vForce** - Perform transcendental and trigonometric functions on vectors of any length.

### Audio Processing
- [Visualizing sound as an audio spectrogram](https://developer.apple.com/documentation/accelerate/visualizing_sound_as_an_audio_spectrogram) - Share image data between vDSP and vImage to visualize audio that a device microphone captures.
- [Applying biquadratic filters to a music loop](https://developer.apple.com/documentation/accelerate/applying_biquadratic_filters_to_a_music_loop) - Change the frequency response of an audio signal using a cascaded biquadratic filter.
- [Equalizing audio with discrete cosine transforms (DCTs)](https://developer.apple.com/documentation/accelerate/equalizing_audio_with_discrete_cosine_transforms_dcts) - Change the frequency response of an audio signal by manipulating frequency-domain data.
- **Biquadratic IIR filters** - Apply biquadratic filters to single-channel and multichannel data.
- **Discrete Cosine transforms** - Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.

### Conversion Between Image Formats
- [Building a basic image conversion workflow](https://developer.apple.com/documentation/accelerate/building_a_basic_image_conversion_workflow) - Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Converting color images to grayscale](https://developer.apple.com/documentation/accelerate/converting_color_images_to_grayscale) - Convert an RGB image to grayscale using matrix multiplication.
- [Applying color transforms to images with a multidimensional lookup table](https://developer.apple.com/documentation/accelerate/applying_color_transforms_to_images_with_a_multidimensional_lookup_table) - Precompute translation values to optimize color space conversion and other pointwise operations.
- [Converting luminance and chrominance planes to an ARGB image](https://developer.apple.com/documentation/accelerate/converting_luminance_and_chrominance_planes_to_an_argb_image) - Create a displayable ARGB image using the luminance and chrominance information from your device's camera.
- **Conversion** - Convert an image to a different format.

### Image Resampling
- [Resampling in vImage](https://developer.apple.com/documentation/accelerate/resampling_in_vimage) - Learn how vImage resamples image data during geometric operations.
- [Reducing artifacts with custom resampling filters](https://developer.apple.com/documentation/accelerate/reducing_artifacts_with_custom_resampling_filters) - Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.
- **Image shearing** - Shear images horizontally and vertically.

### Convolution and Morphology
- [Blurring an image](https://developer.apple.com/documentation/accelerate/blurring_an_image) - Filter an image by convolving it with custom and high-speed kernels.
- [Adding a bokeh effect to images](https://developer.apple.com/documentation/accelerate/adding_a_bokeh_effect_to_images) - Simulate a bokeh effect by applying dilation.
- **Convolution** - Apply a convolution kernel to an image.
- **Morphology** - Dilate and erode images.

### Color and Tone Adjustment
- [Adjusting the brightness and contrast of an image](https://developer.apple.com/documentation/accelerate/adjusting_the_brightness_and_contrast_of_an_image) - Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](https://developer.apple.com/documentation/accelerate/adjusting_saturation_and_applying_tone_mapping) - Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Applying tone curve adjustments to images](https://developer.apple.com/documentation/accelerate/applying_tone_curve_adjustments_to_images) - Use the vImage library's polynomial transform to apply tone curve adjustments to images.
- [Adjusting the hue of an image](https://developer.apple.com/documentation/accelerate/adjusting_the_hue_of_an_image) - Convert an image to L*a*b* color space and apply hue adjustment.
- [Specifying histograms with vImage](https://developer.apple.com/documentation/accelerate/specifying_histograms_with_vimage) - Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](https://developer.apple.com/documentation/accelerate/enhancing_image_contrast_with_histogram_manipulation) - Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- **Histogram** - Calculate or manipulate an image's histogram.

### vImage / vDSP Interoperability
- [Finding the sharpest image in a sequence of captured images](https://developer.apple.com/documentation/accelerate/finding_the_sharpest_image_in_a_sequence_of_captured_images) - Share image data between vDSP and vImage to compute the sharpest image from a bracketed photo sequence.
- [Visualizing sound as an audio spectrogram](https://developer.apple.com/documentation/accelerate/visualizing_sound_as_an_audio_spectrogram) - Share image data between vDSP and vImage to visualize audio that a device microphone captures.

### Sparse Matrices
- [Creating sparse matrices](https://developer.apple.com/documentation/accelerate/creating_sparse_matrices) - Create sparse matrices for factorization and solving systems.
- [Solving systems using direct methods](https://developer.apple.com/documentation/accelerate/solving_systems_using_direct_methods) - Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [Solving systems using iterative methods](https://developer.apple.com/documentation/accelerate/solving_systems_using_iterative_methods) - Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Creating a sparse matrix from coordinate format arrays](https://developer.apple.com/documentation/accelerate/creating_a_sparse_matrix_from_coordinate_format_arrays) - Use separate coordinate format arrays to create sparse matrices.
- **Sparse Solvers** - Solve systems of equations where the coefficient matrix is sparse.

### Arithmetic and Transcendental Functions
- **vecLib** - Perform computations on large vectors.

### Linear Algebra
- [Solving systems of linear equations with LAPACK](https://developer.apple.com/documentation/accelerate/solving_systems_of_linear_equations_with_lapack) - Select the optimal LAPACK routine to solve a system of linear equations.
- [Finding an interpolating polynomial using the Vandermonde method](https://developer.apple.com/documentation/accelerate/finding_an_interpolating_polynomial_using_the_vandermonde_method) - Use LAPACK to solve a linear system and find an interpolating polynomial to construct new points between a series of known data points.
- [Compressing an image using linear algebra](https://developer.apple.com/documentation/accelerate/compressing_an_image_using_linear_algebra) - Reduce the storage size of an image using singular value decomposition (SVD).
- **BLAS** - Perform common linear algebra operations with Apple's implementation of the Basic Linear Algebra Subprograms (BLAS).

### Definite Integration
- **Quadrature** - Approximate the definite integral of a function over a finite or infinite interval.

### Macros
- **Macros**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Accelerate)*