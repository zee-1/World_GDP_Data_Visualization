import pandas as pd

# importing the dataset
gdp = pd.read_csv('data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4353236.csv',skiprows=4)
indicators = pd.read_csv('data/Metadata_Indicator_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4353236.csv')

#cleaning data
l=['Middle East & North Africa (excluding high income)',
 'Middle East & North Africa (IDA & IBRD countries)',
 'Heavily indebted poor countries (HIPC)',
  'Least developed countries: UN classification',
  'IDA blend',
  'IDA only',
 'Africa Eastern and Southern',
 'Pre-demographic dividend','Latin America & Caribbean',
 'Latin America & the Caribbean (IDA & IBRD countries)',
 'Latin America & Caribbean (excluding high income)',
 'Europe & Central Asia (IDA & IBRD countries)',
 'Europe & Central Asia (excluding high income)',
 'South Asia (IDA & IBRD)',
 'Fragile and conflict affected situations',
 'IDA total',
 'Sub-Saharan Africa',
 'Sub-Saharan Africa (IDA & IBRD countries)',
 'Sub-Saharan Africa (excluding high income)','World',
 'High income',
 'OECD members',
 'Post-demographic dividend',
 'IDA & IBRD total',
 'Low & middle income',
 'Middle income',
 'IBRD only',
 'East Asia & Pacific',
 'Upper middle income',
 'North America',
 'Late-demographic dividend',
 'Europe & Central Asia',
 'East Asia & Pacific (excluding high income)',
 'East Asia & Pacific (IDA & IBRD countries)',
 'European Union',
 'Euro area',
 'Early-demographic dividend',
 'Lower middle income',
 'South Asia',
 'Middle East & North Africa']
gdp=gdp.set_index('Country Name')
gdp=gdp.drop(index=l)
gdp=gdp.reset_index()

# extracting data
country_name = list(gdp['Country Name'])
years = list(gdp.columns[4:-1])

# manipulating data for easier use
gdp['Country Name']=gdp['Country Name'].apply(lambda x: x.lower())