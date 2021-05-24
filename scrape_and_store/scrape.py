from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display
from time import sleep
import pandas as pd


def browser_setup(keyword: str):

    display = Display(visible=0, size=(800, 600))
    display.start()
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    browser = webdriver.Firefox(firefox_profile=firefox_profile)


    options = Options()
    options.headless = True
    capabilities = DesiredCapabilities().FIREFOX
    capabilities["marionette"] = True
    driver = webdriver.Firefox(capabilities=capabilities, options=options)
    actions = ActionChains(driver)
    url = "https://www.vinted.co.uk/vetements?search_text="
    # adjusts the link to go to the correct page
    browser = driver.get(url + keyword)
    return browser


def dataframe_setup():
    column_names = ["title", "price", "item_link", "image_link", "item_type"]
    df = pd.DataFrame(columns=column_names)
    return df


def scrape(items: list, quantity: int):
    """
    This function will scrape the titles, prices, item links and image links of a requested category of items.
    Provide a list of categories in place of the items parameter and a number of items to find in place of quantity
    parameter. When finished the function produces a pandas dataframe containing all the data.
    """
    df = dataframe_setup()
    for i in items:
        driver = browser_setup(i)
        all_items = []
        all_titles_list = []
        all_prices_list = []
        all_links_list = []
        all_images_list = []

        while len(all_prices_list) < quantity:
            sleep(5)
            # scrapes all titles
            titles = [title.text for title in driver.find_elements_by_class_name("ItemBox_details__1c8wh")]
            all_titles_list.append(titles)

            # scrapes all prices
            prices = [price.text for price in driver.find_elements_by_class_name("ItemBox_title__2FmDy")]
            all_prices_list.append(prices)

            # scrapes all item links
            item_links = [link.get_attribute("href") for link in
                          driver.find_elements_by_class_name("ItemBox_overlay__1kNfX")]
            all_links_list.append(item_links)

            # scrapes all image links
            image_links = [image.get_attribute("src") for image in
                           driver.find_elements_by_css_selector("div.ItemBox_image__3BPYe img")]
            all_images_list.append(image_links)

            try:
                element = driver.find_element_by_xpath('//a[@class="Pagination_next__DUhdH"]')
                driver.execute_script("arguments[0].click();", element)
            except NoSuchElementException:
                break

        all_titles = [item for sublist in all_titles_list for item in sublist]
        all_prices = [item for sublist in all_prices_list for item in sublist]
        all_links = [item for sublist in all_links_list for item in sublist]
        all_images = [item for sublist in all_images_list for item in sublist]
        all_items.extend((all_titles, all_prices, all_links, all_images))

        # stores the information in a dataframe
        items_df = pd.DataFrame(all_items).T
        mapping = {items_df.columns[0]:'title', items_df.columns[1]: 'price',
                   items_df.columns[2]:'item_link', items_df.columns[3]: 'image_link'}

        items_df = items_df.rename(columns=mapping)
        final_df = df.append(items_df, ignore_index=True)
        category = f"{i}"
        final_df["item_type"] = final_df["item_type"].fillna(value=category)
        driver.quit()

    return final_df


def make_csv(name: str, df):
    """
    This function takes a dataframe and makes it into a csv file. A name for the file needs to be given when calling
    the function.
    """
    string_execute = f"./{name}.csv"
    df.to_csv(path_or_buf=string_execute, header=False, sep=";")
