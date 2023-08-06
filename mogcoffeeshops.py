import streamlit as st
import pandas as pd
import folium

# App title
st.set_page_config(page_title="☕️🌟 Mogadishu Coffee Shops Viz")
st.title('☕️🌟 Mogadishu Coffee Shops Visualization')

st.markdown('''
Application built by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)
''')

# Load the data
df = pd.read_csv('mogCoffeeShops.csv')

# Filter out any missing or irrelevant data
df = df[['Name', 'Location', 'Cuisine', 'Rating', 'Price_Range']].dropna()

# Create a map of the city
m = folium.Map(location=[2.0469, 45.3181], zoom_start=12)

# Add markers for each restaurant
for index, row in df.iterrows():
    marker = folium.Marker(
        location=[row['Location'][0], row['Location'][1]],
        popup=row['Name'],
        icon=folium.Icon(color='red')
    )
    m.add_child(marker)

# Display the map
st.write("Coffee Shops in {}".format(df['Location'].mean()))
st.write(m)

# Interactive map
st.write("Click on a marker to see more details about the Coffee Shop")

@st.button("Filter by Cuisine")
def filter_by_cuisine():
    selected_cuisine = st.selectbox("Select a Cuisine", ["All", "Somali", "Ethiopian", "Kenyan", "Ugandan", "Rwandan"])
    filtered_df = df[(df['Cuisine'] == selected_cuisine)]
    m.clear_markers()
    for index, row in filtered_df.iterrows():
        marker = folium.Marker(
            location=[row['Location'][0], row['Location'][1]],
            popup=row['Name'],
            icon=folium.Icon(color='red')
        )
        m.add_child(marker)

@st.button("Filter by Price Range")
def filter_by_price_range():
    min_price = st.number_input("Enter minimum price", 1, 100)
    max_price = st.number_input("Enter maximum price", 1, 100)
    filtered_df = df[(df['Price_Range'] >= min_price) & (df['Price_Range'] <= max_price)]
    m.clear_markers()
    for index, row in filtered_df.iterrows():
        marker = folium.Marker(
            location=[row['Location'][0], row['Location'][1]],
            popup=row['Name'],
            icon=folium.Icon(color='red')
        )
        m.add_child(marker)

if __name__ == '__main__':
    st.write(m)
    st.show()
