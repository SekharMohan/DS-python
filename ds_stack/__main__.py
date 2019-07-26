from ds_stack.stack import Switcher

print("STACK SAMPLES \n ***************************")

print("Enter your option: \n -----------------------------")
print("1:Stack with Array \n 2:Stack with Linked List")

switcher = Switcher()

option = int(input())

switcher.stack_type(option)



