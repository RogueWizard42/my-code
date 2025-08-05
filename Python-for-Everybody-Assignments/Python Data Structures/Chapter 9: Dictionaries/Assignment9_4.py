#Assignment 9.4
fname = input('Enter a file name:\n')
fh = open(fname)
if len(fname) < 1 : fname = 'mbox-short.txt' 

x = dict()
for line in fh :
    if line.startswith('From ') :   #must remember to keep it simple
        line = line.split()[1]
        #print(line)
        x[line] = x.get(line, 0) + 1 
        #print(x)
  
person = None             
count = None 
for key, value in x.items() : 
    if count is None or value > count :
        person = key
        count = value 
        
print(person, count)            
             
     
        