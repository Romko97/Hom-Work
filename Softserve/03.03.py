# 1.  Спробуйте переписати наступний код через map.
# Він приймає список реальних імен і замінює їх хеш-прізвищами,
# використовуючи  більш надійний метод-хешування.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names) 

# # => [6306819796133686941, 8135353348168144921, -1228887169324443034]

# names = ['Sam', 'Don', 'Daniel'] 
# a=  map(hash, names)
    
# print(list(a)) 

# 2.  Вивести список кольору “red”, який найчастіше зустрічається
# в даному списку  [“red”, “green”, “black”, “red”, “brown”, “red”,
# “blue”, “red”, “red”, “yellow” ] використовуючи функцію filter.






# spysok = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
# a= filter(lambda x: x =='red', spysok)
# print(list(a))



# 3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’],
# перетворити цей список  в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

spysok = ['1','2','3','4','5','7']

a = map(int, spysok)
print(list(a))

list_int = []
for i in spysok:
    list_int.append(int(i))

print(list_int)

# 4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#    a) використовуючи функцію map
#   b) використовуючи функцію map та lambda

def miles_to_kilometers(num_miles):
    return round(num_miles * 1.6,2)
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)
# 
# Знайти найбільший елемент в списку  використовуючи функцію reduce
# 6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. Повертає колекцію тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
# height_total = 0 
# height_count = 0 
# for person in people: 
#     if 'height' in person: 
#         height_total += person['height'] 
#         height_count += 1 
# print(height_total)
# # => 240