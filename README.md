# The New and improved Vinted web scraper

The scrape and store directory contains files that allow for data to be scraped from Vinted and then stored in a Postgre SQL database. The project is made to run through Docker.

To run in Docker:

```
docker build -t web_scraper .
docker run --privileged -p 4000:4000 -d -it web_scraper 
```
## Requirement
Databasse credentials need to be inserted in the store.py file for the program to work. 

## How it works
Running the container will initialise the code in main.py file.

Here's how it works:

This is a list of items we want to look for on Vinted. The list can have any number of items.

```python
items = ["boots", "trousers", "pendant"]`
```
This function then creates a table in the database that keeps track of the item types.

```python
store.item_types_table(items)
```
This will get the data. Data collected will be the name of product, price, link to the item and link to the image.
```python
data = scrape.scrape(items, 3000)
```
The following function will then save the data to a csv file named all_items
```python
scrape.make_csv("all_items", data)
```

Then uploaded to the database using:
```python
store.copy_from_csv()
```

