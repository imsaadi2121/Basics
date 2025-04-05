import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the application
st.title('Iris Dataset Explorer')

# Load the Iris dataset
@st.cache_data
def load_data():
    return sns.load_dataset('iris')

df = load_data()

# Sidebar for user inputs
st.sidebar.header('User Input Features')

# Select species
species = st.sidebar.multiselect('Select Species', options=df['species'].unique(), default=df['species'].unique())

# Select sepal length range
sepal_length = st.sidebar.slider('Sepal Length Range', float(df['sepal_length'].min()), float(df['sepal_length'].max()), (float(df['sepal_length'].min()), float(df['sepal_length'].max())))

# Filter data based on user input
filtered_data = df[(df['species'].isin(species)) & (df['sepal_length'] >= sepal_length[0]) & (df['sepal_length'] <= sepal_length[1])]

# Display filtered data
st.write(f"Displaying {filtered_data.shape[0]} rows of data")
st.dataframe(filtered_data)

# Display pairplot
st.subheader('Pairplot of Selected Data')
pairplot_fig = sns.pairplot(filtered_data, hue='species')
st.pyplot(pairplot_fig)

# Display correlation heatmap
st.subheader('Correlation Heatmap')
numeric_df = filtered_data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
corr = numeric_df.corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

# Display individual feature distributions
st.subheader('Feature Distributions')
feature = st.selectbox('Select Feature', options=numeric_df.columns)
fig, ax = plt.subplots()
sns.histplot(filtered_data[feature], kde=True, ax=ax)
st.pyplot(fig)

# Footer
st.markdown('---')
st.markdown('Built with Streamlit')
