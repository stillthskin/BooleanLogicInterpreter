# Define a dictionary to store the variables and their values
variables = {}

def eval_expression(expression):
    """Evaluate a simple Boolean expression and return the result."""
    # Split the expression into tokens
    tokens = expression.split()
    
    # Initialize a stack for holding the operands
    stack = []
    
    # Iterate through the tokens
    for token in tokens:
        # If the token is a variable, check if it's in the variables dict
        if token in variables:
            stack.append(variables[token])
        # If the token is an operand, push it onto the stack
        elif token in ['True', 'False']:
            stack.append(token == 'True')
        # If the token is an operator, pop the two operands, perform the
        # operation, and push the result back onto the stack
        elif token == '∧':
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)
        elif token == '∨':
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)
        elif token == '¬':
            a = stack.pop()
            stack.append(not a)
        elif token == '(':
            pass
        elif token == ')':
            pass
        else:
            raise ValueError(f'Invalid token: {token}')
    
    # Return the result from the stack
    return stack[0]

# Example expressions
expression1 = 'T ∨ F'
expression2 = 'T ∧ F'
expression3 = '(T ∧ F) = F'
expression4 = 'let X = F'
expression5 = 'let Y = ¬X'
expression6 = '¬X ∧ Y'

# Evaluate the expressions and print the results
print(eval_expression(expression1))
print(eval_expression(expression2))
print(eval_expression(expression3))
exec(expression4)
print(variables)
exec(expression5)
print(variables)
print(eval_expression(expression6))

#Note that the exec function is used to execute the let statements and update the variables dictionary.

