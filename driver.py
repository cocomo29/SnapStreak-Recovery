from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://support.snapchat.com/en-US/i-need-help")
print(driver.title)

# driver.find_element().click()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.page-container div.view-container:nth-child(1) div.ui.container.desktop-navigation:nth-child(3) div.sc-content:nth-child(2) div.fix-a-problem-wizard div.sc-wizard-content.wait-until-loaded.ready div.sc-wizard-question-block:nth-child(1) div.sc-radios div.ui.container.grid.option_wrapper div.sixteen.wide.mobile.eight.wide.computer.column:nth-child(4) div.option label:nth-child(2) > div.sc-radio-circle"))))
# driver.find_element(By.CSS_SELECTOR, "#field-24281229").send_keys(username)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#field-24281229"))))
driver.find_element(By.CSS_SELECTOR, "#field-24281229").send_keys("username")
driver.find_element(By.CSS_SELECTOR, "#field-24335325").send_keys("email")
driver.find_element(By.CSS_SELECTOR, "#field-24369716").send_keys("mobile")
driver.find_element(By.CSS_SELECTOR, "#field-24369726").send_keys("device")
driver.find_element(By.CSS_SELECTOR, "#field-24326423").send_keys("date")
driver.find_element(By.CSS_SELECTOR, "#field-24369736").send_keys("friend")
driver.find_element(By.CSS_SELECTOR, "#field-24641746").send_keys("streak")
driver.find_element(By.CSS_SELECTOR, "#field-22808619").send_keys("info")

#click on a dropdown menu
driver.find_element(By.CSS_SELECTOR, "div.page-container div.view-container:nth-child(1) div.ui.container.desktop-navigation:nth-child(3) div.sc-content:nth-child(2) div.fix-a-problem-wizard div.sc-wizard-content.wait-until-loaded.ready div.contact-form:nth-child(2) div:nth-child(2) form.ui.form div.field:nth-child(9) div.field.required > div.ui.dropdown.selection:nth-child(2)").click()
driver.find_element(By.XPATH, "//div[contains(text(),'No')]").click()

