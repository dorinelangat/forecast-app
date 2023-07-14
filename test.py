import streamlit as st
import requests
from PIL import Image
import pandas as pd
import pickle

# Load the pickled forecast DataFrame
with open('forecast.pkl', 'rb') as f:
    forecast_df = pickle.load(f)
    
st.set_page_config(page_title="Food Balance Forecast", page_icon="🌾", layout="wide")
st.markdown("<h1 style='text-align: center; color: green;'>Food Balance Forecast</h1>", unsafe_allow_html=True)

def main():
    # Streamlit app code
    #st.title("Forecast for Specific Year")

    # Add the flag of Kenya from the provided image URL
    response = requests.get("https://github.com/Muramati/FAOStat-Dataset-Time-Series/raw/main/assets/Flag_of_Kenya.png")
    #image = Image.open(BytesIO(response.content))
    #st.image(image, caption="Flag of Kenya", use_column_width=True)

    # Create a dropdown select for the area input
    area_options = [None, 'Kenya', 'Uganda', 'Tanzania', 'Rwanda']
    area_input = st.selectbox('Select the area:', area_options)

    # Prompt the user to enter a specific year
    target_year_input = st.text_input("Enter the target year for prediction:")

    # Display the forecast for the target year
    if st.button('Predict'):
        if target_year_input in forecast_df.index.year.astype(str).values:
            target_forecast = forecast_df.loc[forecast_df.index.year == int(target_year_input)]
            st.subheader(f"Forecast for {target_year_input}:")
            st.dataframe(target_forecast)
        else:
            st.write(f"No forecast available for {target_year_input}.")

    # Create an expander for the predicted results and explanations
    with st.expander("Click here to see for more details"):
        st.write(f"**Domestic Supply Quantity:** The total amount of a particular agricultural commodity that is available for human consumption within a country. It is calculated as the sum of domestic production, imports, and changes in stocks, minus exports. It is measured in metric tons.")

        st.write(f"**Production:** The amount of a particular agricultural commodity that is produced within a country. It includes both crops and livestock products, and is measured in metric tons.")

        st.write(f"**Export Quantity:** The amount of a particular agricultural commodity that is exported from a country to other countries. It is measured in metric tons.")

        st.write(f"**Import Quantity:** The amount of a particular agricultural commodity that is imported into a country from other countries. It is measured in metric tons.")


if __name__ == '__main__':
    main()