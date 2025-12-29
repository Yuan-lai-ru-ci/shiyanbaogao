x = float(input('Enter the exchange rate from dollar to RMB:'))
y = int(input('Enter 0 to convert dollars to RMB and 1 vice versa:'))

if y == 0:
    z = float(input('Enter the dollar amount:'))
    print('The amount in RMB is:',round(z*x,3))
elif y == 1:
    z = float(input('Enter the RMB amount:'))
    print('The amount in dollars is:',round(z/x,3))
else:
    print('Incorrect input')
