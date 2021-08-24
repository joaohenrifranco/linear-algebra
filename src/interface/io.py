import yaml
import os
import string
from datetime import datetime
import numpy as np

join = ''.join

now_string = datetime.now().strftime("%H%M%S")

input_filename = 'input.txt'
output_filename = f'output_{now_string}.txt'
current_dir_path = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir_path, input_filename)
output_file_path = os.path.join(current_dir_path, output_filename)

# def parse_input_file():
#   with open(input_file_path) as file:
#     try:
#         return file.read(file)   
#     except Exception as exc:
#         print(exc)

def write_output_file(data_dict):
    serialized_dict = serialize_dict(data_dict)
    
    with open(output_file_path, 'w') as file:
        try:
            return file.write(serialized_dict)
        except Exception as exc:
            print(exc)

def serialize_dict(data_dict):
    output = ''

    items = lambda row: join((f'{item:.10f} ' for item in row)).strip()
    rows = lambda matrix: join((f'{items(row)}\n' for row in matrix))
    
    for key in data_dict:
        current = data_dict[key]
        current_str = ''

        # is_1d_array = hasattr(current, 'shape') and len(current.shape) == 1
        # if is_1d_array:
        #     current_str += items(current)

        is_2d_array = hasattr(current, 'shape') and len(current.shape) == 2
        if is_2d_array:
            current_str = rows(current)

        has_extra_line_break = len(current_str) > 0 and current_str[len(current_str)-1] == '\n'
        if has_extra_line_break:
            current_str = current_str[0:len(current_str)-1]

        if current_str == '':
            current_str = f'{current}'

        output = f'{output}# {key}\n{current_str}\n'
    print(output)

    return output


# parse_input_file()
write_output_file({'test': 123,  'array': np.array([[1.123123132,2,3.1231234123],[4,5,6],[7,8,9]]), 'asas': "ddd", 'aaa': 2})