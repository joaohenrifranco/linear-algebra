import sys
import interface.io as io

import core.systems.lu as lu
import core.systems.jacobi as jacobi
import core.systems.gauss_seidel as gauss_seidel
import core.systems.cholesky as cholesky


def run():
    fileManager = io.FileManager(
        input_file_path=sys.argv[1], output_file_path=sys.argv[2])

    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]

    output_dict = {}

    try:
        if icod == 1:
            output_dict["X"] = lu.solve(input_dict["A"], input_dict["B"])
        
        elif icod == 2:
            output_dict["X"] = cholesky.solve(input_dict["A"], input_dict["B"])
        
        elif icod == 3:
            output_dict["X"] = jacobi.solve(
                input_dict["A"], input_dict["B"], input_dict["tolm"])
        
        elif icod == 3:
            output_dict["X"] = gauss_seidel.solve(
                input_dict["A"], input_dict["B"], input_dict["tolm"])
    
    except Exception as exc:
        print(exc)
        output_dict["error"] = str(exc)

    fileManager.write_output(output_dict)

run()
