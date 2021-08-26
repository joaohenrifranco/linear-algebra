import sys
import interface.io as io

import core.interpolation.lagrange as lagrange
import core.interpolation.regression as regression


def run():
    fileManager = io.FileManager(
        input_file_path=sys.argv[1], output_file_path=sys.argv[2])

    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]

    output_dict = {}

    try:
        if icod == 1:
            output_dict["y"] = regression.get_interpolated(input_dict["P"], input_dict["x"])

        elif icod == 2:
            output_dict["y"] = lagrange.get_interpolated(input_dict["P"], input_dict["x"])

        else:
            output_dict["error"] = 'Invalid ICOD'

    except Exception as exc:
        output_dict["error"] = str(exc)

    fileManager.write_output(output_dict)


run()
