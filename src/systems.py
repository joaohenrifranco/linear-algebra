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
    idet = input_dict["idet"]

    output_dict = {}

    if (icod == 3 or icod == 4) and idet != 0:
        output_dict["warning"] = 'Determinant is not supported by this method'

    enableDet = False
    if idet > 0:
        enableDet = True

    try:
        if icod == 1:
            output_dict["X"], output_dict["determinant"] = lu.solve(input_dict["A"], input_dict["B"], enableDet)
        
        elif icod == 2:
            output_dict["X"], output_dict["determinant"] = cholesky.solve(input_dict["A"], input_dict["B"], enableDet)
        
        elif icod == 3:
            output_dict["X"] = jacobi.solve(
                input_dict["A"], input_dict["B"], input_dict["tolm"])
        
        elif icod == 4:
            output_dict["X"] = gauss_seidel.solve(
                input_dict["A"], input_dict["B"], input_dict["tolm"])
        
        else:
            output_dict["error"] = 'Invalid ICOD'
    
    except Exception as exc:
        output_dict["error"] = str(exc)

    if (not enableDet):
        output_dict.pop('determinant', None)

    fileManager.write_output(output_dict)

run()
