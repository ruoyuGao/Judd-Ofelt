CLS
DIM sabc$, labc$, jabc$
5 :
'the sequence is spdfghiklm n  o  q
'                012345678910 11 12

INPUT ; "wavenumber", mu
PRINT "input a if a=1, J>J'  ; if a=0, J=J'  ; if a=2, J<J'"
INPUT ; "s=?", s
INPUT ; "j=?", j
INPUT ; "l=?", l
INPUT ; "a=?", a
IF a = 10 THEN GOTO 10

h = 6.626E-27                                     'Planck content
e = 4.8E-10                                        'Charge of electron
m = 9.105E-28                                      'Mass of electron
c = 2.998E+10                                      'Velocity of light
pi = 3.1415926#:                                 'Circumference of unit  circle
'%%%%%%%%%%%%
nre = 1.96
'%%%%%%%%%%%%

         IF a = 1 THEN
              fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * ((s + l + j + 1) * (s + l + 1 - j) * (j + s - l) * (j + l - s) / (4 * j))
              ff = ((s + l + j + 1) * (s + l + 1 - j) * (j + s - l) * (j + l - s) / (4 * j))
              PRINT "FFF", ff / (2 * j + 1)
         END IF
        
         IF a = 0 THEN
               fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * (1 + (j * (j + 1) + s * (s + 1) - l * (l + 1)) / 2 / j / (j + 1)) ^ 2 * (j * (j + 1) * (2 * j + 1))
               ff = (1 + (j * (j + 1) + s * (s + 1) - l * (l + 1)) / 2 / j / (j + 1)) ^ 2 * (j * (j + 1) * (2 * j + 1))
         END IF

         IF a = 2 THEN
               fed = (h * nre * mu / (6 * c * m * (2 * j + 1))) * ((s + l + j + 2) * (s + j + 1 - l) * (l + j + 1 - s) * (s + l - j) / (4 * (j + 1)))
               ff = ((s + l + j + 2) * (s + j + 1 - l) * (l + j + 1 - s) * (s + l - j) / (4 * (j + 1)))
         PRINT "sdf", ff / (2 * j + 1)
         END IF
         all = (4 * pi ^ 2 * e ^ 2 * nre ^ 3 * h * mu ^ 3) / (3 * (2 * j + 1) * m ^ 2 * c ^ 2) * ff
         aij = 8 * pi ^ 2 * e ^ 2 * mu ^ 2 * nre ^ 2 * fed / m / c
        PRINT "matrix element", ff
        PRINT "fmd=", fed

        PRINT "A", aij
GOTO 5
10 : END






