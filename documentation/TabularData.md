# TabularData

Import, organize, and prepare a table of data to train a machine learning model.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 12.0+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

The **TabularData** framework provides Swift types for loading, manipulating, and analyzing tabular data. Use this framework to import data from CSV or JSON files, organize it into data frames, and prepare it for machine learning workflows.

## Topics

### Data Tables
- **DataFrame** - A collection that arranges data in rows and columns.
- **DataFrameProtocol** - A type that represents a data frame.

### Typed Columns
- **Column** - A column in a data frame.
- **ColumnSlice** - A collection that represents a selection of contiguous elements from a typed column.
- **FilledColumn** - A view on a column that replaces missing elements with a default value.
- **DiscontiguousColumnSlice** - A collection that represents a selection, potentially with gaps, of elements from a typed column.
- **ColumnProtocol** - A type that represents a column.
- **OptionalColumnProtocol** - A type that represents a column that has missing values.

### Type-Erased Columns
- **AnyColumn** - A type-erased column.
- **AnyColumnSlice** - A type-erased column slice.
- **AnyColumnProtocol** - A type that represents a type-erased column.
- **AnyColumnPrototype** - A prototype that creates type-erased columns.

### Statistical Summaries
- **NumericSummary** - A summary of a numerical column.
- **CategoricalSummary** - A categorical summary of a collection's elements.
- **AnyCategoricalSummary** - A type-erased categorical summary.

### Errors
- **JSONReadingError** - A JSON reading error.
- **CSVReadingError** - A CSV reading error.
- **CSVWritingError** - A CSV writing error.
- **ColumnDecodingError** - A column decoding error.
- **ColumnEncodingError** - A column encoding error.
- **SFrameReadingError** - An error when reading a Turi Create scalable data frame.

### Supporting Types
- **Order** - A type that represents a sort ordering.
- **ColumnID** - A column identifier that stores a column's name and the type of its elements.
- **FormattingOptions** - A set of parameters that indicate how to present the contents of data frame or column types to a printable string.
- **JSONWritingOptions** - A set of JSON file-reading options.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TabularData)*