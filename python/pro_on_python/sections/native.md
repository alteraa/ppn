gpt:

### 🧩 Native Extension / Binding Dosyaları

* **\*.c** → C dilinde yazılmış kaynak kod dosyalarıdır. Python ile native extension geliştirmek için kullanılır.

* **\*.cpp** → C++ dilinde yazılmış kaynak kod dosyalarıdır. Performans artırımı veya mevcut C++ kütüphanelerini Python’a bağlamak için kullanılır.

* **\*.h** → C/C++ header dosyalarıdır. Fonksiyon ve sınıf deklarasyonlarını içerir ve diğer kaynak dosyalarında include edilir.

* **\*.hpp** → C++ header dosyalarıdır. `.h` ile aynı işlevi görür, genellikle C++ projelerinde tercih edilir.

* **\*.pyx** → Cython kaynak kod dosyalarıdır. Python ile C/C++ kodunu birleştirerek performans artırımı sağlar.

* **\*.pxd** → Cython header dosyalarıdır. C fonksiyon ve yapılarını `.pyx` dosyalarına tanıtmak için kullanılır.

* **\*.pxi** → Cython include dosyalarıdır. Ortak kod parçalarını farklı `.pyx` dosyalarında paylaşmak için kullanılır.

* **\*.i** → SWIG interface dosyalarıdır. C/C++ kodunu Python’a bind etmek için kullanılır; hangi fonksiyonların ve sınıfların Python’a aktarılacağını belirler.


---

claude:

# 🧩 Native Extension / Binding Dosyaları Kategorisi

## ***.c**
C programming language source files. Python'da performance-critical operations için native C extensions yazımında kullanılır.

**Python C API:** CPython interpreter'ın C interface'i ile direct integration, manual memory management gerektirir.

**Use cases:**
- **Performance bottlenecks:** CPU-intensive algorithms, numerical computations
- **System integration:** Operating system APIs, hardware interfaces  
- **Legacy code integration:** Existing C libraries'i Python'a expose etme

**Example scenarios:** Cryptographic functions, image processing, mathematical computations, embedded systems programming.

**Compilation:** `gcc` veya `clang` ile compile edilir, Python.h header files gerektirir.

## ***.cpp**
C++ source files. Object-oriented C++ code'u Python'a integrate etmek için kullanılır.

**Modern C++ features:** STL containers, smart pointers, template programming, RAII patterns Python integration.

**pybind11 integration:** Modern C++ binding library, header-only, automatic type conversions.

**Performance advantages:** C++ compiler optimizations, template metaprogramming, zero-cost abstractions.

**Complex projects:** Game engines, scientific computing libraries, computer graphics applications.

## ***.h**
C header files. Function declarations, struct definitions, constants, macros için interface definitions.

**API definition:** C functions'ların signatures'ları, data structures'ların layouts'u.

**Include guards:** `#ifndef`, `#define`, `#endif` patterns ile multiple inclusion prevention.

**Python integration:** CPython API headers, custom extension module interfaces.

**Cross-platform:** Platform-specific code için conditional compilation macros.

## ***.hpp**
C++ header files. Class declarations, template definitions, inline functions için modern C++ interface files.

**Template programming:** Header-only libraries, compile-time computations, generic programming.

**Modern C++:** C++11/14/17/20 features, constexpr functions, concepts, ranges.

**pybind11 patterns:** Python binding definitions, automatic type deduction, STL integration.

**Header-only libraries:** Eigen, Boost.Hana gibi modern C++ mathematical libraries integration.

## ***.pyx**
**Cython** source files. Python-like syntax ile C performance achieve eden hybrid programming language.

**Cython language features:**
- **Static typing:** `cdef int x` ile C-level variable declarations
- **Function definitions:** `cpdef` (Python+C), `cdef` (C-only) functions
- **Memory management:** malloc/free, memory views, buffer protocol

**Performance bridge:** Pure Python'dan pure C'ye gradual optimization path.

**NumPy integration:** Efficient array operations, scientific computing optimization.

**Use cases:** NumPy, SciPy, pandas gibi scientific libraries'in performance-critical parts.

## ***.pxd**
Cython definition files. Cython modules arası interface definitions, C libraries için Python declarations.

**External C libraries:** C header files'ları Cython'a expose etme, function signatures mapping.

**Module interfaces:** Cython modules arası communication, public API definitions.

**Type definitions:** C structs, enums, typedefs'i Cython type system'ına mapping.

**Example:**
```cython
# math.pxd
cdef extern from "math.h":
    double sin(double x)
    double cos(double x)
```

## ***.pxi**
Cython include files. Code reuse, common definitions, macro-like functionality için include mechanism.

**Code organization:** Shared Cython code, template-like functionality, modular development.

**Include mechanism:** `include "common.pxi"` ile source code inclusion, preprocessor-style.

**Template patterns:** Generic algorithms, common data structures, utility functions.

**Maintenance:** DRY principle, code duplication elimination, centralized definitions.

## ***.i**
**SWIG (Simplified Wrapper and Interface Generator)** interface files. C/C++ libraries için automatic Python binding generation.

**Interface definition:** C++ classes, functions, variables'ı Python'a expose etme declarations.

**Multi-language:** Python, Java, C#, Ruby, Perl gibi multiple target languages.

**Legacy integration:** Existing large C/C++ codebases için comprehensive binding solution.

**SWIG directives:**
```swig
%module example
%include "std_vector.i"
%include "std_string.i"

%{
#include "example.h"
%}

%include "example.h"
```

**Automatic generation:** `swig -python -c++ example.i` ile Python wrapper code generation.

**Enterprise usage:** Large legacy systems, comprehensive API coverage, multi-language bindings requirement.

---

## 🚀 Performance & Toolchain Karşılaştırması

### Performance Spectrum Örneği
```python
# Pure Python: 100x slower
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Cython (.pyx): 10x faster  
cdef int fibonacci_cy(int n):
    if n < 2: return n
    return fibonacci_cy(n-1) + fibonacci_cy(n-2)

# Pure C (.c): 100x faster
// Hand-optimized C implementation
```

### Tool Karşılaştırma Matrisi

| Tool | Best For | Learning Curve | Performance | Modern Usage |
|------|----------|----------------|-------------|--------------|
| **.pyx (Cython)** | Scientific computing, NumPy integration | Medium | 10-50x | High |
| **.cpp + pybind11** | Modern C++ integration, STL usage | Medium | 50-100x | Very High |
| **.c (Manual)** | Maximum control, embedded systems | Hard | 100x+ | Specialized |
| **.i (SWIG)** | Legacy integration, multi-language | Hard | Variable | Legacy |

### Real-World Examples
```bash
# Scientific computing ecosystem
numpy/core/src/multiarray/     # .c files (low-level operations)
scipy/spatial/_qhull.pyx       # Cython (computational geometry)
scikit-learn/sklearn/          # Mix of .pyx, .cpp (ML algorithms)
pandas/src/                    # C++/Cython hybrid (data processing)
```

### Development Strategy
1. **Profile first:** `python -m cProfile` ile bottleneck identification
2. **Cython next:** `.pyx` ile critical loops optimization  
3. **C++ if needed:** `pybind11` ile complex algorithms
4. **Manual C last resort:** Ultimate performance requirements
