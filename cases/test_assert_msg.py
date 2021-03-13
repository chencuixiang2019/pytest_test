#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(executable_path ="C:\soft\python36\chromedriver.exe")

browser.get("http://ad.hivescrm.cn/creative/image")

sleep(2)

#3.刷新浏览器
# browser.refresh()

browser.maximize_window()
sleep(3)
element=browser.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div/input')
element.click()
element.send_keys("ads")

element=browser.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input')
element.click()
element.send_keys("ads123")

sleep(5)

element=browser.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/button')
element.click()
print('登录成功')

sleep(2)
#登录成功后等待几秒等页面加载完成，不然页面没加载完成，程序会报找不到元素

browser.get("http://ad.hivescrm.cn/creative/image")
sleep(10)
browser.maximize_window()
sleep(15)

#勾选删除
#browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div').click()
# sleep(2)
#点击删除按钮
# browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/button/span').click()
# sleep(2)
# 点击确定
# browser.find_element_by_xpath('//*[@class="el-message-box__wrapper"]//div//div[3]//button[2]').click()
# sleep(20)
# ele= browser.find_element_by_partial_link_text("删除成功")
# assert ele is not None
# page = browser.page_source
# print(page)
# alert_text = browser.switch_to.alert.text
# assert  alert_text == '删除成功'

#点击搜索按钮
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/button[1]').click()

sleep(4)
re = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/button').is_displayed()
print(re)
sleep(1)
#点击勾选
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()



'''
#点击新增
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/button').click()
print("点击新增弹窗成功")
sleep(3)
# browser.switch_to_alert()

#点击选择订单定位成功
browser.find_element_by_xpath('//div[@class="el-dialog__wrapper"]//div//div//form[@class="el-form"]//div//div//div//div//input').click()
sleep(5)
#选择下拉框，定位失败
# browser.find_element_by_xpath('//div[@class="el-select el-select--medium"]//div//div//div//ul//li[1]').click()
#找不到，但是页面能定位得到
browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
#browser.find_element_by_xpath('/html/body/div[5]/div/div/ul/li/span[contains(text(),"US-Electric Mini Garlic Chopper ")]').click()
#ActionChains(browser).double_click('/html/body/div[5]/div/div/ul/li/span[contains(text(),"US-Electric Mini Garlic Chopper ').perform()

print("选择订单成功")
sleep(5)
#找不到元素
# js = "document.body.getElementByClassName(\"el-dialog__wrapper\")[0].getElementByClassName(\"el-dialog__wrapper\").style.display='block';"
# js = "document.getElementByClassName(\"el-upload-list el-upload-list--picture-card\")[0].getElementByClassName(\"el-upload el-upload--picture-card\")[0].getElementByClassName(\"file\")[0].style.display='block';"

# js="document.getElementsByXpath('/html/body/div[2]/div/div[2]/form/div[2]/div/div/div/input').innerText.display='block';"
# browser.execute_script(js)
print("修改成为block")
sleep(5)
WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/form/div[2]/div/div/div')))
# browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[2]/div/div/div').click()
try:
    #这个路径找不到
    #browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[2]/div/div/div').send_keys('C:\\soft\\b21c8701a18b87d60a6c43db0c0828381e30fdcc.png')
    #css_selector可以找到
    #上传多张
    browser.find_element_by_css_selector("[type='file']").send_keys('C:\\soft\\b21c8701a18b87d60a6c43db0c0828381e30fdcc.png')
    sleep(3)
    browser.find_element_by_css_selector("[type='file']").send_keys('C:\\soft\\src=http___c-ssl.duitang.com_uploads_blog_201405_04_20140504112017_4VEi4.jpeg&refer=http___c-ssl.duitang.jpg')
    print("成功上传")

except:
    print("上传图片失败")
#点击确认上传
sleep(10)
browser.find_element_by_xpath('//*[@class="el-button el-button--primary el-button--small"]').click()
sleep(2)
print('上传')
#等待弹窗元素
#WebDriverWait(browser,10).until(EC.alert_is_present())
WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="el-message__content"]')))
#获取弹窗文本
alert=browser.find_element_by_xpath('//*[@class="el-message__content"]').text
print(alert)
#断言可以写
# assert alert=='素材上传成功'


# alert=browser.switch_to.alert
# print(alert.text)
# alert.accept()
sleep(1)
#点击标签
#直接copy的可能页面的DIV会变，所以下标不准，如div[4]
#element=browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[3]/div/div/div[1]/input')
element=browser.find_element_by_xpath('//input[@class="el-select__input is-medium"]')
element.click()
print('点击标签')
sleep(5)
#根据文本定位
element=browser.find_element_by_xpath('//span[(text()="视频")]')
element.click()
print('选择视频标签')
sleep(1)
#根据确定定位父节点的按钮button(前提条件是元素是唯一的)
element=browser.find_element_by_xpath('//button[span[(text()="确 定")]]')
element.click()
print('点击确定')

#等待弹窗元素
#WebDriverWait(browser,10).until(EC.alert_is_present())
WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="el-message__content"]')))
#获取弹窗文本
alert=browser.find_element_by_xpath('//*[@class="el-message__content"]').text
print(alert)
#断言可以写
assert alert=='新增成功'
#再次点击搜索，新增的数据显示在第一条
sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/button[1]').click()
#断言图片名称文本
sleep(5)
alert_text = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[4]/div').text
assert alert_text == 'b21c8701a18b87d60a6c43db0c0828381e30fdcc.png'
'''

browser.quit()