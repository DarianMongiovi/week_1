##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
year_one = int(input('Enter first year: '))
year_two = int(input('Enter year two: '))
difference = year_one - year_two

print(f'Year 1: {year_one}')
print(f'Year 2: {year_two}')
print(f'Difference: {difference}')


#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''

fahrenheit = int(input('Enter Temp in Fahrenheit: '))
celsius = round((fahrenheit - 32) * (5/9), 2)

print(f'Farenheit: {fahrenheit}')
print(f'Celsius: {celsius}')

#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

usd = int(input('Enter amount in US dollars: '))
euro = round(usd * .97, 2)

print(f'USD: {usd}')
print(f'EU: {euro}')

##### ASSIGNMENT ENDS HERE #####
