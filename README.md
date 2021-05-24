# The New and improved Vinted web scraper

The scrape and store directory contains files that allow for data to be scraped from Vinted and then stored in a Postgre SQL database. The project is made to run through Docker.

To run in Docker:

```
docker build https://github.com/MaryJ25/WebScraper
docker run --privileged -p 4000:4000 -d -it selenium_docker 

```

Here's an example for how to use this module and the functions in it: 
 
This is a list of items we want to look for on Vinted.

```python
items = ["boots", "trousers", "pendant"]`
```
This function then creates a table in the database that keeps track of the item types.

```python
store.item_types_table(itmes)
```

```python
INSERT EXAMPLE CODE HERE
```

The above for loop goes through each item in the list. It first makes a corresponding table in the database. 
Then it scrapes the needed data from Vinted. 
The data is put into a csv file and then copied to the database table.
