import time
from tkinter import messagebox as msgbox
import random
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def ws_consolidate_order():
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
    try:
        if driver.find_element(By.XPATH, '//*[@id="home-deals-open-popup"]/div/div[3]/div/div/label').is_displayed():
            driver.find_element(By.XPATH, '//*[@id="home-deals-open-popup"]/div/div[3]/div/div/label').click()
            time.sleep(1)
        else:
            time.sleep(1)
    except NoSuchElementException:
        time.sleep(1)

    print()

    # 검색 창에 첫 번째 consolidate 벤더 네임 입력
    driver.find_element(By.CLASS_NAME, "search-input").send_keys("Allium")
    driver.find_element(By.CLASS_NAME, "btn-search").click()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//*[@id='item-found']/div[1]/ul/li[1]").click()
    driver.implicitly_wait(10)
    
    # consolidate vendor인지 체크
    print("========================Consolidate Vendor========================")
    if driver.find_element(By.CLASS_NAME, "tooltip.mrg_ship").is_displayed():
        print("consolidate vendor : " + driver.find_element(By.CSS_SELECTOR, "[data-nclick-name='item.detail.vlink']").text)

    nqty1 = driver.find_element(By.CLASS_NAME, "nQty")

    time.sleep(3)

    # 제품 쇼핑백에 추가하는 과정
    try:
        if nqty1.is_enabled():
            nqty1.clear()
            nqty1.send_keys("1")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 600)")
            driver.implicitly_wait(3)
            driver.find_element(By.CLASS_NAME, "btn.btn_black_v01.addCart.nclick").click()
            time.sleep(2)
            
            if driver.find_element(By.ID, "message-container-addtoCart").is_displayed():
                print("Successfully added to cart")
                time.sleep(3)
       
        else:
            nqty1.send_keys("1")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 600)")
            driver.implicitly_wait(3)
            driver.find_element(By.CLASS_NAME, "btn.btn_black_v01.addCart.nclick").click()
            time.sleep(2)

            if driver.find_element(By.ID, "message-container-addtoCart").is_displayed():
                print("Successfully added to cart")
                time.sleep(3)

    except NoSuchElementException:
        msgbox.showerror("Error", "카트에 제품을 추가하지 못했습니다.")
        print("Error : Failed to add product to cart")

    # 검색 창에 두 번째 consolidate 벤더 네임 입력
    driver.find_element(By.CLASS_NAME, "search-input").send_keys("Love sense")
    driver.find_element(By.CLASS_NAME, "btn-search").click()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//*[@id='item-found']/div[1]/ul/li[1]").click()
    driver.implicitly_wait(10)

    # consolidate vendor인지 체크
    if driver.find_element(By.CLASS_NAME, "tooltip.mrg_ship").is_displayed():
        print("consolidate vendor : " + driver.find_element(By.CSS_SELECTOR, "[data-nclick-name='item.detail.vlink']").text)

    nqty2 = driver.find_element(By.CLASS_NAME, "nQty")

    time.sleep(3)

    # 제품 쇼핑백에 추가하는 과정
    try:
        if nqty2.is_enabled():
            nqty2.clear()
            nqty2.send_keys("1")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 600)")
            driver.implicitly_wait(3)
            driver.find_element(By.CLASS_NAME, "btn.btn_black_v01.addCart.nclick").click()
            time.sleep(2)
            
            if driver.find_element(By.ID, "message-container-addtoCart").is_displayed():
                print("Successfully added to cart")
                time.sleep(3)

        else:
            nqty2.send_keys("1")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 600)")
            driver.implicitly_wait(3)
            driver.find_element(By.CLASS_NAME, "btn.btn_black_v01.addCart.nclick").click()
            time.sleep(2)

            if driver.find_element(By.ID, "message-container-addtoCart").is_displayed():
                print("Successfully added to cart")
                time.sleep(3)

    except NoSuchElementException:
        msgbox.showerror("Error", "카트에 제품을 추가하지 못했습니다.")
        print("Error : Failed to add product to cart")

    time.sleep(2)
    
    print()
    print("========================Shopping Bag Page========================")

    # 쇼핑백 아이콘에 표시되는 뱃지 넘버 크롤링, 2로 표시되는 지 체크
    shopbagNumber_xpath = driver.find_element(By.XPATH, "//*[@id='miniCount']/em")
    shopbagNumber = shopbagNumber_xpath.text
    print("Shopping Cart badge : " + shopbagNumber)

    # 쇼핑백 아이콘에 표시되는 뱃지 넘버가 2보다 크거나 같으면 쇼핑백 페이지로 이동
    if int(shopbagNumber) >= 2:
        print("Successfully : There are products from two vendors in the shopping bag.")
        driver.find_element(By.CLASS_NAME, "nomulticlick").click()
        driver.implicitly_wait(10)
        time.sleep(1)
        
    else:
        msgbox.showerror("Error", "쇼핑백에 2개 벤더의 제품이 담기지 않았습니다.")
        print("Error : The shopping bag did not contain products from 2 vendors.")

    driver.find_element(By.CSS_SELECTOR, "[data-nclick-name='cart.summary.checkoutall']").click()
    driver.implicitly_wait(10)

    # consolidate shipping 라디오 버튼이 활성화 되어있으면 체크

    radio1 = driver.find_element(By.XPATH, "//*[@id='content']/main/div[1]/div[1]/div[2]/div[2]/div[1]/ul/li[1]/div[1]/label[1]")
    radio2 = driver.find_element(By.XPATH, "//*[@id='content']/main/div[1]/div[1]/div[2]/div[3]/div[1]/ul/li[1]/div[1]/label[1]")
    noteToVendor1 = driver.find_element(By.XPATH, "//*[@id='content']/main/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/textarea")
    noteToVendor2 = driver.find_element(By.XPATH, "//*[@id='content']/main/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/textarea")

    if radio1.is_enabled() and radio2.is_enabled():

        for radio in range(2,4):
            radio_xpath = "//*[@id='content']/main/div[1]/div[1]/div[2]/div[{}]/div[1]/ul/li[1]/div[1]/label[1]".format(radio)
            driver.find_element(By.XPATH, radio_xpath).click()
            time.sleep(1)

        noteToVendor1.send_keys("consolidate vendor 1")
        time.sleep(1)
        noteToVendor2.send_keys("consolidate vendor 2")
        time.sleep(1)

        # consolidation 주문 정보 크롤링
        for info in range(1,3):
            shipping_cost_xpath = "//*[@id='content']/main/div[2]/div/div[3]/div/ul/li[{}]/dl[3]/dd".format(info)
            vendorname_xpath = "//*[@id='content']/main/div[2]/div/div[3]/div/ul/li[{}]/dl[1]/dt".format(info)
            amount_xpath = "//*[@id='content']/main/div[2]/div/div[3]/div/ul/li[{}]/dl[1]/dd".format(info)
            shipping_cost = driver.find_element(By.XPATH, shipping_cost_xpath).text
            vendor_name = driver.find_element(By.XPATH, vendorname_xpath).text
            amount = driver.find_element(By.XPATH, amount_xpath).text
            print("┌{}. Vendor Shipping Cost : ".format(info) + shipping_cost)
            print("│{}. Vendor Name : ".format(info) + vendor_name)
            print("└{}. Vendor Amount : ".format(info) + amount)
            time.sleep(1)

    else:
        msgbox.showerror("Error", "cosnolidate shipping 라디오 버튼이 활성화 되어 있지 않습니다.")
        print("Error : consolidate shipping radio button does not enabled")

    # 주문 과정
    driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-goToPayment.nclick').click()
    time.sleep(2)
    button = driver.find_element(By.XPATH, '//*[@id="content"]/main/div[2]/div/div[1]/button[2]')
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn-dark_grey.btn-checkout.nclick').click()
    driver.implicitly_wait(10)
    time.sleep(5)

    # consolidation 주문 취소 진행
    driver.find_element(By.CLASS_NAME, 'user-avatar').click()
    driver.implicitly_wait(3)
    driver.find_element(By.CLASS_NAME, 'order-history.nclick').click()
    driver.implicitly_wait(10)
    
    time.sleep(5)

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
    # ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[1]/td'))
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
    # ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="order-detail-id"]/div[2]/div[2]/table/tbody/tr[3]/td'))
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
    # ActionChains(driver).double_click(driver.find_element(By.XPATH, '//*[@id="div-lst-order"]/div[2]/ul/li[9]/span'))
    print("------------------------Order Amount------------------------")
    orderAmount = driver.find_element(By.CSS_SELECTOR, '#div-lst-order > div.price_info > ul > li.total > span').text
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

    driver.back()
    driver.implicitly_wait(10)

    time.sleep(3)

    # 두 번째 consolidation Order Details 페이지로 이동
    driver.find_element(By.XPATH, '//*[@id="tab-order-history"]/div[3]/table/tbody/tr[2]/td[3]/a').click()
    driver.implicitly_wait(10)
    print()
    time.sleep(1)

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

    