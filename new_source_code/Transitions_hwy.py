import os
import numpy as np
import constants as CONSTANTS

nre = 2.60
omig = [0.0, 9.83 * 1E-21, 7.08 * 1E-21, 3.08 * 1E-21]
input_main_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input/input_trans')
output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

def process_transitions_hwy(input_path: str, output_path: str):
    print(input_path)
    print(output_path)
    with open(input_path, "r") as f, open(output_path, "w") as f2:
        for j in range(1, 9):
            lvl = f.readline().rstrip(" \n")
            print(lvl)
            for i in range(1, 9):
                la, mu, mj, u2, u4, u6 = [x for x in f.readline().split(',')]
                mu = float(mu)
                mj = float(mj)
                u2 = float(u2)
                u4 = float(u4)
                u6 = float(u6)
                # print(mu)
                print(la, mu, mj, u2, u4, u6)

                con =  (27 * CONSTANTS.h * (2 * mj + 1) * nre) / (8 * CONSTANTS.pi ** 2 * CONSTANTS.mass * CONSTANTS.Vc * mu * (nre ** 2 + 2) ** 2)
                fcal = (omig[1] * u2 ** 2+ omig[2] * u4 ** 2 + omig[3] * u6 ** 2) / con
                a = (64 * CONSTANTS.pi ** 4 * CONSTANTS.e ** 2 * nre * (nre ** 2 + 2) ** 2) * mu ** 3 / (27 * (2 * mj + 1) * CONSTANTS.h) * (omig[1] * u2 + omig[2] * u4 + omig[3] * u6)

                f2.write(f'{lvl},{la},{mu},{int(fcal * 1E+10) / 100},{int(100 * a) / 100}\n')

                if la == "4i15/2":
                    break
            

if __name__ == "__main__":
    whole_input_path = os.path.join(input_main_folder_path, "a.txt")
    whole_output_path = os.path.join(output_folder_path, "tran-2.csv")

    process_transitions_hwy(whole_input_path, whole_output_path)

