
# Graph_Tweets.py
Graphing using [Pandas](http://pandas.pydata.org/), [Numpy](http://www.numpy.org/), and [MatPlotLib](https://matplotlib.org/)

It works by pulling the information (including datetime) from my data file into pandas, combining it with the topic composition file from mallet (some sorting was required, because the mallet data wasn't in the correct numerical order to begin with) and transposing that dataframe into two numpy arrays. 

These arrays can be mapped using matplotlib (since I didn't want to spend too much time coding the selection of lines, I simply comment out the topics I don't want graphed.)

It's pretty kludgy, but the output seems to work.

# Find_Tweets.py

This is a quick way to sort my dataset using the same combination code from Graph_Tweets.py. Output is a csv file of all the tweets that are identified by the most prominent topic, along with their URLs so I can find images. 

# To-Do

- Set up MatPlotLib so you can select the lines you want, rather than comment them out.
- Make the Find_Tweets.py an variable for-loop so you don't have to change the output each time.
- Figure out the issues with output on line 5 in the data