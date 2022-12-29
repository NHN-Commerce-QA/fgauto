import time
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def ws_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # dev-fashiongo 사이트 접속 후 윈도우 최대화
    driver.get("https://dev-www.fashiongo.net/")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)

    # cookie 버튼 찾아낸 후 accept all 버튼 클릭
    try:
        cookiebtn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookiebtn.click()
        time.sleep(1)
    except:
        pyautogui.alert("Error : Cookie accept all btn is not found")
        print("Error : Cookie accept all btn is not found")
        driver.quit()

    # Login 버튼 찾아낸 후 클릭
    try:
        loginbtn = driver.find_element(By.CLASS_NAME, "header_signIn")
        loginbtn.click()
        time.sleep(1)
    except:
        pyautogui.alert("Error : login btn is not found")
        print("Error : login btn is not found")
        driver.quit()

    # ID 및 패스워드 입력 후 로그인
    ID = "nhntester2@yopmail.com"
    PW = "QWER1q2w3e4r!"

    try:
        driver.find_element(By.NAME, "userName").send_keys(ID + Keys.TAB)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(PW + Keys.TAB)
        time.sleep(1)
    except:
        pyautogui.alert("Error : ID or PW is not found")
        print("Error : ID or PW is not found")
        driver.quit()

    # ID 및 PW 입력 후 Sign in 버튼 클릭
    try:
        signin_btn = driver.find_element(By.ID, "btn-signin")
        signin_btn.click()
        time.sleep(7)
    except:
        pyautogui.alert("Error : Sign in btn is not found")
        print("Error : Sign in btn is not found")

    # Introducing Order Updates via Text 팝업 모달이 표시될 때, 닫기 / 없으면 Pass
    introducing_order = driver.find_element(By.ID, "sms-modal-close")
    if introducing_order.is_displayed():
        introducing_order.click()
        time.sleep(1)
    else:
        time.sleep(1)

    # Home Deals 이벤트 팝업 모달이 표시될 때, 닫기 / 없으면 Pass
    homedeals = driver.find_element(By.ID, "home-deals-open-popup-close")
    if homedeals.is_displayed():
        homedeals.click()
        time.sleep(1)
    else:
        time.sleep(1)