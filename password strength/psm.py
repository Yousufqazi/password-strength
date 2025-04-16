import re
import streamlit as st


st.set_page_config(page_title="Password Strength Checker by yousuf khan", page_icon="🌘", layout="centered")

st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: auto;}
            .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}
            .stButton button:hover {background-color: red;}
            </style>
            """, unsafe_allow_html=True)

st.title(" 🔐 Password Strength Generator")
st.write("Enter your password below to check its Security lavel.🔎")


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >=8:
        score += 1
    else:
        feedback.append(" ❌ Password Should be at least 8 characters long.")

    if re.search(r"[A-Z]", password )and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" ❌ Password Should include both uppercase (A-Z) and lower case (a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" ❌ Password Should include atleast one numbers (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" ❌ Include atleast one special character (!@#$%^&*).")

    if score == 4:
        st.success(" ✅ **Strong Password** Your Password is Secure.")
    elif score == 3:
        st.info(" ⚠️ **Moderate Password** - Consider improving security by adding more feature.")
    else:
        st.error(" ❌ **Weak Password** - Your Password is not secure.")

    if feedback:
        with st.expander("🔎 **Improve Your Pasword**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password", type="password", help="Ensure your password is Strong and Secure. 🔐")


if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please Enter a Password first.")
