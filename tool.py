def get_id():
    while True:
        try:
            ID = int(input("What is the user ID?\n"))
        except ValueError:
            print("Not an integer.")
            continue
        if len(str(ID)) < 6:
            print("Not a valid ID")
            continue
        else:
            return ID

def roleID():
    role_list = [4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 22, 27, 38, 54, 71, 72, 73,
    77, 78, 83, 84, 87, 88, 89, 90, 92, 94, 130, 132, 133, 134, 135, 136, 137, 138, 139, 140]

    while True:
        role_selected = input("Enter role IDs separated by spaces.\n")
        role_selected = role_selected.split()
        for role in role_selected:
            if int(role) not in role_list:
                print(str(role) + " is not a valid roleID")
                role_selected.remove(role)
        return role_selected

"""
def append_role(userid, rolelist):
    appended_list = []
    for role in rolelist:
        appended_list.append("(" + userid + ", " + role + ")")
    return appended_list
"""



get_id = get_id()
role_input = roleID()
#append_role = append_role(get_id, roleID)

print(get_id)
print(role_input)
#print(append_role)
