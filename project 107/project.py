import csv
import pandas as pa
import plotly_express as px

data = pa.read_csv('data.csv')

mean = data.groupby(["student_id","level"],as_index = False)["attempt"].mean()

fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()