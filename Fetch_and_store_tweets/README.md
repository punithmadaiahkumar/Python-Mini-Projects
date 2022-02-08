# Fetch and Store Tweets
This python script is used to fetch the required number of tweets of a particular Hashtag through your twitter account and  generates an `.csv` file.

### Tech Stack:
+ Python

### Libraries used:
+ tweepy
+ csv

###  Pre-requirements:
+ install `pip install -r requirements.txt`

### To execute the project:
+ Run `python fetch_store_tweet.py`


### How to execute:
- To execute this script you have to get the API keys from twitter developer account by creating an app at [Twitter developer account](https://developer.twitter.com/apps). For creating an app at  [Twitter developer account](https://developer.twitter.com/apps) you have to follow the below steps

  + step 1: Visit [Twitter Developer Account Website](https://developer.twitter.com/apps) and click on Create app as shown below
  <img src="img/step-1.png" alt="step-1" style="zoom:33%;" />

  + step 2: Click on Apply
    <img src="img/step-2.png" alt="step-2" style="zoom: 50%;" />

  + step 3: Based on your choice select the Reason for using twitter developer tools and Click on Next
  <img src="img/step-3.png" alt="step-3" style="zoom:33%;" />

  + step 4: Enter your country and what you would you call and Click on Next
  <img src="img/step-4.png" alt="step-4" style="zoom:33%;" />

  + step 5: Now Carefully read the questions and answer all the questions as per the requirement. Because based on you answer only the account approval will be taken place
  <img src="img/step-5.png" alt="step-5" style="zoom:33%;" />

  + step 6: If your account successfully approved you can come to homepage  [Twitter developer account](https://developer.twitter.com/apps) and now click on Create an app icon on the right top.

  **Note:** sometimes it takes time to approval of the developer account based on step-5 answers
  <img src="img/step-6.png" alt="step-6" style="zoom:33%;" />

  + step 7: Fill the require fields and click on Create
  <img src="img/step-7.png" alt="step-7" style="zoom:33%;" />

  + step 8: After creating the App click on **Keys and tokens** option you will observe Consumer and Access token keys. Copy them and paste them in the python script
  <img src="img/step-9.png" alt="step-8" style="zoom: 50%;" />


### Output/ Screenshot:
1. Output 1:
    ![Screen shot](output.png)

2. Output 2:
    ![Screen shot](output-2.png)
