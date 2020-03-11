# завдання 12
# dikt = {}
# dikt[1]=1
# dikt['1'] = 2
# dikt[1]+=1
# print(dikt)
# sum = 0
# for k in dikt:
#     print(k)
#     sum += dikt[k]
# print(sum)

#завдання13
#як працює strip
# name = 'aaaa  aaa Academyaaa aa aaa'
# print(name+'123')
# name.strip('a')
# print(name+'123')
# print(name.strip("a") + '123')


#завдання15
# name = "SoftSerf IT Academy"
# print(id(name))
# print(id(name.replace('o','Q')))
# a = name.replace('o','Q')
# print(a)
# print(id(a))
# print(name)
# print(id(name))



#завдання24
#def parse_numbers(num):
#     try:
#         num_to_str = str(num)
#         count_of_event = {int(x) for x in num_to_str if int(x)%2==0}
#         count_of_odd = {int(x) for x in num_to_str if not int(x)%2==0}
#         return {"ood": len(count_of_odd),"even": len(count_of_event)}
#     except ValueError:
#         return False
#     except TypeError:
#         return False

# print(parse_numbers(1100))

#завдання17

# les = ['4', '5', '6', '9','10','12','15']
# les1=les
# les2 = les1[:]
# print(les)
# print(les1)
# print(les2)
# print(id(les))
# print(id(les1))
# print(id(les2))

# les1[0] = '2'
# les2[1] = '3'
# sum = 0 
# for i in (les, les1, les2):
#     print(i)
#     if i[0] == '2':
#         sum += 1
#     if i[1] =='3':
#         sum +=10
# print(sum)


# print(type(lambda:None))

# num = {1,2,3,6,5,2,5,8,1}
# print(len(num))
# print(num)
# print(type(num))

# def fibo(n):
#     f = [1,1]
#     for i in range(2,n):
#         f.append(f[i-1]+f[i-2])
#     return f

# print(fibo(6))

# name = "snow storm"
# name[5] = 'X'
# print(name)