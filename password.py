import streamlit as st
import re #regex


st.set_page_config(page_title="Password Strength Checker",  page_icon="🔑")

st.title("🔒Password Strength Checker")
st.markdown("""
### 👋Welcome to my Password Strength Checker! 
Enter a password to check its strength.""") 

password = st.text_input("Enter a password", type="password")

feedback = [""]

score = 0

if password:
    if len(password) >=8:
        score += 1
    else:
        feedback.append("❌Password is too short. It should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(eg. !@#$%^&*).")

    if score == 4:
        feedback.append("## ✅Excellent! You are good to go👌")
    elif score == 3:
        feedback.append("## 🟢Your password is strong✅")
    elif score == 2:
        feedback.append("## 🟡Your password is moderate. It can be stronger")
    else:
        feedback.append("## ❌Your password is weak. It needs improvement")

    if feedback:
        st.markdown("## Feedback")
        for item in feedback:
            st.write(item)
else:
    st.info("Please enter a password to check its strength.")
    
    
