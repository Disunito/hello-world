number = input("Tell me a number that is a multiple of 10: ")
answer = int(number)

if answer % 10:
    print("\nNO..... goodbye.")
else:
    print(f"\nHey! You did it... {answer} is a multiple of 10.")
