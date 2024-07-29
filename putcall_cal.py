# import numpy as np
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt


st.title("Put Call Parity Calculator")


st.write("---")

def put_call_parity_calc(asset_low, asset_high, strike, premium, call_column_name, put_column_name):
# Dataframe containig arbitrary asset price ranging from 0 to 100
    call = pd.DataFrame({
        'Asset price' : range(asset_low, asset_high+1)
    })
    
# Column for option payoff 
    call['$50 Call Option Payoff']= (call['Asset price']- strike).clip(lower=0)

# Column for option profit 
    call['$50 Call Option Profit'] = (call['$50 Call Option Payoff']- premium)

# Display the data frame 

    st.write("Call option Data:")
    st.write(call)

    # Plot call option

    fig, ax = plt.subplots()
    call.plot(kind='line', x= 'Asset price', y= '$50 Call Option Payoff', ax= ax, label= 'Call Option Payoff')
    call.plot(kind= 'line', x= 'Asset price', y='$50 Call Option Profit', ax= ax, label= 'Call Option Profit')
    ax.set_title(f'{call_column_name} payoff and profit')
    ax.set_xlabel('Asset Price')
    ax.set_ylabel('Payoff /Profit')
    st.pyplot(fig)


    
# Create a DataFrame containing arbitrary asset prices ranging from 0 to 100
    put = pd.DataFrame({
        'Asset price' : range(asset_low,asset_high+1)
          })

# Create a column for Option Payoff
    put['$50 Put Option Payoff'] = (strike - put['Asset price']).clip(lower=0)

# Create a column for Option Profit
    put['$50 Put Option Profit'] = (put['$50 Put Option Payoff'] - premium)

# Display the DataFrame
    st.write("Put option Data:")
    st.write(put)

    # Plot the put option payoff and profit
    fig, ax = plt.subplots()
    put.plot(kind='line', x='Asset price', y='$50 Put Option Payoff', ax=ax, label='Put Option Payoff')
    put.plot(kind='line', x='Asset price', y='$50 Put Option Profit', ax=ax, label='Put Option Profit')
    ax.set_title(f'{put_column_name} Payoff and Profit')
    ax.set_xlabel('Asset Price')
    ax.set_ylabel('Payoff / Profit')
    st.pyplot(fig)

col1= st.columns(1)
with col1[0]:
    st.header('Enter input parameters')
    # input parameters 
    asset_low = st.number_input(label="Low asset price", value=0)
    asset_high = st.number_input(label="High asset price", value= 100)
    strike= st.number_input(label= "Strike Price", value=50)
    premium= st.number_input(label= "Premium", value= 5)
    call_column_name= st.text_input("Call Option Column Name", value= "$50 Call Option")
    put_column_name= st.text_input("Put Option Column Name", value= "$50 Put Option")
    if st.button("Calculate result"):
        put_call_parity_calc(asset_low, asset_high, strike, premium, call_column_name, put_column_name)


