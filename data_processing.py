import pandas as pd
import numpy as np

#import CO2 emmision per capita data of the countries
co2 = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/CO2 Emissions.csv')
print(co2)

#import ev sales data of the countries
evs = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/EV Sales.csv')
print(evs)

#import poulation data of the countries
pop = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/Population by countries.csv')
print(pop)

#rename the header Row Labels into Country
pop = pop.rename(columns={'Row Labels':'Country'})
print(pop)

#removing the first column of both dataframes to calculate per capita value
co2_pc = co2.iloc[:,1:]

evs1 = evs.iloc[:,1:]
print(evs1)

pop1 = pop.iloc[:,1:]
print(pop1)

#divide total ev sales from total populaiton of each countries to get the per capita value
evs_pc = evs1.div(pop1)
evs_pc = evs_pc.round(5)
print(evs_pc)



#summary statistics in co2 percapita
mean_val = pd.DataFrame(co2_pc.mean(axis=1))
mean_val.columns = ['Mean']

median_val = pd.DataFrame(co2_pc.median(axis=1))
median_val.columns = ['Median']

std_dev = pd.DataFrame(co2_pc.std(axis=1))
std_dev.columns = ['Std. Dev']

min_val = pd.DataFrame(co2_pc.min(axis=1))
min_val.columns = ['Min']

max_val = pd.DataFrame(co2_pc.max(axis=1))
max_val.columns = ['Max']

range_val = pd.DataFrame(co2_pc.max(axis=1) - co2_pc.min(axis=1))
range_val.columns = ['Range']

co2_ss = pd.concat([mean_val,median_val,std_dev,min_val,max_val,range_val], axis=1)
print(co2_ss)

#summary statistics in ev sales per capita

mean_val1 = pd.DataFrame(evs_pc.mean(axis=1))
mean_val1.columns = ['Mean']

median_val1 = pd.DataFrame(evs_pc.median(axis=1))
median_val1.columns = ['Median']

std_dev1 = pd.DataFrame(evs_pc.std(axis=1))
std_dev1.columns = ['Std. Dev']

min_val1 = pd.DataFrame(evs_pc.min(axis=1))
min_val1.columns = ['Min']

max_val1 = pd.DataFrame(evs_pc.max(axis=1))
max_val1.columns = ['Max']

range_val1 = pd.DataFrame(evs_pc.max(axis=1) - evs_pc.min(axis=1))
range_val1.columns = ['Range']

evs_ss = pd.concat([mean_val1,median_val1,std_dev1,min_val1,max_val1,range_val1], axis=1)
print(evs_ss)


#isolate the column with countries to a single data frame

countries = pd.DataFrame(evs.iloc[:,:1])
print(countries)

#join all the tables with countries to export as csv files

co2_emission_summary_stat = pd.concat([countries,co2_ss],axis=1)
print(co2_emission_summary_stat)
co2_emission_summary_stat.to_csv('C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/co2_emission_summary_statistics.csv',index=False)

ev_sales_summary_stats = pd.concat([countries,evs_ss],axis=1)
print(ev_sales_summary_stats)
ev_sales_summary_stats.to_csv('C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/ev_sales_summary_statistics.csv',index=False)

ev_sales_per_capita = pd.concat([countries,evs_pc],axis=1)
ev_sales_per_capita.to_csv('C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/ev_sales_per_capita.csv',index=False)
