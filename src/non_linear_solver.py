import sys
import interface.io as io

import core.non_linear.newton as newton
import core.non_linear.broyden as broyden


def run():
    fileManager = io.FileManager(
        input_file_path=sys.argv[1], output_file_path=sys.argv[2])

    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]
    tolm = input_dict["tolm"]
    teta = input_dict["teta"]

    max_iter = 5000
    X0 = [1, 0, 0]

    output_dict = {
        "consts": {"max_iter": max_iter, "X0": X0},
        "inputs": input_dict,
    }

    try:
        if icod == 1:
            output_dict["solution"] = newton.solve(
                X0, teta, max_iter, tolm
            )

        elif icod == 2:
            output_dict["solution"] = broyden.solve(
                X0, teta, max_iter, tolm
            )

        else:
            output_dict["error"] = 'Invalid ICOD'

    except Exception as exc:
        output_dict["error"] = str(exc)

    fileManager.write_output(output_dict)

run()
