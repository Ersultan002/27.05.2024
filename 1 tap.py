list = [21,5,41,6,4,77]

max_number = list[0]
for i in list:
    if i > max_number:
        max_number = i

print(max_number)



list1 = [5,6,7,2,3]

def find_max(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number

print(find_max([55,65,77,25,35]))



class Max:
    def find_max(self):
        list1=[8,95,7,1]
        max_number = list1[0]
        for i in list1:
            if i > max_number:
                max_number = i

        print(max_number)

Obj_max=Max()
Obj_max.find_max()
