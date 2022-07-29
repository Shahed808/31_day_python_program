''' how to use local function as global
 we cannot call the local func untill unless the function is called then only we can call the local func as global'''

# t = 5
# def fuc():
#     global c,t
#     c=10;t=25.2;g=56
#     print(c)
#     print(g)
#     print(t)
# print(t)
# fuc()
# print(t)
# print(c)
# print(t)


''' count  the length of the string without using the built in function'''

# def tuc(m):
#     w=0
#     for i in m:
#         w+=1
#     return w
# print(tuc('python'))                                # 6 (Doubt)


''' having multiple def func and calling each def by other def func'''


# def wk(name='mohd'):
#     print("My name is ",name)
#     ag()
# def ag(age=23):
#     print("my age is ",age)
#     yr()
# def yr(year=2021):
#     print("I am in",year)
# wk()