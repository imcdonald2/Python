def show_magicians(list):
    for magician in list:
        print(magician)

def make_great(list):
    magic_list = []
    for individual in list:
        individual = individual + ' the Great'
        magic_list.append(individual)
    return magic_list

magician_list = ['merlock', 'Houdini', 'Penn']
new_list = make_great(magician_list)
show_magicians(new_list)
print(magician_list)
