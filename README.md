# Web Scraping
Using BeautifulSoup and Selenium, we scrape data from websites and store them in a dataframe using Pandas. We use various websites such as CodeChef, StackOverflow and Flipkart.

## Overview
Web Scraping (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file in your computer or to a database in table (spreadsheet) format.<br/>

Data displayed by most websites can only be viewed using a web browser. They do not offer the functionality to save a copy of this data for personal use. The only option then is to manually copy and paste the data - a very tedious job which can take many hours or sometimes days to complete. Web Scraping is the technique of automating this process, so that instead of manually copying the data from websites, the Web Scraping software will perform the same task within a fraction of the time.

## BeautifulSoup
Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping. Three features make it powerful:
<br/><br/>
• Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application.<br/>
• Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.<br/>
• Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.
<br/><br/>

Here we scrape the data from CodeChef to get all the problems which are on easy difficulty.<br/>
Link: https://www.codechef.com/problems/easy

### Output: 
![]('https://github.com/sreesh2411/web-scraping/blob/main/images/OUTPUT1.gif')

## Selenium
Selenium is a powerful tool for controlling web browsers through programs and performing browser automation. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C#, etc, we will be working with Python. Selenium Tutorial covers all topics such as – WebDriver, WebElement, Unit Testing with selenium. This Python Selenium Tutorial covers Selenium from basics to advanced and professional uses.<br/><br/>

We scrape the data from StackOverflow to obtain the most voted questions on the website.<br/>
Link: https://stackoverflow.com/questions?sort=votes

### Output:
![]('https://github.com/sreesh2411/web-scraping/blob/main/images/OUTPUT2.gif')

A chrome window pops up:
![]('https://github.com/sreesh2411/web-scraping/blob/main/images/2020-10-12.png')

## BeautifulSoup + Selenium
We combine BeautifulSoup and Selenium both to extract data from Flipkart and get the Laptops with buyback guarantee.<br/>
Link: https://www.flipkart.com/laptops/laptops~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g

## Resources:
A tutorial on BeatifulSoup by Keith Galli: https://www.youtube.com/watch?v=GjKQ6V_ViQE <br/>
BeautifulSoup Documentation: https://www.youtube.com/watch?v=GjKQ6V_ViQE <br/>
A comprehensive playlist on Selenium by Tech With Tim: https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ <br/>
Selenium Documentation: https://selenium-python.readthedocs.io/ <br/>
Link for ChromeDriver download: https://chromedriver.chromium.org/ <br/>

 
