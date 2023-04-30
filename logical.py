#1.
# str="a5b7c1"
# output=""
# for char in str:
#     if char.isalpha():
#         var=char
#     else:
#         num=int(char)
#         output=output+(var*num)
# print(output)



#2.
# str=input()
# output=[]
# l1=[]
# for i in range(97,123):
#     c=0
#     j=chr(i)
#     for l in str:
#         if l==j:
#             c+=1
#     if c>0:
#         output+=[j]
#         l1+=[c]
# d=dict(zip(output,l1))
# print(d)

    

#3.
# l=[]
# nums=[2,7,11,15]
# target=int(input("enter a no."))
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             l+=[i,j]
# print(l)



#4.
# string = "GeeksforGeeks"
# a=string.swapcase() 
# print(a)



#5.
# def fun():
#     l=[11,32,30,4,33,2,43,23,4,5]
#     a=sorted(l)
#     l3=[]
#     l4=[]
#     for i in range(len(l)-1):
#         if len(l3)>=5:
#             if a[i+1]-a[i]==1:
#                 l4+=[a[i],a[i+1]]
#         elif a[i+1]-a[i]==1:
#             l3+=[a[i],a[i+1]]
#     dup_=(set(l3))
#     l2=[]
#     for i in dup_:
#         l2+=[i]
#     print([l2,l4])
# fun()



#6.swap one only:

# n=int(input("enter a size of array"))
# arr=[1,2,3,4,5]
# k=int(input("enter a kth value"))
# if(k<=len(arr)):
#         temp=arr[k-1]
#         arr[k-1]=arr[n-1]
#         arr[n-1]=temp
# print(arr)



#7.

#Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.

# Input:
# N = 8, K = 3
# Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
# Output: 1 2 6 4 5 3 7 8
# Explanation: Kth element from beginning is
# 3 and from end is 6.


# n=8
# arr=[1,2,3,4,5,6,7,8]
# k=3
# a=k-1
# b=n-k
# arr[2],arr[5]=arr[b],arr[a]
# print(arr)


#8.
# a="madhu"
# d=len(a)
# for i in range(d):
#     print(a[d-1],end="")
#     d-=1


#9.
# a=input()
# m=""
# for i in a:
#     m=i+m
# print(m)


#10.
# i=1
# while i <=100:
#     if i%7==0:
#         i+=1
#         continue
#     print(i)
#     i+=1


#11.
#  a="madhu"
# d=len(a)
# for i in range(d):
#     print(a[d-1],end="")
#     d-=1



#12.
# n=int(input("enter your size of array"))
# n=6
# l=[1,2,3,4,5,5]
# key=5

# for i in range(len(l)):
#     if key==l[i]:
#         print(i,end=" ")


#13. A TO Z.
# for i in range(65,91):
#     print(chr(i),end=" ")


#14. SQUARE A TO Z
# size=5
# c=0
# for i in range(size):
#     for j in range(size):
#         print(chr(65+c),end=" ")
#         c+=1
#     print()


#15. SQUARE A TO E horizontal
# size=5
# c=0
# for i in range(size):
#     for j in range(size):
#         print(chr(65+c),end=" ")
#     c+=1
#     print()


#16. SQUARE A TO E VERTICAL
# size=5
# for i in range(size):
#     for j in range(65,65+size):
#         print(chr(j),end=" ")
#     print()


#17.
# n=input("enter your name")
# l=len(n)
# for i in range(l):
#     for j in range(i+1):
#         print((n[i]+n[j]),end="")
#     print()
# for i in range(l):
#     for j in range(l-i-1):
#         print((n[i]+n[j]),end="")
#     print()


#18.
# x=13
# def san():
#     x=12
# san()
# print(x)


#19.
# arr = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1]
# for i in range(len(arr)):
#     if arr[i]==0:
#         arr[i]=1
# print(arr)

# a="madhu"
# print(a[1])


# l=[1,2,2,[3,4,5],7,8,9,[1,6,7],3,5]
# for i in range(len(l)):


#20.
# A="RICHA"
# B=1,2,3
# F=str(B)
# for i in F:
#     if i=="(" or i==")" or i=="," or i==" ":
#         continue
#     A+=i
# print(A)


#21.
# n=int(input("enter a no."))
# for i in range(1,n):
#     print(1,"/",i,end=" , ")


#22.
# ch =(input("enter a letter"))
# if ch=="a" or ch=="i" or ch=="o" or ch=="e" or ch=="u":
#     print("its vowel")
# else:
#     print("its consonant")


#23.
# str=input("enter a string")
# vowel=0
# consonant=0
# for i in str:
#     if i in ("a,e,i,o,u,A,E,I,O,U"):
#         vowel+=1
#     elif i.isalpha():
#         consonant+=1
# print("VOWEL",vowel,"CONSONANT",consonant)


#24.
# str=input("enter a string")
# for i in str:
#     if i==" ":
#         continue
#     print(i,end="")



#25.
# f=float(input())
# c=((f-32)*5)/9
# print("CELCIUS",c)

# n=int(input())
# num=int(input())
# for n in range(n,num+1):
#     mul=1
#     for i in range(1,11):
#         mul=n*i
#         print(n,"x",i,"=",mul)
#     print()


#26.
# num1=int(input("enter a 1st no."))
# num2=int(input("enter a 2nd no."))
# num3=int(input("enter 3rd no."))
# min=0
# if num1>num2:
#     min=num2
# else:
#     min=num1
# if min>num3:
#     min=num3
# else:
#     min=min
# print(min)


#27.
# def fac(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fac(n-1)
# n=int(input())
# print("factorial",fac(n))



#28.
# l=[]
# k=12
# d="madhu"
# f=9.0
# l+=[k]
# l+=[d]
# l+=[f]
# print(l)


#29.
# i=1
# while i<5:
#     print(i*"*")
#     i-=1


#30.
# l=["madhu","richa","priya"]
# i=2
# while i>=0:
#     print(l[i],end=" ")
#     i-=1


#31.
# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break


#32.
#find num is prime or not using ifelse:

# num=int(input("enter a no."))
# p=((2**num)-1)%num
# if p==1:
#     print("yes,it is prime")
# else:
#     print("no,it is not prime")


# l=[None]*10
# print(len(l))


#33.
#TWISTED PRIME NO.:
# n=int(input())
# r=0
# k=n
# c=0
# for i in range(len(str(n))):
#     if n>0:
#         r=(r*10)+n%10
#         n//=10
# for j in range(2,k):
#     if n%j==0 and r%j==0:
#         c=1
# if c==1:
#     print("no,its not twisted prime no.")
# else:
#     print("yes,its a twisted prime no.")



#34.
#PASCAL TRIANGLE:-

# x=int(input("enter a length of pascal triangle"))
# for i in range(x):
#     print(" "*(x-i),end="")
#     print(" ".join(map(str,str(11**i))))



# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x) 


# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset) 


#*****
# l=[1,2,5,7,8,4]
# s=14
# sum=0
# final=0
# for i in range(0,(len(l))):
#     for j in range(i+1,len(l)):
#         sum+=l[j]
#         if sum==s:
#             final=(i+2,j+1)
# print(final)
#         for k in range(j+1,len(l)):
#             if (l[i]+l[j]+l[k])==s:
#                 sum=(i+1),(k-1)
# print(sum)


# l=[2,1,3,1]
# l1=[9,10,11,6]
# l2=[]
# i=len(l)-1
# while i>=0:
#     add=l[i]+l1[i]
#     l2+=[add]
#     i-=1
# # print(l2)
# for j in range(len(l2)-1):
#     if l2[j]>=10:
#         r=l2[j]%10
#         div=l2[j]//10
#         l2[j]=r
#         l2[j+1]+=div
# print(l2[::-1])



#QUESSTIONS:

#1.
#SPIRAL PATTERN:
# size=int(input("enter a size"))
# row, col = 0, 0
# b = size - 1
# Left = size - 1
# f = 1
# move = 'r'
# matrix = [[0 for j in range(size)] for i in range(size)]
# for i in range(1, size * size + 1):
#     matrix[row][col] = i
#     if move == 'r':
#         col += 1
#     elif move == 'l':
#         col -= 1
#     elif move == 'u':
#         row -= 1
#     elif move == 'd':
#         row += 1
#     if i == b:
#         b+=Left
#         if f != 2:
#             f = 2
#         else:
#             f = 1
#             Left -= 1
#         if move == 'r':
#             move = 'd'
#         elif move == 'd':
#             move = 'l'
#         elif move == 'l':
#             move = 'u'
#         elif move == 'u':
#             move = 'r'
# print(matrix)
# for i in (matrix):
#     print(i)




# print(ord("a"))


#2.
#string ascii prime:

# name=input()
# sum=0
# for i in range(len(name)):
#     sum+=(ord("i"))
# c=0
# print(sum)
# for j in range(sum):
#     if sum%i==0:
#         c+=1
# if c>=2:
#     print("prime no.")
# else:
#     print("not prime no.")



#3.
#WAVE PRINT:
# size=int(input("enter a size"))
# c=0
# i=0
# j=0
# matrix=[[0 for i in range(size)]for j in range(size)]
# for k in range(1,size*size+1):
#     if j%2==0:
#         matrix[i][j]=k
#         c+=1
#         if c==size:
#             c=0
#             j+=1
#         else:
#             i+=1
#     elif j%2!=0:
#         matrix[i][j]=k
#         c+=1
#         if c==size:
#             c=0
#             j+=1
#         else:
#             i-=1
# # print(matrix)
# for i in (matrix):
#   print(i)




#4.
# str="12 hours"
# m=""
# s=""
# for i in range(len(str)):
#     if str[i].isdigit():
#         m+=(str[i])
#     else:
#         s+=str[i]
# a=(int(m)*2)
# print(a,s)



#5.
# l=["madhu","mansi","malini"]
# m=""
# c=0
# i=0
# for i in range(len(l[i])):
#     for j in range(len(l)-1):
#         if l[j][i]==l[j+1][i]:
#             if l[j][i] not in m:
#                 m+=l[j][i]
#                 c+=1
# if c>0:
#     print("1")
# else:
#     print("-1")


#6. print counting with half num of loop:
# n=int(input("enter your no."))
# i=1
# b=1
# while i <n//2+1:
#     print(b)
#     print(b+1)
#     b+=2
#     i+=1


#7.convert decimal to binary number:
# n=int(input("enter your decimal number"))
# m=[]
# while n>0:
#     div=n//2
#     r=n%2
#     m+=[r]
#     n=div
# print(m[::-1])



#8.OCCURANCE:
# l=["a","b","a","c","a"]
# k=""
# o=""
# for i in range(len(l)):
#     c=1
#     for j in range(i+1,len(l)):
#         if l[i] in k:
#             continue
#         elif l[i]==l[j]:
#             c+=1
#     if l[i] not in k:
#         f=str(c)
#         k+=f
#         k+=l[i]
# for m  in range(len(k)):
#     if k[m].isalpha():
#         o+=k[m]
#         o+=","
#     else:
#         o+=k[m]
# print(o)



# l=["g","o","o","g","l","e"]
# k=""
# o=""
# for i in range(len(l)):
#     c=1
#     for j in range(i+1,len(l)):
#         if l[i] in k:
#             continue
#         elif l[i]==l[j]:
#             c+=1
#     if l[i] not in k:
#         f=str(c)
#         k+=f
#         k+=l[i]
# for m  in range(len(k)):
#     if k[m].isalpha():
#         o+=k[m]
#         o+=","
#     else:
#         o+=k[m]
# print(o)



#OCCURANCE BY DICTIONARY:
# m="mmadhuuuym"
# s=""
# l=[]
# l1=[]
# dic={}
# for i in range(len(m)):
#     c=1
#     if m[i] not in s:
#         for j in range(i+1,len(m)):
#             if m[i]==m[j]:
#                 c+=1
#                 s+=m[i]
#         l+=[m[i]]
#         l1+=[c]
# dic=dict(zip(l,l1))
# print(dic)



#9.
# age=int(input("enter your age"))
# gender=(input("enter your gendre male or female"))
# exp=int(input("enter your experience"))
# if age>18 and age<35:
#     if exp<=5:
#         if gender=="male":
#             print("he is eligible for manager")
#         else:
#             if gender =="female":
#                 print("she is eligible for manager")
#     else:
#         if gender=="male":
#             print("he is your new consultant")
#         else:
#             if gender=="female":
#                 print("she is new consultant")
# else:
#     print("nothing")

            
    
#ALL ELEMENTS WITHOUT DUPLICATES:
# l=[1,2,3,4,5,6,7,1,2,3]
# for i in range(len(l)):
#     c=0
#     for j in range(0,len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1:
#         print(l[i])
                                                                                

#ALL DUPLICATE ELEMENTS:
# l=[1,2,3,4,5,6,7,1,2,3]
# for i in range(len(l)):
#     c=0
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1:
#         print(l[i])
                                                                                

#ALL UNIQUE ELEMENTS:
# l=[1,2,3,4,5,6,7,1,2,3]
# for i in range(len(l)):
#     c=0
#     for j in range(i,len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1:
#         print(l[i])
                                                                                


#ADD TWO LISTS:
# l=[12,13,14,15]
# l2=[9,5,3,1]
# a=[]
# i=1
# div=0
# while i<=len(l):
#     sum=l[-i]+l2[-i]+div
#     if i==len(l):
#         a+=[sum]
#     else:
#         rem=sum%10
#         div=sum//10
#         a+=[rem]
#     i+=1
# print(a)