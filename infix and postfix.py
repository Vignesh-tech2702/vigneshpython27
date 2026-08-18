def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for char in expression:
        if char.isalnum():
            postfix += char

        
        elif char == '(':
            stack.append(char)

        
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() 

        
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix += stack.pop()

            stack.append(char)

    
    while stack:
        postfix += stack.pop()

    return postfix



infix = input("Enter an infix expression: ")
postfix = infix_to_postfix(infix)

print("Infix expression :", infix)
print("Postfix expression:", postfix)
