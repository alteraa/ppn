---
marp: true
# theme: default
theme: rose-pine
title: Let's Get Rusty!
# class:
#   - lead
#   - invert 
paginate: true
style: |
  section {
    font-size: 20px;
    padding-top: 60px;
  }
  section h3 {
    position: fixed;
    top: 10px;
    left: 30px;
    width: 100%;
    padding: 10px 0;
    z-index: 1;
  }
  header {
    z-index: 2;
    width: 95%;
    text-align: right;
  }

---

<!-- _paginate: false -->
<!-- footer: 05.12.2025 -->
<!-- header: :crab: Let's Get Rusty! -->

# :crab: Let's Get Rusty!


---

`let` introduces a variable binding:
```rust
let x; // declare "x"
x = 42; // assign 42 to "x"
```

This can be written as a single line:
```rust
let x = 42;
```

---

Semi-colon marks the end of a statement:
```rust
let x = 42; // statement 1
let y = 17; // statement 2
```

---

Types can be annotated:
```rust
let x: i32;
x = 42;
```

This can also be written as a single line:
```rust
let x: i32 = 42;
```

> You can just use `i32` for everything.

---

You **can't access** uninitializse variables:
```rust
let x;
foo(x);
// error: use of possibly-uninitialized variable "x"
```

However, doing this is completely fine:
```rust
let x;
x = 42;
foo(x);
```

---

This **does nothing** because 42 is a constant: 
```rust
let _ = 42;
```

This calls `foo` but throws away its result: 
```rust
let _ = foo();
```

---

You can assign pairs like `tuple`:
```rust
let pair = ('a', 17);
pair.0; // 'a'
pair.1; // 17
```

Or, with type annotation:
```rust
let pair: (char, i32) = ('a', 17);
```

---

With `assert!` you can check conditions at runtime:
```rust
let (a, b) = ('a', 17);
assert!(a, 'a'); // passes
assert!(b, 17); // passes
assert!(b, 42); // panics!
```

---

Functions are defined with `fn`. This is a void function:
```rust
fn greet() {
    println!("Hello, world!");
}
```

This a integer (*i32*) function:
```rust
fn add(x: i32, y: i32) -> i32 {
    x + y
}
```

> In Rust, the **last expression is the return value**. No `return` keyword is needed. But you can use it if you want to.

---

There is also interior variables:
```rust
let x = "out";
{
    let x = "in";
    println!("{}", x); // prints "in"
}
```

---

This:
```rust
let x = 42;
```

is equivalent to this:
```rust
let x = { 42 };
```
> Blocks are expressions in Rust.

---

This means that the right-hand side can be any expression.
```rust
let x = {
  let y = 1;
  let z = 2;
  y + z
}
println!("{}", x); // prints 3
```

---

If conditions are also expressions:
```rust
fn foo() -> i32 {
    if true {
        42
    } else {
        17
    }
}
```
---

Dots are typically used to access fields or methods:
```rust
let name = "Rusty";
name.len(); // calls the "len" method
```

---

Double colon is used to access associated functions or constants:
```rust
let least = std::cmp::min(1, 2); // calls the "min" function
```

Approximately:
```
crate::file::function
```

- `crate` is the package (library)
- `file` is the module (file)
- `function` is the function name

---

`use` import the namespaces:
```rust
use std::cmp::min;

let least = min(1, 2); // calls the "min" function
```

> Rust has strict use rules. You must import everything you use.
---

Types are namespaces too:
```rust
let x = str::len("Rusty"); // calls the "len" function
```

- `str` is the type (string)
- `len` is the function name

---

Structs are declared with `struct` keyword:
```rust
struct Number {
  odd: bool,
  value: i32,
}
```

They can be initialised using literals:
```rust
let n = Number { odd: true, value: 17 };
let m = Number { odd: false, value: 42 };
```
> The order **does not matter** when initialising structs.

---

`macth` is used for pattern matching:
```rust
match n.value {
  1 => println!("one"),
  2 => println!("two"),
  _ => println!("{}", n.value),
}
```

> `_` is the wildcard pattern that matches anything.

---

You can declare methods on a struct using `impl`:
```rust
impl Number {
  fn is_odd(&self) -> bool {
    self.odd
  }
}
```

You can call methods using dot notation:
```rust
n.is_odd(); // returns true
```

> `&self` is similar to `self` in Python or `this` in C++/Java. It refers to the instance the method is called on.


---

Variable binding is immutable by default:
```rust
let x = 42;
x = 17; // error: cannot assign twice to immutable variable "x"
```

`mut` makes a variable mutable:
```rust
let mut x = 42;
x = 17; // ok
```

> Most languages **have mutable variables** by default. **Rust is opposite.**
> This helps to **avoid accidental mutations** and makes reasoning about code easier.

---

Functions can be generic:
```rust
fn identity<T>(x: T) -> T {
    x
}
```

Structs can be generic too:
```rust
struct Pair<T, U> {
    first: T,
    second: U,
}
```

---

Standard library type `Vec` is a growable array:
```rust
let mut v1 = Vec::new();
v1.push(1);
let mut v2 = Vec::new();
v2.push(false);
// v1 == Vec<i32>
// v2 == Vec<bool>

```

You can also use `vec!` macro to create vectors:
```rust
let v = vec![1, 2, 3, 4, 5];
```

---

Macros are invoked with `!`:
```rust
println!("Hello, world!");
let v = vec![1, 2, 3];
```

> Macros run at compile-time and can generate code. They act like functions but are more powerful.
> In other words, macros are **code that writes code**.

---

`panic!` is an also macro that stops execution:
```rust
panic!("Something went wrong!");
```

---

`enum` defines a type that can be one of several variants:
```rust
enum Color {
    Red,
    Green,
    Blue,
}
let c = Color::Red;
```

---

`Option` is an enum that represents a value that can be present or absent:
```rust
enum Option<T> {
    None,
    Some(T),
}
```

You can use it like this:
```rust
let x: Option<i32> = Some(42);
let y: Option<i32> = None;
```

> Option represents nullable values in a safe way.

---

`unwrap` extracts the value from an `Option`, panicking if it's `None`:
```rust
let x: Option<i32> = Some(42);
let y: i32 = x.unwrap(); // y == 42
```

> If `x` was `None`, this would panic.

---

`Result` is an enum that represents either success or error:
```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

You can use it like this:
```rust
let x: Result<i32, &str> = Ok(42);
let y: Result<i32, &str> = Err("Something went wrong");
```

> Result is used for error handling in Rust.

---

Iterators be like in Rust:
```rust
let natural_numbers = 1..; // infinite iterator of natural numbers
```

> Iterators are lazy and can represent infinite sequences.

---

Arrangements can be created from iterators:
```rust
// 0 or greater
(0..).contains(5); // true
(0..).contains(-1); // false
(3..6).contains(5); // true
(3..6).contains(2); // false
```

---

`for` loops iterate over iterators:
```rust
for n in 1..5 {
    println!("{}", n); // prints 1, 2, 3, 4
}
```

You can also iterate over collections:
```rust
let v = vec![10, 20, 30];
for x in v {
    println!("{}", x); // prints 10, 20, 30
}
```

or even strings:
```rust
for c in "Rusty".chars() {
    println!("{}", c); // prints 'R', 'u', 's', 't', 'y'
}
```

---

You can use `||` to provide a closure (anonymous function):
```rust
let squares: Vec<i32> = (1..5).map(|x| x * x).collect();
// squares == vec![1, 4, 9, 16]
```

You can chain multiple iterator adapters:
```rust
let evens: Vec<i32> = (1..10)
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .collect();
// evens == vec![4, 16, 36, 64, 100]
```

---

Writing Rust is different than reading Rust. Practice is key!
