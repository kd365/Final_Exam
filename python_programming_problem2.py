class Cars:
    def __init__(self):
        self.make = ''
        self.color = ''
        
    def getString(self):
        self.finalString = str(self.make) + ' ' + str(self.color)
        return self.finalString
        
    def printString(self):
        print(self.finalString.upper())
        
if __name__ == "__main__":
    input1 = input("Input the make of your dream car:\n")
    input2 = input("Input the color of your dream car:\n")
    outputString = Cars()
    outputString.make = input1
    outputString.color = input2
    outputString.getString()
    outputString.printString()
