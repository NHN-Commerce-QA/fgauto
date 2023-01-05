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
        time.sleep(0.2)
        driver.find_element(By.NAME, "password").send_keys(PW + Keys.TAB)
        time.sleep(0.2)
    except:
        pyautogui.alert("Error : ID or PW is not found")
        print("Error : ID or PW is not found")
        driver.quit()

    # ID 및 PW 입력 후 Sign in 버튼 클릭
    try:
        signin_btn = driver.find_element(By.ID, "btn-signin")
        signin_btn.click()
        driver.implicitly_wait(15)
    except:
        pyautogui.alert("Error : Sign in btn is not found")
        print("Error : Sign in btn is not found")

    # 로그인 성공
    print("========================Test Account Login========================")
    print("Account ID : " + ID)
    print("Password : " + PW)

    # Introducing Order Updates via Text 팝업 모달이 표시될 때, 닫기 / 없으면 Pass
    if driver.find_element(By.ID, "sms-modal-close").is_displayed():
        driver.find_element(By.ID, "sms-modal-close").click()
        time.sleep(2)
    else:
        time.sleep(1)

    # home deals 팝업이 표시될 때 닫기 / 없으면 Pass
    if driver.find_element(By.XPATH, '//*[@id="home-deals-open-popup"]/div/div[3]/div/div/label').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="home-deals-open-popup"]/div/div[3]/div/div/label').click()
        time.sleep(2)
    else:
        time.sleep(1)