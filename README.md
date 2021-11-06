African Airlines Sentiment Analysis 🛩
==============================

In our highly globalized world, airlines play a crucial role in connecting dispersed parts of the globe. There are, however, differences between every airline and these can affect passenger experience. Public opinion regarding airlines operating out of western countries is well documented; conversely, experiences with African airlines are less discussed. 

In this project, I attempt to address this gap by analyzing reviews of major African airlines in order to evaluate passengers' experiences. I also conduct an aspect-based sentiment analysis leveraging Aspect-Based Sentiment Analysis by Scala Consultants.

The published Medium article can be accessed [here](https://medium.com/@koredeakande001/aspect-based-sentiment-analysis-of-african-airlines-ad6317c48973). For a discussion of results see `Key Findings` section below

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks numbered for ordering 
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Images from the EDA for the Medium article
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment.
    

Requirements
------------
I ran into some problems running the ABSA package with its [default requirements](https://github.com/ScalaConsultants/Aspect-Based-Sentiment-Analysis/blob/master/setup.py). I found the following configuration below to work:

```
#Modeling requirements
aspect-based-sentiment-analysis==2.0.2
transformers==2.5.0
tensorflow==2.2.0

#Data cleaning requirements - all are not neccessary if you want to utilize the provided dataset
cleantext
wordcloud
missingno

#BCa Confidence Interval Requirement
arch

```

It might be best to create a virtual environment to run this project in as the above downgrades packages


Key Findings
------------

### African Airline Review Analysis

Airlines Average Atrribute Ratings            |  Airlines Sentiment Distribution
:-------------------------:|:-------------------------:
![Airlines Average Atrribute Ratings](reports/figures/ratings_parallel_plot.png?raw=true "Title")  |  ![Airlines Sentiment Distribution](reports/figures/sentiment_distribution.png?raw=true "Title") 





- African airlines, in general, are not regarded very positively. A quick view of the distribution of positive/negative/neutral ratings, as well as a consideration of the average rating on all attributes, shows that the airlines, in general, offer at best, fair service.
- The majority of the negative sentiments seem to stem from poor customer service and delayed flights. Therefore, airlines may benefit from focusing their efforts on improving these areas.

### Aspect-Based Sentiment Analysis
![Confusion Matrix](reports/figures/confusion_plot.png?raw=true "Title")
- Ready-to-use ABSA model from [Aspect-based Sentiment Analysis](https://github.com/ScalaConsultants/Aspect-Based-Sentiment-Analysis) package results in a 95% BCa confidence interval of [0.82 , 0.89] for the accuracy rate
- The model performed pretty poorly on predicting reviews with `Neutral` sentiment (see image above). It however, predicted `Negative` and `Positive` reviews pretty accurately
- The ABSA package requires manual specification of aspects that should be searched for in the texts. The accuracy of the specified words largely determines how successful the model will be in aspect detection and sentiment prediction


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
