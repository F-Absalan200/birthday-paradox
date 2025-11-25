import streamlit as st
import logic
import matplotlib.pyplot as plt

st.title("🎂 Birthday Paradox Simulator")
st.image(
    'https://upload.wikimedia.org/wikipedia/commons/d/dd/Birthday_candles.jpg',
    use_container_width=True
)


people = st.number_input("Enter number of people:", min_value=2, max_value=1000, value=23)
trials = st.number_input("Enter number of trials:", min_value=1, max_value=10000000, value=1000)

if st.button("Calculate"):
    result = logic.examination(people, trials)
    
    st.success(f"The probability of shared birthdays is: {result:.4f}%")
    
    fig, ax = plt.subplots()
    ax.bar(["Shared Birthday", "No Shared Birthday"], [result, 100-result], color=['tomato', 'skyblue'])
    ax.set_ylabel("Probability (%)")
    st.pyplot(fig)
    
    st.balloons()
