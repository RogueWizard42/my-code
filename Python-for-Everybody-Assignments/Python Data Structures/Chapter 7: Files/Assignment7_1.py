# Assignment7_1

file = input('Enter file name to view:\n')

viewfile = open('words.txt')

for line in viewfile : 
    linex = line.rstrip()
    print(linex.upper())
    
 
    
    
    