import pyautogui
import keyboard
import python_imagesearch.imagesearch as imgsearch
import sys
import time

exec_stop = False

'''
Before starting to work you should 
replace all the screenshots from img folder
They should have the same name
'''

'''
There are three mods of this bot
First mode prints coordinates of cursor
Second mode is bot for wax drops on atomic hub
Third mode is for binance drop
To choose the mode you should remove the '#' symbol
'''
mode = "coord"
# mode = "bot"
# mode = "bin"

'''
this variables store the coordinates of buttons
you should take them with mode "coord" before drop
'''
buy_button = (1248, 571)
captcha_button = (834, 560)
pay_button = (953, 628)
pay_button_without_captcha = (955, 541)

# coordinates to binance drop
buy_bin = (1169, 761)
pay_bin = (1029, 813)
max_bin = (1240, 571)


def run():
    # infinite loop
    while exec_stop is False:
        # binance mode
        if mode == "bin":
            try:
                # finding max button on screen
                if imgsearch.imagesearch("img/max-bin.png")[0] != -1:
                    pyautogui.click(max_bin)
                    # the flag
                    bool = False

                    # finding buy button
                    while not bool:
                        if imgsearch.imagesearch("img/buy-bin.png")[0] != -1:
                            pyautogui.click(buy_bin)
                            # finding pay button
                            while not bool:
                                if imgsearch.imagesearch("img/pay-bin.png")[0] != -1:
                                    pyautogui.click(pay_bin)
                                    bool = True
                                    sys.exit(0)

                                time.sleep(0.1)

                        time.sleep(0.1)

                time.sleep(0.1)

            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[1])
                sys.exit(0)
        # if mode is bot
        elif mode == "bot":
            try:
                # finding buy button on screen
                if imgsearch.imagesearch("img/buy.png")[0] != -1:
                    pyautogui.click(buy_button)

                    bool = False
                    # finding captcha button
                    while not bool:
                        if imgsearch.imagesearch("img/captcha.png")[0] != -1:
                            pyautogui.click(captcha_button)

                            # finding pay button
                            while not bool:
                                if imgsearch.imagesearch("img/pay.png")[0] != -1:
                                    pyautogui.click(pay_button)
                                    bool = True
                                    sys.exit(0)

                                time.sleep(0.1)

                        time.sleep(0.1)

                time.sleep(0.1)

            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[1])
                sys.exit(0)
        # coord mode
        else:
            try:
                # Print position to console every second
                print(pyautogui.position())
                time.sleep(1)

            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[2])


if __name__ == '__main__':
    run()

