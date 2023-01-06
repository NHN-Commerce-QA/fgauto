import time
from tkinter import messagebox as msgbox
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
        msgbox.showerror("Error", "쿠키 버튼을 찾을 수 없습니다.")
        print("Error : Cookie accept all btn is not found")
        driver.quit()

    # Login 버튼 찾아낸 후 클릭
    try:
        loginbtn = driver.find_element(By.CLASS_NAME, "header_signIn")
        loginbtn.click()
        time.sleep(1)
    except:
        msgbox.showerror("Error", "로그인 버튼을 찾을 수 없습니다.")
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
        msgbox.showerror("Error", "ID나 PW를 찾을 수 없습니다.")
        print("Error : ID or PW is not found")
        driver.quit()

    # ID 및 PW 입력 후 Sign in 버튼 클릭
    try:
        signin_btn = driver.find_element(By.ID, "btn-signin")
        signin_btn.click()
        driver.implicitly_wait(15)
    except:
        msgbox.showerror("Error", "Sign in 버튼을 찾을 수 없습니다.")
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



    # Chat 아이콘 클릭
    try:
        chat_icon = driver.find_element(By.XPATH, "//*[@id='global']/div[1]/div[2]/ul/li[3]/div/a")
        chat_icon.click()
        time.sleep(1)
    except:
        msgbox.showerror("Error", "채팅 아이콘을 찾을 수 없습니다.")
        print("Error : Chat icon is not found")
        time.sleep(1)

    # 새 탭이 오픈되고 채팅 dev-www.fashiongo.net/chat 탭으로 스위칭
    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(5)

    # 벤더 검색
    vendorName = ['allium', 'zenana', 'ZAD', 'Kind Lips', '3VERY', 'a mente', '01 Agrade', 'Eva Franco', 'Celavi', 'Adelyn Rae', 'Day G', '7th Ray']
    choiceVendor = random.choice(vendorName)

    # CSS Selector로 placeholder를 통해 요소를 찾아냄
    driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Search vendor name']").send_keys(choiceVendor)
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
        msgbox.showerror("Error", "벤더 검색에 실패했습니다.")
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
    
    # 키워드 검색 후 검색 필드 닫기
    backbtn = driver.find_element(By.ID, "backBtn")
    backbtn.click()
    driver.implicitly_wait(3)
    time.sleep(3)

    # 채팅방 나가기
    leave = driver.find_element(By.CLASS_NAME, "btn-menu.hide-text") # 클래스 네임으로 찾을 때, 공백은 "."으로 매꿔야 함
    driver.implicitly_wait(3) 
    leave.click()
    driver.implicitly_wait(3)
    leave_room = driver.find_element(By.ID, "leave")
    driver.implicitly_wait(3)
    leave_room.click()
    driver.implicitly_wait(3)

    # 채팅방 나가면 미세한 딜레이가 있어서 여유 시간 추가
    time.sleep(5)

    # 새 창으로 열린 챗 페이지 닫고 기존 페이지로 다시 스위칭
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(3)

    time.sleep(3)

    # 브라우저 종료
    driver.quit()