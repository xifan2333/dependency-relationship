from db import read

def div():
    num1 = read('input/input-1.txt')
    num2 = read('input/input-2.txt')
    return int(num1) / int(num2)

if __name__ == "__main__":
    print(div())