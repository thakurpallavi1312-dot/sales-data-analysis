import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Retail Sales Data Analysis Dashboard")

# Generate Sample Data
np.random.seed(42)
n_rows = 500

data = {
    'OrderID': np.arange(1001, 1001 + n_rows),
    'OrderDate': pd.date_range(start='2023-01-01', periods=n_rows, freq='D'),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home & Kitchen', 'Beauty'], n_rows),
    'Product': np.random.choice(['Laptop', 'Phone', 'Shirt', 'Jeans', 'Blender', 'Lipstick', 'Headphones'], n_rows),
    'Quantity': np.random.randint(1, 5, n_rows),
    'UnitPrice': np.random.uniform(10, 500, n_rows),
    'CustomerRegion': np.random.choice(['North', 'South', 'East', 'West'], n_rows)
}

df = pd.DataFrame(data)
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Sidebar Filter
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox("Select Category", ['All'] + list(df['Category'].unique()))

if selected_category != 'All':
    filtered_df = df[df['Category'] == selected_category]
else:
    filtered_df = df

# Key Metrics
st.metric("Total Revenue", f"${filtered_df['TotalSales'].sum():,.2f}")

# Charts
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
sns.barplot(data=filtered_df, x='CustomerRegion', y='TotalSales', ax=ax[0], palette='Blues_d')
ax[0].set_title("Sales by Region")

top_prod = filtered_df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5)
top_prod.plot(kind='bar', ax=ax[1], color='teal')
ax[1].set_title("Top 5 Products")

st.pyplot(fig)
