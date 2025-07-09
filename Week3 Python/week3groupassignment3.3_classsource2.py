fibs = [1,1]

def main():
    num = ask_for_number()

    while (num >= 0):
        print(f"The fibonacci number of {num} is {fib(num)}")
        num = ask_for_number()
        
def ask_for_number():
    return int(input("Enter a positive number (-1 to quit):"))

def fib(num):
    if num >= len(fibs):
       for i in range(len(fibs), num + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[num]

if __name__ == '__main__':
    main()
