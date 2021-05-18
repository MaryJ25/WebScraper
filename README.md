#The New and improved Vinted web scraper

The scrape and store directory contains files that allow for data to be scraped from Vinted and then stored in a Postgre SQL database. It also contains the geckodriver needed for selenium to run Firefox and scrape the data

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
