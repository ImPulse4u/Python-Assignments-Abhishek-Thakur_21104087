#Q1
x= input("Enter the first number: ")
y= input("Enter the second number: ")
z= input("Enter the third number: ")
avg = (int(x)+int(y)+int(z))/3
print("The average of three numbers is: ", avg) 

#Q2
x = float(input("Enter Gross income: "))
y= int(input("Enter number of dependents: "))
a= (x-10000-(3000*y))*0.2
print("income Tax is: ", a)

#Q3
x  =[ "sid", "Abhi", "m", "Electrical Engineering", 9.5]
print(x) 

#Q4
x= [input("1st student's no. :"),input("2nd student's no. :"),input("3rd student's no. :"),input("4th student's no. :"),input("5th student's no. :")]
x.sort()
print(x) 

#Q5a
colors =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors.pop(3)
print(colors)

#Q5b
colors=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colors[3:5]
colors.insert(3, "Purple")
print(colors)
