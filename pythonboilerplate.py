#!/usr/bin/python3
import sys

red = []
blue = []
green = []

def print_pixel(arr, size):
    # boring function to print a matrix
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            print(arr[i][j], end=' ')
        print('')

def main(size):
    global red, blue, green
    """      
        Inputs: 
        red[][] - stores red component of the image
        green[][] - stores green component of the image
        blue[][] - stores blue component of the image
        size[0] - height of the image
        size[1] - width of the image
         
        Outputs: 
        Modify `red`, `green` and `blue` array itself.
         
        Note: The default code leaves the image unchanged
    """
    # =========================
    #  Write filter logic here
    # =========================
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            red[i][j] = red[i][j]
            blue[i][j] = blue[i][j]
            green[i][j] = green[i][j]

    # =========================
    #  Filter logic ends
    # =========================

if __name__ == '__main__':
    try:
        # first line is height and width of the image
        ht,width = list(map(int, input().strip().split(' ')))

        # input in format red / green / blue
        for i in range(0, ht):
            red.append(list(map(int, input().strip().split(' '))))
        for i in range(0, ht):
            green.append(list(map(int, input().strip().split(' '))))
        for i in range(0, ht):
            blue.append(list(map(int, input().strip().split(' '))))

        # call your magic filter function to do its magic !
        main([ht,width])

        # first line of output is height and width of the image
        print(ht,width)

        # Output in format red / green / blue
        print_pixel(red, [ht,width])
        print_pixel(green, [ht,width])
        print_pixel(blue, [ht,width])

    except Exception as e:
        print(e, file=sys.stderr)
        pass
