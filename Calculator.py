def parse_exp(expression):
    tokens = [] 
    num = ""   
    for char in expression:
        if char.isdigit() or char == '.': 
            num += char 
        elif char in '+-*/%()': 
            if num:
                tokens.append(float(num)) 
                num = "" 
            tokens.append(char) 
        elif char.isspace():
            if num:  
                tokens.append(float(num))  
                num = "" 

    if num:  
        tokens.append(float(num))  

    return tokens

def evaluate(tokens):
      i = 0
      while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '%':
            if tokens[i] == '*':
                result = tokens[i-1] * tokens[i+1]
            elif tokens[i] == '/':
                result = tokens[i-1] / tokens[i+1]
            elif tokens[i] == '%':
                result = tokens[i-1] % tokens[i+1]
            
            tokens[i-1:i+2] = [result]
        else:
            i += 1

      i = 0
      while i < len(tokens):
        if tokens[i] == '+' or tokens[i] == '-':
            if tokens[i] == '+':
                result = tokens[i-1] + tokens[i+1]
            elif tokens[i] == '-':
                result = tokens[i-1] - tokens[i+1]
            
            tokens[i-1:i+2] = [result]
        else:
            i += 1

      return tokens[0]

def calculator(tokens):
    stack = []
    sub_expr = []

    for token in tokens:
        if token == '(':
            stack.append(sub_expr)
            sub_expr = []
        elif token == ')':
            result = evaluate(sub_expr)
            sub_expr = stack.pop()
            sub_expr.append(result)
        else:
            sub_expr.append(token)

    return evaluate(sub_expr)

expression = input("Enter a mathematical expression (for example: 12*4+(56-11)%4+23): ")
tokens = parse_exp(expression)
result = calculator(tokens)
print("Result:", result)
