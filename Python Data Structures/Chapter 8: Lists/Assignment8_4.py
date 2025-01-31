#Assignment 8_4 using a for loop to add word to new list

fname = input('Enter file name:\n')
fh = open(fname).read()
endlist = list() 
#added empty list 'endlist' then use the for loop to 
#add words from file that are not in endlist 
#this ensures that a word is added only once 

x = fh.split()
x.sort()

for word in x :
    if word not in endlist :
        endlist.append(word)
        

print(endlist)