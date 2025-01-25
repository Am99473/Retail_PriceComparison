
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def Barnesdnoble(input1):
    try:
        Element_not_Found = "Sorry, we couldn't find what you're looking for. Please try another search or browse our recommendations below."

        url = 'https://www.barnesandnoble.com/'
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)

        driver.maximize_window()

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.HOME)

        l = []

        time.sleep(5)

        if isinstance(input1, list):
            pass
        else:
            input1 = [input1]

        html = driver.find_element(By.TAG_NAME, 'html')
        html = html.text

        for i in input1:

            a = driver.find_element(By.XPATH, '//*[@id="rhf_header_element"]/nav/div/div[3]/form/div/div[2]/div/input[1]')

            time.sleep(2)

            a.clear()

            a.send_keys(i)

            time.sleep(20)

            aa = driver.find_element(By.XPATH, '//button[@class="btn btn-outline-secondary rhf-search-btn"]')
            aa.click()

            time.sleep(10)

            html = driver.find_element(By.TAG_NAME, 'html')
            html = html.text

            time.sleep(10)
            
            try:
                if Element_not_Found in html:
                    print('element not found....error should not come.')
                    pass
                else:
    
                    item_type = driver.find_elements(By.XPATH, '//p[@class="format-name cold-gray mt-0 mb-xxxs pl-xxxs pr-xxxs"]')
                    item_price = driver.find_elements(By.XPATH, '//span[@class="format-price"]')
    
                    for ii, iii in zip(item_price, item_type):
                        l.append([i, str(ii.text).replace('$',''), iii.text,'Barnesandnoble', ''])
                        print(str(ii.text)[1:])


            except Exception as e:
                i = -100
                print(e)
                pass
            

    except Exception as e:
        print(e)
        Barnesdnoble(input1)
        # pass

    finally:
        driver.close()

    data = pd.DataFrame(l, columns=['ISBN', 'Product Price','Product Type','Companies', 'Product Link'])

    data = data[['ISBN','Product Price', 'Product Type' , 'Companies', 'Product Link' ]]

    data['Currency'] = '$'

    data.to_excel('assets/output/BARNESDNOBLE {}.xlsx'.format(str(input1[0])))

    return data

# Barnesdnoble(  [9780552166775, 9781784851866, 9780593083888] )