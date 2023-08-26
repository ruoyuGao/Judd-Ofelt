import math

while True:
    # 'the sequence is spdfghiklm n  o  q'
    #               '012345678910 11 12'

    mu = float(input("wavenumber: "))
    s = float(input("s=? "))
    j = float(input("j=? "))
    l = float(input("l=? "))
    a = int(input("input a if a=1, J>J'; if a=0, J=J'; if a=2, J<J': "))

    if a == 10:
        break

    h = 6.626e-27  # Planck constant
    e = 4.8e-10  # Charge of electron
    m = 9.105e-28  # Mass of electron
    c = 2.998e+10  # Velocity of light
    pi = math.pi  # Circumference of unit circle
    nre = 1.96

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
