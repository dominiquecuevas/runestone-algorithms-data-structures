from stack import Stack

def bal_symbols(string):
    stack = Stack()

    symbols = {
                ')': '(',
                '}': '{',
                ']': '[',
                '>': '<'
    }

    for char in string:
        if char in symbols.values():
            stack.push(char)
        elif char in symbols:
            if stack.peek() == symbols[char]:
                stack.pop()
            else:
                stack.push(char)

    return stack.isEmpty()

print(bal_symbols('{({([][])}())}'))
print(bal_symbols('{({([>][])}())}'))
print(bal_symbols('[{()]'))