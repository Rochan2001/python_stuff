import time
def print_match(search_pattern):
    filein = input("Enter the file name: ")
    with open(filein,'r') as f:
        for lines in  f:
            if lines.find(search_pattern) >= 0:
                print(lines.rstrip('\n')+"\n")
    toc = time.time()
    print((toc-tic)*1000)
def replace_func(search_string,replace_string):
    filein = input("Enter the file name: ")
    fileout = open('output.txt','w')
    with open(filein,'r') as f:
        for lines in f:
            if lines.find(search_string) >=0:
                temp = lines.replace(search_string,replace_string)
                fileout.write(temp+"\n")
    fileout.close()
   

choice = input("Choose from the following\n1: Search pattern\n2: Replace and write\n")
if choice == '1':
    tic = time.time()
    search_pattern = input("Enter the search pattern: ")
    print_match(search_pattern)
else:
    search_string = input("Enter the string to be searched and replaced: ")
    replace_string = input("Enter the replace String: ")
    replace_func(search_string,replace_string)
toc = time.time()
