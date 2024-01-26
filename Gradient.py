#hi!

def decode():
    file1 = input("what file?")
    if ".hyt" in file1:
        file1 = open(file1,"r+")
        file1read = file1.read()
        print(file1read)
    else:
        print("error: wrong file type")
    command()
def encode():
    #open the file
    file1 = input("what file?")
    if ".hyt" in file1:
        file1 = open(file1,'w')
        
        #initialize an empty list
        word_list= []
        
        print("Please enter data: ")
        line = input()#take input
        word_list.append(line)
        
        
        file1.writelines(word_list)
        
        file1.close()
    else:
        print("error: wrong file type")
    command()
        
def commands():
    print("Commands:")
    print("encode")
    print("decode")
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
        print("opens a file of your choice, must be in the same folder as this file. Must be a .hyt")
        commandd()
    elif command == "commands":
        commands()
    else:
        print("error: wrong/misspelled command")
        commandd()


command()

    
