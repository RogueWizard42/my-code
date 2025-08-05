# Assignment 4.6 Payrollfunction
hours = input('Please Enter Hours:\n')
rate = input('Please Enter Hourly Rate:\n')
hoursf = float(hours)
ratef = float(rate)

def computepay(hoursf, ratef) :
    if hoursf <= 40 :
        pay = hoursf * ratef
    else :    
        if hoursf > 40 :
            pay = (40 * ratef) + ((hoursf - 40) * (ratef * 1.5))
            return pay
        
x = computepay(hoursf, ratef)
print('Pay',x)
        