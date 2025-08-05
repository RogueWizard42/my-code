#Assignment 10.2 
fname = input('Enter a file name:\n')
fh = open(fname)
if len(fname) < 1 : fname = 'mbox-short.txt' 

x = dict()
for line in fh :
    if line.startswith('From ') : 
        line = line.split()[5]
        line = line.split(':')
        #print(line)
        x[line[0]] = x.get(line[0], 0) + 1 
        #print(x)

y = list()        
for key, value in x.items() :    
    y.append((key, value))
    y.sort()
    #print(y)
    
for key, value in y:    
    print(key, value) 
    
          