import pandas as pd
import matplotlib.pyplot as plt


 
datain = pd.read_csv('./input/data_medium.csv', sep=';');



# Graph # 1

lst=datain['mouse_ID'].unique()
for id in lst:
        df_fe_abx = datain[(datain['sample_type']=='fecal')&(datain['mouse_ID']==id)&(datain['treatment']=='ABX')] 

        df_fe_pla = datain[(datain['sample_type']=='fecal')&(datain['mouse_ID']==id)&(datain['treatment']=='placebo')] 
        
        plt.plot(df_fe_abx['experimental_day'],df_fe_abx['counts_live_bacteria_per_wet_g'], color = 'r', linewidth = '0.5')
        plt.plot(df_fe_pla['experimental_day'],df_fe_pla['counts_live_bacteria_per_wet_g'], color = 'b', linewidth = '0.5')

plt.yscale('log')
plt.xlabel('Day')
plt.ylabel('(log scale)')

plt.plot([0],[0], linewidth = '0.5',label = 'ABX')
plt.plot(0,0,linewidth = '0.5',label = 'Placebo')
plt.legend()

# Graph # 2

figc, axc = plt.subplots(nrows=1, ncols=2,sharey = True) 

df_cec_abx = datain[(datain['sample_type']=='cecal')&(datain['treatment']=='ABX')] 
df_cec_pla = datain[(datain['sample_type']=='cecal')&(datain['treatment']=='placebo')] 


vp = axc[0].violinplot(df_cec_abx['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:

axc[0].set_title('ABX Cecal (log scale)')
axc[0].set_yscale('log')

vp = axc[1].violinplot(df_cec_pla['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
axc[1].set_title('Placebo Cecal (log scale)')
axc[1].set_yscale('log')



# Graph # 3
figi, axi = plt.subplots(nrows=1, ncols=2,sharey = True) 

df_ile_abx = datain[(datain['sample_type']=='ileal')&(datain['treatment']=='ABX')] 
df_ile_pla = datain[(datain['sample_type']=='ileal')&(datain['treatment']=='placebo')] 



vp = axi[0].violinplot(df_ile_abx['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:

axi[0].set_title('ABX Ileal (log scale)')
axi[0].set_yscale('log')


vp = axi[1].violinplot(df_ile_pla['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
    
axi[1].set_title('Placebo ileal (log scale)')
axi[1].set_yscale('log')