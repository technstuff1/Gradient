#hi!
import random
import time

time.sleep(0.5)

def decode():
    file1 = input("what file?")
    if ".hyt" in file1:
        file1 = open(file1,"r+")
        file1read = file1.read()
        file1readlist = list(file1read)
        #print(file1readlist)
        x = 0
        list1 = ""
        print("")
        while x != len(file1readlist):
            if file1readlist[x] == "/":
                print(list1)
                list1 = ""
            else:
                list1 = list1 + file1readlist[x]
            x = x + 1
        print("")
    else:
        print("error: wrong file type")
    command()
def encode():
    #open the file
    file1 = input("what file? ")
    if ".hyt" in file1:
        file1 = open(file1,'w')
        
        #initialize an empty list
        word_list= []

        x = 0
        while x != 1:
            print("Please enter data: ")
            line = input()#take input
            if line == "":
                x = 1
            else:
                word_list.append(line + "/")
        
        
        file1.writelines(word_list)
        
        file1.close()
    else:
        print("error: wrong file type")
    command()
        
def commands():
    print("Commands:")
    print("encode")
    print("decode")
    print("help")
    print("type h before a command to get help")
    command()

def commandd():
    command()

def command():
    
    command = input("Commmand:    ")
    if command == "decode":
        decode()
    elif command == "encode":
        encode()
    elif command == "hencode":
        print("encodes a file of your choice, must have file be in the same folder as this file. Must be a .hyt")
        commandd()
    elif command == "hdecode":
        print("opens a file of your choice, must be in the same folder as this file. Must be a .hyt Also, if you enter your data and click enter you add the data to a new line and you can close the file by entering nothing")
        commandd()
    elif command == "commands":
        commands()
    elif command == "help":
        print("Gradient is a tool to make and overwrite .hyt files")
    else:
        print("error: wrong/misspelled command")
        commandd()

file1 = open("!0.huo", 'w')
file1.writelines("Ryan Jacobs")
file1 = open("!0.huo", "r+")
file1 = file1.read()


print("Gradient 1.1, made by", file1)
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 100)
x = x / 100
time.sleep(x)
print("Type 'commands' to see all commands")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
command()

    
