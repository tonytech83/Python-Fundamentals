def save_dwarf(dwarf_data, dwarf):
    dwarf_name = dwarf[0]
    dwarf_hat_color = dwarf[1]
    dwarf_physics = int(dwarf[2])

    if dwarf_hat_color not in dwarf_data:
        dwarf_data[dwarf_hat_color] = {}
        if dwarf_name not in dwarf_data[dwarf_hat_color]:
            dwarfs_data[dwarf_hat_color][dwarf_name] = 0
            if dwarfs_data[dwarf_hat_color][dwarf_name] < dwarf_physics:
                dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics
        else:
            if dwarfs_data[dwarf_hat_color][dwarf_name] < dwarf_physics:
                dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics
    else:
        if dwarf_name not in dwarf_data[dwarf_hat_color]:
            dwarf_data[dwarf_hat_color][dwarf_name] = 0
        if dwarf_data[dwarf_hat_color][dwarf_name] < dwarf_physics:
            dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics


dwarfs_data = {}

while True:
    line = input()
    if line == 'Once upon a time':
        break
    dwarf_info = line.split(' <:> ')
    save_dwarf(dwarfs_data, dwarf_info)

dwarfs_info_list = {}
color_count = {}

for color, dwarf_inf in dwarfs_data.items():
    if color not in color_count:
        color_count[color] = 0
        color_count[color] = len(dwarf_inf)
    else:
        color_count[color] += len(dwarf_inf)

    for name, physic in dwarf_inf.items():
        d_name = f'{color}:{name}'
        d_physic = [physic, color]
        if color not in dwarfs_info_list.keys():
            dwarfs_info_list[d_name] = d_physic
        else:
            dwarfs_info_list[d_name] = d_physic

for color_dwarf, physic in sorted(dwarfs_info_list.items(), key=lambda kvp: (kvp[1][0], color_count[kvp[1][1]]),
                                  reverse=True):
    color, name = color_dwarf.split(':')
    print(f'({color}) {name} <-> {physic[0]}')
