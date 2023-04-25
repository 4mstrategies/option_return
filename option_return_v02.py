import streamlit as st

def option_return(option_type:str, buy_sell:str, lot_size:int, premium:float, strike_price:float, final_price:float):
    lot_size = lot_size*100
    if buy_sell == 'sell':
        if option_type == 'call':
            if final_price < strike_price:
                return premium * lot_size
            else:
                return (strike_price - final_price) * lot_size + premium * lot_size

        elif option_type == 'put':
            if final_price > strike_price:
                return premium * lot_size
            else:
                return (final_price - strike_price) * lot_size + premium * lot_size

    elif buy_sell == 'buy':
        if option_type == 'call':
            if final_price < strike_price:
                return - premium * lot_size
            else:
                return (final_price - strike_price) * lot_size- premium * lot_size

        elif option_type == 'put':
            if final_price > strike_price:
                return - premium * lot_size
            else:
                return (strike_price - final_price) * lot_size- premium * lot_size



option_types = []
buy_sells = []
lot_sizes = []
premiums = []
strike_prices = []

st.write("Please assume price on maturity")
final_prices =  st.number_input('final price')  
n_options = st.number_input('Number of Options', key='n_options', value=2)
st.write("-"*50)

for i in range(n_options):
    col1, col2, col3 = st.columns(3)
    option_types.append(col1.selectbox('Option Type', ['call', 'put'], key=f'option_type_{i}'))
    buy_sells.append(col2.selectbox('Buy/Sell', ['buy', 'sell'], key=f'buy_sell_{i}'))
    lot_sizes.append(col1.number_input('Lot Size', key=f'lot_size_{i}'))
    premiums.append(col2.number_input('Premium', key=f'premium_{i}'))
    strike_prices.append(col3.number_input('Strike Price', key=f'strike_price_{i}'))
    result = option_return(option_types[i], buy_sells[i], lot_sizes[i], premiums[i], strike_prices[i], final_prices)    
    st.write(f"Option {i+1}: {result}")
    st.write("-"*50)

results = []
for i in range(n_options):
    results.append(option_return(option_types[i], buy_sells[i], lot_sizes[i], premiums[i], strike_prices[i], final_prices))




st.write("Total Result")
st.write(f"Total: {sum(results)}")
