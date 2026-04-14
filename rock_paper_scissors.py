import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")
st.write("Play against the computer!")

options = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Your choice:", options)

if st.button("Play!"):
    computer_choice = random.choice(options)
    st.write(f"**Computer chose: {computer_choice}**")
    
    user_move = options.index(user_choice)
    computer_move = options.index(computer_choice)
    
    if user_move == computer_move:
        st.info("🤝 It's a Draw!")
    elif (user_move == 0 and computer_move == 2) or \
         (user_move == 1 and computer_move == 0) or \
         (user_move == 2 and computer_move == 1):
        st.success("🎉 You Win!")
    else:
        st.error("🤖 Computer Wins!")