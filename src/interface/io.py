import os
from datetime import datetime
import numpy as np
import json

join = ''.join

now_string = datetime.now().strftime("%H%M%S")

input_filename = 'input.json'
output_filename = f'output_{now_string}.json'
current_dir_path = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir_path, input_filename)
output_file_path = os.path.join(current_dir_path, output_filename)

class NumpyDecoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        if isinstance(obj, (np.float_, np.float16, np.float32,
                            np.float64)):
            return float(obj)
        if isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def parse_input_file():
    with open(input_file_path) as file:
        try:
            dict = json.load(file)
        except Exception as exc:
            print(exc)

    for key in dict:
        if isinstance(dict[key], list):
            dict[key] = np.array(dict[key])

    return dict

def write_output_file(data_dict):
    with open(output_file_path, 'w') as file:
        try:
            return json.dump(data_dict, file, cls=NumpyDecoder)
        except Exception as exc:
            print(exc)


parse_input_file()
write_output_file({'test': 123,  'array': np.array(
    [[1.123123132, 2, 3.1231234123], [4, 5, 6], [7, 8, 9]]), 'asas': "ddd", 'aaa': 2})
