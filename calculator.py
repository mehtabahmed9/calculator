import streamlit as st

# Set the title of the web app
st.title("Simple Calculator")


# Get user input
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

#Select the operation
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multipy", "Divide"))

# Perform the calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multipy":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"

# Display the result
st.write("Result:", result)
