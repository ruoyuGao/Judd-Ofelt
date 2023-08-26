import math
import os

input_main_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input/input_mag')
output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

h = 6.626e-27  # Planck constant
e = 4.8e-10  # Charge of electron
m = 9.105e-28  # Mass of electron
c = 2.998e+10  # Velocity of light
pi = math.pi  # Circumference of unit circle
nre = 1.96

def process_magnetic(input_path: str, output_path: str):
    with open(input_path, "r") as f, open(output_path, "w") as f2:
        for line in f:
            mu,s,j,l,a = [float(x) for x in line.split(',')]
            fed = 0
            ff = 0
            if a == 1:
                fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * ((s + l + j + 1) * (s + l + 1 - j) * (j + s - l) * (j + l - s) / (4 * j))
                ff = ((s + l + j + 1) * (s + l + 1 - j) * (j + s - l) * (j + l - s) / (4 * j))
                print("FFF", ff / (2 * j + 1))
            if a == 0:
                fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * (1 + (j * (j + 1) + s * (s + 1) - l * (l + 1)) / 2 / j / (j + 1)) ** 2 * (j * (j + 1) * (2 * j + 1))
                ff = (1 + (j * (j + 1) + s * (s + 1) - l * (l + 1)) / 2 / j / (j + 1)) ** 2 * (j * (j + 1) * (2 * j + 1))
            if a == 2:
                fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * ((s + l + j + 2) * (s + j + 1 - l) * (l + j + 1 - s) * (s + l - j) / (4 * (j + 1)))
                ff = ((s + l + j + 2) * (s + j + 1 - l) * (l + j + 1 - s) * (s + l - j) / (4 * (j + 1)))
                print("sdf", ff / (2 * j + 1))
            
            all_var = (4 * pi ** 2 * e ** 2 * nre ** 3 * h * mu ** 3) / (3 * (2 * j + 1) * m ** 2 * c ** 2) * ff
            aij = 8 * pi ** 2 * e ** 2 * mu ** 2 * nre ** 2 * fed / m / c

            print("matrix element:", ff)
            print("fmd=", fed)
            print("A", aij)

            f2.write(f"m={mu}, s={j}, l={l}, a={a}.\n")
            f2.write(f"matrix element:{ff}\n")
            f2.write(f"fmd={fed}\n")
            f2.write(f"A={aij}\n")

if __name__ == "__main__":
    whole_input_path = os.path.join(input_main_folder_path, "magnetic.csv")
    whole_output_path = os.path.join(output_folder_path, "magnetic_output.csv")
    process_magnetic(whole_input_path, whole_output_path)