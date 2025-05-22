---
marp: true
theme: default
_class: lead
paginate: true
backgroundColor: #fff
style: |
  section {
    font-size: 20px;
  }
  section h2 {
    position: fixed;
    top: 10px;
    left: 0;
    width: 100%;
    text-align: center;
    background-color: #fff;
    padding: 10px 0;
    z-index: 10;
    border-bottom: 1px solid #ddd;
  }
  section {
    padding-top: 60px;
  }
---
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.svg') --->

# :snake: Python 201

---

## Content  
_A quick overview of what we’ll cover today_
- **1. Python Data Model:** How Python’s object system works under the hood  
- **2. Sequence Types & Operations:** Detailed behaviors of lists, tuples, ranges  
- **3. Dictionaries & Sets:** Best practices and advanced patterns  
- **4. Text vs. Bytes:** Unicode, encoding, decoding pitfalls  
- **5. Data Class Builders:** Namedtuples vs dataclasses, tips & tricks  
- **6. Object References & Memory:** Reference semantics, GC, profiling  
- **Q&A & Challenge:** Hands-on exercise to reinforce learning

---

## Python Data Model — Why It Matters  

_Understand objects to write truly “Pythonic” code_  
- **Identity, Type, Value:** Every object has a unique `id()`, a class `type()`, and stored data.  
- **Variables as References:** Names point to objects—assigning copies labels, not data.  
- **Protocols & Duck-Typing:** Implement methods like `__len__`, `__iter__` to plug into built-in behaviors.  
- **Mutable vs Immutable:** Knowing which types change in-place vs create new instances avoids subtle bugs.  
- **Benefits:** Custom classes behave like built-ins—iterate, slice, combine, format seamlessly.  

---

## Python Data Model — Identity, Type & Value 

_Show how Python tracks and distinguishes every object_  
- **Identity (`id(obj)`):** Constant during object lifetime; CPython often uses memory addresses.  
- **Type (`type(obj)`):** Determines valid operations—e.g., lists support `.append()`, ints support arithmetic.  
- **Value:** The actual data held (e.g., numbers, sequences, mappings).  
- **Alias Example:**  
  ```python
  a = [1,2,3]
  b = a         # both names reference same list
  b.append(4)
  print(a)      # [1,2,3,4]
  ```
> :bulb: **Tip:**  Use `is` for identity checks, `==` for value equality.

---

## Python Data Model — Special (Dunder) Methods

_Control how your objects integrate with Python syntax_

- **Construction & Representation:**
  - `__new__` / `__init__` for creation
  - `__repr__` returns unambiguous string, `__str__` for user-friendly output
- **Container Protocols:**
  - `__len__` → len(obj)
  - `__getitem__` → indexing & slicing
  - `__iter__` → `for x in obj` loops
  - `__contains__` → `x in obj` checks
- **Numeric & Arithmetic:**
  - `__add__`, `__radd__`, `__iadd__` for `+`, reversed and in-place ops
- **Context Managers:**
  - `__enter__`, `__exit__` for with blocks—ensure cleanup

---

## Python Data Model — Emulating Built-Ins — Card Deck Example

_Demonstrate sequence protocol in a real class_

- **Purpose:** Treat a custom deck like a Python list of cards.

```python
class FrenchDeck:
    ranks = [*map(str, range(2,11)), *'JQKA']
    suits = '♣ ♦ ♥ ♠'.split()
    def __len__(self): return 52
    def __getitem__(self, idx):
        suit = idx // 13 if type(idx)
        rank = idx % 13
        return f"{self.ranks[rank]}{self.suits[suit]}"

deck = FrenchDeck()
```
- `__len__`: Get length of the deck
- ` __getitem__`: Calculate suit & rank from index. Support positive/negative indices, slicing automatically
- **Features Gained:** `len(deck)`, `deck[10]`, `for card in deck`, `random.choice(deck)`

---

## Python Data Model — Numeric Types & Operator Overloading

_Learn how to make classes support `+`, `*`, etc._

- `__add__`: Return new instance for `a + b`.
- `__radd__`: Handle reversed operand `b + a`.
- `__iadd__`: In-place addition for performance when mutability is desired.
- **Example – 2D Vector:**
```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __radd__(self, other):
        return self.__add__(other)  # Reuse __add__
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
```
> :bulb: **Tip:** If class is immutable, skip `__iadd__` to avoid confusion.

---

##  Python Data Model — Context Managers & with Protocol

_Make resource management safer and clearer_

- __enter__: Setup—open file, acquire lock, start timer.
- __exit__: Teardown—close file, release lock, print elapsed time; handles exceptions.
- **Built-In Example:**
```python
with open('data.txt','r', encoding='utf-8') as f:
    data = f.read()
```
- **Custom Timer:**
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Elapsed:", time.time() - self.start)
```
> :bulb: **Tip:** Always use `with` for files, locks, network connections—prevents leaks.

---

## Sequence Types & Operations — Detailed

_Explore capabilities of lists, tuples, ranges_

- List vs Tuple vs Range:
  - List: mutable, dynamic size, rich methods (`append`, `extend`, `pop`).
  - Tuple: immutable, fixed-size, lighter memory footprint.
  - Range: immutable integer sequence, lazy evaluation, ideal for loops.
- Indexing & Negative Indices: Access from end with `-1, -2`.
- Slicing & Steps: Jump elements: `seq[start:stop:step]`.
- Concatenation (`+`) & Repetition (`*`): New sequence creation—avoid inside loops for large lists.
- Membership (`in`): O(n) for lists, O(1) for sets—choose structure accordingly.

---

## Sequence Types & Operations — List Comprehensions & Generator Expressions

_Transform and filter data with concise syntax_

- **List Comprehension:**
```python
squares = [x*x for x in range(10) if x%2==0]
```
- **Generator Expression:**
```python
squares_gen = (x*x for x in range(10))
```
- **Advantages:**
  - **List comps:** readable, fast for small to medium data.
  - **Gen exps:** lazy, memory-efficient for large streams.

> :bulb: **Tip:** When dealing with large files use Gen exps to avoid loading the entire file.

---

## Sequence Types & Operations — Unpacking & Extended Unpacking

_Write clearer code when extracting values_

- Basic Unpacking: `a, b, c = seq`
- Starred Unpacking:
```python
first, *middle, last = seq
```
- Function Calls: Pass list/dict elements as args:
```python
def f(a,b,c): ...
args = [1, 2, 3]
f(*args)
```
- Dict Merge:
```python
merged = {**d1, **d2}
```

---

## Sequence Types & Operations — Slicing & In-Place Assignment

_Modify subsections of lists directly_

- Slice Object:
```python
s = slice(1, 5, 2)
seq[s]
```
- Assign to Slice:
```python
lst[2:5] = [8,9]   # changes length if needed
```
- Pitfalls:
  - Length mismatch → ValueError.
  - Overlapping slices can behave unexpectedly—test carefully.
 
> :bulb: **Tip:** Encapsulate complex slicing logic in helper functions for maintainability.

---

## Sequence Types & Operations — Specialized Sequence Types

_Choose optimal structures for performance_

- `array.array`: Homogeneous C-style arrays; lower memory, faster numeric ops.
- `collections.deque`: Efficient O(1) appends/pops at both ends—ideal queue.
- `memoryview`: Zero-copy slices of binary data—great for large buffers.
- Use Case Example:
  - `deque` for task scheduling in a web server.
  - `memoryview` for slicing huge image buffers without copying.


---

## Dictionaries & Sets — Fundamentals

_Fundamental mapping and unique-collection types_

- dict: Unordered map (3.7+ preserves insertion order), O(1) avg lookup.
- Key Requirements: Hashable (immutable)—strings, numbers, tuples.
- set: Unordered unique items, O(1) membership, ideal for de-duplication.
- frozenset: Immutable set—can be used as dict key or inside other sets.

---

## Dictionaries & Sets — `dict` Core Operations & Patterns

_Beyond basic get/set—advanced techniques_

- Access & Default:
  - d.get(key, default) avoids KeyError.
  - d.setdefault(key, default) initializes missing key.
- Merge & Update:
  - d.update(other)
  - Python 3.9+: d |= other
- Iteration Patterns:
  - for k,v in d.items(): …
  - Comprehension: {k: v*2 for k,v in d.items() if v>0}

> :bulb: **Tip:** You can also use `dict` object as simple cache.

---

## Dictionaries & Sets — Specialized Mappings — defaultdict & Counter

_Powerful tools for common patterns_

- `collections.defaultdict`:
```python
from collections import defaultdict

dd = defaultdict(int)
dd['hits'] += 1  # starts from 0 automatically
```
- `collections.Counter`:
```python
from collections import Counter

cnt = Counter(['a','b','a'])
cnt.most_common(n) # most common n items
```

> **Use Case:** Word frequency analysis, inventory counting.

---

## Dictionaries & Sets — Set Operations & Use Cases

_Leverage mathematical set operations for clarity_

- **Core Ops:**
  - Union: `s | t`
  - Intersection: `s & t`
  - Difference: `s - t`
  - Symmetric Difference: `s ^ t`
- Methods: `add()`, `remove()`, `discard()`, `pop()`.

> **Use Case:** Feature flags, permissions, unique item tracking.

---

## Text vs. Bytes — Text (`str`) Internals & Unicode

_Work confidently with global text data_

- **`str` as Unicode**: Python `str` represents text as a sequence of Unicode code points, not raw bytes.
- **Code Point vs Grapheme**: 
  - Code Point: A single Unicode unit (e.g., `U+0061` for "a").
  - Grapheme: A visible character, which may combine multiple code points (e.g., emojis or accented letters).
- **Normalization**: Ensures consistent representation of text.
  - **NFC**: Combines characters into a single composed form.
  - **NFD**: Decomposes characters into base form + combining marks.
  ```python
  import unicodedata
  text = "e\u0301"  # "e" + combining accent
  normalized = unicodedata.normalize('NFC', text)
  print(normalized)  # Outputs: "é"
  ```
- **Sorting & Comparison**: Use `locale.strxfrm()` for culturally correct ordering.
  - Sorting and comparing text can vary based on cultural or linguistic rules. For example: In English, `"a" < "b"`. In German, "ä" might be treated as "ae" or sorted differently.
  ```python
  import locale
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
  sorted_words = sorted(words, key=locale.strxfrm)
  ```
> :bulb: **Tip**: Normalize text before comparison or storage to avoid subtle bugs.

---

## Text vs. Bytes — Bytes & Binary Data Handling

_Manage raw data for files, networks, images_

- `bytes` vs `bytearray`: Immutable vs mutable sequences of ints 0–255.
- Indexing: `b[i]` → int; `str[i]` → one-char string.
- **File I/O**:
```python
with open('image.png','rb') as f:
    header = f.read(8)
```
> **Use Case:** Building binary messages for sockets or serial devices.

---

## Text vs. Bytes — Encoding & Decoding Best Practices

Avoid common pitfalls in text–binary conversions

Specify Encoding: Always pass encoding='utf-8' to open().

Handle BOM: Use encoding='utf-8-sig' to strip BOM automatically.

Error Modes:

    errors='strict' (default)

    errors='ignore' or 'replace' for resilience.

Pipeline Example: Ingest files from various locales, normalize to UTF-8.

---

## Data Class Builders — Introduction

Simplify data containers with minimal code

Options:

    collections.namedtuple (immutable, index+attr access)

    typing.NamedTuple (class syntax, type hints)

    @dataclass (mutable by default, rich customization)

Benefits: Automatic __init__, __repr__, __eq__.

---

## Data Class Builders — Namedtuple vs NamedTuple vs Dataclass

_Choose the right builder for your use case_

| Feature           | namedtuple       | typing.NamedTuple | @dataclass     |
| ----------------- | ---------------- | ----------------- | -------------- |
| Syntax            | Factory function | Class definition  | Decorator      |
| Mutability        | Immutable        | Immutable         | Mutable/frozen |
| Type Hints        | No               | Yes               | Yes            |
| Default Values    | No               | Yes               | Yes            |
| Per-instance dict | No               | No                | Optional       |

---

## Data Class Builders — Dataclass Deep Dive & Tips

Uncover advanced dataclass features

    frozen=True: Immutable instances—good for hashable records.

    order=True: Auto-generate comparison methods (<, >, etc.).

    field(default_factory=…): Provide new mutable defaults per instance.

    __post_init__: Hook for validation or derived fields.

---

## Object References & Memory — Copying

_Control shared state and avoid hidden bugs_

Alias vs Copy:
    Alias: b = a
    Shallow Copy: b = a[:] or copy.copy(a)
    Deep Copy: b = copy.deepcopy(a)

Pitfall: Shallow copy shares nested objects—modifying inner lists affects both.

Tip: Prefer immutable structures or explicit copies when isolation is needed.

---

## Object References & Memory — Garbage Collection & Memory Management

_See how Python keeps memory healthy_

- Reference Counting: Immediate deallocation when count → 0.
- Cyclic GC: Finds and frees unreachable cycles periodically—configurable via gc module.
- Resource Cleanup: Always use with or explicit close() for files, sockets.
- Memory Leak Warning: Retaining global references or large caches can exhaust memory.

---

## Object References & Memory — Profiling & Optimization Techniques

_Find and fix performance bottlenecks_

sys.getsizeof(obj): Inspect memory footprint of objects.

tracemalloc: Trace and compare memory allocations over time.

timeit Module: Benchmark small code snippets accurately.

Best Practices:

    Choose efficient data types (deque vs list, set vs list membership).

    Avoid repeated concatenation in loops—use list builders or join().

---

## Recap & Key Takeaways

Summarize actionable insights

Leverage Python Protocols: Implement dunder methods for seamless integration.

Pick Right Structures: Match mutability and performance needs.

Handle Text vs Bytes Explicitly: Avoid silent errors—specify encoding modes.

Use Data Class Builders: Reduce boilerplate, enforce structure.

Understand References & GC: Prevent subtle bugs and memory issues.

---

## Further Resources

Guide your continued learning

Books:

    “Fluent Python” (Ramalho) Chapters 1–6

    “Effective Python” (Brett Slatkin) Tips on data model & performance

Documentation:

    Official Python Docs: Data Model, Collections, Dataclasses, gc

    PEPs: 8 (Style), 20 (Zen of Python), 484 (Type Hints)

Tools: REPL introspection (help(), dir()), pydoc, IPython

---

## Q&A & Hands-On Challenge

End with practice to solidify concepts

Challenge:

    Implement a ring buffer class supporting sequence protocol and context manager.

    Use @dataclass for configuration, support len(), indexing, iteration.

Next Steps:

    Build small scripts using each concept.

    Profile memory/CPU and refine your design.