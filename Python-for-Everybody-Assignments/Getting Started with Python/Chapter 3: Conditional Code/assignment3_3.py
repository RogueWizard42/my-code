#assignment 3.3
score = input('Enter Score: ')
scorex = float(score)
if scorex > 1.0 :
    print('Error')
elif scorex < 0.0 :
    print('Error') 
elif scorex >= 0.9 <= 0.99 : 
    print('A')
elif scorex >= 0.8 <= 0.89 : 
    print('B')
elif scorex >= 0.7 <= 0.79 : 
    print('C')
elif scorex >= 0.6 <= 0.69 : 
    print('D')
elif scorex < 0.6 : 
    print('F')
    
           