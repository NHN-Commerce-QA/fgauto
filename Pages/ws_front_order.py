import time
from tkinter import messagebox as msgbox
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

def ws_order():
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



    driver.find_element(By.CLASS_NAME, 'user-avatar').click()
    driver.implicitly_wait(3)
    driver.find_element(By.CLASS_NAME, 'order-history.nclick').click()
    driver.implicitly_wait(10)
    
    time.sleep(3)

    # 첫 번째 오더 히스토리에 대한 정보를 딕셔너리 자료형을 이용해 크롤링
    order_Data = {
        "order_Date" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[1]').text,
        "company" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[2]').text,
        "order_Details" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[3]/a').text,
        "amount" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[5]').text,
        "payment" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[6]').text,
        "order_Status" : driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[7]').text
    } 

    # 주문 날짜, 회사, 디테일 넘버, 금액, 결제 수단 , 오더 상태 등 출력
    print("========================Test Order info========================")
    for key, value in order_Data.items():
        print(key, ":", value)

    time.sleep(1)
    print()

    # Order Details 페이지로 이동
    driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr/td[3]/a').click()
    driver.implicitly_wait(10)
    print("========================Order Details========================")
    print()
    time.sleep(1)

    # 페이지에 표시되는 Order No 정보 일치 확인
    ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[1]/td'))
    print("------------------------Order Number------------------------")
    orderNumber = driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[1]/td').text
    print("Order Number in order details page : " + orderNumber)
    print("Order Number in order history page : " + order_Data["order_Details"])
    if orderNumber == order_Data["order_Details"]:
        print("Successful Message - Order numbers match each other : " + orderNumber + " == " + order_Data["order_Details"])
    else:
        msgbox.showerror("Error Message", "Order numbers do not match each other : " + orderNumber + " ≠ " + order_Data["order_Details"])
        print("Error Message - Order numbers do not match each other : " + orderNumber + " ≠ " + order_Data["order_Details"])
        driver.quit()

    print()
    time.sleep(1)

    # 페이지에 표시되는 Order Date 정보 일치 확인
    ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[3]/td'))
    print("------------------------Order Date------------------------")
    orderDate = driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[3]/td').text
    print("Order Date in order details page : " + orderDate)
    print("Order Date in order history page : " + order_Data["order_Date"])
    if orderDate == order_Data["order_Date"]:
        print("Successful Message - Order Dates match each other : " + orderDate + " == " + order_Data["order_Date"])
    else:
        msgbox.showerror("Error Message", "Order numbers do not match each other : " + orderDate + " ≠ " + order_Data["order_Date"])
        print("Error Message - Order Dates do not match each other : " + orderDate + " ≠ " + order_Data["order_Date"])
        driver.quit()

    print()
    time.sleep(1)

    # 페이지에 표시되는 Order Amount 정보 일치 확인
    ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="div-lst-order"]/div[2]/ul/li[9]/span'))
    print("------------------------Order Amount------------------------")
    orderAmount = driver.find_element(By.XPATH, '//*[@id="div-lst-order"]/div[2]/ul/li[9]/span').text
    print("Order Amount in order details page : " + orderAmount)
    print("Order Amount in order history page : " + order_Data["amount"])
    if orderAmount == order_Data["amount"]:
        print("Successful Message - Order Amounts match do not each other : " + orderAmount + " == " + order_Data["amount"])
    else:
        msgbox.showerror("Error Message", "Order amounts do not match each other : " + orderAmount + " ≠ " + order_Data["amount"])
        print("Error Message - Order amounts do not match each other : " + orderAmount + " ≠ " + order_Data["amount"])
        driver.quit()
    
    print()
    time.sleep(1)

    # 페이지에 표시되는 Order Note 정보 일치 확인 (이전 주문 처리 자동화 코드에서 입력한 데이터가 표시되어야 함)
    ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[7]/p'))
    print("------------------------Order Note------------------------")
    orderNote = driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[7]/p').text
    print("Order Note in order details page : " + orderNote)
    print("Text entered during order processing : " + "Test Automation")
    if orderNote == 'Test Automation':
        print("Successful Message - Order Note match do not each other : " + orderNote + " == " + "Test Automation")
    else:
        msgbox.showerror("Error Message", "Order notes do not match each other : " + orderNote + " ≠ " + "Test Automation")
        print("Error Message - Order notes do not match each other : " + orderNote + " ≠ " + "Test Automation")
        driver.quit()
    
    print()
    time.sleep(2)

    # 오더 캔슬 버튼 클릭
    # 오더 캔슬 버튼이 노출될 때 클릭
    try:
        if driver.find_element(By.CSS_SELECTOR, '#order-detail-id > div.btn-row--ar.margin-top-m > button.btn.btn_b_red.jsCancelOrder').is_displayed():
            driver.find_element(By.CSS_SELECTOR, '#order-detail-id > div.btn-row--ar.margin-top-m > button.btn.btn_b_red.jsCancelOrder').click()
            time.sleep(2)
            # 주문 취소 진행
            if driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[1]/input').is_displayed():
                driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[1]/input').click()
                time.sleep(2)
            # 주문 취소 진행 액션
            print("------------------------Order Cancel------------------------")
            cancelSuccess_alert = driver.find_element(By.CLASS_NAME, 'middle-column-msg-content-text') # 주문 취소 성공 alert
            if cancelSuccess_alert.is_displayed():
                print("Success - The order has been cancelled")
            else:
                msgbox.showerror("Error", "The order has been not cancelled")
                print("Fail - The order has been not cancelled")
        else:
            time.sleep(1)
    except NoSuchElementException:
        time.sleep(1)
    
    # Re-order 진행
    reOrder_element = driver.find_element(By.ID, 'btn-reorder') #re-order 버튼

    # re-order 버튼 2회 클릭
    for i in range(2): # for문에 들어가는 변수를 reOrder_element로 하면 반복문이 제대로 동작하지 않아서 별도의 변수 i를 선언해야 한다.
        reOrder_element.click()
        time.sleep(2)
    
    print()

    print("------------------------Re Order------------------------")
    time.sleep(2)
    
    try:
        if driver.find_element(By.CLASS_NAME, 'middle-column-msg-content-text').is_displayed():
            print("Success - All Reorder Items has been added!")
    except NoSuchElementException:
        driver.refresh()
        driver.implicitly_wait(10)

    time.sleep(3)
    
    shopbadge_number = driver.find_element(By.XPATH, '//*[@id="miniCount"]/em').text
    print("shopping bag : " + shopbadge_number)
    if int(shopbadge_number) == 1:
        print("Success - All Reorder Items has been added!")

    time.sleep(3)

    # 쇼핑백 아이콘에 마우스 Hover 액션
    shoppingbag_icon = driver.find_element(By.XPATH, "//*[@id='miniCount']")
    ActionChains(driver).move_to_element(shoppingbag_icon).perform()
    time.sleep(1)

    # 쇼핑백 페이지로 이동
    shoppingbag_icon.click()
    driver.implicitly_wait(10)
    time.sleep(1)

    # reorder로 주문한 제품 쇼핑백에 추가된 것 확인
    reorder_vendor = driver.find_element(By.CLASS_NAME, 'companyName.nclick').text
    if reorder_vendor == order_Data['company']: 
        print("Check vendor name match : " + reorder_vendor + " == " + order_Data['company'])
    else:
        msgbox.showerror("Fail", "The vendor name of order details is not the same.")
        print("Fail : The vendor name of order details is not the same.")
        driver.quit()

    time.sleep(2)
    print()

    # reorder로 주문한 제품 쇼핑백에서 제거
    driver.find_element(By.CLASS_NAME, 'link-fun.btn-removeVendor').click()
    time.sleep(0.2)
    driver.find_element(By.CLASS_NAME, 'btn-sure').click()
    print("------------------------Remove Cart------------------------")
    print("Success - Removed Cart item")
    driver.implicitly_wait(10)
    time.sleep(3)

    