## Demo Screenshot

![Image of Yaktocat](/Users/frankdu/Learn_Dash_Plotly/Wusthof/Demo.png)

See it live [here](https://wusthofboard.herokuapp.com/)



## Overview

**WustBoard** is an intelligence dashboard rendering rich inter-activities and insights about the kitchen brand: **Wuesthof**.

This project combines the techniques of web crawling, data warehousing, sentiment analysis, data analytics
and visualisation together.
It renders a daily-updated rich presentation in the forms of scatter plot and
time series line charts by three variables: **price**, **comments_volume** and **sentiment_index**.

## Features

* Dropdown Components:

Two dropdown Components enable a user to choose which data aspect to be featured in an axis where
the first Dropdown features the x-axis and the second one features the y-axis.

* Date Slider:

A Date Slider that lets user to switch between different dates to render daily updated scatter plots.

* HoverOver Effect:

In the scatter plot, each scatter represents an unique product with its metadata displayed: name, price,
comments_volume, and/or sentiment_index. Hovering over an scatter will trigger an up-to-date time series data presented by the line chart

* Sentiment_Index:

A polarity value ranges between -1 and 1, where -1 is very negative, 0 is neutral and 1 is very positive.


## Technologies used

Python, TextBlob(NLP Library), Pandas, Google Sheets(as a simple databasing tool), html-Requests(Web scraping),
Plotly.py (Data visualisation), Dash(Micro Python dashboarding web framework).
