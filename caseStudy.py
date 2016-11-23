#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver

class CaseStudy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_anasayfa(self):
        driver = self.driver
        driver.get("http://www.n11.com")
        driver.maximize_window()
        if driver != 0:
            print(driver.title)
            print("Ana Sayfa açıldı")
            time.sleep(2)
        login = driver.find_element_by_link_text("Giriş Yap").click()
        email = driver.find_element_by_id("email").send_keys("test@grr.la")
        password = driver.find_element_by_id("password").send_keys("test321")
        btnLogin = driver.find_element_by_id("loginButton").submit()
        time.sleep(3)
        arama = driver.find_element_by_id("searchData").send_keys("samsung")
        btnSearch = driver.find_element_by_class_name("searchBtn").click()
        time.sleep(4)
        ikinci_sayfa = driver.current_url + "&pg=2"
        driver.get(ikinci_sayfa)
        if driver.get(ikinci_sayfa) != 0:
            print("İkinci Sayfadayız")
            time.sleep(3)
        urunler = driver.find_elements_by_class_name("followBtn") #//*[@id="p-124537844"]/div[2]/span
        urunler[2].click()
        fare = webdriver.ActionChains(driver)
        fare.move_to_element(driver.find_element_by_xpath("//*[@id='header']/div/div/div[2]/div[2]/div[1]/div[1]"))
        fare.perform()
        time.sleep(3)
        favorilerim = driver.find_element_by_xpath("//*[@id='header']/div/div/div[2]/div[2]/div[1]/div[2]/div/a[2]").click()
        time.sleep(3)
        urun1 = driver.find_element_by_xpath("//*[@id='watchList']/tbody/tr/td[3]")
        if urun1 != 0:
            print ("Ürün listede")
            kaldir = driver.find_element_by_xpath("//*[@id='watchList']/tbody/tr/td[1]/a").click()
        time.sleep(3)
        bos = driver.find_element_by_css_selector("#watchList > tbody > tr > td > div")
        if bos != 0:
            print("ürün artık favorilerde değil")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()