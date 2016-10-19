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
            "https://www.facebook.com/247540868619076/posts/1282861751753644",
            "https://www.facebook.com/187171314925/posts/10154076685669926",    # Test the missed page
            "https://www.facebook.com/178875832200695/posts/1220987807989487",  # Long post
            "https://www.facebook.com/172446252825509/posts/1155351581201633"]


for url in POST_URL:
    # Try to get the page
    try:
        driver.get(url)
        while True:
            try:
                driver.find_element_by_id('loginbutton')
                print "[*] Should Log-in"
                import time
                time.sleep(20)
            except:
                break

    except:
        print "[*] Load page exception: ",sys.exc_info()[0]
        print "[*] URL: ", url
        continue
    
    # TODO
    # The comments of the post will not show automatically
    # Current solution: log-in (and log-in will show more comments automatically )


    # Try to get the post content
    try:
        post_div = driver.find_element_by_class_name('userContentWrapper')
        post_content_div = driver.find_element_by_class_name('userContent')
        post_content_text_list = post_content_div.find_elements_by_css_selector('p')
        post_content_text = ''.join(p.text for p in post_content_text_list)
        print post_content_text
    except:
        print "[*] Get post exception: ",sys.exc_info()[0]
        continue

    # Try to reveall all the hidden comments
    try:
        post_div.find_elements_by_class_name('clearfix')[-1].find_element_by_class_name('UFIPagerLink').click()
    except:
        print "[*] Get hidden comments exception: ",sys.exc_info()[0]
    
    # Try to go through all the showed comments
    try:
        comment_list = post_div.find_elements_by_class_name('UFICommentContentBlock')
        for comment_block in comment_list:
            try:
                user_profile = comment_block.find_element_by_css_selector("a")
                user_profile_url = user_profile.get_attribute('href')
                print "User ", user_profile.text
                print "User url ", user_profile_url
                comment_content = comment_block.find_element_by_class_name("UFICommentBody").text
                print comment_content
                print 
                if not comment_content:
                    continue
                # Else, save the info
            except:
                continue
    except:
        print "[*] Donwload comments exception: ",sys.exc_info()[0]
        continue

