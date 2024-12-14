# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:05:10 2024

@author: erabu
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()
data.info()

#counting the number of articles per source
#format of groupby: df.groupby(['column_to_group'])['column_to_count'].count()/.sum
#column_to_count is useful for calculating engagements per source or the like with .sum
data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop('engagement_comment_plugin_count', axis = 1)

#creating a keyword flag
#create a for loop inside a function to isolate each title row
def keywordFlag(keyword):  
    keyword_flag = []
    for x in range(0, len(data)):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordFlag('murder')

#creating a new column in data dataframe
data['keyword_flag'] = pd.Series(keywordflag)

#SentimentIntensityAnalyzer
#sent_int = SentimentIntensityAnalyzer()

# text = data['title'][15]
# sent = sent_int.polarity_scores(text)

# neg = sent['neg']
# neu = sent['neu']
# pos = sent['pos']

#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
for x in range(0, len(data)):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        title_neg_sentiment.append(sent['neg'])
        title_neu_sentiment.append(sent['neu'])
        title_pos_sentiment.append(sent['pos'])
    except:
        title_neg_sentiment.append(0)
        title_neu_sentiment.append(0)
        title_pos_sentiment.append(0)


data['title_neg_sentiment'] = pd.Series(title_neg_sentiment)
data['title_neu_sentiment'] = pd.Series(title_neu_sentiment)
data['title_pos_sentiment'] = pd.Series(title_pos_sentiment)

#writing the data
data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata',index=False)



























