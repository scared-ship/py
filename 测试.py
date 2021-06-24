from selenium import webdriver
import unittest
import time


# class apiteststudy(unittest.TestCase):
#     # 找到浏览器驱动并执行
#     def setUp(self):
#         self.driver = webdriver.Chrome(
#             "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\chormedriver.exe")


    # 执行测试用例
# def test_apiteststudy_url():
#     driver = webdriver.Chrome()
#     firstrequesturl = "https://www.sogou.com/"
#     secondrequesturl = "https://www.baidu.com/"
#     # 首先访问sogou首页
#     driver.get(firstrequesturl)
#     # 然后在访问Baidu首页
#     driver.get(secondrequesturl)
#     # 后退至上次访问的sogou首页
#     time.sleep(2)
#     driver.back()
#     # 前进至访问的baidu首页
#     time.sleep(2)
#     driver.forward()
#     print("...执行成功...")
#
#
# def teardown(self):
#     # 退出浏览器
#     self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
driver = webdriver.Chrome()
driver.get("http://xt-test.yeba.im/")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="adminlogin"]/form[1]/div[1]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="admin"]/div[1]/div/div/input').send_keys("15810")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="admin"]/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="admin"]/div[4]/button').click()
driver.get("http://www.sohu.com")
driver.back()
driver.quit()
