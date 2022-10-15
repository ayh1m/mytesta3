import turtle
import pixart

def q4(c):
    for i in c:
        turtle.forward(pixart.PIXEL_SIZE)

        if i == "0":
            pixart.draw_black_pixel()
        elif i == "1":
            pixart.draw_white_pixel()
        elif i == "2":
            pixart.draw_red_pixel()
        elif i == "3":
            pixart.draw_yellow_pixel()
        elif i == "4":
            pixart.draw_orange_pixel()
        elif i == "5":
            pixart.draw_green_pixel()
        elif i == "6":
            pixart.draw_yellowgreen_pixel()
        elif i == "7":
            pixart.draw_sienna_pixel()
        elif i == "8":
            pixart.draw_tan_pixel()
        elif i == "9":
            pixart.draw_gray_pixel
        elif i == "A":
            pixart.draw_darkgray_pixel()
        else:
            return False

        turtle.penup()

def q5():
    current_row = 1
    while True:
        c = str(input('Enter your string: '))
        
        if q4(c) == False:
            return
        if c == "":
            return

        pixart.move(current_row, 0)
        current_row += 1

def main():
    pixart.initialize()
    q5()
    input("Enter any key to close... ")
main()