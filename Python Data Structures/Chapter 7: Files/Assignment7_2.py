#Assignment 7.2 
count = 0
zork = 0
fname = input("Enter file name: ")
fhand = open(fname)


for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count = count + 1
        a = line.find('0')
        x = line[a:]
        zork = zork + float(x)
        
avg = zork/count

print("Average spam confidence:",avg)