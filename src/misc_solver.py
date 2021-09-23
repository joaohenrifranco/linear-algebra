import sys
import io

import core.misc.derivative as derivative
import core.misc.derivative_richard_ext as derivative_richard_ext
import core.misc.integral as integral
import core.misc.roots as roots


def main():
    fileManager = io.FileManager(
        input_file_path=sys.argv[1], output_file_path=sys.argv[2])

    input_dict = fileManager.parse_input()
    icod = input_dict["icod"]

    output_dict = {
        "inputs": input_dict
    }

    try:
        if icod == 1:
            a = input_dict['a']
            b = input_dict['b']
            constants = input_dict['constants']
            tolm = input_dict['tolm']
            method = input_dict['method']
            output_dict['root'] = roots.solve(a, b, constants, tolm, method)

        elif icod == 2:
            n = input_dict['n']
            a = input_dict['a']
            b = input_dict['b']
            constants = input_dict['constants']
            method = input_dict['method']
            output_dict['integral'] = integral.solve(
                a, b, n, constants, method)

        elif icod == 3:
            dX = input_dict['dX']
            a = input_dict['a']
            constants = input_dict['constants']
            method = input_dict['method']
            output_dict['derivative'] = derivative.solve(
                a, dX, constants, method)

        elif icod == 4:
            dX = input_dict['dX']
            constants = input_dict['constants']
            output_dict['extrapolation'] = derivative_richard_ext.solve(
                dX[0], dX[1], constants)

        else:
            output_dict['error'] = 'Invalid code'

    except Exception as e:
        output_dict['error'] = str(e)

    fileManager.write_output(output_dict)


main()
