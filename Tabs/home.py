"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Diabetes Prediction System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            🏍️ "Unleash the Thrill, Share the Ride: Introducing Motorbike Shareability, India's New Adventure Avenue! 🇮🇳 Embark on a revolutionary journey where every twist of the road becomes a shared memory. Imagine cruising through the vibrant tapestry of India's landscapes, from bustling bazaars to serene ghats, all while forging unforgettable connections. With our state-of-the-art motorbike sharing platform, ignite a sense of camaraderie as you swap stories at every pitstop, creating bonds as strong as steel. Fuel both your wanderlust and your eco-conscious spirit by reducing your carbon footprint, one exhilarating ride at a time. Whether you're a lone wolf seeking companions for your escapades or a social spirit eager to rev up with new friends, motorbike shareability caters to every rider's fantasy. Join us in redefining travel, one shared adventure under the sun. 🌄 Let's ride together, let's ride India!" 🌟🛵
        </p>
    """, unsafe_allow_html=True)
