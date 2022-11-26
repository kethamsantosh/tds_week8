import streamlit as st

st.write("""
# Multiplication of two Integers

This app multiplies two input Integers
""")
#Get Input


def user_input_features():
    num1 = st.number_input("Number 1", step=1)
    num2 = st.number_input("Number 2", step=1)

    data = {'NUM1': num1,
            'NUM2': num2,
            }

    return f'Multiplication of {num1}, {num2} is ---------> {num1*num2}'

result = user_input_features()


st.subheader('Result')
st.write(result)
