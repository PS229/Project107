import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("project.csv")
student = df.loc[df["id"] == "TRL_987"]
print(student.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = ["Level 1", "Level 2", "Level 3", "Level 4"],
    y = student.groupby("level")["attempt"].mean() 
))
fig.show()