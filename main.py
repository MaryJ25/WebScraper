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
    print("Hello and welcome to Vinted web Scraper")
    print("It's not pretty or fast, but it does the job")
    answer = "N"
    while answer == "N":
        items = items_to_scrape()
        print("The items that will be scraped are: ")
        print(items)
        answer = input("Are you happy with this selection? Y/N \n").upper()
        if answer != "Y" or answer != "N":
            pass

    print("lets begin")


main()
