# The New and improved Vinted web scraper

The scrape and store directory contains files that allow for data to be scraped from Vinted and then stored in a Postgre SQL database. The project is made to run through Docker.

To run in Docker:

```
docker build -t web_scraper .
docker run --privileged -p 4000:4000 -d -it web_scraper 
```

Here's an example for how to use this module and the functions in it: 
 
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
The data needs to be saved to a csv and then uploaded using:
```python
scrape.make_csv("all_items", data)
```

The data is put into a csv file and then copied to the database table.
