#Vinted web scraper

The scrape and store module contains files that allow for data to be scraped from Vinted and then stored in a Postgre SQL database.

Here's an example for how to use this module and the functions in it: 
 
This is a list of items we want to look for on Vinted.

```python
items = ["boots", "trousers", "pendant"]`
```
This function then creates a table in the database that keeps track of the item types.

```python
store.item_types_table(items[0], items[1], items[2])
```

```python
for index, item in enumerate(items):
    store.make_table(item)
    data = scrape.scrape(item, 3000, index+1)
    scrape.make_csv(item, data)
    con = store.connect()
    store.copy_from_df(con, item, item)
```

The above for loop goes through each item in the list. It first makes a corresponding table in the database. 
Then it scrapes the needed data from Vinted. 
The data is put into a csv file and then copied to the database table.