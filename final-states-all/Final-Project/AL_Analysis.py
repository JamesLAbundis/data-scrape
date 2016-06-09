
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import plotly.plotly as py
get_ipython().magic('matplotlib inline')

py.sign_in('vnxiclaire', 'uq7kt26gym')
conn = create_engine("sqlite:///database.sqlite")


county_query = 'SELECT * FROM county_facts'
countydf = pd.read_sql(county_query, conn)

total_info = '''SELECT * 
                 FROM primary_results as p'''
primdf = pd.read_sql(total_info, conn)
facts_dict = 'SELECT * FROM county_facts_dictionary'
dictdf = pd.read_sql(facts_dict, conn)



# In[2]:

#column label clean up
countydf.columns
#rename column area_name to county
countydf = countydf.rename(columns={ 'area_name': 'county'})


# In[3]:

#removes "county" suffix in county column
def removecounty(row):
    return row["county"].split(" ")[0]
    
countydf['county'] = countydf.apply(removecounty, axis=1)


# In[ ]:




# In[4]:

#Creates dictionary with
countydict = dictdf.set_index('column_name').to_dict()


# # Important County Fact Keys:
# 
# Race:
# 
# 'RHI725214': 'Hispanic or Latino, percent, 2014'
# 
# 'RHI625214': 'Two or More Races, percent, 2014'
# 
# 'RHI825214': 'White alone, not Hispanic or Latino, percent, 2014'
# 
# 'RHI525214': 'Native Hawaiian and Other Pacific Islander alone, percent, 2014'
# 
# 'RHI425214': 'Asian alone, percent, 2014'
# 
# 'RHI325214': 'American Indian and Alaska Native alone, percent, 2014'
# 
# 'RHI225214': 'Black or African American alone, percent, 2014'
# 
# 'RHI125214': 'White alone, percent, 2014'
# 
# 'POP815213': 'Language other than English spoken at home, pct age 5+, 2009-2013'
# 
# Gender:
# 
# 'SEX255214': 'Female persons, percent, 2014'
# 
# Economic Status:
# 
# 'PVY020213': 'Persons below poverty level, percent, 2009-2013'
# 
# 'INC910213': 'Per capita money income in past 12 months (2013 dollars), 2009-2013'
# 
# 'INC110213': 'Median household income, 2009-2013'
# 
# Education:
# 'EDU635213': 'High school graduate or higher, percent of persons age 25+, 2009-2013'
# 
# 'EDU685213': "Bachelor's degree or higher, percent of persons age 25+, 2009-2013"
# 
# Age:
# 
# 'AGE295214': 'Persons under 18 years, percent, 2014'
# 
# 'AGE775214': 'Persons 65 years and over, percent, 2014'
# 
# Population:
# 
# 'POP010210': 'Population, 2010'
# 
# 'POP060210': 'Population per square mile, 2010'
# 
# 'POP645213': 'Foreign born persons, percent, 2009-2013'
# 
# 'PST040210': 'Population, 2010 (April 1) estimates base'
# 
# 'PST045214': 'Population, 2014 estimate'
# 
# 'PST120214': 'Population, percent change - April 1, 2010 to July 1, 2014'
# 

# 
# 
# 

# In[5]:


#analysis on Alabama
state_label="AL"albdf = primdf.ix[(primdf["state_abbreviation"] == state_label)]
repub = albdf.ix[(albdf["party"] == "Republican")]
democ = albdf.ix[(albdf["party"] == "Democrat")]
#get county facts on Alabama
albfacts = countydf.ix[(countydf["state_abbreviation"] == state_label)]
democmerge = pd.merge(democ, albfacts, on= 'county')
repubmerge = pd.merge(repub, albfacts, on = 'county')
bernAL = democmerge.ix[(democmerge['candidate'] == "Bernie Sanders")]
hillAL = democmerge.ix[(democmerge['candidate'] == "Hillary Clinton")]


# In[6]:

trumpAL = repubmerge.ix[(repubmerge['candidate'] == "Donald Trump")]
cruzAL = repubmerge.ix[(repubmerge['candidate'] == "Ted Cruz")]


# In[ ]:




# In[7]:

fig = {
    'data': [
           {
            'x': bernAL.AGE775214,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.AGE775214,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.AGE775214,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.AGE775214,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': '%People 65 yrs or older', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}

py.iplot(fig, filename='pandas/multiple-scatter_' + state_label)


# In[ ]:




# In[8]:

fig6 = {
    'data': [
           {
            'x': bernAL.RHI825214,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.RHI825214,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.RHI825214,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.RHI825214,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': '%White alone, not Hispanic or Latino', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}



# In[9]:

py.iplot(fig6, filename='pandas/multiple-scatter6_' + state_label)


# In[10]:

fig2 = {
    'data': [
           {
            'x': bernAL.EDU635213,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.EDU635213,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.EDU635213,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.EDU635213,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': ' %people High school grad or higher', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}

py.iplot(fig2, filename='pandas/multiple-scatter2_' + state_label)


# In[ ]:




# In[ ]:


    


# In[11]:

fig3 = {
    'data': [
           {
            'x': bernAL.SEX255214,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.SEX255214,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.SEX255214,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.SEX255214,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': ' Female persons % 2014', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}

py.iplot(fig3, filename='pandas/multiple-scatter3_' + state_label)


# In[ ]:




# In[12]:

fig4 = {
    'data': [
           {
            'x': bernAL.INC110213,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.INC110213,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.INC110213,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.INC110213,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': ' Income', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}

py.iplot(fig4, filename='pandas/multiple-scatter4_' + state_label)


# In[ ]:




# In[13]:

fig5 = {
    'data': [
           {
            'x': bernAL.POP060210,
            'y': bernAL.fraction_votes, 
            'text': bernAL.county, 
            'mode': 'markers', 
            'name': 'bern'},
            {
            'x': hillAL.POP060210,
            'y': hillAL.fraction_votes, 
            'text': hillAL.county, 
            'mode': 'markers', 
            'name': 'hill'},
            {
            'x': trumpAL.POP060210,
            'y': trumpAL.fraction_votes, 
            'text': trumpAL.county, 
            'mode': 'markers', 
            'name': 'trump'},
             {
            'x': cruzAL.POP060210,
            'y': cruzAL.fraction_votes, 
            'text': cruzAL.county, 
            'mode': 'markers', 
            'name': 'cruz'},
           

    ],
    'layout': {
        'xaxis': {'title': ' Population Density %', 'type': 'log'},
        'yaxis': {'title': "Fraction of Votes"}
    }
    
}

py.iplot(fig5, filename='pandas/multiple-scatter5_' + state_label)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[14]:

#drop duplicate and not used columns from results table
democmerge = democmerge.drop(["fips_x",'fips_y','state_abbreviation_y'], axis =1)
repubmerge = repubmerge.drop(["fips_x",'fips_y','state_abbreviation_y'], axis =1)


# In[15]:

#rename column names
democmerge = democmerge.rename(columns = {'state_abbreviation_x':'state_abbreviation' })
repubmerge = repubmerge.rename(columns = {'state_abbreviation_x':'state_abbreviation' })


# In[16]:

#filter down dataframe to variables used for regression model
democmerge.columns
export = democmerge[['state','state_abbreviation','county','party','candidate','fraction_votes',"AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']]
export_repub = repubmerge[['state','state_abbreviation','county','party','candidate','fraction_votes',"AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']]


# In[17]:

export_final = pd.concat([export, export_repub])


# In[18]:

export_final = export_final.reset_index()

export_final.columns = ['id', 'state','state_abbreviation','county','party','candidate','fraction_votes',"AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']


# In[19]:

export_final.to_csv(state_label + "_Analysis_all.csv")


# In[20]:

set(primdf['state_abbreviation'])


# In[ ]:



