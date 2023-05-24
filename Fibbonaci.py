"""
	Author: Akshay Pawar
	Date: March 31 2023
	
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""

def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("Enter A Number : : "))

if numero < 0:
	print("Number Is Not Valid")

i = 0

print("Fibbonaci Series : : ")

for i in range(1, numero):
	print(fibonacci(i))

