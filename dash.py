import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

# Function to create a connection to the database and return the cursor
def create_connection():
    conn = sqlite3.connect('data.db')  # This creates/opens the SQLite database
    cursor = conn.cursor()
    return conn, cursor

# Function to create the table if it doesn't exist
def create_table():
    conn, cursor = create_connection()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# Function to insert a new record into the table
def insert_user(name, age):
    conn, cursor = create_connection()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

# Function to get all users from the database
def get_all_users():
    conn, cursor = create_connection()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# Function to delete a user by ID
def delete_user(user_id):
    conn, cursor = create_connection()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

# Function to update the user age
def update_user_age(user_id, new_age):
    conn, cursor = create_connection()
    cursor.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
    conn.commit()
    conn.close()

# Streamlit interface
def main():
    st.title('Streamlit SQLite Dashboard with Pandas and NumPy')

    # Create the database table if it doesn't exist
    create_table()

    # Sidebar for navigation
    menu = ['Home', 'Add User', 'View Users', 'Update User Age', 'Delete User']
    choice = st.sidebar.selectbox('Select Action', menu)

    if choice == 'Home':
        st.subheader('Welcome to the SQLite Dashboard')
        st.write('Use the sidebar to navigate through different actions.')

    elif choice == 'Add User':
        st.subheader('Add a New User')
        name = st.text_input('Enter name')
        age = st.number_input('Enter age', min_value=0)

        if st.button('Add User'):
            if name and age:
                insert_user(name, age)
                st.success(f'User {name} added successfully!')
            else:
                st.error('Please enter valid data.')

    elif choice == 'View Users':
        st.subheader('View All Users')

        # Fetch all users from the database
        users = get_all_users()
        if users:
            # Convert to pandas DataFrame for better visualization
            df = pd.DataFrame(users, columns=['ID', 'Name', 'Age'])

            # Display a table of users using Pandas
            st.dataframe(df)

            # Display statistical summary of the data using NumPy and Pandas
            st.subheader('Statistical Summary')
            st.write(df.describe())

            # Plotting age distribution using NumPy
            age_distribution = np.histogram(df['Age'], bins=10)
            st.subheader('Age Distribution')
            st.bar_chart(age_distribution[0])  # Plot the frequency of each age bin
        else:
            st.write('No users found in the database.')

    elif choice == 'Update User Age':
        st.subheader('Update User Age')
        user_id = st.number_input('Enter user ID to update', min_value=1)
        new_age = st.number_input('Enter new age', min_value=0)

        if st.button('Update Age'):
            if user_id and new_age:
                update_user_age(user_id, new_age)
                st.success(f'User ID {user_id} age updated to {new_age}!')
            else:
                st.error('Please enter valid user ID and age.')

    elif choice == 'Delete User':
        st.subheader('Delete a User')
        user_id = st.number_input('Enter user ID to delete', min_value=1)

        if st.button('Delete User'):
            if user_id:
                delete_user(user_id)
                st.success(f'User with ID {user_id} deleted successfully!')
            else:
                st.error('Please enter a valid user ID.')

if __name__ == "__main__":
    main()
