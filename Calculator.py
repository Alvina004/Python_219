
def parse_exp(expression):
    tokens = [] 
    num = ""   
    for char in expression:
        if char.isdigit() or char == '.': 
            num += char 
        elif char in '+-*/': 
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

def calculator(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            if tokens[i] == '*':
                result = tokens[i-1] * tokens[i+1]
            elif tokens[i] == '/':
                result = tokens[i-1] / tokens[i+1]
            
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

expression = input("Enter a mathematical expression (for example: 12+896-742/58*365): ")
tokens = parse_exp(expression)
result = calculator(tokens)
print("Result:", result)  
