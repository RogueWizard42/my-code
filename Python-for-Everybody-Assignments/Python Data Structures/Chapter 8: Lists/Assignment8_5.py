#Assignment 8_5

fname = input('Enter a file name:\n')
fh = open(fname)
count = 0
 
 
for line in fh :
    if line.startswith('From ') : 
        x = line.split()[1]  
        print(x)
        count = count + 1
     
print('There were',count,'lines in the file with From as the first word')             
    
     
    

    
   
    
    
