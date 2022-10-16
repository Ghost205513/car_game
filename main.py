def field():
    for y in range(25):
        for x in range(80):
            if x == y + 42:
                print("\\", end='')
            elif x == -y + 35:
                print("/", end='')
            elif (x == 38) or (x == 39):
                print("|", end='')
            else:
                print(end=' ')
        print()


if __name__ == '__main__':
    field()

