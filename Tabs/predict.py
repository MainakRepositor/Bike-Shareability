"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Bike Pick.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Bike Count", int(df["Bike_Count"].min()), int(df["Bike_Count"].max()))
    B = st.slider("Hour", int(df["Hour"].min()), int(df["Hour"].max()))
    C = st.slider("Temperature (°C)", int(df["Temperature"].min()), int(df["Temperature"].max()))
    D = st.slider("Humidity (%)", int(df["Humidity"].min()), int(df["Humidity"].max()))
    E = st.slider("Wind speed (Nauts)", int(df["Wind_speed"].min()), int(df["Wind_speed"].max()))
    F = st.slider("Visibility (m)", float(df["Visibility"].min()), float(df["Visibility"].max()))
    G = st.slider("Dew point (°C)", float(df["Dew_point"].min()), float(df["Dew_point"].max()))
    H = st.slider("SolarRadiation", int(df["SolarRadiation"].min()), int(df["SolarRadiation"].max()))
    I = st.slider("Rainfall (cm)", int(df["Rainfall"].min()), int(df["Rainfall"].max()))
    J = st.slider("Snowfall (cm)", int(df["Snowfall"].min()), int(df["Snowfall"].max()))
    st.info('''1 : Summer | 2 : Winter | 3 : Spring | 4 : Autumn''')
    K = st.slider("Seasons", int(df["Seasons"].min()), int(df["Seasons"].max()))
    st.info('''1 : Holiday | 2 : Working Day''')
    L = st.slider("Holiday", int(df["Holiday"].min()), int(df["Holiday"].max()))
    
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("High chance of bike being borrowed")
        else:
            st.warning("Low changes of bike being borrowed")

        # Print teh score of the model 
        st.write("The model has an accuracy of ", (score*100),"%")
