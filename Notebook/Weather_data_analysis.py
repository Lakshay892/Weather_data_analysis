import pandas as pd
data = pd.read_csv(r"WeatherDataset.csv")
data
data.head()
data.shape
data.index
data.columns
data.dtypes
data['Weather'].unique()
data.nunique()
data.count()
data['Weather'].value_counts()
data.info()

# Q) 1.  Find all the unique 'Wind Speed' values in the data.
data.head(2)
data.nunique()
data['Wind Speed_km/h'].nunique()
data['Wind Speed_km/h'].unique() # Answer

# Q) 2. Find the number of times when the 'Weather is exactly Clear'.
data.head(2)
# value_counts()
data.Weather.value_counts()
# Filtering
#data.head(2)
data[data.Weather == 'Clear']
# groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')

# Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
data.head(2)
data[data['Wind Speed_km/h'] == 4] # Answer

# Q. 4) Find out all the Null Values in the data.
data.isnull().sum()
data.notnull().sum()

# Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
data.head(2)
data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)
data.head()

# Q.6) What is the mean 'Visibility' ?
data.head(2)
data.Visibility_km.mean()

# Q. 7) What is the Standard Deviation of 'Pressure'  in this data?
data.Press_kPa.std()

# Q. 8) Whats is the Variance of 'Relative Humidity' in this data ?
data['Rel Hum_%'].var()

# Q. 9) Find all instances when 'Snow' was recorded.
# value_counts()
#data.head(2)
data['Weather Condition'].value_counts()

#Filtering
data[data['Weather Condition'] == 'Snow']

# str.contains
data[data['Weather Condition'].str.contains('Snow')].tail(50)

# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
data.head(2)
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]

# Q. 11) What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?
data.head(2)
data.groupby('Weather Condition').min()

data.groupby('Weather Condition').max()

# Q. 12) Show all the Records where Weather Condition is Fog.
data[data['Weather Condition'] == 'Fog']

# Q. 13) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].tail(50)

# Q. 15) Find all instances when :
### A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
### or
### B. 'Visibility is above 40'

data.head(2)
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)]

# By - Lakshay Bhardwaj