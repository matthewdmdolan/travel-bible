import sqlite3

import requests
import json
import pandas as pd
import time

# Define a function to fetch details for a list of countries
def fetch_countries(country_list):
    base_url = "https://restcountries.com/v3.1/name/"
    all_countries = []

    for country_name in country_list:
        response = requests.get(base_url + country_name)
        if response.status_code == 200:
            all_countries.extend(response.json())
        time.sleep(1)  # Introducing a delay of 2 seconds between each request

    return all_countries


# Obtain a list of all countries first (you can get a list from other source or limit it to some countries you're interested in)
countries_to_fetch = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                      'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                      'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                      'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of',
                      'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island',
                      'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso',
                      'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
                      'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
                      'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
                      'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia',
                      'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                      'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
                      'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland',
                      'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia',
                      'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',
                      'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                      'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong',
                      'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland',
                      'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
                      'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait',
                      'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                      'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of',
                      'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique',
                      'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of',
                      'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
                      'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
                      'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway',
                      'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea',
                      'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
                      'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy',
                      'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',
                      'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines',
                      'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
                      'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia',
                      'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands',
                      'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland',
                      'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan',
                      'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',
                      'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu',
                      'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
                      'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                      'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British',
                      'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']


# Fetch countries data in batches
batch_size = 10
parsed_data = []

for i in range(0, len(countries_to_fetch), batch_size):
    batch_countries = countries_to_fetch[i: i + batch_size]
    country_data = fetch_countries(batch_countries)

    for country in country_data:
        country_info = {}
        country_info["Name"] = country["name"]["common"]
        country_info["Name Official"] = country["name"]["official"]
        # currency_data = list(country["currencies"].values())[0]
        # country_info["Currency Name"] = currency_data["name"]
        # country_info["Currency Symbol"] = currency_data["symbol"]
        # country_info["Capital"] = country["capital"]
        country_info["Region"] = country["region"]
        # country_info["Subregion"] = country["subregion"]
        # country_info["Languages"] = ', '.join(country["languages"].values())
        country_info["Lat lng"] = country["latlng"]
        country_info["Area"] = country["area"]
        country_info["Population"] = country["population"]

        parsed_data.append(country_info)

    time.sleep(2)  # Introducing a delay of 5 seconds between each batch

df = pd.DataFrame(parsed_data)
df['Lat lng'] = df['Lat lng'].apply(str)
print(df)

# Write to SQLite3 database
conn = sqlite3.connect('travel_info_database.sqlite3')
df.to_sql('country_info', conn, if_exists='replace', index=False)
conn.close()

print("Data written to SQLite3 database.")
