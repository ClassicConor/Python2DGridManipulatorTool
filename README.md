# TwoDArrayTool: A Python Class for 2D Array Operations

(README.md created with Claude 3.5 Sonnet)

## Overview

TwoDArrayTool is a Python class designed to perform various operations on 2D arrays (lists of lists). It provides methods for array manipulation, data analysis, and element retrieval. The class is useful for tasks involving matrices or grid-like data structures.

Key features:
- Initialize with a custom 2D array or use a default 3x3 array
- Store and manage multiple arrays
- Perform operations like flattening, data type counting, and element adjacency checks
- Advanced operations such as column rolling

## Usage

To use the TwoDArrayTool, first initialize an instance:

```python
tool = TwoDArrayTool()  # Uses default 3x3 array
# or
custom_array = [[1, 2], [3, 4], [5, 6]]
tool = TwoDArrayTool(custom_array)
```

Then, you can call various methods on the tool instance to perform operations on the array(s).

## Methods

This introduction provides context for the class, explains its purpose, and gives a brief example of how to initialize it. You can place this section at the beginning of the document, followed by the list of methods and their descriptions.



# TwoDArrayTool Methods

- `printMainArray()`: Prints the main array.

```python
  tool.printMainArray()
  # [1, 2, 3]
  # [4, 5, 6]
  # [7, 8, 9]
```

- `viewArrays()`: Displays all saved arrays.

- `getArrays()`: Returns list of saved arrays.

- `addArray(array)`: Adds new array to saved arrays.

```python
tool.addArray([[1, 2], [3, 4]])
```

- `removeArray()`: Removes array from saved arrays (prompts for input).

- `setPrimaryArray()`: Changes primary array to a saved array (prompts for input).

- `getRowCount(array=None)`: Returns number of rows.
  ```python
  tool.getRowCount()  # 3
  ```

- `flattenArray(array=None)`: Flattens 2D array to 1D.
  ```python
  tool.flattenArray()  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

- `getItemCount(array=None)`: Returns total item count.
  ```python
  tool.getItemCount()  # 9
  ```

- `getItemCountPerRow(array=None)`: Returns items per row.
  ```python
  tool.getItemCountPerRow()  # [3, 3, 3]
  ```

- `getAllDataTypeCount(array=None)`: Counts data types in array.
  ```python
  tool.getAllDataTypeCount()  # {'int': 9}
  ```

- `get1DAdjacentColumn(row, col, topLength, bottomLength, array=None)`: Gets adjacent column items.
  ```python
  tool.get1DAdjacentColumn(1, 1, 1, 1)  # [2, 5, 8]
  ```

- `get1DAdjacentRow(row, col, leftLength, rightLength, array=None)`: Gets adjacent row items.
  ```python
  tool.get1DAdjacentRow(1, 1, 1, 1)  # [4, 5, 6]
  ```

- `get2DAdjacent(row, col, perimeter, array=None)`: Gets 2D adjacent items.
  ```python
  tool.get2DAdjacent(1, 1, 1)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

- `getDataTypeCountPerRow(array=None)`: Counts data types per row.
  ```python
  tool.getDataTypeCountPerRow()  # [{'int': 3}, {'int': 3}, {'int': 3}]
  ```

- `getNumberTotal(array=None)`: Sums all numbers.
  ```python
  tool.getNumberTotal()  # 45
  ```

- `getIntegerTotal(array=None)`: Sums integers.
  ```python
  tool.getIntegerTotal()  # 45
  ```

- `getFloatTotal(array=None)`: Sums floats.
  ```python
  tool.getFloatTotal()  # 0 (no floats in default array)
  ```

- `getRowAdjacentPerimeterStrings(row, col, perimeter, array=None)`: Gets adjacent strings in row.

- `advancedColumnRolling(amount, column, array=None, skipEmpty=True)`: Rolls specified column.
  ```python
  tool.advancedColumnRolling(1, 1)
  # [[1, 8, 3], [4, 2, 6], [7, 5, 9]]
  ```

This overview covers all the public methods of the TwoDArrayTool class, providing a brief description and a small example for each where applicable.
