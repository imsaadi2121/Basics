import streamlit as st

# Set the title of the application
st.title('University Admission Form')

# Create a form using the 'with' notation
with st.form(key='admission_form'):
    # Input fields
    full_name = st.text_input(label='Full Name')
    age = st.number_input(label='Age', min_value=0, max_value=100, step=1)
    email = st.text_input(label='Email Address')
    phone = st.text_input(label='Phone Number')
    gender = st.radio("Gender", ("Male", "Female", "Other", "Prefer Not To Say"))
    program = st.selectbox(
        'Intended Program of Study',
        ('Computer Science', 'Business Administration', 'Mechanical Engineering', 'Art History', 'Other')
    )
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Process the form submission
if submit_button:
    # Basic validation
    if not full_name:
        st.error("Please enter your full name.")
    elif not email:
        st.error("Please enter your email address.")
    elif not phone:
        st.error("Please enter your phone number.")
    else:
        # Display the entered information
        st.success("Thank you for your submission!")
        st.write("Here is the information you provided:")
        st.write(f"**Full Name:** {full_name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Email Address:** {email}")
        st.write(f"**Phone Number:** {phone}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Intended Program of Study:** {program}")
