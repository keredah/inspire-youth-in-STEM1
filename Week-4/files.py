#There are four different methods (modes) for opening a file:
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#In addition you can specify if the file should be handled as binary or text mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)
#Syntax
#To open a file for reading it is enough to specify the name of the file:
#f = open("demofile.txt")
#The code above is the same as:
#f = open("demofile.txt", "rt")
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
#Note: Make sure the file exists, or else you will get an error.

# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes

file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print( "Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


