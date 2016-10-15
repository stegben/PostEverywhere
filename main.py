#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# Import selenium Lib.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome binary address
CHROME_DRIVER = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

# Let's pretend we have url already
POST_URL = ["https://www.facebook.com/247540868619076/posts/1283033715069781",
            "https://www.facebook.com/247540868619076/posts/1282861751753644"]

for url in POST_URL:
    try:
        driver.get(url)
    except:
        print sys.exc_info()[0]
