import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("W1: Data and visualization using Numpy")
st.markdown("Here you can see the dataframe created during this weeks project, and a map showing all the Airbnb listings: the blue dots represent listings close to the chosen location and the green dot represents the chosen location to visit. ")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude: ",
    lon="Longitude: ",
    color="Location: ",
    color_discrete_sequence=["green", "blue"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price: ",
    hover_data=["Meters from chosen location", "Location: "],
    labels={"color": "On the map: "},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 100 pounds per night
dataframe = dataframe[dataframe["Price"] <= 100]

st.dataframe(dataframe)

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "€ " + dataframe["Price"].round(2).astype(str) # <--- CHANGE THIS POUND SYMBOL IF YOU CHOSE CURRENCY OTHER THAN POUND
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "On my bucket list", 0.0: "Airbnb property"}
)

