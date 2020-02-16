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