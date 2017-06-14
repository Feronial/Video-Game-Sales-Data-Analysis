#The code adds global console sales in the data set

import pandas as pd
import numpy as np
import multiprocessing as mp

path = " Data Path Here ""

Filled_df = pd.read_csv(path + '\\null_ds(Processed)_Parts\\null_ds_FINAL.csv')
temp = Filled_df
S_Platforms = pd.read_csv(path + 'Platforms_TotalSale.csv')
temp['Total_Sale'] = np.nan #Creating console sale feature
length = len(temp)
length_Platform = len(S_Platforms)


            
   
def t_sale (temp_df,S_Platform,i_iter,length,length_Platform):
    
     #This segment checks whether platfors matches and adds appropriate value to tuple
    for i_iter in range(i_iter,length): #range(start,finish) ATTENTİON !
        for x in range (length_Platform):    
            if temp['Platform'].loc[i_iter] == S_Platforms['Platform'].loc[x]:
                temp['Total_Sale'].loc[i_iter] = S_Platforms['Total_Sale'].loc[x]
    
       
    temp.to_csv(path + '\\null_ds(Processed)_Parts\\'+'T_Sale_Part'+ str(i_iter)+ '.csv' )


if __name__ == '__main__': 
    
                   
        p1 = mp.Process(target = t_sale , args=(temp,S_Platforms,0,length/4,length_Platform))
        p1.start();
        
        p2 = mp.Process(target = t_sale , args=(temp,S_Platforms,length/4,length/2,length_Platform))
        p2.start();
                   
        p3 = mp.Process(target = t_sale , args=(temp,S_Platforms,length/2,(3*length/4),length_Platform))
        p3.start();
                   
        p4 = mp.Process(target = t_sale , args=(temp,S_Platforms,(3*length/4),length,length_Platform))
        p4.start();