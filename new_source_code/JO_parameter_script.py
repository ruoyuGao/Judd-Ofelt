import os
import numpy as np
import constants as CONSTANTS


def process_all_files(input_folder_path: str, output_folder_path: str):
    """
    Process all files in a folder
    """
    for filename in os.listdir(input_folder_path):
        outpu_filename = filename.replace('input', 'output')
        input_file_path = os.path.join(input_folder_path, filename)
        output_file_path = os.path.join(output_folder_path, outpu_filename)
        # open file and calculate the JO parameter
        clean_output_file(output_file_path)
        B = process_JO_parameter(input_file_path, output_file_path)
        process_theoretical_oscillator_sthengths(B, input_file_path, output_file_path)
    
def process_JO_parameter(input_file_path: str, out_put_file_path: str) -> list:
    """
    Calculate the JO parameter for a file
    """
    # open file and calculate the JO parameter
    with open(input_file_path, "r") as f:
        M, N, nre, thickness, concen, mj = [float(x) for x in f.readline().split(',')]
        M = int(M)
        N = int(N)
        nre = float(nre)
        print(f"File: {input_file_path} - M: {M}, N: {N}, nre: {nre}, thickness: {thickness}, concen: {concen}, mj: {mj}")
        Fex = np.zeros(int(M+1), dtype=float)
        B = np.zeros(int(M+1), dtype=float)
        a = np.zeros((int(M+1), 4), dtype=float)
        parea = np.zeros(int(M+1), dtype=float)
        result = np.zeros(int(M+1), dtype=float)
        levels = ["default" for _ in range(int(M+1))]
        for i, line in enumerate(f, start=1):
            levels[i], mj, parea[i], mu, u2, u4, u6 = [float(item.strip()) if item.strip().replace('.', '', 1).isdigit() else item.strip() for item in line.split(",")]
            # print(f"levels: {levels[i]}, mj: {mj}, parea: {parea[i]}, mu: {mu}, u2: {u2}, u4: {u4}, u6: {u6}")
            Fex[i] = (CONSTANTS.mass * CONSTANTS.Vc ** 2) / (CONSTANTS.pi * CONSTANTS.e ** 2) * parea[i] / thickness / concen * 1E-20
            cont = (27 * CONSTANTS.h * (2 * mj + 1) * nre) / (8 * CONSTANTS.pi ** 2 * CONSTANTS.Vc * CONSTANTS.mass * mu * (nre ** 2 + 2) ** 2)
            result[i] = int(1E+10 * Fex[i]) / 100
            # print(f"result{i}: {result[i]}")
            B[i] = Fex[i] * cont
            a[i][1] = u2
            a[i][2] = u4
            a[i][3] = u6

        
        with open(out_put_file_path, 'a') as f:
            f.write(f"experimental oscillator sthengths\n")
            for i in range(int(M+1)):
                f.write(f"{levels[i]}, {result[i]}\n")
        
        #create eye metrix named Q
        Q = np.eye(int(M+1), dtype=float)
        nn = int(N if M != N else M-1) 

        for k in range(1, nn + 1):
            U = 0.0
            for i in range(k, M + 1):
                if abs(a[i][k]) > U:
                    U = abs(a[i][k])

            alpha = 0.0
            for i in range(k, M + 1):
                t = a[i][k] / U
                alpha += t * t

            if a[k][k] > 0.0:
                U = -U

            alpha = U * (alpha ** 0.5)
            if abs(alpha + 1) == 1:
                L = 0
                print("end1")

            U = (2.0 * alpha * (alpha - a[k][k])) ** 0.5
            if U + 1.0 != 1.0:
                a[k][k] = (a[k][k] - alpha) / U
                for i in range(k + 1, M + 1):
                    a[i][k] = a[i][k] / U
                
                for j in range(1, M + 1):
                    t = 0.0
                    for L in range(k, M + 1):
                        t += a[L][k] * Q[L][j]
                    for i in range(k, M + 1):
                        Q[i][j] -= 2.0 * t * a[i][k]
                
                for j in range(k + 1, N + 1):
                    t = 0.0
                    for L in range(k, M + 1):
                        t += a[L][k] * a[L][j]
                    for i in range(k, M + 1):
                        a[i][j] -= 2.0 * t * a[i][k]

                a[k][k] = alpha
                for i in range(k + 1, M + 1):
                    a[i][k] = 0.0

        L = 1
        for i in range(1, M):
            for j in range(i + 1, M+1):
                t = Q[i][j]
                Q[i][j] = Q[j][i]
                Q[j][i] = t
             
        c = np.zeros(int(N+1), dtype=float)
        for i in range(1, N + 1):
            D = 0.0
            for j in range(1, M + 1):
                D += Q[j][i] * B[j]
                c[i] = D
        B[N] = c[N] / a[N][N]

        for i in range(N - 1, 0, -1):
            D = 0.0
            for j in range(i + 1, N + 1):
                D += a[i][j] * B[j]
                B[i] = (c[i] - D) / a[i][i]
        
        OMEGA_2 = f"omega(2)={B[1]}"
        OMEGA_4 = f"omega(4)={B[2]}"
        OMEGA_6 = f"omega(6)={B[3]}"

        print(OMEGA_2)
        print(OMEGA_4)
        print(OMEGA_6)

        with open(out_put_file_path, 'a') as f:
            f.write(f"omega(2)={OMEGA_2}\n")
            f.write(f"omega(4)={OMEGA_4}\n")
            f.write(f"omega(6)={OMEGA_6}\n")

    return B
    
def process_theoretical_oscillator_sthengths(B: list, input_file_path: str, out_put_file_path: str):
    with open(input_file_path, "r") as f:
        M, N, nre, thickness, concen, mj = [float(x) for x in f.readline().split(',')]
        M = int(M)
        N = int(N)
        print(f"File: {input_file_path} - M: {M}, N: {N}, nre: {nre}, thickness: {thickness}, concen: {concen}, mj: {mj}")
        levels = ["default" for _ in range(int(M+1))]
        parea = np.zeros(int(M+1), dtype=float)
        result_fcal = np.zeros(int(M+1), dtype=float)
        for i, line in enumerate(f, start=1):
            levels[i], mj, parea[i], mu, u2, u4, u6 = [float(item.strip()) if item.strip().replace('.', '', 1).isdigit() else item.strip() for item in line.split(",")]
            cont = (27*CONSTANTS.h*(2*mj+1)*nre)/(8*CONSTANTS.pi**2*CONSTANTS.Vc*CONSTANTS.mass*mu*(nre**2+2)**2)
            fcal = (B[1] * u2 + B[2] * u4 + B[3] * u6) / cont
            result_fcal[i] = int(1E+10 * fcal) / 100
            print(f"{levels[i]}, {result_fcal[i]}")
    
        with open(out_put_file_path, 'a') as f:
            f.write(f"theoretical oscillator sthengths\n")
            for i in range(1, int(M+1)):
                f.write(f"{levels[i]}, {result_fcal[i]}\n")

def clean_output_file(out_put_file_path: str):
    with open(out_put_file_path, 'w') as f:
        f.write("")

if __name__ == "__main__":
    process_all_files('/Users/ruoyugao/Downloads/Judd-Ofelt/input', '/Users/ruoyugao/Downloads/Judd-Ofelt/output')