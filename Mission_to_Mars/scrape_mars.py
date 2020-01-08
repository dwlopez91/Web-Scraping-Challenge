from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_data():
    output = {}

    #creating the path 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #first url for mars data
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find(class_='content_title')

    news_title_text = news_title.a.text

    news_title_text

    #use soup to scrape text 
    news_p = soup.find(class_='article_teaser_body')

    news_p_text = news_p.text
    
    #adding news p text to dictionary
    output['news_p_text'] = news_p_text

    #getting Mars image
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    browser.click_link_by_partial_text('FULL IMAGE')

    img_html = browser.html
    img_soup = BeautifulSoup(img_html, 'html.parser')

    img_address = img_soup.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()
    print(img_address)

    featured_image_url = "https://www.jpl.nasa.gov"+img_address
    print(featured_image_url)
    
    #adding featured image url to dictionary
    output['featured_image_url'] = featured_image_url

    #url for Mars Facts 
    facts_url = 'https://space-facts.com/mars/'
    
    table = pd.read_html(facts_url)
    table

    df = table
    #find out the type
    type(df)

    #first table only for Mars only data
    df2 = df[0]

    df2.columns = ['Mars Profile', 'Values']
    df2

    #convert table to HTML
    html_table = df2.to_html()
    html_table

    df2.to_html('table.html')

    #adding hemisphere urls to dictionary
    output['html_table'] = html_table

    #Mars Hemispheres
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    
    #adding hemisphere urls to dictionary
    output['hemisphere_image_urls'] = hemisphere_image_urls

    #scrape mars weather from Twitter
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    html = browser.html
    weather_soup = BeautifulSoup(html, "html.parser")

    mars_weather_tweet = weather_soup.find('p', class_='TweetTextSize').text
    print(mars_weather_tweet)

    #adding mars weather tweet text to dictionary
    output['mars_weather_tweet'] = mars_weather_tweet

    return output