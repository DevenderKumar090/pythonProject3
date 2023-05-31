'spam eggs'

s = 'First line.\nsecond line.'
print(s)

print('c:\some\name')

print(r'c:some\name')

text = ("Put several strings within parentheses "
        "to have them joined together.")
print(text)

word = 'python'
print(word[0])
print(word[5])

############################# LISTS #################

sqaures = [1,2,3,4,5,6]
print(sqaures)
print(sqaures[0])
print(sqaures[-3])
print(sqaures[:])

letters =['a','b','c','d','e','f','g']
print(letters)

# replace some values
letters[2:5] = ['C','D','E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)




for num in range(2,12):
        if num % 2 == 0:
                print("Found an even number",num)
                continue
        print("Found an odd number",num)

# paasss Statement
# while True:
#         pass
#match statement###

####Functions########################

def fib(n): ## write an fibonacci seriews upto n
        """print an fibonacci series upto n"""
        a, b = 0, 1
        while a < n:
                print(a, end=' ')
                a, b = b, a+b
        print()



### now call the function
fib(1000)
f = fib
f(2300)
print(fib(0))

# return fibonacci series upto n
def fib2(n):
        """return a list containing the fibonacci series up to n"""
        result = []
        a, b = 0, 1
        while a < n:
                result.append(a)
                a, b = b, a+b
        return result


f1500 = fib2(1500)
print(f1500)

##default argument values
def ask_ok(prompt, retries=4, reminder='Please try again'):
        while True:
                ok =input(prompt)
                if ok in('y','ye','yes'):
                        return True
                if ok in('n','no','nop','nope'):
                        return False
                retries = retries - 1
                if retries < 0:
                        raise ValueError('Invalid user response')
                print(reminder)
ask_ok('Do you really want to quit')









