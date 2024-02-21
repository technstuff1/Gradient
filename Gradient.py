#hi!
import os.path
import random
import time

hq = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']

time.sleep(0.5)

def decode():
    file1 = input("what file?  ")
    time.sleep(random.randint(1, 2))
    #print(file1)
    if file1[-1] == 't' and file1[-2] == 'y' and file1[-3] == 'h' and file1[-4] == '.':
        file1 = open(file1,"r+")
        file1read = file1.read()
        file1read = str(file1read)
        if file1read[0] == ip[0] and file1read[1] == ip[1] and file1read[2] == ip[2]:
            file1read= file1read.replace(ip, '')
            #print(file1read)
            file1read = file1read.replace('[', '')
            #print(file1read)
            file1read = file1read.replace(']', '')
            #print(file1read)
            file1read = file1read.replace("'", '')
            #print(file1read)
            file1read = file1read.replace('/', '')
            file1read = file1read.split(', ')        
            #print(file1read)
            file1read.pop(-1)
            #print(file1read)
            x = 0
            list1 = ""
            print("")
            #print(file1read[x])
            while x != len(file1read):
                if file1read[x] == "`":
                    print(list1)
                    list1 = ""
                elif file1read[x] == '*':
                    list1 = list1 + ' '
                else:
                    list1 = list1 + hq[int(file1read[x])]
                x = x + 1
            print("")
        else:
            print("invalid ip")
    else:
        print("error: wrong file type")
    command()
def encode():
    word_list = []
    ipask = input('enter receivers ip, enter "me" to send to self  ')
    if ipask == "me":
        file1 = open("!!.huo", 'r')
        ipto = file1.read()
    else:
        ipto = ipask
    #open the file
    file1 = input("what file? ")
    if ".hyt" in file1:
        file1 = open(file1,'w')
        
        #initialize an empty list
        word_list= []

        x = 0
        while x != 1:
            print("Please enter data: ")
            print('')
            line = input()#take input
            print('')
            if line == "":
                x = 1
            else:
                y = 0
                line_encoded = []
                while y < len(line):
                    letter = line[y]
                    #print(letter)
                    if letter == ' ':
                        line_encoded.append('*')
                        y = y + 1
                    else:
                        letter = hq.index(letter)
                        #print(letter)
                        line_encoded.append(str(letter) + "/")
                        y = y + 1
                #print(line_encoded)
                line_encoded.append('`')
                #print(line_encoded)
                line_encoded = str(line_encoded)
                #print(line_encoded)
                line_encoded = line_encoded + ', '
                #print(line_encoded)
                word_list.append(line_encoded)
                #print(word_list)                
                    
        
        file1.writelines(ipto)
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
print("Gradient 1.5, made by", file1.read())
file1.close()
x = random.randint(5, 10)
x = x / 100
time.sleep(x)
print("")
x = random.randint(5, 10)
x = x / 100
if os.path.isfile('./!!.huo') == False:
    file1 = open("!!.huo", 'w')
    while x != 1:
        ip = input("set local ip:  ")
        if len(ip) > 3 or len(ip) < 3:
            print("too long/short ip")
        elif len(ip) == 3:
            x = 1
    file1.writelines(ip)
    file1 = open('!!.huo', 'r')
    print(file1.read())
else:
    file1 = open("!!.huo", 'r')
    ip = file1.read()
    print(ip)
    
file1.close
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

    
