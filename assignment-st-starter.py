# import packages


# show the title


# read csv and show the dataframe


# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
data = pd.read_csv('train.csv')

# Set up the title with your name
st.title('Titanic App by [YANLIN LIU]')

# Display the dataset
st.write(data)

# Create a figure with three subplots for the boxplots of Fare by Pclass
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plotting the box plot for each Pclass
for i, pclass in enumerate(sorted(data['Pclass'].unique())):
    sns.boxplot(ax=axes[i], x='Pclass', y='Fare', data=data[data['Pclass'] == pclass])
    axes[i].set_title(f'Fare by Pclass = {pclass}')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
st.pyplot(fig)