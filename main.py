from TwoDArrayTool import TwoDArrayTool as at
import sys

arrays = [
    [0, 1, 2, 4, 4, 5, 2, 2, 5],
    [3, 4, 5, 4, 5],
    [6, 7, 8, 7.4, 3],
    [9, 10, 11, 4, 1, 2],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    [True, None],
    [3.4, 2.1, 99.8, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
    ["fff", True],
    ]

arrays2 = [
    ["a", 2, "a", "2", "c"],
    ["a", "b", 3, 5, 1],
    ["a", "b", 0, "1", "a"],
    ["a", "b", 0, "1", "a"],
    ["a", "b", 0, "1", "a"],
]

tool1 = at(arrays2)

adjacentStrings = tool1.getRowAdjacentPerimeterStrings(2, 2, 2, arrays2)

for string in adjacentStrings:
    print(string)

sys.exit()

tool = at(arrays)

adjacentItems = tool.get2DAdjacent(2, 2, 2, flat=True)

for item in adjacentItems:
    print(item)

dataTypes = tool.getDataTypeCount(adjacentItems)

dataTypePerRow = tool.getDataTypeCountPerRow()

print(dataTypePerRow)

for i, row in enumerate(dataTypePerRow):
    for key, value in row.items():
        print(f"Row {i}:")
        print(f"{key} - {value}")
