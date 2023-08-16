# geokakao

The `geokakao` package provides a convenient way to utilize the Kakao API for converting addresses into GeoPackages. This package allows you to extract coordinates (longitude and latitude) from provided addresses and integrate them into a DataFrame. You can then convert the enriched DataFrame back into the GeoPackage format, facilitating seamless integration of address data with geographic coordinates.

## Features

- Convert addresses to coordinates (longitude and latitude) using the Kakao API.
- Integrate coordinate information into a DataFrame containing address data.
- Convert the enriched DataFrame back into the GeoPackage format.

## Installation

To install the `geokakao` package, you can use the following pip command:

```bash
pip install geokakao
```

## Usage

Here's a simple example of how to use the geokakao package:
```python
# Load your DataFrame with address information
data = {'Name': ['국립공원공단 본사',
                 '국립공원연구원 본원',
                 '치악산국립공원사무소'],
        'Address': ['강원특별자치도 원주시 혁신로 22',
                    '강원특별자치도 원주시 단구로 171',
                    '강원특별자치도 원주시 소초면 무쇠점2길 26']}
df = pd.DataFrame(data)
```
```python
# Convert addresses to coordinates and integrate into the DataFrame
gk.add_coordinates_to_dataframe(df, 'Address')
df.to_csv('korea_np.csv', index=False, encoding='utf-8')
```
```python
# Save the enriched DataFrame to a GeoPackage file
input_csv = "korea_np.csv"
output_gpkg = "korea_np.gpkg"

gk.csv_to_gpkg(input_csv, output_gpkg)
```
