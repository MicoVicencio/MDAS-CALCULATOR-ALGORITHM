def extractor(expression): #Extracting integers and operations
    import re
    numbers = list(map(float, re.findall(r'\d+', expression)))
    operations = re.findall(r'[\+\-\*/]', expression)
    return numbers, operations

def calculate(expression): #calculating the mathematical expresion using MDAS rule
    values, operations = extractor(expression)
    
    print("Operations:", operations)
    print("Values before calculation:", values)
    
    result = 0
    
    while '*' in operations or '/' in operations:
        for i in range(len(operations)):
            if operations[i] == '*':
                values[i] = values[i] * values[i+1]
                del values[i+1]
                del operations[i]
                break
            elif operations[i] == '/':
                values[i] = values[i] / values[i+1]
                del values[i+1]
                del operations[i]
                break
    
    while '+' in operations or '-' in operations:
        for i in range(len(operations)):
            if operations[i] == '+':
                values[i] = values[i] + values[i+1]
                del values[i+1]
                del operations[i]
                break
            elif operations[i] == '-':
                values[i] = values[i] - values[i+1]
                del values[i+1]
                del operations[i]
                break
    
    result = values[0]
    print("Result:", result)
    return result

# Example usage
expression = input("Enter a normal mathematical sequence:")
calculate(expression)
