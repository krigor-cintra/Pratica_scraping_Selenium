# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:01:08 2024

@author: krigor
"""

# In[]:
    
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://177.221.27.2:8079/transparencia/")
driver.implicitly_wait(0.5)

submit_button = driver.find_element(by=By.ID, value="LnkMenuPessoal")
submit_button1 = driver.find_element(by=By.ID, value="LnkServidores")

submit_button.click()
submit_button1.click()
'''if submit_button.is_displayed():
    submit_button.click()
else:
    print("Elemento oculto. Tente lidar com a visibilidade.")'''


#driver.quit()

# %%
