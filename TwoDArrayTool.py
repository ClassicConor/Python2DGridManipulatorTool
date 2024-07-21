import itertools

class TwoDArrayTool:
    """
    A class to represent a 2D array tool.
    """

    def __init__(self, arr=None):
        """
        Constructs all the necessary attributes for the 2D array tool object.
        Checks if the array is a 2D array. If it isn't, it raises an error.
        Adds it to the saved arrays.
        """

        print("TwoDArrayTool initialized")
        self.savedArrays = []
        is2DArray = self.__checkIfTwoDArray(arr)
        if is2DArray:
            self.arr = arr
            print("Primary array initialised")
        else:
            self.arr = self.__initialiseBasicArray()
            print("Basic array initialised.")

        self.savedArrays.append(self.arr)
        print("Primary array initialised\nArray added to saved arrays.")

    def __initialiseBasicArray(self):
        """
        Initialise a basic array
        """

        return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    def printMainArray(self):
        """
        Print the main array
        """

        print("\n".join("    " + str(row) for row in self.arr))

    def __checkIfTwoDArray(self, array=None):
        """
        Check if the array is a 2D array
        """

        if array is None:
            return None

        for row in array:
            if not isinstance(row, list):
                print("Array is not a 2D array")
                return None
            for item in row:
                if isinstance(item, list):
                    print("Array is not a 2D array")
                    return None

        print("Array is a 2D array")
        return array

    def viewArrays(self):
        """
        View the arrays
        """

        if not self.savedArrays:
            print("No arrays to view")
            return
        
        print("List of arrays:")

        for i, array in enumerate(self.savedArrays):
            if array is None:
                print("No arrays to view")
                return
            print(f"{i + 1}:")
            print("\n".join("    " + str(row) for row in array))

    def getArrays(self):
        """
        Grab the arrays
        """

        return self.savedArrays if self.savedArrays else None

    def addArray(self, array=None):
        """
        Save an array to the saved arrays
        """

        is2DArray = self.__checkIfTwoDArray(array)

        if is2DArray:
            self.savedArrays.append(array)
            print("Array saved")
        else:
            print("Array not saved")

    def removeArray(self, position=None):
        """
        Remove the array
        """

        self.viewArrays()

        while True:
            position = input("Enter the position of the array you want to remove (q to break): ")
            try:
                position = int(position)
                if position <= 0 or position > len(self.savedArrays):
                    print("Position is out of range. Please enter another number.")
                elif position > 0 and position <= len(self.savedArrays):
                    self.savedArrays.pop(position - 1)
                    print("Array removed")
                    break
            except ValueError:
                if position.lower() == 'q':
                    break
                print("Please provide a valid position")

    def setPrimaryArray(self):
        """
        Change the primary array to the array at the specified position
        """

        if self.savedArrays is None:
            print("No arrays to change primary array to")
            return
        
        print("This is currently the primary array:")
        self.printMainArray()

        print("\nList of arrays:")
        self.viewArrays()

        while True:
            position = input("Enter the position of the array you want to change the primary array to (q to quit): ")

            try:
                position = int(position)
                if position <= 0 or position > len(self.savedArrays):
                    print("Position is out of range")
                elif position > 0 and position <= len(self.savedArrays):
                    self.arr = self.savedArrays[position - 1]
                    print("Primary array changed")
                    break
            except ValueError:
                if position.lower() == 'q':
                    break
                print("Please provide a valid position")

        self.printMainArray()

    def __checkIfArrayNone(self, array):
        """
        Check if the array is None
        """

        if array is None:
            print("Using primary array instead")
            return self.arr
        return array

    def getRowCount(self, array=None):
        """
        Get the number of rows in the 2D array
        """

        array = self.__checkIfTwoDArray(array)
        array = self.__checkIfArrayNone(array)
        return len(array)

    def flattenArray(self, array=None):
        """
        Flatten the 2D array
        """

        array = self.__checkIfTwoDArray(array)
        array = self.__checkIfArrayNone(array)
        return list(itertools.chain(*array))

    def getItemCount(self, array=None):
        """
        Get the number of items in the 2D array
        """

        array = self.__checkIfTwoDArray(array)
        array = self.__checkIfArrayNone(array)
        return len(list(itertools.chain(*array)))
    
    def getItemCountPerRow(self, array=None):
        """
        Get the number of items in each row of the 2D array
        """

        array = self.__checkIfTwoDArray(array)
        array = self.__checkIfArrayNone(array)
        return [len(row) for row in array]

    def getAllDataTypeCount(self, array=None):
        """
        Get the count of each data type in the 2D array
        """

        array = self.__checkIfTwoDArray(array)
        array = self.__checkIfArrayNone(array)

        dataTypes = {}
        for row in array:
            for item in row:
                if type(item).__name__ in dataTypes:
                    dataTypes[type(item).__name__] += 1
                else:
                    dataTypes[type(item).__name__] = 1
        return dataTypes

    def __checkInitialRowCol(self, row, col, array=None):
        """
        Check if the initial row and column indexes are within the range of the 2D array
        """

        if row < 0 or row >= self.getRowCount(array=array):
            print("Initial row index out of range")
            return False
        if col < 0 or col >= self.getItemCountPerRow(array=array)[row]:
            print("Initial column index out of range")
            return False
        
        return True

    def get1DAdjacentColumn(self, row=0, col=0, topLength=0, bottomLength=0, array=None):
        """
        Get the adjacent items in the column of the 2D array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        if not self.__checkInitialRowCol(row, col, array=array):
            print("Initial row or column index out of range")
            return
        
        topMostItem = row - topLength
        bottomMostLength = row + bottomLength

        if topMostItem < 0:
            print("You cannot get an item whose index is less than 0")      
        if bottomMostLength >= self.getRowCount():
            print("You cannot get an item whose index is more than the number of rows")

        finalList = []

        for i in range(topMostItem, bottomMostLength + 1):
            try:
                finalList.append(self.arr[i][col])
            except IndexError:
                finalList.append(None)
        return finalList

    def get1DAdjacentRow(self, row=0, col=0, leftLength=0, rightLength=0, array=None):
        """
        Get the adjacent items in the row of the 2D array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        if not self.__checkInitialRowCol(row, col, array=array):
            print("Initial row or column index out of range")
            return

        leftMostItem = col - leftLength
        rightMostItem = col + rightLength

        if leftMostItem < 0:
            print("You cannot get an item whose index is less than 0")
            leftMostItem = 0
        if rightMostItem >= self.getItemCountPerRow(array=array)[row]:
            print("You cannot get an item whose index is more than the length of the row")
            rightMostItem = self.getItemCountPerRow(array=array)[row] - 1

        return self.arr[row][leftMostItem:rightMostItem + 1]
    
    def __check2DPerimeter(self, row, col, perimeter, array):
        """
        Check the perimeter of the 2D array.
        If it goes outside the perimeter, raise an error.
        """

        topPosition = row - perimeter
        bottomPosition = row + perimeter
        leftPosition = col - perimeter
        rightPosition = col + perimeter
    
        if topPosition < 0:
            print("You cannot get an item whose index is less than 0")
            # topPosition = 0
        if bottomPosition >= self.getRowCount(array=array):
            print("You cannot get an item whose index is more than the number of rows")
            # bottomPosition = self.getRowCount(array=array) - 1
        if leftPosition < 0:
            print("You cannot get an item whose index is less than 0")
            # leftPosition = 0
        if rightPosition >= self.getItemCountPerRow(array=array)[row]:
            print("You cannot get an item whose index is more than the length of the row")
            # rightPosition = self.getItemCountPerRow(array=array)[row] - 1
        
        return topPosition, bottomPosition, leftPosition, rightPosition
        
    def get2DAdjacent(self, row=0, col=0, perimeter=0, array=None):
        """
        Get the adjacent items in the 2D array within a specified perimeter
        """

        if not self.__checkInitialRowCol(row, col, array=array):
            raise IndexError("Initial row or column index out of range")
        
        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        topMostItem, bottomMostItem, leftMostItem, rightMostItem = self.__check2DPerimeter(row, col, perimeter, array)
        
        finalList = []
        for i in range(topMostItem, bottomMostItem + 1):
            finalList.append([])
            for j in range(leftMostItem, rightMostItem + 1):
                try:
                    if j < 0 or i < 0:
                        finalList[-1].append(None)
                    else:
                        finalList[-1].append(self.arr[i][j])
                except IndexError:
                    finalList[-1].append(None)

        return finalList
    
    def getDataTypeCount(self, array=None):
        """
        Get the count of each data type in an array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        flatArray = self.flattenArray(array)

        dataTypes = self.__getTypesPerRow(flatArray)

        return dataTypes
    
    def __getTypesPerRow(self, array=None):
        """
        Get the count of each data type in the array        
        """

        dataTypes = {}
        for item in array:
            if type(item).__name__ in dataTypes:
                dataTypes[type(item).__name__] += 1
            else:
                dataTypes[type(item).__name__] = 1
        return dataTypes
    
    def getDataTypeCountPerRow(self, array=None):
        """
        Get the count of each data type in each row of the 2D array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        wholeList = []
        for row in array:
            wholeList.append(self.__getTypesPerRow(array=row))
        return wholeList

    
    def getNumberTotal(self, array=None):
        """
        Get the total of all numbers in the 2D array
        """
        
        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)
        flatArray = self.flattenArray(array)

        return sum([item for item in flatArray if isinstance(item, (int, float))])
    
    def getIntegerTotal(self, array=None):
        """
        Get the total of all integers in the 2D array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)
        flatArray = self.flattenArray(array)

        return sum([item for item in flatArray if isinstance(item, int)])
    
    def getFloatTotal(self, array=None):
        """
        Get the total of all floats in the 2D array
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)
        flatArray = self.flattenArray(array)

        return sum([item for item in flatArray if isinstance(item, float)])
    
    def getRowAdjacentPerimeterStrings(self, row=1, col=1, perimeter=1, array=None):
        """
        Get the adjacent strings in the row of the 2D array within a specified perimeter
        """

        if not self.__checkInitialRowCol(row, col, array=array):
            raise IndexError("Initial row or column index out of range")

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        topPosition, bottomPosition, leftPosition, rightPosition = self.__check2DPerimeter(row, col, perimeter, array)
        
        adjacentStrings = []

        for i in range(topPosition, bottomPosition + 1):
            j = leftPosition
            while j <= rightPosition:
                try:
                    print(f"Item: {array[i][j]}")
                    if isinstance(array[i][j], str):
                        j, string = self.__grabWholeString(i, j, array)
                        adjacentStrings.append(string)
                    else:
                        j += 1
                except IndexError:
                    j += 1

        return adjacentStrings

    def __grabWholeString(self, row, col, array):
        """
        Grab the whole string in the 2D array
        """

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

        string = "".join(array[row][leftPointer:rightPointer + 1])
        return rightPointer + 1, string
    
    def advancedColumnRolling(self, amount=0, column=0, array=None, skipEmpty=True):
        """
        Roll the columns of the 2D array by a specified amount
        """

        array = self.__checkIfArrayNone(array)
        array = self.__checkIfTwoDArray(array)

        if not self.__checkColumnLength(column, array):
            raise IndexError("Column index out of range")

        if skipEmpty:
            array = self.__rollWithSkipEmpty(amount, column, array)
        else:
            array = self.__rollWithoutSkipEmpty(amount, column, array)

        return array
    
    def __checkColumnLength(self, column, array):
        """
        Check if the column index is within the range of the 2D array
        """
        longestRow = max([len(row) for row in array])
        if column < 0 or column >= longestRow:
            return False
        return True

    def __rollWithSkipEmpty(self, amount, column, array):
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

        return newArray

    def __rollWithoutSkipEmpty(self, amount, column, array):
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
            print("item", row[column])
            savedValues.append(row[column])

        savedValues = savedValues[-amount:] + savedValues[:-amount]
        initialRowLengths = initialRowLengths[-amount:] + initialRowLengths[:-amount]

        newArray = []
        for i, row in enumerate(array):
            row[column] = savedValues[i]
            newArray.append(row)

            for item in reversed(row):
                if item is None:
                    row.remove(item)

        print("Array after:", *newArray, sep='\n')

        return newArray