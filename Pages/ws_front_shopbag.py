import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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




    # 메인 홈에서 검색 필드에 랜덤 벤더 입력
    vendorName = ['allium', 'zenana', '7th Ray']
    vendorChoice = random.choice(vendorName)

    try:
        driver.find_element(By.CLASS_NAME, "search-input").click()
        driver.implicitly_wait(3)
        pyautogui.typewrite(vendorChoice, interval=0.1)
        driver.implicitly_wait(3)
        driver.find_element(By.CLASS_NAME, "btn-search").click()
        driver.implicitly_wait(10)
    except:
        pyautogui.alert("Error : Vendor search failed")
        print("Error : Vendor search failed")
        driver.quit()

     
    # 가장 맨 앞 부터 3번째 아이템까지 순차적으로 쇼핑백에 추가   
    for item_number in range(1, 4):
        item_path = "//*[@id='item-found']/div[1]/ul/li[{}]".format(item_number)
        driver.find_element(By.XPATH, item_path).click()
        driver.implicitly_wait(10)
        # QTY 입력
        try:
            nqty = driver.find_element(By.ID, "lb_qty")
            # QTY입력 칸에 값이 있다면 지우고 수량 1 입력, 없다면 그냥 1 입력
            if nqty.is_enabled():
                nqty.clear()
                nqty.send_keys("1")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, 600)")
                driver.implicitly_wait(3)
            else:
                nqty.send_keys("1")
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, 600)")
                driver.implicitly_wait(3)
        except:
            pyautogui.alert("Error : Qty input not found")
            print("Error : Qty input not found")
            driver.quit()

        # Add To Shopping Bag 버튼 클릭
        try:
            driver.find_element(By.CSS_SELECTOR, "#content > div > div.pdt_wrap.renewal_premium > div.pdt_detail > div.btn_group > span").click()
            driver.implicitly_wait(10)
            time.sleep(3)
        except:
            pyautogui.alert("Error : Add to shoppingbag button not found")
            print("Error : Add to shoppingbag button not found")
        # 쇼핑백 아이콘에 표시되는 숫자 뱃지 크롤링
        shopbagNumber_xpath = driver.find_element(By.XPATH, "//*[@id='miniCount']/em")
        shopbagNumber = shopbagNumber_xpath.text
        print("Shopping Cart badge : " + shopbagNumber)

        # 원래 쇼핑백이 비어있는 상태에서, 쇼핑백 아이콘에 표시되는 넘버 뱃지가 1보다 크거나 같은 경우 추가된 것 확인
        if int(shopbagNumber) >= 1: # shopbagNumber는 1이라는 텍스트를 추출하였기 때문에, int형 변환을 해주어야 관계연산자가 성립된다.
            print("Success message : product added to shppoingbag")
            driver.back()
            driver.implicitly_wait(10)
            time.sleep(1)
        # 원래 쇼핑백이 비어있는 상태에서, 쇼핑백 아이콘에 표시되는 숫자가 1이 아니라면 추가되지 않은 것으로 판단
        else:
            pyautogui.alert("Error : product not added to shoppingbag")
            print("Error : product not added to shoppingbag")
            driver.quit()
    
    # 브라우저 새로고침
    driver.refresh()
    driver.implicitly_wait(10)
    time.sleep(1)
    
    # 쇼핑백 아이콘에 마우스 Hover 액션
    shoppingbag_icon = driver.find_element(By.XPATH, "//*[@id='miniCount']")
    ActionChains(driver).move_to_element(shoppingbag_icon).perform()
    time.sleep(1)
    # 쇼핑백 페이지로 이동
    shoppingbag_icon.click()
    driver.implicitly_wait(10)
    time.sleep(1)

    # 총 주문금액 데이터 크롤링
    totalAmount_classname = driver.find_element(By.CLASS_NAME, 'totalCheckoutAmount')
    totalAmount = totalAmount_classname.text
    print("Total Amount : " + totalAmount)

    # 쇼핑백에 담긴 제품 체크아웃 진행
    checkOutbtn = driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-checkoutAll.nclick')

    if checkOutbtn.is_enabled():
        checkOutbtn.click()
        driver.implicitly_wait(10)
        time.sleep(1)
    else:
        driver.find_element(By.CLASS_NAME, 'base-checkbox').click()
        time.sleep(2)
        checkOutbtn.click()
        driver.implicitly_wait(10)
        time.sleep(1)

    # Shipping 단계 - 벤더에게 보낼 note 작성 후 다음 단계
    note_To_vendor = driver.find_element(By.CLASS_NAME, 'noteToVendor')
    ActionChains(driver).move_to_element(note_To_vendor).perform()
    time.sleep(1)
    note_To_vendor.send_keys('Test Automation')
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-goToPayment.nclick').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-goToReview.nclick').click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-checkout.nclick').click()
    time.sleep(7)
    driver.implicitly_wait(15)

