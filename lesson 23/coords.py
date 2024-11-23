num_x = int(input("введите координату х: "))
num_y = int(input("введите координату у: "))
def koordinati(num_x, num_y):
        if num_x >0 and num_y >0:
            print('1')
        if num_x <0 and num_y <0:
            print("3")
        if num_x <0 and num_y >0:
            print("2")
        if num_x >0 and num_y <0:
            print("4")
koordinati(num_x, num_y)
