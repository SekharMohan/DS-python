from ds_sorting.bubble_sort import BubbleSort

print("Sorting Algorithms :)")
print("*************************")

print("Bubble Sort!")
arr = [int]
b_sort = BubbleSort()
no_of_element = int(input("Enter the no of element to sort"))
for x in range(0, no_of_element):
    var = int(input())
    arr.insert(x, var)
print(arr)
b_sort.sortElements(arr)