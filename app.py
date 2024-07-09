import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5  # Example: Number of problems to generate

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

start_time = time.time()
wrong = 0

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        if guess == str(answer):
            break
        else:
            print("Incorrect. Try again.")
            wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("--------------------")
print("Nice work! You finished in", total_time, "seconds.")
print("Number of wrong answers:", wrong)
