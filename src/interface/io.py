import os
from datetime import datetime
import numpy as np
import json

join = ''.join




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

class FileManager:
    def __init__(self, input_file_path, output_file_path):
        # Old method
        # self.created_time = datetime.now().strftime("%H%M%S")
        # self.current_dir_path = os.path.dirname(os.path.abspath(main_file))
        # self.input_filename = 'input.json'
        # self.output_filename = f'output_{self.created_time}.json'
        # self.input_file_path = os.path.join(self.current_dir_path, self.input_filename)
        # self.output_file_path = os.path.join(self.current_dir_path, self.output_filename)
        
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def parse_input(self):
        dict = {}
        with open(self.input_file_path) as file:
            try:
                dict = json.load(file)
            except Exception as exc:
                print(exc)

        for key in dict:
            if isinstance(dict[key], list):
                dict[key] = np.array(dict[key])

        return dict

    def write_output(self, data_dict):
        with open(self.output_file_path, 'w') as file:
            try:
                return json.dump(data_dict, file, cls=NumpyDecoder)
            except Exception as exc:
                print(exc)
