CLS
DIM omig(3)

'***************************************************************************

OPEN "d:\JOCal\hwy\a.dat" FOR INPUT AS #2
OPEN "d:\JOCal\hwy\tran-2.txt" FOR OUTPUT AS #3

h = 6.626E-27                                      'Pulank contant
e = 4.8E-10                                        'Charge of electron
m = 9.105E-28                                      'Mass of electron
c = 2.998E+10                                      'Velocity of light
pi = 3.1415926#:                                   'Circumference of unit  circle

'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nre = 2.60
omig(1) = 9.83 * 1E-21
omig(2) = 7.08 * 1E-21
omig(3) = 3.08 * 1E-21
'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

FOR j = 1 TO 8
    INPUT #2, lvl$
    FOR i = 1 TO 8
        INPUT #2, la$
        INPUT #2, mu, mj, u2, u4, u6
        PRINT mu
        con = (27 * h * (2 * mj + 1) * nre) / (8 * pi ^ 2 * m * c * mu * (nre ^ 2 + 2) ^ 2)
        fcal = (omig(1) * u2 ^ 2 + omig(2) * u4 ^ 2 + omig(3) * u6 ^ 2) / con
        a = (64 * pi ^ 4 * e ^ 2 * nre * (nre ^ 2 + 2) ^ 2) * mu ^ 3 / (27 * (2 * mj + 1) * h) * (omig(1) * u2 + omig(2) * u4 + omig(3) * u6)
        WRITE #3, lvl$, la$, mu, INT(fcal * 1E+10) / 100, INT(100 * a) / 100

        IF la$ = "4i15/2" THEN GOTO 10
   NEXT i
10 :
NEXT j
CLOSE #2, #3
END
          

