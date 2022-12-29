import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def ws_shopbag():
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


        
    # 메인 홈에서 검색 필드에 랜덤 벤더 입력
    vendorName = ['allium', 'zenana', 'Kind Lips', 'a mente', '01 Agrade', '7th Ray']
    choiceVendor = random.choice(vendorName)

    try:
        driver.find_element(By.CLASS_NAME, "search-input").click()
        driver.implicitly_wait(3)
        pyautogui.typewrite(choiceVendor, interval=0.1)
        driver.implicitly_wait(3)
        driver.find_element(By.CLASS_NAME, "btn-search").click()
        driver.implicitly_wait(10)
    except:
        pyautogui.alert("Error : Vendor search failed")
        print("Error : Vendor search failed")
        driver.quit()

    # 가장 맨 앞 3개 아이템 쇼핑백에 추가    
    # try:
    driver.find_element(By.XPATH, "//*[@id='item-found']/div[1]/ul/li[1]").click()
    driver.implicitly_wait(10)

    nqty = driver.find_element(By.ID, "lb_qty")

    if nqty.is_enabled():
        nqty.clear()
        nqty.send_keys("1")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
    else:
        nqty.send_keys("1")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#content > div > div.pdt_wrap.renewal_premium > div.pdt_detail > div.btn_group > span").click()
    driver.implicitly_wait(5)
    time.sleep(2)
    
    driver.refresh()
    driver.implicitly_wait(5)
    time.sleep(2)

    # except:
    # pyautogui.alert("Error : Shopping bag add failed")
    # print("Error : Shopping bag add failed")
    # driver.quit()
    # driver.find_element(By.XPATH, "//*[@id='item-found']/div[1]/ul/li[2]").click()
    # driver.find_element(By.XPATH, "//*[@id='item-found']/div[1]/ul/li[3]").click()