import geopandas as gpd
from geodatasets import get_path
import geodatasets
import pandas as pd
from shapely.geometry import Point

shapefile_path = r'C:/Users/Matt/Streamlit/data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)
world = world.to_crs(epsg=3395)  # Use World Mercator projection (EPSG:3395)

eq_df = pd.read_csv('data/Volcanoes.csv')
eq_df_cleaned = eq_df.dropna(subset=['latitude', 'longitude'])
eq_df_cleaned['country'] = ''

for row in range(len(eq_df_cleaned)):
    earthquake_point = Point(float(eq_df_cleaned.loc[row, 'longitude']), float(eq_df_cleaned.loc[row, 'latitude']))
    earthquake_gs = gpd.GeoSeries(earthquake_point, crs="EPSG:4326")
    earthquake_gs = earthquake_gs.to_crs(epsg=3395)

    # Now check if the point is inside any country
    matched_country = world[world.contains(earthquake_gs.geometry[0])]
    # If matched_country is not empty, fetch the country name
    if not matched_country.empty:
        # Ensure to access the first row
        country_name = matched_country.iloc[0]["NAME"]  # Adjust to correct column name
    else:
        # If no match, find the nearest country
        world["distance"] = world.geometry.centroid.distance(earthquake_gs.geometry[0])

        # Check if distance column is populated and not empty
        if not world["distance"].empty:
            nearest_country = world.loc[world["distance"].idxmin()]
            country_name = nearest_country["NAME"]  # Adjust to correct column name
        else:
            country_name = "Unknown"  # Handle cases where distance calculation fails

    eq_df_cleaned.loc[row, 'country'] = country_name

eq_df_cleaned.to_csv('data/Volcanoes_cleaned.csv', index=False)