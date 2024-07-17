from Exceptions import OneDArrayError, MoreThanTwoDArrayError
import itertools

class TwoDArrayTool:
    def __init__(self, arr):
        print("TwoDArrayTool initialized")
        self.arr = arr
        self.checkIfTwoDArray()

    def checkIfTwoDArray(self):
        for array in self.arr:
            if not isinstance(array, list):
                raise OneDArrayError()
            for item in array:
                if isinstance(item, list):
                    raise MoreThanTwoDArrayError()
                
        print("Array is a 2D array")

    def getRowCount(self, array=None):
        array = self.checkIfArrayNone(array)
        return len(array)
    
    def flattenArray(self, inputArray):
        try:
            return list(itertools.chain(*inputArray))
        except TypeError:
            pass
        return inputArray

    def getItemCount(self):
        return len(list(itertools.chain(*self.arr)))
    
    def getItemCountPerRow(self, array=None):
        array = self.checkIfArrayNone(array)
        return [len(row) for row in array]
    
    def checkInitialRowCol(self, row, col):
        if row < 0 or row >= self.getRowCount():
            raise IndexError("Initial row index out of range")
        if col < 0 or col >= self.getItemCountPerRow()[row]:
            raise IndexError("Initial column index out of range")
        
    def getAllDataTypeCount(self):
        dataTypes = {}
        for row in self.arr:
            for item in row:
                if type(item).__name__ in dataTypes:
                    dataTypes[type(item).__name__] += 1
                else:
                    dataTypes[type(item).__name__] = 1
        return dataTypes
    
    def get1DAdjacentCol(self, row, col, topLength=1, bottomLength=1):
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
        self.checkInitialRowCol(row, col)

        leftMostItem = col - leftLength
        rightMostItem = col + rightLength

        if leftMostItem < 0:
            raise IndexError("You cannot get an item whose index is less than 0")
        if rightMostItem >= self.getItemCountPerRow()[row]:
            raise IndexError("You cannot get an item whose index is more than the length of the row")

        return self.arr[row][leftMostItem:rightMostItem + 1]
    
    def check2DPerimeter(self, row, col, perimeter, array):
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
        wholeList = []
        for row in self.arr:
            dataTypes = {}
            for item in row:
                if type(item).__name__ in dataTypes:
                    dataTypes[type(item).__name__] += 1
                else:
                    dataTypes[type(item).__name__] = 1
            wholeList.append(dataTypes)
        return wholeList
    
    def checkIfArrayNone(self, array):
        if array is None:
            return self.arr
        return array
    
    def getNumberTotal(self, array=None):
        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, (int, float))])
    
    def getIntegerTotal(self, array=None):
        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, int)])
    
    def getFloatTotal(self, array=None):
        array = self.checkIfArrayNone(array)
        flatArray = self.flattenArray(array)
        return sum([item for item in flatArray if isinstance(item, float)])
    
    def getRowAdjacentPerimeterStrings(self, row, col, perimeter=1, array=None):
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