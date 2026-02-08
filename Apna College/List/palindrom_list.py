list = [1, "ABC", 1]
cpy_list = list.copy()
cpy_list.reverse()
if(cpy_list == list):
    print("YES")
else:
    print("NO")