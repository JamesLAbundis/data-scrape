
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('jlabundi', 'aof7otmb5f')


# In[2]:

df = pd.read_csv('past_predictions.csv')
fut_pred = pd.read_csv("future_predictions.csv")

df['acc'] = df['acc'].astype(str)


# In[3]:

berndf = df.ix[df["p_winner"] == 'BS']
hilldf = df.ix[df["p_winner"] == 'HC']


# In[4]:

trace1 = go.Bar(
    x=berndf['state'],
    y=berndf['margin'],
    name='Bernie Sanders',
    opacity = 0.8,
    text = berndf['acc']
)

trace2 = go.Bar(
    x=hilldf['state'],
    y=hilldf['margin'],
    name='Hillary Clinton',
    opacity = 0.8,
    text = hilldf['acc']
)


# In[5]:

data = [trace1, trace2]
layout = go.Layout( title = "Multi-Var Linear Reg Model Past Predictions", barmode='group',
                   yaxis = dict(zeroline = False,
                          title = "Win Margin"),
                   xaxis = dict(zeroline = False,
                          title = 'State')
                  )

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='grouped-bar')


# In[6]:

berndf = fut_pred.ix[fut_pred["p_winner"] == 'BS']
hilldf = fut_pred.ix[fut_pred["p_winner"] == 'HC']


# In[7]:



trace1 = go.Bar(
    x=berndf['state'],
    y=berndf['margin'],
    name='Bernie Sanders',
    opacity = 0.8
)

trace2 = go.Bar(
    x=hilldf['state'],
    y=hilldf['margin'],
    name='Hillary Clinton',
    opacity = 0.8
)

data = [trace1, trace2]
layout = go.Layout( title = "Multi-Var Linear Reg Model Future Predictions", barmode='group',
                  
                   yaxis = dict(zeroline = False,
                          title = "Win Margin"),
                   xaxis = dict(zeroline = False,
                          title = 'State')
                  )

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Multi-Var Linear Reg Model Future Predictions')


# In[8]:

berndf = pd.read_csv('bernie_national.csv')
hilldf = pd.read_csv("hillary_national.csv")
trends = pd.read_csv("trends.csv")


# In[9]:

cols = berndf.columns


# In[10]:


trace0 = go.Scatter(
    x = berndf['AGE775214'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['AGE775214'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = '% Of People Over 65 YRS vs Fraction of Vote',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = "Age: % Of People Over 65 YRS")
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='% Of People Over 65 YRS vs Fraction of Vote')


# In[11]:

trace0 = go.Scatter(
    x = berndf['RHI825214'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['RHI825214'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = '% White Alone (Not Hisapanic/Latino) vs Fraction of Vote',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = "% White Alone (Not Hisapanic/Latino)")
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='% White Alone (Not Hisapanic/Latino) vs Fraction of Vote')


# In[12]:

trace0 = go.Scatter(
    x = berndf['EDU635213'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['EDU635213'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = '% People High school grad or higher VS Fraction of Votes',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = "% High school graduate or higher of persons age 25+, 2009-2013")
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='% People High school grad or higher VS Fraction of Votes')
    


# In[13]:

trace0 = go.Scatter(
    x = berndf['SEX255214'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['SEX255214'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = '% Female persons 2014 VS Fraction of Votes',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = "Female persons % 2014")
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='% Female persons 2014 VS Fraction of Votes')


# In[14]:

trace0 = go.Scatter(
    x = berndf['INC110213'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['INC110213'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Median Household Income VS Fraction of Votes',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = "Median Household Income,2009-2013")
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Median Household Income VS Fraction of Votes')


# In[15]:

trace0 = go.Scatter(
    x = berndf['POP060210'],
    y = berndf['fraction_votes'],
    name = 'Bernie Sanders',
    mode = 'markers',
    text = berndf['state_abbreviation'],
    marker = dict(
        size = 10,
        
        color = 'rgba(30, 144, 255, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = hilldf['POP060210'],
    y = hilldf['fraction_votes'],
    name = 'Hillary Clinton',
    mode = 'markers',
    text = hilldf['state_abbreviation'],
    marker = dict(
        size = 10,
        color = 'rgba(255, 128, 0, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Population per square mile, 2010 VS Fraction of Votes',
              yaxis = dict(zeroline = False,
                          title = "Fraction of Votes"),
              xaxis = dict(zeroline = False,
                          title = 'Population per square mile, 2010')
             )


fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Population per square mile, 2010 VS Fraction of Votes')


# In[16]:

trends

slopes = list(trends['slope'])
bst = trends.ix[ trends['candidate']=='BS']
hct = trends.ix[ trends['candidate']=='HC']

for i in range(len(slopes)):
    slopes[i] = "Slope: " + str(slopes[i])
slopes


# In[17]:

#graph of future predictions


trace1 = go.Bar(
    x=bst['title'],
    y=bst['r_value'],
    name='Bernie Sanders',
    opacity = 0.8,
    text =slopes[:6]
)

trace2 = go.Bar(
    x=hct['title'],
    y=hct['r_value'],
    name='Hillary Clinton',
    opacity = 0.8,
    text = slopes[6:]
)

data = [trace1, trace2]
layout = go.Layout( title = "Comparing Indicators for the Fraction of the Vote",
                   barmode='group',
                   yaxis = dict(zeroline = False,
                          title = "R-Squared"),
                   xaxis = dict(zeroline = False,
                          title = 'Variables(Indicators)')
                  
                  )

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Comparing Indicators for the Fraction of the Vote')


# In[ ]:



