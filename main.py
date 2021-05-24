from scrape_and_store import scrape, store


def main():
    items = ["boots", "trousers", "pendant"]
    store.item_types_table(items)
    store.all_items_table()
    data = scrape.scrape(items, 3000)
    scrape.make_csv("all_items", data)
    store.copy_from_csv()


main()
