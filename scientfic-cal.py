import streamlit as st
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x > 0:
        return math.log10(x)
    else:
        return "Undefined (logarithm of non-positive number)"

def main():
    st.title("Scientific Calculator")
    st.write("This is a simple scientific calculator built using Streamlit.")

    # Select operation
    operation = st.selectbox("Select an operation:", ['+', '-', '*', '/', '^', '√', 'sin', 'cos', 'tan', 'log'])

    # Input numbers
    num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
    num2 = None
    if operation not in ('√', 'sin', 'cos', 'tan', 'log'):
        num2 = st.number_input("Enter the second number:", value=0.0, format="%.2f")

    # Calculate result
    if st.button("Calculate"):
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
        elif operation == '√':
            result = sqrt(num1)
        elif operation == 'sin':
            result = sin(num1)
        elif operation == 'cos':
            result = cos(num1)
        elif operation == 'tan':
            result = tan(num1)
        elif operation == 'log':
            result = log(num1)
        else:
            result = "Invalid Operation"

        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
