'''
Created on Feb 29, 2020

@author: ITAUser
'''
#read&write - mod name

#basic concepts
#open file - open()

file1="filename.txt","mode"

#mod r: read, w: write

#read- read(), readline() - stores value as a string
#write - write()

#create a new file
    file1 = open("hello.txt","a")
    file1.close()

#write to the file
    string = "hellow my name is Raya"
    file1.write(string)
    
#write multiple lines
    line = ["dogs ", "are ","cool "]
    file1.writeLines(line)
    file1.close()
    
#read file
    file1.open("hello.txt", "r")
    text = file1.read()
    file1.close()
    
    print(text)