import os
import time

WIDTH = 79
HEIGHT = 7
message=str(input("Enter the message to be displayed")).upper()
printedMessage = [ "","","","","","","" ]
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "A" : [ "  *  ",
                       " * * ",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "B" : [ "**** ",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "****" ],

               "C" : [ "*****",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "D" : [ "**** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "**** " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],

               "F" : [ "*****",
                       "*    ",
                       "*    ",
                       "**** ",
                       "*    ",
                       "*    ",
                       "*    " ],

               "G" : [ "*****",
                       "*    ",
                       "*    ",
                       "*  **",
                       "*   *",
                       "*   *",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "J" : [ "*****",
                       "   * ",
                       "   * ",
                       "   * ",
                       "   * ",
                       "   * ",
                       "***  " ],

               "K" : [ "*   *",
                       "*  * ",
                       "* *  ",
                       "**   ",
                       "* *  ",
                       "*  * ",
                       "*   *" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "M" : [ "*   *",
                       "** **",
                       "* * *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *" ],
               
               "N" : [ "*   *",
                       "**  *",
                       "* * *",
                       "*  **",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "P" : [ "*****",
                       "*   *",
                       "*****",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    " ],

               "Q" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "* * *",
                       "*  **",
                       "*** *" ],

               "R" : [ "*****",
                       "*   *",
                       "*   *",
                       "**** ",
                       "**   ",
                       "* *  ",
                       "*  * " ],

               "S" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "    *",
                       "    *",
                       "*****" ],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],


               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "V" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " * * ",
                       "  *  " ],
               
               "W" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "* * *",
                       " * * " ],

               "X" : [ "*   *",
                       "*   *",
                       " * * ",
                       "  *  ",
                       " * * ",
                       "*   *",
                       "*   *" ],

               "Y" : [ "*   *",
                       " * *",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "Z" : [ "*****",
                       "    *",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ],

               "'" : [ "  *  ",
                       "  *  ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     " ],

               ":" : [ "  *  ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "  *  " ],

               ";" : [ "  *  ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "  *  ",
                       " *   " ],

               ")" : [ " *   ",
                       "   * ",
                       "    *",
                       "    *",
                       "    *",
                       "   * ",
                       " *   " ],

               "(" : [ "   * ",
                       " *   ",
                       "*    ",
                       "*    ",
                       "*    ",
                       " *   ",
                       "   * " ],
               
               "," : [ "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "  *  ",
                       " *   " ],

               "1" : [ "  *  ",
                       " **  ",
                       "* *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "2" : [ " *** ",
                       "*   *",
                       "    *",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*****" ],
               
               }
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

offset = WIDTH
while True:
    os.system("cls")
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    offset -=1
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    time.sleep(0.05)
