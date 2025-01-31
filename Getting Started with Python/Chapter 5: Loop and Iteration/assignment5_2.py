#assignment 5.2
largest = None
smallest = None

while True : 
    val = input('Please Enter a Number:\n')
    if val == 'done' : 
        break
    
    try : 
        ival = int(val)
        
        if largest is None:
            largest = ival
        elif ival > largest:
            largest = ival
            
        elif smallest is None:
            smallest = ival
        elif ival < smallest:
            smallest = ival
    
    except:
        print('Invalid input')
        
print('Maximum is ', largest)
print('Minimum is ', smallest)         
                             
        