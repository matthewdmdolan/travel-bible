# The Travel Bible

This repo aims to make tracking my own travels, both past and future, a lot easier. 

Ultimately, the repo ingests two google sheet files into sqlite tables. 1) Past Travel Experiences ii) Planned Travel Experiences. Both these tables are ingested monthly to ensure updates and written to an SQLite DB for data integrity. Furthermore, an api call is made to gain up to date social/demographic/demographic information on each country, e.g. population, using the REST Countries API (source: https://restcountries.com/)

The SQL Config file is for checking the database schema and ensuring all tables are loaded. Annoyingly due to the limited functionality of Tableau Public I then have to write the SQL Query to CSV for visualisation. So please ignore the sqlite-to-csv file if you are lucky enough to have the full Tableau Desktop version with all it's shiny drivers.

The main Script orchestrates all of this. Txt file with requirements has been included.

Finally, the solution is visualised using Tableau: https://public.tableau.com/app/profile/matt.dolan/viz/TravelBible. 


