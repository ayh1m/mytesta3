import pixart
import turtle

def draw_row(colour1, colour2):
    """Draws a row of pixels of alternating colors"""

    for _ in range(pixart.COLUMNS//2):
        pixart.draw_pixel(colour1)
        pixart.draw_pixel(colour2)

def checkerboard():
    current_row = 1
    colour1 = "Black"
    colour2 = "Red"

    for _ in range(pixart.ROWS):
        draw_row(colour1, colour2)
        pixart.move(current_row, 0)
        current_row += 1

        # Swaps colours
        temp = colour1
        colour1 = colour2
        colour2 = temp

def main():
    pixart.initialize()
    checkerboard()
    turtle.done()

if __name__ == '__main__':
    main()