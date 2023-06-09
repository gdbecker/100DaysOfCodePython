# 100 Days of Code: Python
# July 27, 2022
# Custom web scraper: LEGO part colors

# Import modules
from bs4 import BeautifulSoup
import requests
import pandas

# Starting lists for making csv later
id_data = []
name_data = []
rgb_data = []
num_parts_data = []
num_sets_data = []
first_year_data = []
last_year_data = []
href_data = []

# Make soup for LEGO part colors
response = requests.get("https://rebrickable.com/colors/")
wp = response.text
soup = BeautifulSoup(wp, "html.parser")

# Get all colors rows from table
tables = soup.findChildren(name="table", id="colors_table")
parts_table = tables[0]

parts_rows = parts_table.findChildren("tr")
parts_rows.reverse()

# Go through each row and pull desired data, add to each data list
for row in parts_rows:
    try:
        row_data = row.findChildren("td")
        id_data.append(row_data[1].getText())
        name_data.append(row_data[2].getText())
        rgb_data.append(row_data[3].getText())
        num_parts_data.append(row_data[4].getText())
        num_sets_data.append(row_data[5].getText())
        first_year_data.append(row_data[6].getText())
        last_year_data.append(row_data[7].getText())
        href_data.append("https://rebrickable.com" + row_data[0].find("a")["href"])
    except:
        pass

# Make part colors dictionary, assign to a DataFrame, convert to csv
parts_dict = {
    "ID": id_data,
    "Name": name_data,
    "RGB": rgb_data,
    "Num Parts": num_parts_data,
    "Num Sets": num_sets_data,
    "First Year": first_year_data,
    "Last Year": last_year_data,
    "Link": href_data
}

df = pandas.DataFrame(parts_dict)
df.to_csv("lego_parts_colors.csv")