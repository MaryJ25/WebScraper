from scrape_and_store import scrape, store


def items_to_scrape():
    print("Default items are boots, trousers, pendant.")
    answer = input("Do you want to run the scraper the default items? Y/N \n").upper()
    if answer == "Y":
        items = ["boots", "trousers", "pendant"]
    elif answer == "N":
        items = []
        number = int(input("How many items do you want to scrape? \n"))
        for i in range(number):
            item = input("What item do you want to scrape? \n")
            items.append(item)
        print(items)
    else:
        print("Use Y or N.")
        answer = input("Do you want to run the scraper the default items? Y/N \n").upper()

    return items


def main():
    items = ["boots", "trousers", "pendant"]
    store.item_types_table(items)
    store.all_items_table()
    data = scrape.scrape(items, 100)
    scrape.make_csv("all_items", data)
    store.copy_from_csv()


main()
