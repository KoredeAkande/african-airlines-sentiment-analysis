#Import packages
import aspect_based_sentiment_analysis as absa
import numpy as np

#Load the basic configuration of the ABSA package
nlp = absa.load()

#Note down the possible aspect classes – and their relevant (aspect) terms
aspect_classes = {'seat':['seat'], 
                  'cabin_staff_service': ['crew', 'service', 'staff', 'attendant'], 
                  'food': ['food','meal','breakfast','lunch','dinner'],
                  'inflight_entertainment': ['entertainment','ife','movies','shows', 'music', 'films'], 
                  'ground_service': ['ground service', 'ground  staff'], 'wifi': ['wifi', 'internet']}


def review_absa(review):

    #List to store the detected aspect sentiment (if any) for each aspect
    review_aspect_sentiment = []

    #Iterate through all the aspects (e.g. seat, ground staff service, etc.)
    for aspect_class in aspect_classes.keys():

        #List to store the avg sentiment for all relevant aspect terms
        term_sentiments = []

        #Iterate through all the aspect terms for an aspect
        for aspect_term in aspect_classes[aspect_class]:

            #If the term is in the review
            if aspect_term in review:

                try:
                    #Try to calculate the sentiment for the aspect term
                    sent = nlp(review,aspects = [aspect_term])

                    #Append the sentiment score to the sentiment scores list
                    term_sentiments.append(np.array(sent.subtasks[aspect_term].examples[0].scores))

                except:
                    
                    #If any error or exception arises, just pass
                    pass


            #If the term is not in the review, pass
            else:
                pass

        #If there were multiple aspect terms, find the average sentiment values across all terms
        #Note: This is reported in the form [neutral,negative,positive]
        if len(term_sentiments) > 1:

            avg_sentiments = np.array(term_sentiments).mean(axis=0)

        #If just one, no need to find the average
        elif len(term_sentiments) == 1:

            avg_sentiments = np.array(term_sentiments)

        #If len == 0, no review with the aspect terms was found
        else:
            avg_sentiments = None

        #If avg_sentiment is None, append np.nan indicating no sentiment for the aspect
        if avg_sentiments is None:

            review_aspect_sentiment.append("No sentiment detected")
        
        #If a sentiment score was determined,
        else:

            #Get the sentiment category (neutral,negative,positive) with the largest probability
            max_idx = np.argmax(avg_sentiments)

            if max_idx == 2:

                review_aspect_sentiment.append("Positive")

            elif max_idx == 1:

                review_aspect_sentiment.append("Negative")

            else:

                review_aspect_sentiment.append("Neutral")

    aspect_sentiment_pairs = [*zip([word.replace('_',' ').capitalize() for word in aspect_classes.keys()],review_aspect_sentiment)]
    
    return aspect_sentiment_pairs




