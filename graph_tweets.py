# plotting the total number of mentions of topics over time

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.ticker as mtick
import numpy as np
import datetime

dforlando = pd.read_csv("ORLANDO_Full.csv", usecols=[2], header=0, names=['Time'], nrows=89999, parse_dates=True)
dfmallet = pd.read_csv("mallet15.txt", delim_whitespace=True, header=0, usecols=[1,2], index_col=False, dtype='object', names=['File','Topic'], nrows=89999)
dftime = pd.to_datetime(dforlando['Time'], infer_datetime_format=True)

dfmalletseries = dfmallet['File'].str.replace('\D+', ' ')
dfmallettrue = dfmallet.merge(dfmalletseries.to_frame(), left_index=True, right_index=True)
df2 = pd.to_numeric(dfmallettrue['File_y'])
dfmalletorder = dfmallettrue.merge(df2.to_frame(), left_index=True, right_index=True)
df3 = dfmalletorder.sort_values(['File_y_y'])

df_final = df3.join(dftime, on=['File_y_y'])
datasorted = df_final.sort_values(['Time'])
print(datasorted)


dates = np.array(datasorted['Time'])
values = np.array(datasorted['Topic'])

#topic 0
count0 = datasorted.loc[datasorted['Topic'] == '0']
output0v = np.array(count0['Topic'])
output0d = np.array(count0['Time'])
output0y = np.linspace(0,len(output0d),len(output0d))


#Topic 1
count1 = datasorted.loc[datasorted['Topic'] == '1']
output1v = np.array(count1['Topic'])
output1d = np.array(count1['Time'])
output1y = np.linspace(0,len(output1d),len(output1d))

#topic 2
count2 = datasorted.loc[datasorted['Topic'] == '2']
output2v = np.array(count2['Topic'])
output2d = np.array(count2['Time'])
output2y = np.linspace(0,len(output2d),len(output2d))

#topic 3
count3 = datasorted.loc[datasorted['Topic'] == '3']
output3v = np.array(count3['Topic'])
output3d = np.array(count3['Time'])
output3y = np.linspace(0,len(output3d),len(output3d))

#topic 4
count4 = datasorted.loc[datasorted['Topic'] == '4']
output4v = np.array(count4['Topic'])
output4d = np.array(count4['Time'])
output4y = np.linspace(0,len(output4d),len(output4d))

#topic 5
count5 = datasorted.loc[datasorted['Topic'] == '5']
output5v = np.array(count5['Topic'])
output5d = np.array(count5['Time'])
output5y = np.linspace(0,len(output5d),len(output5d))

#topic 6
count6 = datasorted.loc[datasorted['Topic'] == '6']
output6v = np.array(count6['Topic'])
output6d = np.array(count6['Time'])
output6y = np.linspace(0,len(output6d),len(output6d))

#topic 7
count7 = datasorted.loc[datasorted['Topic'] == '7']
output7v = np.array(count7['Topic'])
output7d = np.array(count7['Time'])
output7y = np.linspace(0,len(output7d),len(output7d))

#topic 8
count8 = datasorted.loc[datasorted['Topic'] == '8']
output8v = np.array(count8['Topic'])
output8d = np.array(count8['Time'])
output8y = np.linspace(0,len(output8d),len(output8d))

#topic 9
count9 = datasorted.loc[datasorted['Topic'] == '9']
output9v = np.array(count9['Topic'])
output9d = np.array(count9['Time'])
output9y = np.linspace(0,len(output9d),len(output9d))

#topic 10
count10 = datasorted.loc[datasorted['Topic'] == '10']
output10v = np.array(count10['Topic'])
output10d = np.array(count10['Time'])
output10y = np.linspace(0,len(output10d),len(output10d))

#topic 11
count11 = datasorted.loc[datasorted['Topic'] == '11']
output11v = np.array(count11['Topic'])
output11d = np.array(count11['Time'])
output11y = np.linspace(0,len(output11d),len(output11d))

#topic 12
count12 = datasorted.loc[datasorted['Topic'] == '12']
output12v = np.array(count12['Topic'])
output12d = np.array(count12['Time'])
output12y = np.linspace(0,len(output12d),len(output12d))

#topic 13
count13 = datasorted.loc[datasorted['Topic'] == '13']
output13v = np.array(count13['Topic'])
output13d = np.array(count13['Time'])
output13y = np.linspace(0,len(output13d),len(output13d))

#topic 14
count14 = datasorted.loc[datasorted['Topic'] == '14']
output14v = np.array(count14['Topic'])
output14d = np.array(count14['Time'])
output14y = np.linspace(0,len(output14d),len(output14d))


fig, ax = plt.subplots()
formatter = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis_date()
ax.set_xlabel('Time (CST)')
ax.set_ylabel('Number of Tweets')
line0 = plt.plot(output0d, output0y, linestyle='-', label='0: LGBTQ')
line1 = plt.plot(output1d, output1y, linestyle='--', label='1: gun control')
line2 = plt.plot(output2d, output2y, linestyle='-.', label='2: blood donations')
#line3 = plt.plot(output3d, output3y, linestyle=':', label='3: Blood Donations') #this gives an error
#line4 = plt.plot(output4d, output4y, linestyle='-', label='4')
#line5 = plt.plot(output5d, output5y, linestyle='-', label='5')
#line6 = plt.plot(output6d, output6y, linestyle='-', label='6')
#line7 = plt.plot(output7d, output7y, linestyle='-', label='7')
#line8 = plt.plot(output8d, output8y, linestyle='-', label='8')
#line9 = plt.plot(output9d, output9y, linestyle='-', label='9')
line10 = plt.plot(output10d, output10y, linestyle='-', label='10: victims')
#line11 = plt.plot(output11d, output11y, linestyle='-', label='11: Gun Control') #gun control
line12 = plt.plot(output12d, output12y, linestyle='-', label='12: islamic terrorism')
#line13 = plt.plot(output13d, output13y, linestyle='-', label='13')
#line14 = plt.plot(output14d, output14y, linestyle='-', label='14')
leg = ax.legend(loc='upper left')
leg.get_frame().set_alpha(0.4)
plt.show()
# can activate different lines via commenting out the appropriate code. 