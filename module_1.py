#Output a string to the terminal
print('Where is Miguel?')

#Get a string from user
miguel_location = input()

#Output variable to terminal
print('Miguel is')
print(miguel_location)


#Promt user for value and save to variable
num_chocolate = int(input('How much chocolate did you eat: '))

chocolate_price = float(input('How much did each chocolate cost: '))

#Store product of variables into new variable
total = num_chocolate * chocolate_price

#Output variables to terminal using concatenation
print('I bought ' + str(num_chocolate) + ' chocolates for $' + str(round(total)) + '.')


#Output variables to terminal using formatted strings
print(f'I bought {num_chocolate} chocolates for ${round(total, 2)}.')