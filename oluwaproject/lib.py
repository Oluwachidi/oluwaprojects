def try_me(n):
    for i in range(1, n+1):
        if i % 3 ==0 and i % 5 ==0:
            print('fizzBuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

if __name__ == "__main__":
    print(try_me())
