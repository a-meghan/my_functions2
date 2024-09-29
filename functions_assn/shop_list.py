#Task 1

shopping_list = []

def addItems(list):
    print("Let's add some things to our shopping list!")
    while True:
        item = input("Add items to your list, and enter 'done' when finished. ")
        if item.lower() == "done":
            break
        list.append(item)
        print(f'{item.title()} added to shopping list.')

addItems(shopping_list)
print(shopping_list)

#Task 2
def removeItems(list):
    print("\nAnything you want to remove? ")
    while True:
        del_item = input("Tell me what items you would like to remove, and enter 'done' when finished. ")
        if del_item.lower() == "done":
            break
        if del_item in list:
            list.remove(del_item)
        else:
            print("Item is not in shopping list.")
        
removeItems(shopping_list)
print(shopping_list)

#Task 3
def format_list(list):
    print("\nLets see what this looks like all nice & neat!")
    abc_list = sorted(list)
    for item in abc_list:
        print(item.title())

format_list(shopping_list)