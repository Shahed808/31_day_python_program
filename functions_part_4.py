''' sum func()'''

# def imp():
#     a = int(input("Enter the value of a :"))
#     b = int(input("Enter the value of b :"))
#     c = a+b
#     # return c
#     # return (f"The value of {a}+{b} is {c}")
#     return ("The value of {} + {}is {}".format(a,b,c))
# print(imp())


''' function definition'''

# def tug(a,b):
#     add=a+b
#     print("the add is ",add)
# def guc(a,b):
#     sub=a-b;div=a/b
#     print("sub is ",sub, "div is ",div)

# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))
# tug(a,b)                                # the add is  30
# guc(a,b)                                # sub is  -10 div is  0.5
    
    
''' printing the def func using return func'''

# def kil(z,y):
#     h=z+y
#     t=z-y
#     k=z**y
#     return h,t,k
# z=int(input("Enter the value of z :"))
# y=int(input("Enter the value of y :"))
# # print(kil(z,y))
# kil(z,y)
# h,t,k=(kil(z,y))
# print("The sum of z+y is",h,"the sub of z-y is ",t,"the exp of z**y is ")
# print(f"The value of {z} + {y} is {h}, The value of {z} - {y} is {t}, The value of {z} ** {y} is {k}")

''' function return several values '''
# def ts(a1,a2):
#     p= a1+a2
#     q=a1-a2
#     r=a1/a2
#     s=a1*a2
#     return p,q,r,s
# a1=float(input("Enter any number :"))
# a2=float(input("Enter any number :"))
# print(ts(c,d))
# ts(a1,a2)
# ts(a1,a2)
# p,q,r,s = ts(a1,a2)
# print(p,q,r,s)
# ap=ts(c,d)
# for j in ap:
#     print(j)
# print(ap)
# print(f"The add of {a1} +{a2} is {p}, The sub of {a1}- {a2} is {q}, The div of {a1} / {a2} is {r}, The mul of {a1} * {a2} is {s}")
# print("The add of a1+a2 is ",p, "The sub of a1-a2 is",q, "The div of a1/a2 is",r, "The mul of a1*a2 is",s)



''' sorting group of numbers'''

# def lim(kim):
#     kim.sort()
#     print(kim)
#     for n in kim:
#         print(n,end=' ')
# f= [int(w) for w in input("Enter the value of f :").split()]
# lim(f)

# ''' 2nd method'''
# lus=[int(e) for e in input().split()]
# lus.sort(reverse=True)
# print(lus)


''' Note: The value of the global variable can be used by local function variable
  containing print .
  But the value of the local variable cannot be used by the global function variable
  containing print.'''

# r = 10
# def num():
#     r = 25
#     print(r)                  # 10
# num()                         # 25
# print(r)                      # 25

''' if we want to use local variable as global then we can use this method '''
# r = 10
# def num():
#     global r
#     r = 25
#     print(r)                              
# print(r)                                    # 10
# num()                                       # 25
# print(r)                                    # 25

''' assign the func to variable'''

# def var(n1):
#     return 'hii'+" " + n1
# str=input("Enter any name :")
# f1=var(str)
# print(f1)                                       # hii dss
# print(var("coding"))                            # hii coding


# def char(n1):
#     return print('hii'+" " + n1) 
# n1=input("Enter any name :")
# print(f"The name of the session is {n1}")
# char('hii')
# char('hack')


''' function inside the function '''

# def yup(sut):
#     def message():
#         return "Where are you from? " 
#     g = message()+sut
#     return g
# t = input("Enter any name ")
# b= yup(t)
# print(b)                                # Where are you from? pubg


''' passing paramerter to another function '''

# def bes(carie):
#   return ("How is your job going on?"+carie)
# def mess():
#   return b
# b = input("Enter any name :")
# r = bes(b)
# print(r)                # How is your job going on?kar
# x = bes(mess())
# print(x)                # How is your job going on?kar
# print(bes("dor"))       # How is your job going on?dor
# u=mess()
# print(u)                 # kar


''' returning another func'''

# def dir():
#   def mig():
#     return "I am from future"
#   return mig
# n = dir()
# print(n())


''' '''
# def o(pre):
#   l = "Hii "+pre
#   return l
# c = input("Enter any name :")
# print(o(c))

def hr(sum):
  sum.insert(1,77)
  return sum
sum=[1,8,9,5,4,1,0,2,6]
print(hr(sum))

def hr(sum):
  sum.pop()
  return sum
sum=[int(e) for e in input("Enter the values : ").split()]    # Enter the values : 1 5 6 2  5 6 1  9 5 2 6 3
print(hr(sum))            # [1, 5, 6, 2, 5, 6, 1, 9, 5, 2, 6]