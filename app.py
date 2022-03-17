from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json
import time



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


driver = webdriver.Chrome(executable_path = '/home/vladyslav/uw_transfer_catalog/uw_transfer_catalog/chromedriver')


def open_browser(url):
    driver.get(url)


def get_table_objects():

    #Get web-elements Colleg
    try:
        element_colleg = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/table[@class="dataentrytable"]/tbody/tr[1]/td[2]/select/option')

    except Exception as ex:
        print(ex)

    for text_colleg in element_colleg:

        #Get text web-elements Colleg
        get_text_colleg = text_colleg.text

        if 'Wyoming' in get_text_colleg:
            print(get_text_colleg)

            text_colleg.click()
            # time.sleep(2)

            #Get web-elements USP Attribute
            try:
                element_usp = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/table[@class="dataentrytable"]/tbody/tr[2]/td[8]/select/option')

            except Exception as ex:
                print(ex)

            for text_usp in element_usp:
                
                #Get text web-elements USP Attribute
                get_text_usp = text_usp.text

                if 'All' in get_text_usp:
                    continue

                print(get_text_usp)
                text_usp.click()
                # time.sleep(2)

                #Button Search
                driver.find_element(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/button[@id="id____UID1"]/div[@class="defaultButtonSmall"]').click()
                time.sleep(2)


                #Get elements Table
                try:
                    element_table = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/table/tbody/tr/td[@class="dddefault"]')

                except Exception as ex:
                    print(ex)

                for text_table in element_table:

                    #Get text elements Table
                    get_text_table = text_table.text
                    print(get_text_table)
                





def main():
    try:
        open_browser('https://wyossb.uwyo.edu/bnrprod/bwckytfc.p_display_transfer_catalog')
        driver.implicitly_wait(20)

        get_table_objects()
        driver.implicitly_wait(20)

            
        

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
