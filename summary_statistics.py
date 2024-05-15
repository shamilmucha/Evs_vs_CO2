import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

co2 = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/CO2 Emissions.csv')
print(co2)

evs = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/EV Sales.csv')
evs = evs.iloc[:,1:]
print(evs)

co2_ss = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/co2_emission_summary_statistics.csv')
print(co2_ss)

ev_ss = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/ev_sales_summary_statistics.csv')
print(ev_ss)


sns.set_theme(style="whitegrid")

#mean values of ev sales per capita
sns.barplot(data=ev_ss, x="Country",y="Mean").set_title('Average EV Sales per capita')
plt.show()

#mean values of co2 emission per capita
sns.barplot(data=co2_ss, x="Country",y="Mean").set_title('Average CO2 Emissions per capita in Tons')
plt.show()

