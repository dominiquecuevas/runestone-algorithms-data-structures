from stack import Stack

def bal_parens(string):
    stack = Stack()

    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                stack.push(char)

    return stack.isEmpty()

print(bal_parens('((()))'))
print(bal_parens('(()'))
print(bal_parens('((m(h))()'))