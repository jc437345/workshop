__author__ = 'jc437345'

lower = 40
upper = 100
#print("Enter a number (" + str(lower) + "-" + str(upper) + "):")
str = "Enter a number {} - {}:".format(lower,upper)
print(str)


for i in range(lower, upper):
          print("ASCII CODE {} CHAR {}".format(i, chr(i)))
