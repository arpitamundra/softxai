#Question: Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# # The numbers obtained should be printed in a comma-separated sequence on a single line.
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#
# print(','.join(l))
# #---------------Write a program which can compute the factorial of a given numbers.(recursive func)
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input())
# print(fact(x))
#
# #-----------With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
# # that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#
# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print(d)
#
# #----Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)
#
# #Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
#
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


def constr(rowsum,colsum):
    rows = len(rowsum)
    cols = len(colsum)
    matrix = [[0]*cols  for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            value = min(rowsum[i],colsum[j])
            matrix[i][j] = value
            rowsum[i] -= value
            colsum[j] -= value
    return matrix
print(constr([3,8],[4,7]))
