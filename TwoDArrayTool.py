from Exceptions import OneDArrayError, MoreThanTwoDArrayError
import itertools

class TwoDArrayTool:

    """A class to represent a 2D array tool."""

    def __init__(self, arr):
        print("TwoDArrayTool initialized")
        self.arr = arr
        self.checkIfTwoDArray()
        self.savedArrays = [self.arr]

    def checkIfTwoDArray(self):
        """Check if the array is a 2D array"""
        for array in self.arr:
            if not isinstance(array, list):
                raise OneDArrayError()
            for item in array:
                if isinstance(item, list):
                    raise MoreThanTwoDArrayError()
        print("Array is a 2D array")

    def viewArrays(self):
        """View the arrays"""
        for i, array in enumerate(self.savedArrays):
            print(f"{i}: {array})")

    def grabArrays(self):
        """Grab the arrays"""
        return self.savedArrays

    def saveArray(self, array):
        """Save the array"""
        self.savedArrays.append(array)
        print("Array saved")

    def removeArray(self, position):
        """Remove the array"""
        self.savedArrays.pop(position)
        print("Array removed")

    def getRowCount(self, array=None):
        """Get the number of rows in the 2D array"""

        array = self.checkIfArrayNone(array)
        return len(array)

    def flattenArray(self, inputArray):
        """Flatten the 2D array"""
        try:
            return list(itertools.chain(*inputArray))
        except TypeError:
            pass
        return inputArray

    def getItemCount(self):
        """Get the number of items in the 2D array"""

        return len(list(itertools.chain(*self.arr)))
    
    def getItemCountPerRow(self, array=None):
        """Get the number of items in each row of the 2D array"""

        array = self.checkIfArrayNone(array)
        return [len(row) for row in array]
    

    def checkInitialRowCol(self, row, col):
        """Check if the initial row and column indexes are within the range of the 2D array"""

        if row < 0 or row >= self.getRowCount():
            raise IndexError("Initial row index out of range")
        if col < 0 or col >= self.getItemCountPerRow()[row]:
            raise IndexError("Initial column index out of range")
        
    def getAllDataTypeCount(self):
        """Get the count of each data type in the 2D array"""

        dataTypes = {}
        for row in self.arr:
            for item in row:
                if type(item).__name__ in dataTypes:
                    dataTypes[type(item).__name__] += 1
                else:
                    dataTypes[type(item).__name__] = 1
        return dataTypes
    
    def get1DAdjacentCol(self, row, col, topLength=1, bottomLength=1):
        """Get the adjacent items in the column of the 2D array"""

        self.checkInitialRowCol(row, col)
        topMostItem = row - topLength
        bottomMostLength = row + bottomLength

        if topMostItem < 0:
            raise IndexError("You cannot get an item whose index is less than 0")
        if bottomMostLength >= self.getRowCount():
            raise IndexError("You cannot get an item whose index is more than the number of rows")

        finalList = []

        for i in range(topMostItem, bottomMostLength + 1):
            try:
                finalList.append(self.arr[i][col])
            except IndexError:
                raise ValueError("Cannot grab an item that doesn't exist")
        return finalList

    def get1DAdjacentRow(self, row, col, leftLength=1, rightLength=1):
        """Get the adjacent items in the row of the 2D array"""

        self.checkInitialRowCol(row, col)
        leftMostItem = col - leftLength
        rightMostItem = col + rightLength

        if leftMostItem < 0:
            raise IndexError("You cannot get an item whose index is less than 0")
        if rightMostItem >= self.getItemCountPerRow()[row]:
            raise IndexError("You cannot get an item whose index is more than the length of the row")

        return self.arr[row][leftMostItem:rightMostItem + 1]
    
    def check2DPerimeter(self, row, col, perimeter, array):
        """
        Check the perimeter of the 2D array.
        If it goes outside the perimeter, raise an error.
        """

        topPosition = row - perimeter
        bottomPosition = row + perimeter
        leftPosition = col - perimeter
        rightPosition = col + perimeter
    
        if topPosition < 0:
            raise IndexError("You cannot get an item whose index is less than 0")
        if bottomPosition >= self.getRowCount(array=array):
            raise IndexError("You cannot get an item whose index is more than the number of rows")
        if leftPosition < 0:
            raise IndexError("You cannot get an item whose index is less than 0")
        if rightPosition >= self.getItemCountPerRow(array=array)[row]:
            raise IndexError("You cannot get an item whose index is more than the length of the row")
        
        return topPosition, bottomPosition, leftPosition, rightPosition
        
    def get2DAdjacent(self, row, col, perimeter=1, flat=True, array=None):
        """Get the adjacent items in the 2D array within a specified perimeter"""

        self.checkInitialRowCol(row, col)
        array = self.checkIfArrayNone(array)
        topMostItem, bottomMostItem, leftMostItem, rightMostItem = self.check2DPerimeter(row, col, perimeter, array)
        
        finalList = []
        if flat:
            for i in range(topMostItem, bottomMostItem + 1):
                for j in range(leftMostItem, rightMostItem + 1):
                    try:
                        finalList.append(self.arr[i][j])
                    except IndexError:
                        raise ValueError("Cannot grab an item that doesn't exist")
        else:
            for i in range(topMostItem, bottomMostItem + 1):
                try:
                    finalList.append(self.arr[i][leftMostItem:rightMostItem + 1])
                except IndexError:
                    raise ValueError("Cannot grab an item that doesn't exist")

        return finalList
    
    def getDataTypeCount(self, array):
        """Get the count of each data type in an array"""

        flatArray = self.flattenArray(array)
        print(flatArray)
        dataTypes = {}
        for item in flatArray:
            if type(item).__name__ in dataTypes:
                dataTypes[type(item).__name__] += 1
            else:
                dataTypes[type(item).__name__] = 1
        return dataTypes
    
    def getDataTypeCountPerRow(self):
        """Get the count of each data type in each row of the 2D array"""

        wholeList = []
        for row in self.arr:
            wholeList.append(self.getDataTypeCount(array=row))
        return wholeList
    
    def checkIfArrayNone(self, array):
        """Check if the array is None"""

        if array is None:
            return self.arr
        return array
    
    def getNumberTotal(self, array=None):
        """Get the total of all numbers in the 2D array"""
        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, (int, float))])
    
    def getIntegerTotal(self, array=None):
        """Get the total of all integers in the 2D array"""

        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, int)])
    
    def getFloatTotal(self, array=None):
        """Get the total of all floats in the 2D array"""

        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, float)])
    
    def getRowAdjacentPerimeterStrings(self, row, col, perimeter=1, array=None):
        """Get the adjacent strings in the row of the 2D array within a specified perimeter"""

        self.checkInitialRowCol(row, col)
        array = self.checkIfArrayNone(array)
        topPosition, bottomPosition, leftPosition, rightPosition = self.check2DPerimeter(row, col, perimeter, array)
        
        adjacentStrings = []

        for i in range(topPosition, bottomPosition + 1):
            j = leftPosition
            while j <= rightPosition:
                print(f"Item: {array[i][j]}")
                if isinstance(array[i][j], str):
                    j, string = self.grabWholeString(i, j, array)
                    adjacentStrings.append(string)
                else:
                    j += 1

        return adjacentStrings

    def grabWholeString(self, row, col, array):
        """Grab the whole string in the 2D array"""

        leftPointer, rightPointer = col, col
        while leftPointer > 0 and isinstance(array[row][leftPointer - 1], str):
            leftPointer -= 1
            if leftPointer == 0:
                break
            if not isinstance(array[row][leftPointer - 1], str):
                break

        while rightPointer < len(array[row]) - 1 and isinstance(array[row][rightPointer + 1], str):
            rightPointer += 1
            if rightPointer == len(array[row]) - 1:
                break
            if not isinstance(array[row][rightPointer + 1], str):
                break

        string = array[row][leftPointer:rightPointer + 1]

        return rightPointer + 1, string
    
    def advancedColumnRolling(self, amount, column, array=None, skipEmpty=True):
        """Roll the columns of the 2D array by a specified amount"""

        array = self.checkIfArrayNone(array)

        if skipEmpty:
            array = self.rollWithSkipEmpty(amount, column, array)
        else:
            array = self.rollWithoutSkipEmpty(amount, column, array)

        return array

    def rollWithSkipEmpty(self, amount, column, array):
        """
        Roll the columns of the 2D array by a specified amount.
        This method skips rows where the length is too short to perform the column rotation.
        """

        print("Array before:", *array, sep='\n')
        
        newArray = []
        valuesToChange = []
        skippedRows = []

        for row in array:
            try:
                if column >= len(row):
                    newArray.append(None)
                    skippedRows.append(row)
                else:
                    newArray.append(row)
                    valuesToChange.append(row[column])
            except IndexError:
                continue

        valuesToChange = valuesToChange[-amount:] + valuesToChange[:-amount]

        for i, row in enumerate(newArray):
            if row is None:
                newArray[i] = skippedRows.pop(0)
            else:
                newArray[i][column] = valuesToChange.pop(0)

        print("Array after", *newArray, sep='\n')

    def rollWithoutSkipEmpty(self, amount, column, array):
        """
        Roll the columns of the 2D array by a specified amount without skipping empty coordinates
        This means that if the column rotation goes beyond the length of the row, it will wrap around to the end of that next row.
        This is in contrast to the previous method where the row is skipped if the column rotation goes beyond the length of the row.
        """

        print("Array before:", *array, sep='\n')

        longestRow = max([len(row) for row in array])
        initialRowLengths = []
        savedValues = []

        for row in array:
            initialRowLengths.append(len(row))
            while len(row) < longestRow:
                row.append(None)
            savedValues.append(row[column])

        savedValues = savedValues[-amount:] + savedValues[:-amount]
        initialRowLengths = initialRowLengths[-amount:] + initialRowLengths[:-amount]

        newArray = []
        for i, row in enumerate(array):
            row[column] = savedValues[i]
            newArray.append(row)

            if initialRowLengths[i] < longestRow:
                newArray[i] = newArray[i][:initialRowLengths[i]]

        print("Array after:", *newArray, sep='\n')