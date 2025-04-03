def add_tree_copies(my_list,data):

    for i in range(3):
        my_list.append(data)
    
my_list = []
message = input(" \033[1;3m enter message to a copy: \033[0m")
print("list before = " ,my_list)
add_tree_copies(my_list,message)
print("List after = ", my_list)

