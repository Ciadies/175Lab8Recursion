'''
Created on Mar. 11, 2024

@author: sebbe
'''
def mylen(alist):
    if alist == []:
        return 0
    else:
        length = 1 + mylen(alist[1:]) 
        return length
    
def intDivision(n,m):
    if n <= 0 and m < 0 :
        raise Exception("Invalid value")
    if n - m < 0:
        return 0
    else: 
        return 1 + intDivision(n-m,m)
    
def sumDigits(number):
    if number < 0:
        raise Exception("Invalid Value")
    str_num = str(number)
    if len(str_num) == 1:
        return int(str_num)
    elif len(str_num) == 0:
        return 0
    else:
        return int(str_num[0]) + sumDigits(int(str_num[1:]))

def reverseDisplay(number):
    if number < 0:
        raise Exception("Invalid Value")
    
    str_num = str(number)
    
    if len(str_num) == 1 or 0:
        print(str_num)
    else:
        print(str_num[len(str_num)-1], end ="")
        reverseDisplay(int(str_num[:len(str_num) -1]))

def binary_search2(target,alist,low,high):
    if low > high:
        return "item not in list"
    elif target == alist[low]:
        return low    
    else:
        return binary_search2(target, alist, low+1, high)
    
    
def main():
    print("Exercise 1")
    alist=[43,76,97,86]
    print(mylen(alist))
    print("Exercise 2")
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m))
    print("Exercise 3")
    number = int(input('Enter a number: '))
    print(sumDigits(number))
    print("Exercise 4")
    number = int(input('Enter a number:'))
    reverseDisplay(number)
    print("Exercise 5")
    some_list = [-8,-2,1,3,5,7,9]
    print(binary_search2(9,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))


main()
