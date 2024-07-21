from TwoDArrayTool import TwoDArrayTool as at
import sys

arrays = [
    [0, 1, 2, 4, 4, 5, 2, 2, 5],
    [3, 4, 5, 4, 5],
    [6, 7, 8, 7.4, 3],
    [9, 10, 11, 4, 1, 2],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    [True, None],
    [3.4, "nah", "b", "o", "i", 0.3, 0.4, 0.5, 0.6, 0.7],
    ["fff", True, "f", "a", "d"],
    ]

arrays2 = [
    [0, 1, 2, 4, 4, 5, 2, 2, 5],
    [3, 4, 5, 4, 5],
    [6, 7, 8, 7.4, 3],
    [9, 10, 11, 4, 1, 2],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
]

# arrays = None

def main():

    tool1 = at(arrays)

    # tool1.addArray()
    # tool1.setPrimaryArray()

    adjacentStrings = tool1.advancedColumnRolling(1, 3, skipEmpty=False)

    # dataTypes = tool1.getDataTypeCount()
    # print("Data Types", dataTypes)

    # finalList = tool1.get1DAdjacentRow(row=3, col=3, leftLength=5, rightLength=20)
    # print("Final List", *finalList, sep="\n")

    sys.exit()

if __name__ == "__main__":
    main()