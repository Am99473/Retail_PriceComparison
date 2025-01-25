
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import re


# import requests
# from PIL import Image
# from io import BytesIO
# import easyocr


# def extract_text_from_image_url(image_url):
#     # Download the image from the URL
#     response = requests.get(image_url)
#     img = Image.open(BytesIO(response.content))

#     # Create an OCR reader using the English language
#     reader = easyocr.Reader(['en'])

#     # Perform OCR using easyocr
#     result = reader.readtext(img)

#     # Extracted text from the result
#     text = ' '.join([entry[1] for entry in result])

#     return text


def Amazon_KSA(input1):
    try:
        Element_not_Found = "Try checking your spelling or use more general terms"

        url = 'https://www.amazon.sa/?language=en_AE'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(15)
        # i = 100
        # try:
        #     while(i>0):
                
        #         if driver.find_element(By.XPATH, '//input[@class="a-span12"]').is_displayed():
                
        #             time.sleep(10)
    
        #             temp_url = driver.find_element(By.XPATH,'//div[@class="a-row a-text-center"]').find_element(By.TAG_NAME,'img').get_attribute('src')
        #             Capcha_text = extract_text_from_image_url(temp_url)
        #             time.sleep(3)
        #             driver.find_element(By.XPATH, '//input[@class="a-span12"]').send_keys(Capcha_text)
        #             time.sleep(10)
        #             driver.find_element(By.XPATH,'//button[@class="a-button-text"]').click()
    
        #             time.sleep(5)
                    
        #             if driver.find_element(By.XPATH, '//input[@class="a-span12"]').is_displayed():
        #                 i = 100
        #             else:
        #                 i = -100
        #             #driver.get(driver.current_url)

        # except Exception as e:
        #     pass




        if isinstance(input1, list):
            pass
        else:
            input1 = [input1]

        time.sleep(5)
        l = []

        for i in input1:

            search_bar_click = driver.find_elements(By.XPATH, '//input[@class="nav-input nav-progressive-attribute"]')

            time.sleep(5)

            a = search_bar_click[0]
            b = search_bar_click[1]

            time.sleep(5)

            a.clear()

            a.send_keys(i)

            time.sleep(5)

            b.click()

            time.sleep(5)

            html = driver.find_element(By.TAG_NAME, 'html')
            html = html.text

            time.sleep(10)

            try:
                if Element_not_Found in html:
                    print('element not found....error should not come.')
                    pass
                else:
                    print('this should not run after the above statement')
                    
                    Item_Title = driver.find_element(By.XPATH, '//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]')
                    
                    item_link = driver.find_element(By.XPATH, '//a[@class="a-link-normal s-line-clamp-4 s-link-style a-text-normal"]')
                    item_link = item_link.get_attribute('href')
                    driver.get(item_link)
    
                    time.sleep(5)
    
                    # temp_list1 = driver.find_elements(By.XPATH, '//span[@class="a-button a-spacing-mini a-button-toggle format"]')
                    # temp_list2 = driver.find_elements(By.XPATH, '//span[@class="a-button a-button-selected a-spacing-mini a-button-toggle format"]')
    
    
                    Product_category     =   driver.find_elements(By.XPATH, '//span[@class="slot-title"]')
                    Product_price        =   driver.find_elements(By.XPATH, '//span[@class="slot-price"]')
                    
                    
                    for ii, iii in zip(Product_category,Product_price):
                        
                        print('i and ii values are : ')
                        print(ii.text)
                        print(iii.text)

                        l.append(['Amazon KSA'] +  [i] + [ii.text] + [re.findall(r'\d+\.\d+', iii.text[1:])[0]] + [item_link])

                        
                        
    
                    # for ii in Final_List:
                    #     l.append([i] + [ii.text.split('\n')[0]] + [str(ii.text.split('\n')[-1]).split('£')[-1]] + ['Amazon UK'])

            except Exception as e:
                i = -100
                print(e) 
                pass

    except Exception as e:
        print(e)

    finally:
        driver.close()


    data = pd.DataFrame(data=l, columns=['Companies', 'ISBN', 'Product Type' , 'Product Price', 'Product Link'])

    data = data[['ISBN', 'Companies' ,'Product Price', 'Product Type' , 'Product Link']]

    data['Currency'] = 'SAR'

    data.to_excel('assets/output/AMAZON_KSA {}.xlsx'.format(str(input1[0])))

    return data

# Items = pd.read_excel('assets/input/ISBN_INPUT.xlsx')
# Item = Items['ISBN'].unique().tolist()
# Amazon_KSA( Item )

# Amazon_KSA( [9780552166775, 9781784851866])


