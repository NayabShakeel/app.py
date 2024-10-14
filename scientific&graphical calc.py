import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import streamlit as st

def scientific_calculator():
    st.title("Scientific Calculator")

    operation = st.selectbox("Choose an operation", [
        "Addition", "Subtraction", "Multiplication", "Division", 
        "Square Root", "Power", "Logarithm", "Factorial", 
        "Exponential", "Trigonometric Functions", "Inverse Trigonometric Functions", 
        "Hyperbolic Functions"
    ])

    if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        st.write("Result:", result)

    elif operation == "Square Root":
        num = st.number_input("Enter a number", value=0.0)
        result = np.sqrt(num)
        st.write("Result:", result)

    # Add the rest of the operations similarly
    # ...

def graphical_calculator():
    st.title("Graphical Calculator")
    
    expression = st.text_input("Enter a function (e.g., x**2, sin(x)):")
    if expression:
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        
        # Generate values
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [expr.subs(x, val) for val in x_vals]

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(x_vals, y_vals, label=str(expr))
        plt.title("Graph of " + str(expr))
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(0, color='black',linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        st.pyplot(plt)

def main():
    st.sidebar.title("Select Calculator")
    calculator_type = st.sidebar.radio("Choose:", ["Scientific Calculator", "Graphical Calculator"])

    if calculator_type == "Scientific Calculator":
        scientific_calculator()
    else:
        graphical_calculator()

    # Add footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Made by Nayab Shakeel</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
