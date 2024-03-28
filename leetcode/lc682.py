def calPoints(operations: list[str]) -> int:
    stack = []
    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-2] + stack[-1])
        else:
            stack.append(int(op))
    return sum(stack)

operations = ["5","2","C","D","+"]
result = calPoints(operations)
print("Sum of stack:", result)
