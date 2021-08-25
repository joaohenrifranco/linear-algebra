import sys
import interface.io as io

import core.systems.lu as lu
import core.systems.jacobi as jacobi
import core.systems.gauss_seidel as gauss_seidel
import core.systems.cholesky as cholesky

def main():
    fileManager = io.FileManager(input_file_path=sys.argv[1], output_file_path=sys.argv[2])
    input_dict = fileManager.parse_input()

    if input_dict["icod"] == 1:
        lu.solve()
    elif input_dict["icod"] == 2:
        jacobi.solve()


main()