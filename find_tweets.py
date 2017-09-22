#Tweet Finding

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.ticker as mtick
import numpy as np
import datetime

dforlando = pd.read_csv("ORLANDO_Full.csv", usecols=[3,4], header=0, names=['url', 'text'], nrows=89999, parse_dates=True)
dfmallet = pd.read_csv("mallet15.txt", delim_whitespace=True, header=0, usecols=[1, 2], dtype='object', names=['File', 'Topic'], nrows=89999)
#removed pulling in the file #, can add it again if you want but it'll probably be another set of code. 

dfmalletseries = dfmallet['File'].str.replace('\D+', ' ')
dfmallettrue = dfmallet.merge(dfmalletseries.to_frame(), left_index=True, right_index=True)
df2 = pd.to_numeric(dfmallettrue['File_y'])
dfmalletorder = dfmallettrue.merge(df2.to_frame(), left_index=True, right_index=True)
df3 = dfmalletorder.sort_values(['File_y_y'])

df_final = df3.join(dforlando, on=['File_y_y'])


topic0 = df_final.loc[df_final['Topic'] == '0']
topic1 = df_final.loc[df_final['Topic'] == '1']
topic2 = df_final.loc[df_final['Topic'] == '2']
topic3 = df_final.loc[df_final['Topic'] == '3']
topic4 = df_final.loc[df_final['Topic'] == '4']
topic5 = df_final.loc[df_final['Topic'] == '5']
topic6 = df_final.loc[df_final['Topic'] == '6']
topic7 = df_final.loc[df_final['Topic'] == '7']
topic8 = df_final.loc[df_final['Topic'] == '8']
topic9 = df_final.loc[df_final['Topic'] == '9']
topic10 = df_final.loc[df_final['Topic'] == '10']
topic11 = df_final.loc[df_final['Topic'] == '11']
topic12 = df_final.loc[df_final['Topic'] == '12']
topic13 = df_final.loc[df_final['Topic'] == '13']
topic14 = df_final.loc[df_final['Topic'] == '14']


#Change this to the topic you want to output to csv.
topic7.to_csv(r'exemplars7.csv')
