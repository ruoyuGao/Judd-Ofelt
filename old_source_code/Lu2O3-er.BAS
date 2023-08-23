CLS

DIM SHARED levels$(20), parea(20), Fex(20), fcal(20), Q(20, 20), a(20, 3), B(20), c(20)

OPEN "d:\JOCal\hwy\input-1.txt" FOR INPUT AS #1
OPEN "d:\JOCal\hwy\output-1.dat" FOR OUTPUT AS #3

'*************************************************************************************
h = 6.626E-27                                     'Planck content                  :'*
e = 4.8E-10                                       'Charge of electron              :'*
mass = 9.105E-28                                  'Mass of electron                :'*
Vc = 2.998E+10                                    'Velocity of light               :'*
pi = 3.1415926#:                                  'Circumference of unit  circle   :'*
'**************************************************************************************
   
    INPUT #1, M, N, nre, thickness, concen, mj

    FOR i = 1 TO M
        INPUT #1, levels$(i), mj, parea(i), mu, u2, u4, u6
           Fex(i) = (mass * Vc ^ 2) / (pi * e ^ 2) * parea(i) / thickness / concen * 1E-20
                           
   
         WRITE #3, " ", levels$(i), INT(1E+10 * Fex(i)) / 100
         PRINT " ", levels$(i), INT(1E+10 * Fex(i)) / 100
       
        cont = (27 * h * (2 * mj + 1) * nre) / (8 * pi ^ 2 * Vc * mass * mu * (nre ^ 2 + 2) ^ 2)
        IF i = 1 THEN
           Fex(i) = Fex(i) - fmd
        END IF
        B(i) = Fex(i) * cont
       
           a(i, 1) = u2
           a(i, 2) = u4
           a(i, 3) = u6

    NEXT i
'***************************************************************************
    FOR i = 1 TO M
       FOR j = 1 TO M
          Q(i, j) = 0!
            IF i = j THEN
               Q(i, j) = 1!
            END IF
       NEXT j
    NEXT i
    nn = N
    IF M = N THEN
       nn = M - 1
    END IF
    FOR k = 1 TO nn
        U = 0!
        FOR i = k TO M
           IF ABS(a(i, k)) > U THEN
              U = ABS(a(i, k))
           END IF
        NEXT i
        alpha = 0!
        FOR i = k TO M
           t = a(i, k) / U
           alpha = alpha + t * t
        NEXT i
        IF a(k, k) > 0! THEN
           U = -U
        END IF
        alpha = U * SQR(alpha)
        IF ABS(alpha + 1) = 1 THEN
           L = 0
           PRINT "end1"
        END IF
        U = SQR(2! * alpha * (alpha - a(k, k)))
        IF U + 1! <> 1 THEN
           a(k, k) = (a(k, k) - alpha) / U
           FOR i = k + 1 TO M
               a(i, k) = a(i, k) / U
           NEXT i
           FOR j = 1 TO M
              t = 0!
              FOR L = k TO M
                 t = t + a(L, k) * Q(L, j)
              NEXT L
              FOR i = k TO M
                 Q(i, j) = Q(i, j) - 2! * t * a(i, k)
              NEXT i
           NEXT j
           FOR j = k + 1 TO N
               t = 0!
               FOR L = k TO M
                  t = t + a(L, k) * a(L, j)
               NEXT L
               FOR i = k TO M
                  a(i, j) = a(i, j) - 2! * t * a(i, k)
               NEXT i
           NEXT j
           a(k, k) = alpha
           FOR i = k + 1 TO M
               a(i, k) = 0!
           NEXT i
        END IF
    NEXT k
    L = 1
    FOR i = 1 TO M - 1
       FOR j = i + 1 TO M
           t = Q(i, j)
           Q(i, j) = Q(j, i)
           Q(j, i) = t
       NEXT j
    NEXT i
'******************************************************
    FOR i = 1 TO N
        D = 0!
        FOR j = 1 TO M
           D = D + Q(j, i) * B(j)
        NEXT j
        c(i) = D
    NEXT i
    B(N) = c(N) / a(N, N)
    FOR i = N - 1 TO 1 STEP -1
        D = 0!
        FOR j = i + 1 TO N
            D = D + a(i, j) * B(j)
        NEXT j
        B(i) = (c(i) - D) / a(i, i)
    NEXT i



WRITE #3, "omega(2)=", B(1)
WRITE #3, "omega(4)=", B(2)
WRITE #3, "omega(6)=", B(3)

PRINT "J-O Parameters"
PRINT "omega(2)=", B(1)
PRINT "omega(4)=", B(2)
PRINT "omega(6)=", B(3)
'***************************************************************************

CLOSE #1

OPEN "d:\JOCal\hwy\input-1.txt" FOR INPUT AS #1

'*************************************************************************************
h = 6.626E-27                                     'Planck content                  :'*
e = 4.8E-10                                       'Charge of electron              :'*
mass = 9.105E-28                                  'Mass of electron                :'*
Vc = 2.998E+10                                    'Velocity of light               :'*
pi = 3.1415926#:                                  'Circumference of unit  circle   :'*
'**************************************************************************************

WRITE #3, "theoretical oscillator sthengths"
PRINT "theoretical oscillator sthengths"
INPUT #1, M, N, nre, thickness, concen, mj

FOR i = 1 TO M
        INPUT #1, levels$(i), mj, parea(i), mu, u2, u4, u6
        cont = (27 * h * (2 * mj + 1) * nre) / (8 * pi ^ 2 * Vc * mass * mu * (nre ^ 2 + 2) ^ 2)
        fcal = (B(1) * u2 + B(2) * u4 + B(3) * u6) / cont
        WRITE #3, " ", levels$(i), INT(1E+10 * fcal) / 100
        PRINT " ", levels$(i), INT(1E+10 * fcal) / 100
NEXT i
CLOSE #1, #3
END

