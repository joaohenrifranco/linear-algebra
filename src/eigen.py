import sys
import interface.io as io

import core.eigen.jacobi as jacobi
import core.eigen.power_method as power_method
from core.systems.lu import computeDeterminant


def run():
    fileManager = io.FileManager(
        input_file_path=sys.argv[1], output_file_path=sys.argv[2])

    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]
    tolm = input_dict["tolm"]
    idet = input_dict["idet"]

    enableDet = False
    if idet > 0:
        enableDet = True

    output_dict = {}

    if enableDet:
        output_dict["determinant"] = computeDeterminant(
            input_dict["A"], copy=True)

    try:
        if icod == 1:
            output_dict["eigenvector"], output_dict["eigenvalue"], output_dict["iteration_count"] = power_method.run(
                input_dict["A"], tolm
            )

        elif icod == 2:
            output_dict["eigenvectors"], output_dict["eigenvalues"], output_dict["iteration_count"] = jacobi.run(
                input_dict["A"], tolm
            )

        else:
            output_dict["error"] = 'Invalid ICOD'

    except Exception as exc:
        raise(exc)
        output_dict["error"] = str(exc)

    fileManager.write_output(output_dict)


run()
