import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


co2 = pd.read_csv(r'file_path')
co2 = co2.rename(columns={'Country':'Year'})
co2 = co2.replace({'Australia':'Aus_CO2','Austria':'Aut_CO2','Belgium':'Bel_CO2','Canada':'Can_CO2','China':'Chn_CO2','Denmark':'Den_CO2','Finland':'Fin_CO2','France':'Fra_CO2','Germany':'Ger_CO2','Italy':'Ita_CO2','Japan':'Jpn_CO2','Netherlands':'Nld_CO2','Norway':'Nor_CO2','Portugal':'Ptg_CO2','South Korea':'Kor_CO2','Spain':'Esp_CO2','Sweden':'Swe_CO2','Switzerland':'Swi_CO2','United Kingdom':'UK_CO2','USA':'USA_CO2'},regex=True)
co2 = co2.set_index('Year').T
print(co2)

evs = pd.read_csv(r'file_path')
evs = evs.rename(columns={'Country':'Year'})
evs = evs.replace({'Australia':'Aus_evs','Austria':'Aut_evs','Belgium':'Bel_evs','Canada':'Can_evs','China':'Chn_evs','Denmark':'Den_evs','Finland':'Fin_evs','France':'Fra_evs','Germany':'Ger_evs','Italy':'Ita_evs','Japan':'Jpn_evs','Netherlands':'Nld_evs','Norway':'Nor_evs','Portugal':'Ptg_evs','South Korea':'Kor_evs','Spain':'Esp_evs','Sweden':'Swe_evs','Switzerland':'Swi_evs','United Kingdom':'UK_evs','USA':'USA_evs'},regex=True)
evs = evs.set_index('Year').T
print(evs)

#Country = Australia

co2_aus = co2.iloc[:,:1]
evs_aus = evs.iloc[:,:1]

aus_cor = pd.concat([co2_aus,evs_aus],axis=1)
print(aus_cor)

aus_per = aus_cor.corr(method='pearson')
print(aus_per)

sns.jointplot(x="Aus_CO2",y="Aus_evs",data=aus_cor,kind='reg')

#country = Austria

co2_aut = co2.iloc[:,1:2]
evs_aut = evs.iloc[:,1:2]

aut_cor = pd.concat([co2_aut,evs_aut], axis=1)
print(aut_cor)

aut_per = aut_cor.corr(method='pearson')
print(aut_per)

sns.jointplot(x="Aut_CO2",y="Aut_evs",data=aut_cor,kind='reg')


#country = Belgium

co2_bel = co2.iloc[:,2:3]
evs_bel = evs.iloc[:,2:3]

bel_cor = pd.concat([co2_bel,evs_bel], axis=1)
print(bel_cor)

bel_per = bel_cor.corr(method='pearson')
print(bel_per)

sns.jointplot(x="Bel_CO2",y="Bel_evs",data=bel_cor,kind='reg')


#country = Canada

co2_can = co2.iloc[:,3:4]
evs_can = evs.iloc[:,3:4]

can_cor = pd.concat([co2_can,evs_can], axis=1)
print(can_cor)

can_per = can_cor.corr(method='pearson')
print(can_per)

sns.jointplot(x="Can_CO2",y="Can_evs",data=can_cor,kind='reg')



#country = China

co2_chn = co2.iloc[:,4:5]
evs_chn = evs.iloc[:,4:5]

chn_cor = pd.concat([co2_chn,evs_chn], axis=1)
print(chn_cor)

chn_per = chn_cor.corr(method='pearson')
print(chn_per)

sns.jointplot(x="Chn_CO2",y="Chn_evs",data=chn_cor,kind='reg')



#country = Denmark

co2_den = co2.iloc[:,5:6]
evs_den = evs.iloc[:,5:6]

den_cor = pd.concat([co2_den,evs_den], axis=1)
print(den_cor)

den_per = den_cor.corr(method='pearson')
print(den_per)

sns.jointplot(x="Den_CO2",y="Den_evs",data=den_cor,kind='reg')



#country = Finland

co2_fin = co2.iloc[:,6:7]
evs_fin = evs.iloc[:,6:7]

fin_cor = pd.concat([co2_fin,evs_fin], axis=1)
print(fin_cor)

fin_per = fin_cor.corr(method='pearson')
print(fin_per)

sns.jointplot(x="Fin_CO2",y="Fin_evs",data=fin_cor,kind='reg')



#contry = France

co2_fra = co2.iloc[:,7:8]
evs_fra = evs.iloc[:,7:8]

fra_cor = pd.concat([co2_fra,evs_fra], axis=1)
print(fra_cor)

fra_per = fra_cor.corr(method='pearson')
print(fra_per)

sns.jointplot(x="Fra_CO2",y="Fra_evs",data=fra_cor,kind='reg')



#country = Germany

co2_ger = co2.iloc[:,8:9]
evs_ger = evs.iloc[:,8:9]

ger_cor = pd.concat([co2_ger,evs_ger], axis=1)
print(ger_cor)

ger_per = ger_cor.corr(method='pearson')
print(ger_per)

sns.jointplot(x="Ger_CO2",y="Ger_evs",data=ger_cor,kind='reg')



#country = Italy

co2_ita = co2.iloc[:,9:10]
evs_ita = evs.iloc[:,9:10]

ita_cor = pd.concat([co2_ita,evs_ita], axis=1)
print(ita_cor)

ita_per = ita_cor.corr(method='pearson')
print(ita_per)

sns.jointplot(x="Ita_CO2",y="Ita_evs",data=ita_cor,kind='reg')


#country = Japan

co2_jpn = co2.iloc[:,10:11]
evs_jpn = evs.iloc[:,10:11]

jpn_cor = pd.concat([co2_jpn,evs_jpn], axis=1)
print(jpn_cor)

jpn_per = jpn_cor.corr(method='pearson')
print(jpn_per)

sns.jointplot(x="Jpn_CO2",y="Jpn_evs",data=jpn_cor,kind='reg')


#country = Korea(South)

co2_kor = co2.iloc[:,11:12]
evs_kor = evs.iloc[:,11:12]

print(co2_kor)
print(evs_kor)

kor_cor = pd.concat([co2_kor,evs_kor], axis=1)
print(kor_cor)

kor_per = kor_cor.corr(method='pearson')
print(kor_per)

sns.jointplot(x="Kor_CO2",y="Kor_evs",data=kor_cor,kind='reg')


#country = Netherlands

co2_nld = co2.iloc[:,12:13]
evs_nld = evs.iloc[:,12:13]

print(co2_nld)
print(evs_nld)

nld_cor = pd.concat([co2_nld,evs_nld], axis=1)
print(nld_cor)

nld_per = nld_cor.corr(method='pearson')
print(nld_per)

sns.jointplot(x="Nld_CO2",y="Nld_evs",data=nld_cor,kind='reg')


#country = Norway

co2_nor = co2.iloc[:,13:14]
evs_nor = evs.iloc[:,13:14]

print(co2_nor)
print(evs_nor)

nor_cor = pd.concat([co2_nor,evs_nor], axis=1)
print(nor_cor)

nor_per = nor_cor.corr(method='pearson')
print(nor_per)

sns.jointplot(x="Nor_CO2",y="Nor_evs",data=nor_cor,kind='reg')


#country = Portugal

co2_ptg = co2.iloc[:,14:15]
evs_ptg = evs.iloc[:,14:15]

print(co2_ptg)
print(evs_ptg)

ptg_cor = pd.concat([co2_ptg,evs_ptg], axis=1)
print(ptg_cor)

ptg_per = ptg_cor.corr(method='pearson')
print(ptg_per)

sns.jointplot(x="Ptg_CO2",y="Ptg_evs",data=ptg_cor,kind='reg')


#country = Spain

co2_esp = co2.iloc[:,15:16]
evs_esp = evs.iloc[:,15:16]

print(co2_esp)
print(evs_esp)

esp_cor = pd.concat([co2_esp,evs_esp], axis=1)
print(esp_cor)

esp_per = esp_cor.corr(method='pearson')
print(esp_per)

sns.jointplot(x="Esp_CO2",y="Esp_evs",data=esp_cor,kind='reg')


#country = Sweden

co2_swe = co2.iloc[:,16:17]
evs_swe = evs.iloc[:,16:17]

print(co2_swe)
print(evs_swe)

swe_cor = pd.concat([co2_swe,evs_swe], axis=1)
print(swe_cor)

swe_per = swe_cor.corr(method='pearson')
print(swe_per)

sns.jointplot(x="Swe_CO2",y="Swe_evs",data=swe_cor,kind='reg')


#country = Switzerland

co2_swi = co2.iloc[:,17:18]
evs_swi = evs.iloc[:,17:18]

print(co2_swi)
print(evs_swi)

swi_cor = pd.concat([co2_swi,evs_swi], axis=1)
print(swi_cor)

swi_per = swi_cor.corr(method='pearson')
print(swi_per)

sns.jointplot(x="Swi_CO2",y="Swi_evs",data=swi_cor,kind='reg')


#country = United Kingdom

co2_uk = co2.iloc[:,18:19]
evs_uk = evs.iloc[:,18:19]

print(co2_uk)
print(evs_uk)

uk_cor = pd.concat([co2_uk,evs_uk], axis=1)
print(uk_cor)

uk_per = uk_cor.corr(method='pearson')
print(uk_per)

sns.jointplot(x="UK_CO2",y="UK_evs",data=uk_cor,kind='reg')



#country = United States of America

co2_usa = co2.iloc[:,19:]
evs_usa = evs.iloc[:,19:]

print(co2_usa)
print(evs_usa)

usa_cor = pd.concat([co2_usa,evs_usa], axis=1)
print(usa_cor)

usa_per = usa_cor.corr(method='pearson')
print(usa_per)

sns.jointplot(x="USA_CO2",y="USA_evs",data=usa_cor,kind='reg')

#Obtain the plots of the countries

plt.show()
