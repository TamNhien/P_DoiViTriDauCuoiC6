def swapfirstlast3(lst):
    if len(lst) >= 2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst
lst = [12, 35, 9, 56, 24]
print("The original input is: ",lst)

result=swapfirstlast3(lst)

print("The output after swap first and last is: ",result)

