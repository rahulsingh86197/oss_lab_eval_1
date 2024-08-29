attend = []

def mark_present(name):
    if name not in attend:
        attend.append(name)
        print("Name added succesfully")
    else:
        print("Name already present")

def remove_student(name):
    if name in attend:
        attend.remove(name)
        print("Name removed successfully")
    else:
        print("Name not found")

        
def is_present(name):
    pre = False
    if name in attend:
        pre = True
    return pre


def display_attendance():
    print(attend)

def quick_sort(arr):
    
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

def check(name1,name2):
    large = False
    if(name1[0] > name2[0]):
        large = True
    return large


def bubble_sort():
    i = 0
    length = len(attend)

    while i < length-1:
        j = i;
        while j < length-1:
            if(check(attend[j],attend[j+1])):
               temp = attend[j]
               attend[j]= attend[j+1]
               attend[j+1] = temp

               
    

i = int(input("Np. of student : "))

while i > 0:
    add = input("Add name : ")
    mark_present(add)
    i = i-1

rem = input("Remove name : ")
remove_student("Rama")


print("Check if Ram is present : ")
print(is_present("Ram"))

print("The names of present students : ")
display_attendance()

sorted_arr = []
sorted_arr = quick_sort(sorted_arr)

print("Sorted names : ")

display_attendance()
