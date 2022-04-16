import math as m
import random


#ex_1
# Գրեք ծրագիր, որը կավելացնի, հանի, կբազմապատկի կամ կբաժանի երկու թվեր: 
# Գործողության համարները և նշանը մուտքագրվում են օգտագործողի կողմից:
# Հաշվարկն ավարտելուց հետո ծրագիրը չպետք է դադարեցվի, 
# այլ պետք է պահանջի նոր տվյալներ հաշվարկների համար։ 
# Ծրագրի ավարտը պետք է իրականացվի՝ որպես գործողության նշան մուտքագրելով «0» նիշը:
# Եթե ​​օգտագործողը մուտքագրում է անվավեր նիշ (ոչ թե «0», «+», «-», «*», «/»),
# ապա ծրագիրը պետք է տեղեկացնի նրան սխալի մասին և նորից հարցնի գործողության բնույթը։
# Նաև տեղեկացրեք օգտատիրոջը զրոյի վրա բաժանելու անհնարինության մասին,
# եթե նա որպես բաժանարար մուտքագրել է 0։

# fstan = 10
# while fstan > 0:
#     n1 = int(input("input first number"))
    # v = input("input action")
    # n2 = int(input("input second number"))
    # sum1 = n1 + n2
    # sum2 = n1 - n2
    # sum3 = n1 * n2
    # sum4 = n1 / n2
    # if v == "0":
    #     break
    # elif v == "+":
    #     print(f"{n1}+{n2}={sum1}")
    # elif v == "-":
    #     print(f"{n1}-{n2}={sum2}")
    # elif v == "*":
    #     print(f"{n1}*{n2}={sum3}")
    # elif v == "/":
    #     if n2 == 0:
    #         print("the number can not be divided by 0")
    #     else:
    #         print(f"{n1}/{n2}={sum4}")
    # else:
    #     print("the action is unknown, try again")
    # fstan += 1



#ex_2
# Գտե՛ք թվերի հետևյալ շարքի n տարրերի գումարը՝ 1 -0,5 0,25 -0,125 ...
#  Ստեղնաշարից մուտքագրվում է տարրերի թիվը (n):

    
# n1 = int(input("input number"))
# v1 = 1
# count = 1
# summ = 1
# fstan = 6
# while fstan < 10:
#     v1 /= -2
#     summ += v1
#     count += 1
#     if count == n1:
#         print(summ)
#         break
#     else:
#         count += 0


#ex_3
# Ստեղնաշարից ստանալով N, գծեք N կողմով քառակուսի, 
#  որի էլեմենտները կլինեն ‘*’, իսկ անկյունագծերը կլինեն ‘#’:

# n = 6
# list1 = []
# for i in range(n):
#     row = ['.' for _ in range(n)]
#     list1.append(row)
# for i in range(len(list1)):
#     list1[0][i] = '0'
#     list1[i][-1] = '0'
#     list1[i][0] = '0'
#     list1[-1][i] = '0'
# for i in list1:
#     print(i)





    


# ex_4
# Գեներացրեք է 2-ից մեծ տասը բնական թիվ։
#  Հաշվիր, թե քանի պարզ թիվ կա դրանց մեջ:

# arqimed = 0
# count2 = 0
# while arqimed < 10:
#     n = random.randint(2,100)
#     print(n)
#     v1 = 2
#     count1 = 0
#     while v1 <= n:
#         mukuch = n % v1
#         print(f"{n}%{v1}={mukuch}")
#         if mukuch == 0:
#             count1 += 1
#         v1 += 1
#     if count1 == 1:
#         count2 += 1
#     arqimed += 1
# print(count2)
    

# Ստուգեք փակագծերը: Դուք ունեք 3 տեսակի փակագծեր ՛() [] {}՛, օրինակ:
#  ՛({{}} {] []}})՛! Ստուգեք, որ յուրաքանչյուր բաց փակագիծ ունի փակ փակագիծ:
#   Այսինքն ձեր ծրագիրը պետք է վերադարձնի True կամ False, Օրինակ՝ 
#   եթե մոտքագրել եք '{}()[]' կամ '({[]}){}()' ծրագիրը կվերադարձնի True,
#    իսկ եթե մուտքագրել եք '([){]}' կամ ((()){}[] ծրագիրը կվերադարձնի False:

# string = '([()]){[()]}()'
# st = ''
# for i in string:
#     if i == '{':
#         st += i
#     elif i == '[':
#         st += i
#     elif i == '(':
#         st += i
#     elif i == '}':
#         if st[-1] != '{':
#             print(False)
#             break
#         st = st[:-1]
#     elif i == ']':
#         if st[-1] != '[':
#             print(False)
#             break
#         st = st[:-1]
#     elif i == ')':
#         if st[-1] != '(':
#             print(False)
#             break
#         st = st[:-1]
# else:
#     if len(st) != 0:
#         print(False)
#     else:
#         print(True)


# Գրել ծրագիր որը կգեներացնի list որի երկարությունը կլինի 10 
# իսկ էլեմենտներ պետք է լինեն  1000 - 9999 միջակայքում բնական թվեր,
#  բնական թվերից թվանշանների գումարում գտե՛ք ամենամեծը։
#  Ցուցադրել այս թիվը և նրա թվանշանների գումարը:


flan = 0
while flan < 10:
    list1 = 0
    n = random.randint(1000,10000)
    list1 = n
    flan += 1
    count = 0
    for i in list1:
        j  = i % 10
        i //= 10
        count += j
    print(list1)
    

 
# list1 = random.randint(100,1000)
# summ = 0
# for i in list1:
#     i // 10
#     if i < 10:
#         v1 = i
#     summ += v1
# print(summ)