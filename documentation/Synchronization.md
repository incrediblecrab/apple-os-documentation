# Synchronization

Build synchronization constructs using low-level, primitive operations.

**Platforms:** iOS 18.0+ | iPadOS 18.0+ | Mac Catalyst 18.0+ | macOS 15.0+ | tvOS 18.0+ | visionOS 2.0+ | watchOS 11.0+

## Topics

### Atomic Values
- **Atomic** - An atomic value
- **AtomicLazyReference** - A lazily initializable atomic strong reference
- **WordPair** - A pair of two word sized UInts
- **AtomicRepresentable** protocol - A type that supports atomic operations through a separate atomic storage representation
- **AtomicOptionalRepresentable** protocol - An atomic value that also supports atomic operations when wrapped in an Optional

### Memory Ordering Semantics
- **AtomicLoadOrdering** - Specifies the memory ordering semantics of an atomic load operation
- **AtomicStoreOrdering** - Specifies the memory ordering semantics of an atomic store operation
- **AtomicUpdateOrdering** - Specifies the memory ordering semantics of an atomic read-modify-write operation
- **atomicMemoryFence** function - Establishes a memory ordering without associating it with a particular atomic operation

### Structures
- **Mutex** - A synchronization primitive that protects shared mutable state via mutual exclusion

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Synchronization)*