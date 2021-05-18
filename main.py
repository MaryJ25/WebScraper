# from scrape_and_store import scrape
# from scrape_and_store import store


def main():
    print("Hello and welcome to Vinted web Scraper")
    print("It's not pretty or fast, but it does the job")
    answer = input("Do you want to run the scraper with default items? Y/N \n").upper()
    if answer == "Y":
        items = ["boots", ]
    elif answer == "N":
        items = []
        number = int(input("How many items do you want to scrape? \n"))
        for i in range(number):
            item = input("What item do you want to scrape? \n")
            items.append(item)
        print(items)
    else:
        print("Not an option")


main()
