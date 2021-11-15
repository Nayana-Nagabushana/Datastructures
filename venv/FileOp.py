def filewrite():
    myfile = open('myfirstfile.txt','w')
    myfile.write("This is my first assignment in AOS \n")
    myfile.close()

def fileread():
    myfile = open('myfirstfile.txt','r')
    contents = myfile.read()
    print(contents)
    myfile.close()

