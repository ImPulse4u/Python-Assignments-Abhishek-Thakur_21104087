#Q1
#(a)
string="Python is a case sensitive language"
print(len(string))
#(b)
print(string[::-1])
#(c)
print(string[10:26])
#(d)
print(string[0:10]+'object oriented'+string[26:35])
#(e)
print(string.find('a'))
#(f) 
print(string.replace(" ",""))
print()

#Q2
name="Abhishek Thakur"
SID=21104087
department_name="EE"
CGPA="9.9"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))
print()

#Q3
#a=56 b=10
a=0b111000
b=0b1010
#(a)
print(bin(a&b))
print()
#(b)
print(bin(a|b))
print()
#(c)
print(bin(a^b))
print()
#(d)
print(bin(a<<2))
print(bin(b<<2))
print()
#(e)
print(bin(a>>2))
print(bin(b>>4))
print()

#Q4
n1=int(input("Give first number:"))
n2=int(input("Give second number:"))
n3=int(input("Give third number:"))

if(n1>n2):
    if(n1>n3):
        print(n1,"is greatest number")
    else:
        print(n3,"is greatest number")
else:
    if(n2>n3):
        print(n2,"is greatest number")
    else:
        print(n3,"is greatest number")
print()        

#Q5
string=input("Enter string:")
if("name"in string):
    print("Yes")
else:
    print("No")
print()    

#Q6
s1=int(input("Enter length of first side:"))
s2=int(input("Enter length of second side:"))
s3=int(input("Enter length of third side:"))

if(s1+s2>s3 and s2+s3>s1 and s1+s3>s2):
    print("Yes")
else:
    print("No")
