import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_berlian.sav', 'rb'))

st.title('Estimasi Harga Berlian')

carat = st.number_input('Input nilai Carat')
depth = st.number_input('Input nilai Depth')
table = st.number_input('Input nilai Table')
x = st.number_input('Input nilai X')
y = st.number_input('Input nilai Y')
z = st.number_input('Input nilai Z')

predict = ''

if st.button('Estimasi Harga Berlian'):
    predict = model.predict(
        [[carat, depth, table, x, y, z]]
    )
    st.write ('Estimasi harga diamond dalam $ US (Ribu) : ', predict)
    st.write ('Estimasi harga diamond dalam IDR :', predict*14991)