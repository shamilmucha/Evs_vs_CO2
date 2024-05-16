import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

co2 = pd.read_csv(r'file_path')
print(co2)

evs = pd.read_csv(r'file_path')
evs = evs.iloc[:,1:]
print(evs)

co2_ss = pd.read_csv(r'file_path')
print(co2_ss)

ev_ss = pd.read_csv(r'file_path')
print(ev_ss)


sns.set_theme(style="whitegrid")

#mean values of ev sales per capita
sns.barplot(data=ev_ss, x="Country",y="Mean").set_title('Average EV Sales per capita')
plt.show()

#mean values of co2 emission per capita
sns.barplot(data=co2_ss, x="Country",y="Mean").set_title('Average CO2 Emissions per capita in Tons')
plt.show()

