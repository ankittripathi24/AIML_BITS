# TweetAnalysis

# Project Title

This project entails sentiment analysis of airline passengers' tweets, aiming to analyze the sentiments expressed by passengers towards airlines. It involves processing large volumes of tweet data to extract insights into customer perceptions and sentiments, particularly focusing on identifying positive and negative sentiments.

The project serves various stakeholders in the aviation industry, including airlines, aviation authorities, and customer service departments. Airlines can utilize the sentiment analysis results to gauge customer satisfaction levels, identify areas for improvement, and tailor their services accordingly. Aviation authorities can leverage the insights to monitor public sentiment towards airlines and address any emerging issues or concerns. Customer service departments can use the analysis to promptly address customer feedback and enhance overall customer experience.

## Installation

Instructions on how to install the project, for example:

1. Clone the repository:
    ```
    git clone https://github.com/ankittripathi24/TweetAnalysis.git
    ```

2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Softwares

Python version: 3.10
Anaconda: 
Vader: 

## Model pre-conditions

What format of CSV file with data is expected:

## Model creation
Model Creation includes:
1) Data Pre-processing
2) Data Cleaning
3) Model Selection (on the basis of AUC score select the best model)

## Usage

Instructions on how to use the project, for example:

1. Start the Airflow web server:
    Precondition: Airflow Quick Start: https://airflow.apache.org/docs/apache-airflow/stable/start.html
    
    ```
    airflow webserver -p 8080
    ```

2. Access the Airflow web interface at `http://localhost:8080`.

3. Unpause the DAG in the Airflow web interface.

4. Start the Streamlit app:
    ```
    streamlit run pySentimentAnalysis.py
    ```

## DAG

A brief description of the DAG and its tasks:

1. `get_data`: This task downloads data from a GitHub URL and pushes it to XCom.

2. `recreate_model`: This task pulls the data from XCom, creates a blank model for testing purposes, and pushes the model to XCom.

3. `save_model`: This task pulls the model from XCom and saves it to a .pkl file in a specific folder.


## Streamlit App

The Streamlit app provides an interactive interface for analyzing tweet data. It offers the following options:

1. **Enter Tweet:** Manually enter a tweet for analysis.
2. **Upload Tweet CSV:** Upload a CSV file of tweets for analysis.
3. **Get Tweets from Scrapper:** Get tweets from a web scrapper for analysis.

In addition to these options, the app also displays stats of the uploaded data. The data for the Streamlit app gets refreshed by the Airflow DAG as per the schedule.

## Folder Structure

**Model** : AI ML\final_model.pkl, AI ML\vectorizer.pkl
**Output Folder** : AI ML\Capstone Project 9\Capstone Project 9\C_\1-GG\Cap9\Airline Twitter Sentimet Analysis_Dataset_OutputFiles
**iPymb Files**:  AI ML\Capstone Project 9\Capstone Project 9\ipynb Files



## Contributing


## License
