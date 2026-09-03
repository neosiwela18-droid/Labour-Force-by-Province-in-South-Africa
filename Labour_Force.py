import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("notinjob.csv")

x = list(df["placeName"])  
y = df["Value:Count_Person_InLaborForce"]

from matplotlib.ticker import FuncFormatter

def millions(value, position):
    return f"{value / 1_000_000:.1f}M"

plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))

plt.bar(x, y, width=0.4)
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))

plt.xlabel("Province", labelpad=20, fontweight = 'bold')
plt.ylabel("People in Labour Force", labelpad= 20, fontweight = 'bold')
plt.title("Labour Force by Province in South Africa", fontweight = 'bold', fontsize=15)
plt.grid(axis="y", alpha=0.4,linestyle="--")
  
plt.show()
