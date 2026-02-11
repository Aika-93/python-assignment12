#Task 1: Plotting with Pandas

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Connect to the Database 
conn = sqlite3.connect("../db/lesson.db")

#Load employee revenue data using SQL
df = pd.read_sql("SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id", conn)
print(df.head())

#Close the database connection 
conn.close()

#Create a bar chart: x = employee last name, y = revenue
df.plot(x = "last_name", y = "revenue", kind = "bar", color = "purple", title = "Total Sales Revenue per Employee")

#Show the plot
plt.show()