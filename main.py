# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint
import PySimpleGUI as sg
def guessNumber():
    # layout = [[sg.Text("Input minimum number: ")],
    #           [sg.Input(key='min_num')],
    #           [sg.Text("Input maximum number: ")],
    #           [sg.Input(key='max_num')],
    #           [sg.Text("Input Turn: ")],
    #           [sg.Input(key='turn_num')],
    #           [sg.Button('OK')],
    #           [sg.Text(size=(40,1), key='chance')],
    #           [sg.Text(size=(40,1), key='input_num')]
    #           ]
    #
    # # Create the window
    # window = sg.Window("Guess the Number", layout, margins=(500,250))
    #
    # # Create an event loop
    # while True:
    #     event, values = window.read()
    #     # End program if user closes window or
    #     # presses the OK button
    #     if event == "OK":
    #         ans = randint(values['min_num'], values['max_num'])
    #         window['chance'].update('You have ' + values['turn_num'] + " Chances.")
    #     elif event == sg.WIN_CLOSED:
    #         break
    #
    # window.close()
    min_num = int(input("Input minimum number: "))
    max_num = int(input("Input maximum number: "))
    turn_num = int(input("Input Turn: "))
    ans = randint(min_num, max_num)
    while (True):
        if (turn_num == 0):
            print("You lose! The number is " + str(ans))
            print("\n")
            break
        print("You have " + str(turn_num) + " Chances.")
        input_num = int(input("Please input Number for guess the number between " + str(min_num) + " to " + str(max_num) + ": " ))
        turn_num -= 1
        if (input_num < ans and turn_num != -1):
            print("Greater than! >" + str(input_num))
            print("\n")
        elif (input_num > ans and turn_num != -1):
            print("Lass than! <" + str(input_num))
            print("\n")
        elif (input_num == ans and turn_num != -1):
            print("Collect! The number is " + str(ans))
            print("\n")
            break
        else:
            print("You lose! The number is " + str(ans))
            print("\n")
            break
guessNumber()