from selenium import webdriver



driver = webdriver.Chrome()#change to PhantomJS() if you don't want browser to open up


url = "https://onyolo.com/m/"+input("what is the yolo code(the thing in the URL): ")+"?"

driver.get(url)

text = input("What would you like spammed: ")
numberOfSpams = int(input("How many times do you want this spammed: "))
while numberOfSpams!=0:
    driver.find_element_by_xpath('//*[@id="text"]').send_keys(text)
    driver.find_element_by_xpath('//*[@id="send-button"]').click()
    driver.refresh()
    print("--------->Sent")
    numberOfSpams-=1


