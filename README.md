# Project Idea 
Amazon has over 130+ millions of reviews and ratings for customers to make their buying decisions. However, reading reviews, comparing rankings and ratings take time, especially when unreliable products flood the market place by fake reviews and ratings. Leveraging 50 GB customer buying records, I create **_a dashboard for Amazon users to check the reliability of a specific product, based on trustworthiness of reviews and ratings_**. 

#### Project Slide
https://docs.google.com/presentation/d/1CJkFzqABHCsr9JGt8ByJdXUaWfwLAsKnYuK8jKnMsEw/edit#slide=id.g4ea19a762d_0_8

Insight Platform: https://docs.google.com/presentation/d/1Ip7DDsDuzonyqgxwMOh5q6okE-Y9OTgXkw2r_WnFB_c/edit#slide=id.g4ea321c474_0_0

# Tech Stack

![pipeline](https://user-images.githubusercontent.com/11646036/51764047-f1730980-2088-11e9-9584-d076dcaf27bc.png)


# Data Source
Amazon review data: !http://jmcauley.ucsd.edu/data/amazon/
1. Review data (40 GB) 
2. Product metadata (10 GB)

![reviews_df](https://user-images.githubusercontent.com/11646036/51401319-4bab2200-1aff-11e9-8083-0c8741a102c3.png)
  

# Engineering Challenge
1. How to join different datasets, especially there're 50 datasets seperated within AWS S3.
2. How to join/query efficiently?
3. How to adjust the reliable ratio in the real-time manner.

# Business Value
This dashboard updates the reliability of each product in a real-time manner, which prevents customers from chewing too many misleading product information/reviews and misplacing an unsatisfied order.

# MVP
A web application that user can enter the product name. It will automatically show the **_adjusted ratings_** and some basic information (e.g. item name, price etc) based on sentiments from each Amazon reviews. 


### Run codes on Spark
![reviewdata_schema](https://user-images.githubusercontent.com/11646036/51766297-10749a00-208f-11e9-850d-e8b5c689179a.png)



![metadata_schema](https://user-images.githubusercontent.com/11646036/51766305-14082100-208f-11e9-8607-476e7f283e98.png)


# Stretch Goals
* Workflow automation: Schedulers like Airflow?
* Optimize the performance: Join different data sources, caching
