
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import re
import math
get_ipython().magic('matplotlib inline')

primdf =  pd.read_csv("primary_results.csv")
countydf = pd.read_csv("county_facts.csv")
dictdf = pd.read_csv("county_facts_dictionary.csv")


# In[2]:

#column label clean up
#rename column area_name to county
countydf = countydf.rename(columns={ 'area_name': 'county'})


# In[3]:

#removes "county" suffix in county column
def removecounty(row):
    return row["county"].split(" ")[0]
    
countydf['county'] = countydf.apply(removecounty, axis=1)


# In[4]:

#Creates dictionary with
countydict = dictdf.set_index('column_name').to_dict()


# In[5]:

democ = primdf.ix[(primdf["party"] == "Democrat")]

democmerge = pd.merge(democ, countydf, on= 'county')

#drop duplicate and not used columns from results table
democmerge = democmerge.drop(["fips_x",'fips_y','state_abbreviation_y'], axis =1)

#rename column names
democmerge = democmerge.rename(columns = {'state_abbreviation_x':'state_abbreviation' })

bern = democmerge.ix[(democmerge['candidate'] == "Bernie Sanders")]
hill = democmerge.ix[(democmerge['candidate'] == "Hillary Clinton")]


# In[6]:


bern = bern.groupby('state_abbreviation')[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210', "fraction_votes"]].mean()
hill = hill.groupby('state_abbreviation')[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210', "fraction_votes"]].mean()
corr_str = []


# In[7]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x = "AGE775214", y =  "fraction_votes", alpha = .4)
    plot.set_xlabel("Percent of people 65 years and older")
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. % of people over 65 yrs ")
    
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern["AGE775214"], bern["fraction_votes"])
#extracts title of simple linear regression
title = ("Age")
corr_str.append(('BS',title,slope,r_value)) 


# In[8]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x = 'RHI825214', y =  "fraction_votes", alpha = .4)
    plot.set_xlabel('%White alone, not Hispanic or Latino')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. % White alone,not Hispanic/Latino ")

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern["RHI825214"], bern["fraction_votes"])
title = ("Race")
corr_str.append(('BS',title,slope,r_value))


# In[9]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x = 'EDU635213', y =  "fraction_votes", alpha =.4)
    plot.set_xlabel('High school graduate or higher,% of persons age 25+, 2009-2013')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. %people High school grad or higher")

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern['EDU635213'], bern["fraction_votes"])
title = ("Education")
corr_str.append(('BS',title,slope,r_value))


# In[10]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x = 'SEX255214', y =  "fraction_votes" , alpha = .4)
    plot.set_xlabel('Female persons % 2014')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. Female persons % 2014")  
    
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern['SEX255214'], bern["fraction_votes"])
title = ("Sex")
corr_str.append(('BS',title,slope,r_value))
    


# In[11]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x = 'INC110213', y =  "fraction_votes", alpha = .4)
    plot.set_xlabel('Median household income,2009-2013')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. Median household income")    
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern['INC110213'], bern["fraction_votes"])
title = ("Income")
corr_str.append(('BS',title,slope,r_value))


# In[12]:

with plt.style.context("fivethirtyeight"):
    plot = bern.plot.scatter(x ='POP060210', y = "fraction_votes", alpha = .4)
    plot.set_xlabel('Population per square mile, 2010')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Bernie: Fraction of Votes VS. Population Density")    

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(bern['POP060210'], bern["fraction_votes"])
title = ("Population")
corr_str.append(('BS',title,slope,r_value))


# In[13]:

with plt.style.context("fivethirtyeight"):
    hplot = hill.plot.scatter(x = "AGE775214", y =  "fraction_votes", c = "green")
    hplot.set_xlabel("Percent of people 65 years and older")
    hplot.set_ylabel("Fraction of Votes")
    hplot.set_title("Hillary: Fraction of Votes VS. % people 65 yrs+")  

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill["AGE775214"], hill["fraction_votes"])
title = ("Age")
corr_str.append(('HC',title,slope,r_value))


# In[14]:

with plt.style.context("fivethirtyeight"):
    hplot = hill.plot.scatter(x = 'RHI825214', y =  "fraction_votes",c = "green")
    hplot.set_xlabel('%White alone, not Hispanic or Latino')
    hplot.set_ylabel("Fraction of Votes")
    hplot.set_title("Hillary: Fraction of Votes VS. % White alone,not Hispanic/Latino")
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill['RHI825214'], hill["fraction_votes"])
title = ("Race")
corr_str.append(('HC',title,slope,r_value))


# In[15]:

with plt.style.context("fivethirtyeight"):
    plot = hill.plot.scatter(x = 'EDU635213', y =  "fraction_votes", c ="green")
    plot.set_xlabel('High school graduate or higher,% of persons age 25+, 2009-2013')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Hillary: Fraction of Votes VS. %people High school grad or higher")
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill['EDU635213'], hill["fraction_votes"])
title = ("Education")
corr_str.append(('HC',title,slope,r_value))


# In[16]:

with plt.style.context("fivethirtyeight"):
    plot = hill.plot.scatter(x = 'SEX255214', y =  "fraction_votes", c = "green")
    plot.set_xlabel('Female persons % 2014')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Hillary: Fraction of Votes VS. Female persons % 2014")   
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill['SEX255214'], hill["fraction_votes"])
title = ("Sex")
corr_str.append(('HC',title,slope,r_value))


# In[17]:

with plt.style.context("fivethirtyeight"):
    plot = hill.plot.scatter(x = 'INC110213', y =  "fraction_votes", c = 'green')
    plot.set_xlabel('Median household income,2009-2013')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Hillary: Fraction of Votes VS. Median household income")    
    
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill['INC110213'], hill["fraction_votes"])
title = ("Income")
corr_str.append(('HC',title,slope,r_value))


# In[18]:

with plt.style.context("fivethirtyeight"):
    plot = hill.plot.scatter(x ='POP060210', y = "fraction_votes",c = "green")
    plot.set_xlabel('Population per square mile, 2010')
    plot.set_ylabel("Fraction of Votes")
    plot.set_title("Hillary: Fraction of Votes VS. Population Density")   
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(hill['POP060210'], hill["fraction_votes"])
title = ("Population")
corr_str.append(('HC',title,slope,r_value))


# In[19]:

len(corr_str)


# In[20]:

from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score

#multi variable regression model for Bernie Sanders

X = bern[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']]
y = np.log(bern['fraction_votes']/ (1-bern['fraction_votes']))

model = LinearRegression()
model.fit(X,y)


# In[21]:

#get all states available in county data frame
allstates = list(countydf['state_abbreviation'].dropna())
allstates = set(allstates)

#get all states available in 
somestates = list(primdf['state_abbreviation'].dropna())
somestates = set(somestates)
len(somestates)


# In[22]:

#gets all the states we do not have results for
result = []

for state in allstates:
    if state not in somestates:
        result.append(state)
print(result)


# In[23]:

bern_pred = []

predf = countydf.groupby('state_abbreviation')[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']].mean()

predf = predf.drop(somestates)

index = predf.index

cols = predf.columns

count = 0

#model.predict([10.282758620689656, 49.193103448275878, 88.65517241379311, 45.731034482758623, 62611.34482758621, 7.7413793103448274])
for row in predf.iterrows():
    
    result_array = model.predict(list(row[1]))
    
    res = ( math.e**result_array[0] / (1+math.e**result_array[0]))

    bern_pred.append((index[count], res))
    count+=1


# In[24]:

#print out predictions along with state abbreviations
print(bern_pred)


# In[25]:

#multi variable regression model for Hillary Clinton

X = hill[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']]
y = hill['fraction_votes']

model = LinearRegression()
model.fit(X,y)


# In[26]:

hill_pred = []
    
predf = countydf.groupby('state_abbreviation')[["AGE775214",'RHI825214','EDU635213','SEX255214','INC110213','POP060210']].mean()

#drops states that we already have primary results for
predf = predf.drop(somestates)

index = predf.index

cols = predf.columns

count = 0

#model.predict([10.282758620689656, 49.193103448275878, 88.65517241379311, 45.731034482758623, 62611.34482758621, 7.7413793103448274])
for row in predf.iterrows():
    
    result_array = model.predict(list(row[1]))
    
    res = ( math.e**result_array[0] / (1+math.e**result_array[0]))

    hill_pred.append((index[count], res))

    count+=1


# In[27]:

print(hill_pred)


# In[28]:

#calculates the margin between fraction of vote for each model, who won according to my models,
#and in what state

margins = []
count = 0
for result in bern_pred:
    state = result[0]
    winner  = None
    if result[1] > hill_pred[count][1]:
        winner = "BS"
    else:
        winner = "HC"
    diff = np.abs(result[1] - hill_pred[count][1])
    
    margins.append((state,winner,diff))
  


# In[29]:

margdf = pd.DataFrame(margins)
margdf = margdf.rename(columns = {0: 'state', 1: 'p_winner', 2: 'margin'})


# In[30]:


updatelist = [('AK','BS'),('HI','BS'),('WA','BS'),('WI','BS'),('WY','BS'),('NY','HC'),('CT','HC'),('DE','HC'),('MD','HC'),('PA','HC'),('RI','BS'),('IN','BS'),('OR','BS'),('WV','BS'),('KY','HC')]
winners = pd.DataFrame(updatelist)
winners = winners.rename(columns = {0: 'state', 1: 'a_winner'})


# In[31]:

compare = pd.merge(winners, margdf, on = 'state')
compare["acc"] = (compare['a_winner'] == compare['p_winner'])

print('Model accuracy for updated primaries: ', compare['acc'].sum()/ len(compare)*100, "%")
compare.to_csv('past_predictions.csv', index = False)


# In[33]:

trends = pd.DataFrame(corr_str)
trends = trends.rename(columns = {0: 'candidate', 1:'title', 2:'slope', 3: 'r_value'})
trends['r_value'] = np.abs(trends['r_value'] )
trends.to_csv('trends.csv', index = False)


# In[54]:

future_states = ['CA','MT','NJ','NM','ND','SD','DC']
f_pred = []

count = 0
for result in bern_pred:
    state = result[0]
    winner  = None
    if result[1] > hill_pred[count][1]:
        winner = "BS"
    else:
        winner = "HC"
    diff = np.abs(result[1] - hill_pred[count][1])
    
    if state in future_states:
        
        f_pred.append((state,winner,diff))


# In[58]:

f_predf = pd.DataFrame(f_pred, columns = margdf.columns)
f_predf.to_csv("future_predictions.csv")


# In[35]:

bern.to_csv('bernie_national.csv', index = True)
hill.to_csv('hillary_national.csv', index = True)


# In[ ]:



