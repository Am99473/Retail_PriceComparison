from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys



def Kinokuniya_UAE(input_List):
    try:
        Item_List = []
        Element_Not_Found = "No results."

        url = 'https://uae.kinokuniya.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(10)

        driver.find_element(By.XPATH, '//input[@class="textArea"]').send_keys(9781785042720)
        time.sleep(10)
        driver.find_element(By.XPATH, '//input[@class="searchIcon"]').click()
        time.sleep(10)

        driver.get(driver.current_url)

        time.sleep(10)

        if isinstance(input_List, list):
            pass
        else:
            input_List = [input_List]

        for i in input_List:

            a = driver.find_element(By.XPATH , '//input[@class="textArea"]')

            a.clear()

            a.send_keys(i)

            time.sleep(10)

            aa = driver.find_element(By.XPATH, '//input[@class="searchIcon"]')

            aa.click()

            print('searchIcone found')

            time.sleep(10)

            html = driver.find_element(By.TAG_NAME, 'html')
            html = html.text
            
            try:
                if Element_Not_Found in html:
                    pass
                else:
    
                    item = driver.find_element(By.XPATH , '//div[@class="inner_box"]')
                    item = item.find_element(By.TAG_NAME, 'a')
                    link = item.get_attribute('href')
                    driver.get(item.get_attribute('href'))
    
                    product_Price = driver.find_element(By.XPATH , '//li[@class="price"]')
                    product_Price = product_Price.find_element(By.TAG_NAME, 'span').text
    
                    print(product_Price.split(' ')[-1])
                    
                    print('Working 1')
                    
                    Book_Version = driver.find_element(By.XPATH, '//table[@class="bookData"]')
                    Book_Version = Book_Version.find_element(By.TAG_NAME, 'td').text
                    
                    print('Working 2')
                    
                    print(Book_Version)
    
                    Item_List.append([i,product_Price.split(' ')[-1],Book_Version,'Kinokuniya UAE', link])


            except Exception as e:
                i = -100
                print(e)
                pass

        driver.delete_all_cookies()


    except Exception as e:
        print(e)
        Kinokuniya_UAE(input_List)
        # pass

    finally:
        driver.close()


    data = pd.DataFrame(data=Item_List, columns=['ISBN', 'Product Price','Product Type','Companies', 'Product Link'])
    data = data[['ISBN','Product Price', 'Product Type' , 'Companies', 'Product Link']]
    data['Currency'] = 'AED'

    data.to_excel('assets/output/KINOKUNIYA {}.xlsx'.format(str(input_List[0])))

    return data

# '''
# list1 = [9781785042720,9781612681139]

# result = Kinokuniya_UAE(list1)

# print(result)
# '''

# Kinokuniya_UAE([9780552166775])