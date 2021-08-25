import sys
import interface.io as io

import core.systems.lu as lu
import core.systems.jacobi as jacobi
import core.systems.gauss_seidel as gauss_seidel
import core.systems.cholesky as cholesky

def run():
    fileManager = io.FileManager(input_file_path=sys.argv[1], output_file_path=sys.argv[2])
    
    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]

    output_dict = {}

    try:
        if icod == 1:
            output_dict["X"] = lu.solve(input_dict["A"], input_dict["B"])
        elif icod == 2:
            cholesky.solve()
        elif icod == 3:
            jacobi.solve()
        elif icod == 3:
            gauss_seidel.solve()
    except Exception as exc:
        output_dict["error"] = exc

    fileManager.write_output(output_dict)

run()