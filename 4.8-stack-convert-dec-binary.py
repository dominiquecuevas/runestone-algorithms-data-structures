from stack import Stack

def divide_by_2(num):
    stack = Stack()
    
    while num > 0:
        remainder = num % 2
        stack.push(remainder)
        num = num // 2

    binary_string = ""
    while not stack.isEmpty():
        binary_string = binary_string + str(stack.pop())
    return binary_string

print(divide_by_2(42))
print(bin(42))

def base_converter(num, base):
    digits = '0123456789ABCDEF'
    stack = Stack()

    while num > 0:
        remainder = num % base
        stack.push(remainder)
        num = num // base

    binary_string = ''
    while not stack.isEmpty():
        binary_string += digits[stack.pop()]

    return binary_string

print(base_converter(25,2))
print(bin(25))
print(base_converter(25,16))
print(format(25,'02x'))