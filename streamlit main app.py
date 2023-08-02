import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe=pickle.load(open(r'C:\Users\sn767\coding\code\python\pipe.pkl','rb'))

df=pd.read_csv(r'C:\Users\sn767\coding\code\python\Cleaned_laptop_data.csv')



st.title('Laptop Price Predictor')

Brand=st.selectbox('Brand',sorted(df['Company'].unique()))

Type=st.selectbox('Type',sorted(df['TypeName'].unique()))

Ram=st.selectbox('Ram',sorted(df['Ram'].unique()))

weight=st.number_input('Weight')


Touch_screen =st.selectbox('Touch Screen',['Yes','No'])

Ips=st.selectbox('Ips',['Yes','No'])

screen_size=st.number_input('Screen Size')


resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

Cpu=st.selectbox('Cpu_Brand',sorted(df['Cpu_brand'].unique()))

Hdd=st.selectbox('HDD',sorted(df['HDD'].unique()))

Ssd=st.selectbox('SDD',sorted(df['SSD'].unique()))

Gpu=st.selectbox('Gpu brand',sorted(df['Gpu brand'].unique()))

Os=st.selectbox('OS',sorted(df['os'].unique()))


if st.button('Predict Price'):
    if Touch_screen == 'Yes':
        Touch_screen=1
    else:
        Touch_screen=0

    if Ips == 'Yes':
        Ips=1
    else:
        Ips=0

    X_res=int(resolution.split('x')[0])
    Y_res =int(resolution.split('x')[1])

    ppi=(((X_res**2)+(Y_res**2))**0.5)/screen_size

    query=np.array([Brand,Type,Ram,weight,Touch_screen,Ips,ppi,Cpu,Hdd,Ssd,Gpu,Os])
    query=pd.Series(query)

    predicted_value_exp =int(np.exp(pipe.predict([query])[0]))

    st.title(f'₹ {predicted_value_exp}')
