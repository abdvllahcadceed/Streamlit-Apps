import streamlit as st
import pandas as pd
import folium


# App title
st.set_page_config(page_title="☕️🌟 Mogadishu Coffee Shops Viz")
st.title('☕️🌟 Mogadishu Coffee Shops Visualization')

st.markdown('''
Application built by [Abdullahi M. Cadceed](https://twitter.com/@abdullahcadceed)
''')

# Coffee shops data
coffeeShops = pd.DataFrame({
    Name = ['Beydan', 'Kaizen', 'Castello', 'Salool', 'Java'],
    Latitude = [2.033, 2.037, 2.030, 2.036, 2.032],
    Longitude = [45.313, 45.302, 45.303, 45.305, 45.315],
    Cuisine = ['Shaah', 'Cunno', 'Cabitaan', 'Daango', 'Qaaci'],
    Rating = [4.50, 4.70, 4.40, 4.30, 4.80]
})

# Function to create an interactive map
def create_map(data):
    city_map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=14)

    for index, row in data.iterrows():
        folium.Marker(
            location=[row[Latitude], row[Longitude]],
            popup=f"{row[Name]} ({row[Cuisine]}) - Rating: {row[Rating]}",
            icon=folium.Icon(color='blue')
        ).add_to(city_map)

    return city_map

# Main Streamlit app
def main():

    # Display the coffee shops data in a table
    st.subheader('Coffee Shops Data')
    st.dataframe(coffeeShops)

    # Filter by cuisine type
    cuisine_type = st.selectbox('Filter by Cuisine', coffeeShops['Cuisine'].unique())
    if cuisine_type != 'All':
        filtered_data = coffeeShops[coffeeShops['Cuisine'] == cuisine_type]
    else:
        filtered_data = coffeeShops

    # Filter by minimum rating
    min_rating = st.slider('Minimum Rating', 0.0, 5.0, 0.0, 0.1)
    filtered_data = filtered_data[filtered_data['Rating'] >= min_rating]

    # Display filtered data
    st.subheader('Filtered Coffee Shops Data')
    st.dataframe(filtered_data)

    # Display the map
    st.subheader('Coffee Shops Map')
    coffee_map = create_map(filtered_data)
    st.write(coffee_map)

if __name__ == '__main__':
    main()
