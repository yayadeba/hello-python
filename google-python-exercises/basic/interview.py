#Python Interview Question
# #1 Fizz Buzz

# for num in range(1,101):
# 	if num % 5 == 0 and num % 3 == 0:
# 		print ("FizzBuzz")
# 	elif num % 3 == 0:
# 		print ("Fizz")
# 	elif num % 5 == 0:
# 		print ("Buzz")
# 	else:
# 		print (num)


# #2 Fibonacci Swqueence

# a,b = 0,1
# for i in range(0,10):
# 	print (a)
# 	a,b = b, a+b


# #3 List

# my_list = [1,2,3,4,5,6,7,8,9,10]
# #Give me each number in a list squared
# squares = [num*num for num in my_list]
# print (squares)


# #4 Fibonacci Generator
def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield  "{}: {}".format(i+1, a)
        a, b = b, a + b
for item in fib(100):
    print (item)
