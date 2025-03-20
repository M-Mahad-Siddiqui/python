Sure! Let's go through the common data structures in Python: **Tuple**, **Set**, **Collection (collections module)**, **Dictionary**, **String**, and others. I'll explain each one with details and examples.

### 1. **Tuple**

A **tuple** is an ordered collection of items. Unlike lists, tuples are **immutable**, meaning once a tuple is created, you cannot modify it (i.e., no changing, adding, or removing items). Tuples are defined using parentheses `()`.

#### Key Points:
- **Ordered**: Elements have a defined order.
- **Immutable**: Cannot be changed after creation.
- **Allows duplicates**: Multiple occurrences of the same element are allowed.
- **Heterogeneous**: Elements can be of different data types.

#### Syntax:
```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)
```

#### Example:
```python
# Tuple example
colors = ("red", "green", "blue")
print(colors[1])  # Output: green
```

---

### 2. **Set**

A **set** is an unordered collection of unique items. Sets are defined using curly braces `{}` or the `set()` constructor.

#### Key Points:
- **Unordered**: The elements have no index.
- **No duplicates**: A set only keeps unique elements.
- **Mutable**: You can add or remove elements.

#### Syntax:
```python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(3)

# Checking membership
print(2 in my_set)  # Output: True
```

#### Example:
```python
# Set example
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}
```

---

### 3. **Collections (from the `collections` module)**

The **collections** module provides specialized container datatypes, such as `Counter`, `deque`, `OrderedDict`, and `defaultdict`, which are useful for certain types of problems.

#### a) `Counter`
- Counts the frequency of elements in a collection (e.g., list, string).

```python
from collections import Counter
my_list = [1, 2, 2, 3, 3, 3, 4]
counter = Counter(my_list)
print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1, 4: 1})
```

#### b) `deque`
- A double-ended queue that allows appending and popping elements from both ends.

```python
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # Output: deque([0, 1, 2, 3, 4])
```

#### c) `OrderedDict`
- A dictionary that remembers the order of elements.

```python
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

#### d) `defaultdict`
- A dictionary that returns a default value if a key doesn't exist.

```python
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
print(d['b'])  # Output: 0 (default value)
```

---

### 4. **Dictionary**

A **dictionary** is an unordered collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable.

#### Key Points:
- **Unordered**: No index, but the keys are unique.
- **Mutable**: You can change, add, or remove items.
- **Key-value pairs**: Each item is a pair consisting of a key and a value.

#### Syntax:
```python
# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Accessing elements
print(my_dict["name"])  # Output: John

# Adding an item
my_dict["country"] = "USA"

# Removing an item
del my_dict["age"]
```

#### Example:
```python
# Dictionary example
person = {"name": "Alice", "age": 30, "city": "London"}
print(person["name"])  # Output: Alice
```

---

### 5. **String**

A **string** is an immutable sequence of characters. You can perform various operations like slicing, concatenation, and more.

#### Key Points:
- **Immutable**: Strings cannot be modified after creation.
- **Sequence**: You can access individual characters using indices.
- **Supports a variety of methods**: Like `upper()`, `lower()`, `replace()`, etc.

#### Syntax:
```python
# Creating a string
my_string = "Hello, World!"

# Accessing characters
print(my_string[0])  # Output: H

# String methods
print(my_string.upper())  # Output: HELLO, WORLD!
```

#### Example:
```python
# String example
greeting = "Hello, Python!"
print(greeting.lower())  # Output: hello, python!
```

---

### 6. **List**

A **list** is an ordered collection of items that is **mutable**. Lists can hold items of any data type and support indexing, slicing, and a variety of methods.

#### Key Points:
- **Ordered**: Elements have a defined order.
- **Mutable**: You can modify, add, or remove items.
- **Allows duplicates**: Lists can contain duplicate elements.

#### Syntax:
```python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying an element
my_list[2] = 10

# Adding an item
my_list.append(6)

# Removing an item
my_list.remove(4)
```

#### Example:
```python
# List example
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
```

---

### 7. **Array**

An **array** is a collection of items of the same type. In Python, you typically use the `array` module for arrays, but most of the time, **lists** serve the same purpose.

#### Key Points:
- **Homogeneous**: All elements must be of the same type.
- **Mutable**: You can modify arrays after creation.

#### Syntax:
```python
import array
arr = array.array('i', [1, 2, 3, 4])
print(arr[1])  # Output: 2
```

#### Example:
```python
# Array example
import array
arr = array.array('d', [1.5, 2.5, 3.5])
arr.append(4.5)
print(arr)  # Output: array('d', [1.5, 2.5, 3.5, 4.5])
```

---

### Summary of Data Structures:

| Data Structure | Characteristics                                | Syntax Example                                |
|----------------|-------------------------------------------------|----------------------------------------------|
| **Tuple**      | Immutable, Ordered, Allows duplicates           | `my_tuple = (1, 2, 3)`                       |
| **Set**        | Unordered, No duplicates, Mutable               | `my_set = {1, 2, 3}`                         |
| **Dictionary** | Unordered, Key-value pairs, Mutable             | `my_dict = {"name": "John", "age": 25}`      |
| **String**     | Immutable, Sequence of characters               | `my_string = "Hello"`                        |
| **List**       | Ordered, Mutable, Allows duplicates             | `my_list = [1, 2, 3]`                        |
| **Array**      | Homogeneous, Mutable                            | `import array; arr = array.array('i', [1, 2])` |
| **Collections**| Specialized containers (Counter, deque, etc.)   | `from collections import Counter`            |

These are the fundamental data structures in Python. Each has its own advantages, depending on the specific problem you're solving. Let me know if you'd like more detailed examples or specific use cases!