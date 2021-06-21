def work(driver) :
    i = 0
    j = 0
    inumber = 0
    jnumber = 0
    while i < 500: #좋아요 100개까지 계속진행
        try:
            while j < 500 :


                hashtag = "좋아요반사"
                driver.get("https://www.instagram.com/explore/tags/" + hashtag)
                delay(4)

                picture = driver.find_elements_by_class_name('_9AhH0')[9]
                picture.click()
                delay(6)

                try:

                    like_btn = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    like_btn.click()
                    delay(5)

                    print(j + 1, '좋아요')
                    j = j + 1
                    jnumber = j + jnumber

                except :
                    delay(10) #예외발생 잠시중지
        except NoSuchElementException as e: #예외 발생 시 에러 출력 및 계속 진행
            print("[Error발생]", e)
            pass
        except Exception as e: #예외 발생시 에러출력
            print("[에러 주기값 조정이 필요합니다.]", e.args)

        print('오늘은 좋아요' , j ,'번을 완료했습니다.')
        i = j
         #inumber = i + inumber
