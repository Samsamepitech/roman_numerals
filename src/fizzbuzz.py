

def fizzbuzz(num):
    
    if num %3 == 0 and num %5 == 0:
        x="FizzBuzz"

    elif num %3 == 0:
        x="Fizz"

    elif num %5 == 0:
        x="Buzz"
    else: 
        x=num

    return x

def main():
    for num in range (1,101):
        print(fizzbuzz(num))

if __name__== '__main__':
    main()