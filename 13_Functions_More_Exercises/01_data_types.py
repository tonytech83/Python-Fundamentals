def data_type_result(data):
    data_type = data[0]
    if data_type == 'int':
        return int(data[1]) * 2
    elif data_type == 'real':
        return f'{(float(data[1]) * 1.5):.2f}'
    else:
        return f'${data[1]}$'


received_data = []
for _ in range(2):
    line = input()
    received_data.append(line)

print(data_type_result(received_data))
