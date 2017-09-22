
Graphing using [Pandas](http://pandas.pydata.org/), [Numpy](http://www.numpy.org/), and [MatPlotLib](https://matplotlib.org/)

It works by pulling the information (including datetime) from my data file into pandas, combining it with the topic composition file from mallet (some sorting was required, because the mallet data wasn't in the correct numerical order to begin with) and transposing that dataframe into two numpy arrays. 

These arrays can be mapped using matplotlib (since I didn't want to spend too much time coding the selection of lines, I simply comment out the topics I don't want graphed.)

It's pretty kludgy, but the output seems to work.