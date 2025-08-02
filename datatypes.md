# 1.1 Python Basics

**Python** is a high-level, interpreted, general-purpose programming language.  
It was created by **Guido van Rossum** and **first released in 1991**.

---

## 📝 Variables

A **variable** is a name that stores data, such as a number, text, or other information, which you can use and change in your program.

## 📚 Data Types

**Data types** define the kinds of values you can store and work with in Python. Each variable in Python has a data type, which tells Python how to handle it.

---

### 🔤 Text Type

- **`str`** — for storing text (strings)
    ```
    name = "Alice"
    ```

---

### 🔢 Numeric Types

- **`int`** — whole numbers (integers)
    ```
    age = 25
    ```
- **`float`** — decimal numbers (floating point)
    ```
    height = 5.8
    ```
- **`complex`** — complex numbers
    ```
    z = 1 + 2j
    ```

---

### 📋 Sequence Types

- **`list`** — an ordered, mutable collection
    ```
    fruits = ["apple", "banana", "cherry"]
    ```
- **`tuple`** — an ordered, immutable collection
    ```
    coordinates = (10, 20)
    ```
- **`range`** — a sequence of numbers, often used in loops
    ```
    for i in range(5):  # 0, 1, 2, 3, 4
        print(i)
    ```

---

### 🗺️ Mapping Type

- **`dict`** — stores key-value pairs
    ```
    student = {"name": "Alice", "age": 21}
    ```

---

### 🔢 Set Types

- **`set`** — an unordered collection of unique items
    ```
    unique_numbers = {1, 2, 3}
    ```
- **`frozenset`** — like set, but immutable
    ```
    frozen = frozenset([1, 2,```

---

### ⚖️ Boolean Type

- **`bool`** — represents `True` or `False` (often used for logic)
    ```
    is_active = True
    ```

---

### 💾 Binary Types

- **`bytes`** — immutable sequence of bytes
    ```
    b = b"hello"
    ```
- **`bytearray`** — mutable sequence of bytes
    ```
    ba = bytearray([50,
    ```
- **`memoryview`** — a memory view object for handling buffers
    ```
    mv = memoryview(b"hello")
    ```

---

### 🚫 None Type

- **`NoneType`** — represents the absence of a value (`None`)
    ```
    nothing = None
    ```

---

> **Tip:** You can check the type of any object using the `type()` function:
> ```
> print(type(42))  # <class 'int'>
> ```

---

Happy coding!
