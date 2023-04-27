from selenium import webdriver, By
#from selenium.webdriver.common.by import By

a = webdriver.Firefox(executable_path = "Users\obada\Downloads\firefox_driver")
a.get("https://www.python.org/")
b = a.find_element(By.CSS_SELECTOR, ".medium-widget.event-widget.last .shrubbery .menu").text.split("\n")
a.quit()

d = dict()

for c in range(0, len(b), 2):
    d[c] = { "Date": b[c], "Name": b[c + 1] }
    
print(d)