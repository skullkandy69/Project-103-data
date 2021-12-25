import pandas as pd
import plotly.express as px
df = pd.read_csv("line_chart.csv")
fig = px.scatter(df,x="Year" , y = "Per capita income",  title = "Per Capita Income" , color = "Country")
fig.show()ho