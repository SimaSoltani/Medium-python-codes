### This is to show that the itertuples is way faster than iterrows
## https://medium.com/swlh/why-pandas-itertuples-is-faster-than-iterrows-and-how-to-make-it-even-faster-bc50c0edd30d
### suppose that we have a huge dataframe that we want to count the number of occerance of different combination in col1 and col2 and count this in a dictionary
%%time
results2 = defauldict(lambda: defaultdic(int))

for i,(col1,col2,col3) n big_df.iterrows()
  results2[col1][col2]+=col3
  
  
  
%%time
results3 = defaultdict(lambda:defaultdic(int))

for (_,col1,col2,col3) in big_df.itertuples():
  results3[col1][col2]+=col3
