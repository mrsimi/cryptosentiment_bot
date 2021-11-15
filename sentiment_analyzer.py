from typing import Text
from textblob import TextBlob
import re


def clean_text(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def maximum(pos, neg, neu):
    if pos >= neg and pos >= neu:
        return 'POSITIVE'
    elif neg >= pos and neg >= neu: 
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

def get_sentiments(dataList, provider):
  

    positives = 0
    negatives = 0
    neutral = 0
    total = len(dataList)

    print('sentiment calculation began..')

    for content in dataList:
        result = TextBlob(clean_text(content[0]))
        
        polarity = result.sentiment.polarity

        if polarity > 0: 
            positives+=1
        elif polarity == 0:
            neutral +=1
        else: 
            negatives += 1

    report = {'positives': positives, 'negatives': negatives, 'neutral': neutral, 'total': total, 
            'overall': maximum(positives, negatives, neutral), 'source': provider}
    
    text_report= '{0} posts were analyzed, \n {1} were classified as being positive, \n {2} were classified as negative whilst the remaining \n {3} where dimmed neutral. \n Overall the sentimenent on this coin is {4} \n\n Data Source: {5}'.format(total, positives, negatives, neutral, maximum(positives, negatives, neutral), provider)

    print('generating report')
    
    return report, text_report
            