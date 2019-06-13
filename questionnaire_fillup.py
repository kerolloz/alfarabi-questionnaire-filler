from selenium import webdriver
import os

def save_and_submit():
    driver.find_element_by_xpath("//button[@class='btn btn-icon btn-primary glyphicons circle_ok center']").click()
    # save and submit

USERNAME = os.environ['STUDENT_USERNAME']
PASSWORD = os.environ['STUDENT_PASSWORD']

driver = webdriver.Firefox()

driver.get("https://alfarabi.mans.edu.eg/login")

username_input = driver.find_element_by_xpath("//input[@name='username']")
password_input = driver.find_element_by_xpath("//input[@name='password']")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
driver.find_element_by_xpath("//input[@name='userType'][@value='2']").click()  # usertype = student
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()    # signin button

subjects = driver.find_elements_by_xpath("//li[@class='glyphicons dropMenu']")

for subject in subjects:
    subject.click()

    driver.find_element_by_xpath("//input[@class='uniform'][@type='checkbox']").click()  # check on doctor name
    good_ratings = driver.find_elements_by_xpath("//input[@type='radio'][@value='3']")

    for rating in good_ratings:
        rating.click()  # check all "I totally agree" radio buttons

    strengths, weaknesses = driver.find_elements_by_xpath("//input[@type='text']")
    strengths.send_keys("...")
    weaknesses.send_keys("...")
    
    save_and_submit()

general_questionnaires = driver.find_elements_by_xpath("//li[@class='glyphicons']")

for g_q in general_questionnaires:
    g_q.click()
    good_ratings = driver.find_elements_by_xpath("//input[@type='radio'][@value='2']")

    for rating in good_ratings:
        rating.click()

    save_and_submit()


driver.close()
