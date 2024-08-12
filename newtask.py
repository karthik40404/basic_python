# def is_even(number):
#     return (number // 2) * 2 == number

# def main():
#     number = int(input("Enter a number: "))
#     if is_even(number):
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

# main()

# def swap_numbers_list(a, b):
#     numbers = [a, b]
#     numbers[0], numbers[1] = numbers[1], numbers[0]
#     return numbers[0], numbers[1]

# def main():
#     a = int(input("Enter the first number (a): "))
#     b = int(input("Enter the second number (b): "))
#     print(f"Before swapping: {a}{b}")
#     a, b = swap_numbers_list(a, b)
#     print(f"After swapping:{a}{b}")


# main()

# a = int(input("Enter the first number (a): "))
# b = int(input("Enter the second number (b): "))
# a, b = b, a
# print('a =', a)
# print('b =', b)

# Set the height of the pyramid


# for i in range(7):
#     for j in range(5 - i + 1):
#         print(' ', end='')
#     for k in range(2 * i - 1):
#         print('*', end='')
#     print()



# for i in range(7):
#     if i == 0:
#         print('*' * 5)
#     elif i == 1:
#         print('*' * 4)
#     elif i == 2:
#         print('*' * 6)
#     elif i == 3:
#         print('*' * 3)
#     elif i == 4:
#         print('*' * 2)
#     elif i == 5:
#         print('*' * 5)
#     elif i == 6:
#         print('*' * 1)


# pattern = [5, 4, 6, 3, 2, 5, 1]
# for i in pattern:
#     print('*' * i)

# for i in range(3):
#     for j in range (4):
#         a=65
#         print(chr(i+j),end="")
#     print()
