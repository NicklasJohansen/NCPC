IDENTIFICATION DIVISION.
PROGRAM-ID. HOTHIKE.

DATA DIVISION.
    WORKING-STORAGE SECTION.
    01 lin PIC X(1000).
    01 linepos PIC 999 VALUE 1.
    01 n PIC S9(4).
    01 X.
       02 Z PIC S99 OCCURS 50 TIMES.
    01 d PIC ZZ.
    01 t PIC -Z9.
    01 v PIC S99 VALUE 50.
    01 i PIC 99.

PROCEDURE DIVISION.
    ACCEPT lin
    MOVE FUNCTION NUMVAL(lin) TO n
    ACCEPT lin
    PERFORM VARYING i FROM 1 BY 1 UNTIL i GREATER THAN n
       UNSTRING lin DELIMITED BY SPACE INTO Z(i) WITH POINTER linepos
    END-PERFORM
    PERFORM VARYING i FROM 1 BY 1 UNTIL i GREATER THAN n - 2
       IF FUNCTION MAX(Z(i), Z(i + 2)) < v THEN
          SET v TO FUNCTION MAX(Z(i), Z(i + 2))
          SET d TO i
       END-IF
    END-PERFORM
    MOVE v TO t
    DISPLAY d, " ", t
    STOP RUN.
