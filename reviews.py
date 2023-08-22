import pandas as pd
readpath = 'C:/Users/William McConnell/Documents/CodeLousivilleProjects/wine-reviews-exercise-whmcconnell7170/data/winemag-data-130k-v2.csv.zip'
writepath = 'C:/Users/William McConnell/Documents/CodeLousivilleProjects/wine-reviews-exercise-whmcconnell7170/data/reviews-per-country.csv'
df = pd.read_csv(readpath, index_col = 0)
df = pd.DataFrame(df)

#df = df.groupby('country').points.agg(['mean'])
df = df.groupby('country').agg({'country': ['count'], 'points': ['mean']})
df.columns = ['count', 'points']
#print(df.loc['France'])
df.points = round(df.points, 1)
df = df.to_csv(writepath)

