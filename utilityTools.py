from dataframe import years,country_name,gdp,indicators
import plotly.graph_objects as go
from plotly.offline import iplot
import seaborn as sns
import plotly.express as px

# init with years initializes the comboBox with the years
def init_with_years(obj):
    """
    Initializes the comboBox with the years
        Args:
            obj: the comboBox object
    """
    for i in years:
        obj.addItem(i)

# init with countries initializes the comboBox with the countries
def init_with_countries(obj):
      """
        Initializes the comboBox with the countries name
            Args:
                obj: the comboBox object
      """
      for i in country_name:
            obj.addItem(i)

# show choropleth shows the choropleth map for the selected year
def show_choropleth(year):
    """ 
        show choropleth shows the choropleth map for the selected year
            Args:
                year: the selected year(string)
    """

    # creating the choropleth map

    # create the data for the choropleth map
    data = dict(
            type='choropleth',
            locations=gdp['Country Code'],
            z = gdp[year],
            zmax=int(30000000000000),           # set the range of the choropleth map max at 30T for better visualization
            zmin=int(gdp[year].min()),
            colorscale='deep',
            text=gdp['Country Name'],
            colorbar = {'title' : indicators['INDICATOR_NAME'][0]}
            )

    # create the layout for the choropleth map
    layout = dict(
    title = year+' Global GDP',
    geo = dict(
    showframe = True,
    showocean=True,
    projection = {'type':'natural earth'}
    )
    )
    # create the choropleth map
    choromap = go.Figure(data=[data],layout=layout)
    # plot the choropleth map
    iplot(choromap)

# plot with plotly plots lineplot of the countries in the data_list
def plot_with_plotly(data_list):
    """
        plot with plotly plots lineplot of the countries in the data_list
            Args:
                data_list: the list of the formatted dataframes of the countries to be plotted ( list of dataframes)
    """
    fig = go.Figure()
    for data in data_list:
        fig.add_trace(
            go.Scatter(x=data.index[4:],y=data[data.columns[0]][4:],name = data.columns[0],mode='lines')
        )
    fig.show()

# get country data returns the formatted dataframe for the selected country
def get_country_data(country_name):
    """
        get country data returns the formatted dataframe for the selected country
            Args:
                country_name: the selected country(string)
            Format:
                Years on the rows and country name as the column name
    """
    country_name = country_name.lower()
    if gdp['Country Name'].isin([country_name]).any():
        new = gdp[gdp['Country Name'] == country_name].transpose().copy()
        new.columns = list(gdp[gdp['Country Name'] == country_name]['Country Code'])
        return new
    else:
        return "Country Not Found"

# barplot top contributors shows the barplot of the top contributors for the selected year
def barplot_top_contributors(year):
        sns.set_style('whitegrid')
        c=['red', 'yellow', 'black', 'blue', 'orange','purple','green']
        fig = px.bar(gdp, y=gdp.sort_values(by=year,ascending=False).head(7)['Country Name'], x=gdp.sort_values(by=year,ascending=False).head(7)[year], height=500,width=1000,title='WORLD GDP BY COUNTRY (In billion dollars) on  '+year,color=c)
        fig.update_layout(showlegend=False,title_x=0.5)
        fig.show()