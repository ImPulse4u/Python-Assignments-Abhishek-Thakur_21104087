#Q1
print("Ans 1")

def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')

#Q2
print("\n\nAns 2")

#input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else is same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
    
#Q3   
print("Ans 3")
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#(a)
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#(b)
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")

#(c)
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")

#(d)
setresult = set(result)
print("<d> Set:",setresult)

#(e)
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutableSet)

#f)
print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

#Q4
print("Ans 4")
class Student:
    def __init__(self, student,roll_number):
        self.name = student
        self.roll_number = roll_number
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Abhishek Thakur", 21104087)
print("Object is created")
#printing the assigned value
print(f"The name of the student it {student1.name} and SID is {student1.roll_number}.")
#deleting the object
del student1
print("\n")

#Q5
print("Ans 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
    def func(self):
       print("Name of employee is:",self.name,"and salary is:",self.salary)   
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
employee1.func()
employee2.func()
employee3.func()
#part (a) updating salary
employee1.salary = 70000
print(f"(a) The updated salary of {employee1.name} is {employee1.salary} ")
def func(self):
       print("Name of employee is:",self.name,"and salary is:",self.salary)
employee1.func()
employee2.func()
employee3.func()
#part (b) deleting a record
del employee3
print("(b)Record of Viren deleted")
def func(self):
       print("Name of employee is:",self.name,"and salary is:",self.salary)
employee1.func()
employee2.func()

print("\n")


#Q6
print("Ans 6")
#we will use the concept of anagrams

def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    mylist=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            mylist.append(perm[:i]+char+perm[i:])
    return mylist       


George_word=input("Enter the word by George:")
Possible_words=anagram(George_word)
Barbie_word=input("Enter word by Barbie:")

if Barbie_word in Possible_words:
    print("Your Friendship is real.")
else:
    print("Your Friendship is fake.")
print("Done")
