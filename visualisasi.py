import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

order_orderdata_df = pd.read_csv("https://raw.githubusercontent.com/indhialhawa/Bangkit_VisualisasiData/main/data.csv")
monthly_orders_df = pd.read_csv("https://raw.githubusercontent.com/indhialhawa/Bangkit_VisualisasiData/main/data1.csv")

st.title('DASHBOARD DATA E-COMMERCE')

# Pertanyaan 1
monthly_orders_df['order_purchase_timestamp'] = pd.to_datetime(order_orderdata_df['order_purchase_timestamp'])
df_2018 = monthly_orders_df[(monthly_orders_df['order_purchase_timestamp'].dt.year == 2018)]
monthly_sales = df_2018.resample('M', on='order_purchase_timestamp')['order_count'].sum()

st.title('Tren Pembelian Tahun 2018')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_sales.index, monthly_sales.values, marker='o', color='skyblue', linestyle='-')
ax.set_title('Total Pembelian per Bulan (2018)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Pembelian')

st.pyplot(fig)

monthly_orders_df['order_purchase_timestamp'] = pd.to_datetime(order_orderdata_df['order_purchase_timestamp'])
df_2018 = monthly_orders_df[(monthly_orders_df['order_purchase_timestamp'].dt.year == 2018)]
monthly_sales = df_2018.resample('M', on='order_purchase_timestamp')['revenue'].sum()

st.title('Tren Revenue Tahun 2018')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_sales.index, monthly_sales.values, marker='o', color='skyblue', linestyle='-')
ax.set_title('Total Revenue per Bulan (2018)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Pembelian')

st.pyplot(fig)

# Pertanyaan 2
payment_type_sum = order_orderdata_df.groupby(by=["payment_type"]).agg({
    "payment_value": "sum"
}).reset_index()

st.title('Total Pembayaran Berdasarkan Tipe Pembayaran')

plt.figure(figsize=(10, 6))
sns.barplot(x='payment_type', y='payment_value', data=payment_type_sum, palette='pastel')
plt.title('Total Pembayaran Berdasarkan Tipe Pembayaran', fontsize=15)
plt.xlabel('Tipe Pembayaran', fontsize=12)
plt.ylabel('Total Pembayaran', fontsize=12)

st.pyplot(plt)
