# Project Idea 
Amazon has over 130+ millions of reviews and ratings for customers to make their buying decisions. However, reading reviews, comparing rankings and ratings take time, especially when Amazon recommended several products and most of them have high ratings. Leveraging 50 GB customer buying records, I create **_an adjusted ratings, which has counted in the subjectivity and polarity of each reviews_**. 

# Demo
Live demo: http://ec2-54-244-215-93.us-west-2.compute.amazonaws.com:8050/
Youtube (in case the server is down): https://www.youtube.com/watch?v=cFgAHGjCXqo
Project Slide:
https://docs.google.com/presentation/d/1Ip7DDsDuzonyqgxwMOh5q6okE-Y9OTgXkw2r_WnFB_c/edit#slide=id.g4ea321c474_0_0


# Tech Stack

![pipeline](https://user-images.githubusercontent.com/11646036/51764047-f1730980-2088-11e9-9584-d076dcaf27bc.png)


# Data Source
Amazon review data: http://jmcauley.ucsd.edu/data/amazon/
1. Review data (40 GB) 
2. Product metadata (10 GB)

![reviews_df](https://user-images.githubusercontent.com/11646036/51401319-4bab2200-1aff-11e9-8083-0c8741a102c3.png)
  

# Engineering Challenge
How to join two large tables in MySQL?
Solution: Use MySQL Index
![index](https://user-images.githubusercontent.com/11646036/53174597-0a46e000-359f-11e9-8269-d33d516c4599.png)

# Business Value
This dashboard provides an easy way for users to compare products without chewing too many subjective reviews and misplacing an unsatisfied order.

# MVP
A web application that user can enter the product name. It will automatically show the **_adjusted ratings_** and some basic information (e.g. item name, price etc) based on sentiments from each Amazon reviews. 


# Stretch Goals
* Updates the adjusted ratings of each product in a real-time manner (streaming)
* Workflow automation: Schedulers like Airflow
* Optimize the product: Join different data sources
