import math as m
import random



#ex_1
# Մուտքագրել բնական թիվ, Ցուցադրել էկրանին,
#  թե ինչ պարզ բաժանարարներից է բաղկացած մուտքագրված բնական թիվը:

# n = int(input("input number"))
# mukuch = 1
# while True:
#     v1 = n / mukuch
#     mukuch += 1
#     if v1 % 1 == 0:
#         flan = 1
#         count = 0
#         while True:
#             fstan = v1 % flan
#             flan += 1
#             if fstan == 0:
#                 count +=1
#             if flan > v1:
#                 break
#         if count == 2:
#             print(v1)
#     if mukuch > n:
#         break



#ex_2
# Գտեք բոլոր կատարյալ թվերը մինչև 10000: 
# Կատարյալ թիվն այն թիվն է, որը հավասար է իր բոլոր բաժանարարների գումարին,
#  բացի իրենից:Օրինակ՝ 6 թիվը կատարյալ է, քանի որ բացի իրենից բաժանվում է 
#  1, 2 և 3 թվերի վրա, որոնք գումարվում են 6-ի։

# for i in range(2,10001):
#     num1 = i
#     sum = 0
#     for j in range(1,num1):
#         mukuch = num1 % j
#         if mukuch == 0:
#             sum += j
#     if sum == i:
#         print(sum)



#ex_3
# Մուտքագրեք նմական թվերի միջակայք՝ սկիզբ և վերջ, ինչպես նաև քանակ,
#  Բնական թվերի մուտքագրված միջակայքում գտե՛ք նրանց,
#   որոնց բաժանարարների թիվը մուտքագրված քանակից պակաս չէ։
#  Գտնված թվերի համար ցուցադրեք բաժանարարների և բոլոր բաժանարարների թիվը:

# start1 = int(input("input start"))
# stop1 = int(input("input stop"))
# count1 = int(input("input count"))

# for i in range(start1,stop1+1):
#     v1 = i
#     k1 = 0
#     count2 = 0
#     list1 = []
#     while True:
#         k1 += 1
#         mukuch = v1 % k1
#         if mukuch == 0:
#             count2 +=1
#             list1.append(k1)
#         if k1 > v1:
#             break
#     if count2 >= count1:
#         print(f"the {v1} has {count2} divisors {list1} ")



#ex_4
# Գրել ծրագիր որը կգեներացնի list որի երկարությունը կլինի 10 
# իսկ էլեմենտներ պետք է լինեն  1000 - 9999 միջակայքում բնական թվեր,
#  բնական թվերից թվանշանների գումարում գտե՛ք ամենամեծը։ 
# Ցուցադրել այս թիվը և նրա թվանշանների գումարը:

# list1 = []
# list2 = []
# for i in range(1,11):
#     j = random.randint(1000,10000)
#     list1.append(j)
#     sum1 = 0
#     for k1 in str(j):
#         sum1 += int(k1)
#     list2.append(sum1)
# list2.sort()
# print(list2[-1])      
# print(list1)






n1 = random.randint(10,100)
sum = 0
while True:
    v1 = n1 % 10
    sum += v1
    if v1 == 0:
        break 
print(f"{n1} , {sum}")