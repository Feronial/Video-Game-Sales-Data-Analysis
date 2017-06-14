
#Code saves genre feature another csv file for Structured Database 
import pandas as pd


path = " Data Path Here "
genres = []
tempset = pd.read_csv(path+'abc.csv')
count = 0



for i in tempset['Genre']:
   
   if i not in genres: # Checking same genre in the list
       genres.insert(count,i)
       count = count + 1

       
genre_df = pd.DataFrame(genres,columns = ['Genre',])
#genre_df.to_csv(path + 'Genres.csv')      
        