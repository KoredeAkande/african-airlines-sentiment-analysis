African Airlines Sentiment Analysis 🛩
==============================

In our highly globalized world, airlines play a crucial role in connecting dispersed parts of the globe. There are, however, differences between every airline and these can affect passenger experience. Public opinion regarding airlines operating out of western countries is well documented; conversely, experiences with African airlines are less discussed. 

In this project, I attempt to address this gap by analyzing reviews of major African airlines in order to evaluate passengers' experiences. I also conduct an aspect-based sentiment analysis leveraging Aspect-Based Sentiment Analysis by Scala Consultants.

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
```

It might be best to create a virtual environment to run this project in as the above downgrades packages



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
