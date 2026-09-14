import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Configuration
st.set_page_config(page_title="Financial Dashboard", layout="wide")
st.title("📊 Divisional Financial Performance")

# 2. CLEAN DATASET (We use lists inside columns to guarantee no empty syntax)
data = {
    "Division": ["Division A", "Division B", "Division C"],
    "Sales":,
    "Gross Profit":,
    "Gross_Margin": [40.0, 40.0, 30.0]
}
division_summary = pd.DataFrame(data)

# 3. Display high-level metric cards
total_sales = division_summary['Sales'].sum()
total_profit = division_summary['Gross Profit'].sum()

col1, col2 = st.columns(2)
col1.metric(label="Total Company Sales", value=f"${total_sales:,.2f}")
col2.metric(label="Total Gross Profit", value=f"${total_profit:,.2f}")

st.markdown("---") 

# 4. Build Grouped Chart Layout
divisions = division_summary['Division']
sales = division_summary['Sales']
gross_profit = division_summary['Gross Profit']
gross_margin = division_summary['Gross_Margin']

x = np.arange(len(divisions))
width = 0.25

fig, ax1 = plt.subplots(figsize=(10, 5))

bar1 = ax1.bar(x - width, sales, width, label='Sales ($)', color='royalblue')
bar2 = ax1.bar(x, gross_profit, width, label='Gross Profit ($)', color='forestgreen')

ax2 = ax1.twinx()
bar3 = ax2.bar(x + width, gross_margin, width, label='Gross Margin (%)', color='orange')

ax1.set_xlabel('Divisions', fontweight='bold')
ax1.set_ylabel('Currency Value ($)', fontweight='bold')
ax2.set_ylabel('Percentage (%)', color='orange', fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels(divisions)

bars = [bar1, bar2, bar3]
labels = [b.get_label() for b in bars]
ax1.legend(bars, labels, loc='upper left')
plt.tight_layout()

# 5. Render inside Streamlit
st.subheader("Performance Breakdown Chart")
st.pyplot(fig)

if st.checkbox("Show Raw Data Table"):
    st.dataframe(division_summary)
