Used Python and SQLAlchemy to do climate analysis and data exploration of a Hawaii climate database. Analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Loaded the query results into a Pandas DataFrame.

* Calculateed the rainfall per weather station using the previous year's matching dates.

* Calculateed the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

* Designed a query to retrieve the last 12 months of temperature observation data.

  * Filtered by the station with the highest number of observations.

  * Plotted the results as a histogram with `bins=12`.

### Climate App

Designed a Flask API based on the queries. 

  * Includes home page and list of all routes that are available

  * Converts query results to a dictionary.

  * Returns the JSON representation of the dictionary.

### Analysis 

* Conducted statistical analysis to inform decisions about when to take vacation in Hawaii. 
