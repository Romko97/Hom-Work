boolean_list= [True, True, False, True, True, False, False, True]
print(f"The origion list is{boolean_list}")
res_true, res_false = [],[]
for i, item in enumerate(boolean_list):
    temp = res_true if item else res_false
    temp.append(i)
print(f"True indexes: {res_true}" )
print(f"False indexes: {res_false}" )