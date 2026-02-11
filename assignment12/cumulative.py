#Task 2: A Line Plot with Pandas

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Connect to the Database 
conn = sqlite3.connect("../db/lesson.db")

#Load order totals into a DataFrame using SQL 
df = pd.read_sql("SELECT o.order_id, SUM(p.price * l.quantity) AS total_price FROM orders o JOIN line_items l ON o.order_id  = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY o.order_id", conn)

print(df.head())

#Close the database connection 
conn.close()

#Function to calculate cumulative revenue
def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

#Add cumulative column to the DataFrame
df['cumulative'] = df.apply(cumulative, axis=1)

#Plot cumulative revenue vs order_id
df.plot(x = "order_id", y = "cumulative", kind="line", title = "Cumulative Revenue Over Orders")
plt.show()


#Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata

#Load the wind dataset
df1 = pldata.wind(return_type='pandas')

#Show first and last 10 rows
print(df1.head(10))
print(df1.tail(10))

#Clean 'strength' column
df1["strength"] = df1["strength"].str.replace(r'[^0-9.]', '', regex=True)
df1["strength"] = df1["strength"].astype(float)

#Create interactive scatter plot
fig = px.scatter(df1, x = "strength", y = "frequency", color = "direction", title = "Wind Strength vs Requency by Direction", hover_data = ["frequency"])

#Save plot as HTML and open it in browser
fig.write_html("wind.html", auto_open=True)

