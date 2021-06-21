import time
import pyperclip

from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def delay(sec):
    time.sleep(1 + sec + random() * sec)

def auto_login(driver):
    driver.find_element(By.CSS_SELECTOR, '.dgCUZv').click()
    delay(0)
    print("로그인하는중")
    pyperclip.copy('bosal61')
    text_id = pyperclip.paste()
    driver.find_element(By.CSS_SELECTOR, '#id').send_keys(text_id)
    delay(1)
    pyperclip.copy('ehdgus3357*')
    text_pw = pyperclip.paste()
    driver.find_element(By.CSS_SELECTOR, '#pw').send_keys(text_pw)
    delay(1)
    driver.find_element(By.CSS_SELECTOR, '#btnLogin').click()
    delay(1)
    print("로그인완료")

def auto_review(driver):
    driver.find_element_by_css_selector(' .icon-font.icon-font-chat').click()
    delay(3)
    print("리뷰로이동")
    delay(1)
    driver.switch_to.window(driver.window_handles[1])  # 새로운탭으로 이동하여 제어 미답변클릭
    driver.find_element(By.CSS_SELECTOR, '#review-page > div.radio-group.mx-sm-2.mb-3 > label:nth-child(2)').click()
    print("리뷰쓰기시작")
    delay(1)

def review_text(driver):
    button = driver.find_element(By.CSS_SELECTOR,
                                 '#review-page > div.review-wrap > div > div:nth-child(1) >'
                                 'div.review-info > div.CEOCommentCreator-module__2atd > button')

    while button == button:

        try:
            driver.find_element(By.CSS_SELECTOR,
                                '#review-page > div.review-wrap > div > div:nth-child(1) > div.review-info >'
                                'div.CEOCommentCreator-module__2atd > button').click()
            delay(2)
            driver.find_element(By.CSS_SELECTOR,
                                '#review-page > div.review-wrap > div > div:nth-child(1) > div.review-info >'
                                'div.CEOCommentCreator-module__1BLi > div.textarea-wrap > textarea').send_keys('테스팅중입니다.')

            # driver.find_element(By.CSS_SELECTOR, '.button.small.inGroup').click() 확인 버튼누르면 완료
        except NoSuchElementException as e: # 예외 발생 시 에러 출력 및 계속 진행
            print("[Error발생]", e)
            pass
        except Exception as e: # 예외 발생시 에러출력
            print("[에러 주기값 조정이 필요합니다.]", e.args)

        break



def main():
    driver = webdriver.Chrome()
    driver.get('https://ceo.baemin.com')
    # driver.maximize_window()
    # 창이뜨지않게조절하는 소스넣기
    # 핸들리스 방어소스넣기
    # 사람이움직이는것처럼표현하는 소스넣기 gpu x
    delay(1)
    auto_login(driver)
    delay(1)
    auto_review(driver)
    review_text(driver)
    print("우리 매장의 댓글이 전부 달렸어요~ 사장님은 리뷰읽어만주시고 매장에 신경써주세요~!")
    delay(20)


main()

# Quit 인터페이스 만들기
