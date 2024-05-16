import pandas as pd
import matplotlib as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

co2 = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/CO2 Emissions.csv')
co2 = co2.rename(columns={'Country':'Year'})
co2 = co2.replace({'Australia':'Aus_CO2','Austria':'Aut_CO2','Belgium':'Bel_CO2','Canada':'Can_CO2','China':'Chn_CO2','Denmark':'Den_CO2','Finland':'Fin_CO2','France':'Fra_CO2','Germany':'Ger_CO2','Italy':'Ita_CO2','Japan':'Jpn_CO2','Netherlands':'Nld_CO2','Norway':'Nor_CO2','Portugal':'Ptg_CO2','South Korea':'Kor_CO2','Spain':'Esp_CO2','Sweden':'Swe_CO2','Switzerland':'Swi_CO2','United Kingdom':'UK_CO2','USA':'USA_CO2'},regex=True)
co2 = co2.set_index('Year').T


evs = pd.read_csv(r'C:/Users/Shamil Malinda/Desktop/Assignment/Projects/Final Report/Final Report Python/Final Report Code/ev_sales_per_capita.csv')
evs = evs.rename(columns={'Country':'Year'})
evs = evs.replace({'Australia':'Aus_evs','Austria':'Aut_evs','Belgium':'Bel_evs','Canada':'Can_evs','China':'Chn_evs','Denmark':'Den_evs','Finland':'Fin_evs','France':'Fra_evs','Germany':'Ger_evs','Italy':'Ita_evs','Japan':'Jpn_evs','Netherlands':'Nld_evs','Norway':'Nor_evs','Portugal':'Ptg_evs','South Korea':'Kor_evs','Spain':'Esp_evs','Sweden':'Swe_evs','Switzerland':'Swi_evs','United Kingdom':'UK_evs','USA':'USA_evs'},regex=True)
evs = evs.set_index('Year').T


#Country = Australia

co2_aus = co2.iloc[:,:1]
evs_aus = evs.iloc[:,:1]

aus_cor = pd.concat([co2_aus,evs_aus],axis=1)
print(aus_cor)

aus_model = ols('Aus_CO2 ~ Aus_evs', data = aus_cor).fit()
anova_table = sm.stats.anova_lm(aus_model, typ=2)
print(anova_table)

#country = Austria

co2_aut = co2.iloc[:,1:2]
evs_aut = evs.iloc[:,1:2]

aut_cor = pd.concat([co2_aut,evs_aut], axis=1)
print(aut_cor)

aut_model = ols('Aut_CO2 ~ Aut_evs', data = aut_cor).fit()
anova_table = sm.stats.anova_lm(aut_model, typ=2)
print(anova_table)


#country = Belgium

co2_bel = co2.iloc[:,2:3]
evs_bel = evs.iloc[:,2:3]

bel_cor = pd.concat([co2_bel,evs_bel], axis=1)
print(bel_cor)

bel_model = ols('Bel_CO2 ~ Bel_evs', data = bel_cor).fit()
anova_table = sm.stats.anova_lm(bel_model, typ=2)
print(anova_table)


#country = Canada

co2_can = co2.iloc[:,3:4]
evs_can = evs.iloc[:,3:4]

can_cor = pd.concat([co2_can,evs_can], axis=1)
print(can_cor)

can_model = ols('Can_CO2 ~ Can_evs', data = can_cor).fit()
anova_table = sm.stats.anova_lm(can_model, typ=2)
print(anova_table)



#country = China

co2_chn = co2.iloc[:,4:5]
evs_chn = evs.iloc[:,4:5]

chn_cor = pd.concat([co2_chn,evs_chn], axis=1)
print(chn_cor)

chn_model = ols('Chn_CO2 ~ Chn_evs', data = chn_cor).fit()
anova_table = sm.stats.anova_lm(chn_model, typ=2)
print(anova_table)



#country = Denmark

co2_den = co2.iloc[:,5:6]
evs_den = evs.iloc[:,5:6]

den_cor = pd.concat([co2_den,evs_den], axis=1)
print(den_cor)

den_model = ols('Den_CO2 ~ Den_evs', data = den_cor).fit()
anova_table = sm.stats.anova_lm(den_model, typ=2)
print(anova_table)



#country = Finland

co2_fin = co2.iloc[:,6:7]
evs_fin = evs.iloc[:,6:7]

fin_cor = pd.concat([co2_fin,evs_fin], axis=1)
print(fin_cor)

fin_model = ols('Fin_CO2 ~ Fin_evs', data = fin_cor).fit()
anova_table = sm.stats.anova_lm(fin_model, typ=2)
print(anova_table)



#contry = France

co2_fra = co2.iloc[:,7:8]
evs_fra = evs.iloc[:,7:8]

fra_cor = pd.concat([co2_fra,evs_fra], axis=1)
print(fra_cor)

fra_model = ols('Fra_CO2 ~ Fra_evs', data = fra_cor).fit()
anova_table = sm.stats.anova_lm(fra_model, typ=2)
print(anova_table)



#country = Germany

co2_ger = co2.iloc[:,8:9]
evs_ger = evs.iloc[:,8:9]

ger_cor = pd.concat([co2_ger,evs_ger], axis=1)
print(ger_cor)

ger_model = ols('Ger_CO2 ~ Ger_evs', data = ger_cor).fit()
anova_table = sm.stats.anova_lm(ger_model, typ=2)
print(anova_table)



#country = Italy

co2_ita = co2.iloc[:,9:10]
evs_ita = evs.iloc[:,9:10]

ita_cor = pd.concat([co2_ita,evs_ita], axis=1)
print(ita_cor)

ita_model = ols('Ita_CO2 ~ Ita_evs', data = ita_cor).fit()
anova_table = sm.stats.anova_lm(ita_model, typ=2)
print(anova_table)


#country = Japan

co2_jpn = co2.iloc[:,10:11]
evs_jpn = evs.iloc[:,10:11]

jpn_cor = pd.concat([co2_jpn,evs_jpn], axis=1)
print(jpn_cor)

jpn_model = ols('Jpn_CO2 ~ Jpn_evs', data = jpn_cor).fit()
anova_table = sm.stats.anova_lm(jpn_model, typ=2)
print(anova_table)


#country = Korea(South)

co2_kor = co2.iloc[:,11:12]
evs_kor = evs.iloc[:,11:12]


kor_cor = pd.concat([co2_kor,evs_kor], axis=1)
print(kor_cor)

kor_model = ols('Kor_CO2 ~ Kor_evs', data = kor_cor).fit()
anova_table = sm.stats.anova_lm(kor_model, typ=2)
print(anova_table)


#country = Netherlands

co2_nld = co2.iloc[:,12:13]
evs_nld = evs.iloc[:,12:13]


nld_cor = pd.concat([co2_nld,evs_nld], axis=1)
print(nld_cor)

nld_model = ols('Nld_CO2 ~ Nld_evs', data = nld_cor).fit()
anova_table = sm.stats.anova_lm(nld_model, typ=2)
print(anova_table)


#country = Norway

co2_nor = co2.iloc[:,13:14]
evs_nor = evs.iloc[:,13:14]


nor_cor = pd.concat([co2_nor,evs_nor], axis=1)
print(nor_cor)

nor_model = ols('Nor_CO2 ~ Nor_evs', data = nor_cor).fit()
anova_table = sm.stats.anova_lm(nor_model, typ=2)
print(anova_table)


#country = Portugal

co2_ptg = co2.iloc[:,14:15]
evs_ptg = evs.iloc[:,14:15]


ptg_cor = pd.concat([co2_ptg,evs_ptg], axis=1)
print(ptg_cor)

ptg_model = ols('Ptg_CO2 ~ Ptg_evs', data = ptg_cor).fit()
anova_table = sm.stats.anova_lm(ptg_model, typ=2)
print(anova_table)


#country = Spain

co2_esp = co2.iloc[:,15:16]
evs_esp = evs.iloc[:,15:16]


esp_cor = pd.concat([co2_esp,evs_esp], axis=1)
print(esp_cor)

esp_model = ols('Esp_CO2 ~ Esp_evs', data = esp_cor).fit()
anova_table = sm.stats.anova_lm(esp_model, typ=2)
print(anova_table)


#country = Sweden

co2_swe = co2.iloc[:,16:17]
evs_swe = evs.iloc[:,16:17]


swe_cor = pd.concat([co2_swe,evs_swe], axis=1)
print(swe_cor)

swe_model = ols('Swe_CO2 ~ Swe_evs', data = swe_cor).fit()
anova_table = sm.stats.anova_lm(swe_model, typ=2)
print(anova_table)


#country = Switzerland

co2_swi = co2.iloc[:,17:18]
evs_swi = evs.iloc[:,17:18]


swi_cor = pd.concat([co2_swi,evs_swi], axis=1)
print(swi_cor)

swi_model = ols('Swi_CO2 ~ Swi_evs', data = swi_cor).fit()
anova_table = sm.stats.anova_lm(swi_model, typ=2)
print(anova_table)


#country = United Kingdom

co2_uk = co2.iloc[:,18:19]
evs_uk = evs.iloc[:,18:19]


uk_cor = pd.concat([co2_uk,evs_uk], axis=1)
print(uk_cor)

uk_model = ols('UK_CO2 ~ UK_evs', data = uk_cor).fit()
anova_table = sm.stats.anova_lm(uk_model, typ=2)
print(anova_table)



#country = United States of America

co2_usa = co2.iloc[:,19:]
evs_usa = evs.iloc[:,19:]


usa_cor = pd.concat([co2_usa,evs_usa], axis=1)
print(usa_cor)

usa_model = ols('USA_CO2 ~ USA_evs', data = usa_cor).fit()
anova_table = sm.stats.anova_lm(usa_model, typ=2)
print(anova_table)
