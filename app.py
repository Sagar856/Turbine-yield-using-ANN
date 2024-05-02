import pickle
import streamlit as st
import numpy as np

st.title("Turbine Energy yield prediction Using ANN ")  

# Loading pickle files
model = pickle.load(open('webfiles/model.pkl', 'rb'))
x_train = pickle.load(open('webfiles/x_train_scaled.pkl', 'rb'))
y_train = pickle.load(open('webfiles/y_train.pkl', 'rb'))
x_test = pickle.load(open('webfiles/x_test_scaled.pkl', 'rb'))
fitted_model = pickle.load(open('webfiles/fitted_model.pkl', 'rb'))


# Taking Input from Users
# Input CDP(Compressor discharge pressure)
cdp = st.number_input(
    "CDP (Compressor discharge pressure) *",
    placeholder='Enter CDP',value=None
)
# Input GTEP(Gas turbine exhaust pressure)
gtep = st.number_input(
    "GTEP (Gas turbine exhaust pressure) *",
    placeholder='Enter GTEP',value=None
)
# Input TIT(Turbine inlet temperature)
tit = st.number_input(
    "TIT (Turbine inlet temperature) *",
    placeholder='Enter TIT',value=None
)
# Input TAT (Turbine after temperature)
tat = st.number_input(
    "TAT (Turbine after temperature) *",
    placeholder='Enter TAT',value=None
)
# Input AFDP
afdp = st.number_input(
    "AFDP (Air filter difference pressure)*",
    placeholder='Enter AFDP',value=None
)
# Input CO (Carbon monoxide)
co = st.number_input(
    "CO (Carbon monoxide) *",
    placeholder='Enter CO',value=None
)
# Input AT(Ambient temperature)
at = st.number_input(
    "AT (Ambient temperature) *",
    placeholder='Enter AT',value=None
)


# Converting input values into compatible array format
input_values = ([[ cdp,  gtep,  tit, tat, afdp, co, at],])
# input_values = ([[ 1.26334938,  1.33726395,  1.04657966, -0.68732919, -0.32243559, -0.63830171, -0.68276134],])
prediction_values = np.array(input_values)

# CDP	GTEP	TIT 	TAT 	AFDP	CO	AT

# Predicting Turbine yield based on given inputs
st.write('All fields are mandatory *')
if st.button('Check Output'):
    predicted_output = model.predict(prediction_values)
    st.text(predicted_output[0][0])

st.divider()
st.page_link("https://github.com/Sagar856/Car-Price-Prediction-Model-SB.git",label = 'Click here -- Git-hub source code')