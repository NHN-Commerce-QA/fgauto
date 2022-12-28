import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def ws_chat():
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
        pyautogui.alert("Error : login btn is not found!")
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
        time.sleep(5)
        driver.implicitly_wait(3)
    except:
        pyautogui.alert("Error : Sign in btn is not found")
        print("Error : Sign in btn is not found")

    # Introducing Order Updates via Text 팝업 모달이 표시될 때, 닫기 / 없으면 Pass
    introducing_order = driver.find_element(By.ID, "sms-no-thanks")
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

    # Chat 아이콘 클릭
    try:
        chat_icon = driver.find_element(By.XPATH, "//*[@id='global']/div[1]/div[2]/ul/li[3]/div/a")
        chat_icon.click()
        time.sleep(1)
    except:
        pyautogui.alert("Error : Chat icon is not found")
        print("Error : Chat icon is not found")
        time.sleep(1)

    # 새 탭이 오픈되고 채팅 dev-www.fashiongo.net/chat 탭으로 스위칭
    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(5)

    # 벤더 검색
    vendorName = ['allium', 'zenana', 'ZAD', 'Kind Lips', '3VERY', 'a mente', '01 Agrade', 'Eva Franco', 'Celavi', 'Adelyn Rae', 'Day G', '7th Ray']
    choiceVendor = random.choice(vendorName)

    # 벤더를 검색하는데 자동화 프로그램으로는 로딩이 지속되는 현상이 있어서, 별도로 pyautogui 라이브러리를 활용하여 검색
    driver.find_element(By.XPATH, "//*[@id='contanier']/div/div/section[1]/main/div[3]/div/input").click()
    pyautogui.typewrite(choiceVendor, interval=0.1)
    driver.implicitly_wait(15)
    time.sleep(5)
    # Xpath 및 Class name으로 엘리먼트를 찾아낼 수 없는 오류가 지속적으로 발생하여, CSS selector 방법으로 해결
    driver.find_element(By.CSS_SELECTOR, "#js-chat-List > div > ul > li").click()
    driver.implicitly_wait(5)

    # 검색한 랜덤 벤더를 문자열 형태로 추출
    vendorTitle_xpath = driver.find_element(By.XPATH, "//*[@id='top-vendor-name']")
    vendorTitle = vendorTitle_xpath.text
    print('chat random vendor : ' + vendorTitle)
    time.sleep(4)

    # 선택한 랜덤 벤더에게 여러가지 채팅 메시지 전송
    try:
        driver.find_element(By.CLASS_NAME, "input-chat").send_keys(('Hello,  ' + vendorTitle) + Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "input-chat").send_keys('I am sending a chat using an test automation program.' + Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "input-chat").send_keys('How are you doing?' + Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "input-chat").send_keys('How is the weather today?' + Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "input-chat").send_keys(('Have a good today, ' + vendorTitle) + Keys.RETURN)
        time.sleep(4)
    except:
        pyautogui.alert("Error : Vendor search failed.")
        print("Error : Vendor search failed.")
        driver.implicitly_wait(3)

    # 키워드 검색
    search_icon = driver.find_element(By.ID, "btn-keyword-search")
    search_icon.click()
    driver.implicitly_wait(3)

    search_field = driver.find_element(By.XPATH, "//*[@id='chat-header-section']/div[1]/div[1]/input")
    search_field.send_keys(vendorTitle)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='chat-header-section']/div[1]/div[1]/button[1]").click()
    driver.implicitly_wait(5)
    time.sleep(5)

    # 채팅방 나가기
    # leave_room = driver.find_element(By.CLASS_NAME, "btn-menu hide-text")
    # leave_room.click()
    # driver.implicitly_wait(3)

    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])
    # driver.implicitly_wait(3)

    