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
source_data = driver.page_source


def main(url):
    list_ = [
        'Central Wyoming College',
        'Eastern Wyoming College',
        'Northern Wyoming Comm Coll',
        'Northwest College-Wyoming',
        'NotHLCAccred Wyo Tech',
        'University of Wyoming',
        'Western Wyoming Comm College',
        'Wyoming Catholic College'
    ]

    list_colleg = []
    
    try:

        driver.get(url)
        driver.implicitly_wait(20)
        # source_data = driver.page_source
        
        # soup = bs(source_data, 'html.parser')

        get_colleg = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/table/tbody/tr[1]/td[2]/select/option')
        # print(type(get_colleg))

        # for _ in range(len(get_colleg)):

        for colleg in get_colleg:
            # print(1)
            get_text_colleg = colleg.text

            if get_text_colleg not in list_:
                continue

            print(get_text_colleg)

            colleg.click()
            time.sleep(2)

            get_usp_atribut = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/table/tbody/tr[2]/td[8]/select/option')
            # print(4)

            for usp_atribute in get_usp_atribut:
                # print(5)

                get_text_usp_atribut = usp_atribute.text
                # print(6)
                # print('------------')

                if get_text_usp_atribut == 'All':
                    continue
                
                usp_atribute.click()
                time.sleep(2)

                button_search = driver.find_element(By.XPATH, '//div[@class="pagebodydiv"]/form[2]/button/div/div').click()
                # print(button_search.text)
                # button_search.click()
                
                time.sleep(3)
                get_table = driver.find_elements(By.XPATH, '//div[@class="pagebodydiv"]/table[@class="datadisplaytable"]/tbody/tr/td[@class="dddefault"]')

                for text_table in get_table:
                    get_text_table = text_table.text
                    print(get_text_table)

            
            
        

    except Exception as ex:
        print(ex)

    finally:
        time.sleep(5)
        driver.close()
        driver.quit()




if __name__ == '__main__':
    main('https://wyossb.uwyo.edu/bnrprod/bwckytfc.p_display_transfer_catalog')