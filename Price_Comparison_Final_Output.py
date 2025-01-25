from threading import Thread
import pandas as pd
import time
import os
import AMAZON_FINAL
import AMAZON_UK_FINAL
import Barnesdnoble_FINAL
import Kinokuniya_UAE_FINAL
 

Items = pd.read_excel('assets/input/ISBN_INPUT.xlsx')
Item = Items['ISBN'].unique().tolist()

list1 = Item
input_List = []

for i in range(1,3):
    input_List.append(list1[ int(len(list1)/3)*i - int(len(list1)/3) : int(len(list1)/3) * i  ])
    
input_List.append(list1[int(len(list1)/3) * i:])

for i in input_List:
    print(i)
    print('Iteration_Completed')
    print('\n')
    

def func1(ii):
    AMAZON_FINAL.Amazon_KSA(ii)
def func2(ii):
    AMAZON_UK_FINAL.Amazon_UK(ii)
def func3(ii):
    Barnesdnoble_FINAL.Barnesdnoble(ii)
def func4(ii):
    Kinokuniya_UAE_FINAL.Kinokuniya_UAE(ii)


thread1 = Thread(target=func1, args=(i,))
thread2 = Thread(target=func2, args=(i,))
thread3 = Thread(target=func3, args=(i,))
thread4 = Thread(target=func4, args=(i,))

# Start all threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()
thread4.join()


dir_path = r'assets/output\\'

# list to store files
res = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        # data = pd.read_excel('T:/Working Folder/Aman/R&D work Python/Price_Comprison/Results/Latest_Result/{}'.format(path))
        print('assets/output/{}'.format(path))
        data = pd.read_excel('assets/output/{}'.format(path))

        res.append(data)
    print('Next File should come')

result = pd.concat(res)

# result.to_excel('T:/Working Folder/Aman/R&D work Python/Price_Comprison/Results/Latest_Result/MY_OUTPUT.xlsx')

result.to_csv('assets/output/MY_OUTPUT.csv', index=False)