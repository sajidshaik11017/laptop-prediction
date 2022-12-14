import streamlit as st
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")


company = st.selectbox('Brand',df['Company'].unique())

Type = st.selectbox('Type',df['TypeName'].unique())

Ram = st.selectbox('RAM(in GB'),[2,4,6,8,12,24,16,32,64]

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('IPS',['No','Yes'])

screen_size = st.number_input('Screen Size')

resolution =st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('predict price'):
    pass
