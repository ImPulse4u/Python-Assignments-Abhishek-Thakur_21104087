#Q1
print("Q1")
string1=input("Give a string:")
list1=[]
list2=string1.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:          #it is for one word
    for i in string1:      #created a list with the characters
        list1.append(i) 
    for j in list1:        #created a condition where all unique keys
        if j in d:         #get value 1 and when a key repeats it increases 
            d[j]=d[j]+1    #value by 1
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        #this is for multiple words
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t) 
    print()


#Q2
print("Q2")
month=int(input("Give month:"))


if(month in[1,3,5,7,8,10,12]):
    day=int(input("Give day:"))
    if(1<=day<=31):
        year=int(input("Give year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date:","1/1/",year+1)
            elif(day==31):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("Give day:"))
    if(1<=day<=30):
        year=int(input("Give year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(day==30):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year:"))
    if(1800<=year<=2025):
        day=int(input("Give day:"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date:",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date:",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")
print()    

#Q3
print("Q3")
alist=[5,6,7,8,9,10]
list_with_tuples=[]
for i in alist:
    list_with_tuples.append((i,i**2))
print(list_with_tuples)
print()

#Q4
print("Q4")
Grade_points=int(input("Give a number between 4 and 10 including them:"))
if(Grade_points==4):
    print("Performance=Poor")
    print("Letter Grade=D")
elif(Grade_points==5):
    print("Performance=Below Average")
    print("Letter Grade=C")
elif(Grade_points==6):
    print("Performance=Average")
    print("Letter Grade=C+")
elif(Grade_points==7):
    print("Performance=Good")
    print("Letter Grade=B")
elif(Grade_points==8):
    print("Performance=Very Good")
    print("Letter Grade=B+")
elif(Grade_points==9):
    print("Performance=Excellent")
    print("Letter Grade=A")
elif(Grade_points==10):
    print("Performance==Outstanding")
    print("Letter Grade=A+")
else:
    print("error")
print()

#Q5
print("Q5")
Word="ABCDEFGHIJK"

counter=1

#we first identify the pattern which says that
#we need to first leave gaps equal to (counter-1) where counter tells
#the row no. and the alphabets should decrease after every row 

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1

print()

#Q6
print("Q6")
dic = {}
name = input("Enter Name: ")
sid = int(input("Enter SID: "))
dic[sid] = name
ch = input("Do you want to enter more details[y/n]: ")
while ch=="y":
    name = input("Enter Name: ")
    sid = int(input("Enter SID: "))
    dic[sid] = name
    ch = input("Do you want to enter more details[y/n]: ")
    
#b
print("\nDetails of the students: ") 
print("SID\tName")
for i in dic:
    print("{}\t{}".format(i, dic[i]))
    
print("\nSorted dictionary using student SID: ") 
sort_id = {k: v for k, v in sorted(dic.items())}
print("SID\tName")
for i in sort_id:
    print("{}\t{}".format(i, dic[i]))    
        
print("\nSorted dictionary using student Names: ") 
sort_names = {k: v for k, v in sorted(dic.items(), key = lambda v:v[1])}
print("SID\tName")
for i in sort_names:
    print("{}\t{}".format(i, dic[i]))   
        
id = int(input("\nEnter the SID of the student: "))
if id in dic:
    print("Name of the student is: ",dic[id])
else:
    print("The entered SID is not found")

print()

#Q7
#fibonacci sequence
print("Q7")
first_term=int(input("Give a number:"))
second_term=int(input("Give a number:"))
#now it will keep on printing the sequence till you say y and to stop it say n
sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop going further:")
print("Now we got a list having a fibonacci series-")
print(series)

#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("Average of the sequence:")
print(sum/len(series))
print()

#Q8
print("Q8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
print("(a)")
required_Set=Set1^Set2
print(required_Set)
print()

#(b)
print("(b)")
required_Set=Set1^(Set2^Set3)
print(required_Set)
print()

#(c)
print("(c)")
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(required_Set)
print()

#(d)
print("(d)")
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set=new_Set-Set1
print(required_Set)
print()

#(e)
print("(e)")
required_Set=new_Set-(Set1|Set2|Set3)
print(required_Set)
print()

    
    
    
