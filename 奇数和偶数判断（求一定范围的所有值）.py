start = input("The minimum value of the input range:")
end = input("The maximum value of the input range:")
start = int(start)
end = int (end)
choice = input("To choose between odd and even numbers, 'o' for odd numbers, 'e' for even numbers:")

if start < end:
    for i in range(start, end + 1):
        if choice == "e" or choice == "E":
            if i % 2 == 0:
                print(i)
        elif choice == "o" or chice == "O":
            if i % 2 == 1:
                print(i)
        else:
            print("Please enter a valid number and try again!")
else:
    print("Please enter a significant number!")




input()

