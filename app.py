import streamlit as st

# Title of Portfolio
st.title("Projects")

# Introduction Section
st.header("About Me")
st.markdown("""
Hello!
""")

# Button for each project
if st.button("Project 1: Stock Price Prediction"):
    st.write("### Stock Price Prediction")
    st.markdown("In this project, I predicted stock prices using machine learning models.")
    st.write("You can see the code for this project in the next section.")
    import project_1  # Import the project file


# Add more projects in a similar way
