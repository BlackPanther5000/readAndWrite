'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''

'''
START HERE
'''

'''Write a File'''
#1) Create a file with Python that is named after your first and last name.  
#   Then write your first name on the first line with Python and your last name
#   on the second line with Python. 

file1 = open("rayaRonaghy.txt","w")
file1.write("Raya ")
file1.write("Ronaghy ")
file1.close()

#2) In the same file you just created describe one of the projects you created
#   with at least 5 lines and how you think you can improve.

file1 = open("rayaRonaghy.txt","a")
file1.write("Line 1: One of the projects I created is the 'Rock, Paper, Scissors' project. ")
file1.write("Line 2: I am proud of the way I made this project, but I think it could improve visually. ")
file1.write("Line 3: It would be nice if the game had visuals to go along with it. ")
file1.write("Line 4: Maybe an image of a rock, or paper, or scissors could show when the player selects one. ")
file1.write("Line 5: But I still think the game is great without it. ")
file1.close()

#3) Within 5 lines of the previous lines you've written on, describe what line 
#   you are on, on that line. Then close the file

'''Read a file'''
#4) Open the previous file you created. Create an if statement that checks if
#   the mode is r. If the mode is r, create a variable named contents and set
#   the variable with .read() of the file you created. Print the contents of
#    the file. Close the file

file1 = open("rayaRonaghy.txt","r")
if print(file1.mode) == "r":
    contents = file1.read()
    print(contents)
    file1.close()

#5) Open the same file you created. Create a variable that uses .readLines() of
# the file Create a for loop that prints each line in the file.

file1 = open("rayaRonaghy.txt","r")
line = file1.readline()
while line:
    print(line)
    line = file1.readline()
file1.close()

#6) Print the first, middle, and last line in the file.
file1 = open("rayaRonaghy.txt","r")
lines = file1.readlines()
file1.close
print(lines[0])
print(lines[3])
print(lines[6])