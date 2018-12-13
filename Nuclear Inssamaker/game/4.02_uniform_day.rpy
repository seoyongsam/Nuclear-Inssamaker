#이미지 선언
image gyobok = "uniform_day/gyobok.jpg"
image jjangge = "uniform_day/jjangge.jpg"
image pizza = "uniform_day/pizza.jpg"

# 4월 2일 월요일 교복데이 이벤트
# month4 week1 day 1
label uniform_day:
    "어제는 만우절이었다. 그런데 일요일이었어서 오늘 과 동기들이 다같이 교복을 입고 등교를 했다."
    "과 동기들이 만우절 기념으로 점심식사를 함께 야외에서 배달음식을 먹자고 한다."
    "하지만 약속한 시간에 수업이 있다. 어떻게 할까?"

    menu:
        "수업을 째고 동기들과 점심을 먹으러 간다":
            #hp & 공부 파라미터-, 과 파라미터 up, 개별 캐릭터와 파라미터는 변함이 없고 과 친밀도가 올라감
            $ hp -= 20
            $ study_parameter -= 10
            $ gwa_parameter += 10
            call parameter_maxmin_check

            "수업을 째고 동기들이랑 점심을 먹으러 캠퍼스 안에 있는 잔디밭에 갔다."
            show gyobok at truecenter

            Hyunjae "얘들아 오늘 점심으로 뭐먹을까??"
            Daehyun "야외에서 시켜먹을 때는 중식이지!"
            Samyong "중식? 그럼 우리 꿔바로우 하나 시키자!"
            Daehyun "ㅋㅋㅋ 우리가 말하는 중식은 짜장면, 짬뽕 말하는거야"
            Samyong "나 한국와서 짜장면, 짬뽕 한번도 안먹어 봤어! 그거 먹자 ㅎㅎㅎ"
            Jinil "야 무슨소리야 밖에 나왔으면 들고 다니면서 먹을 수 있는 피자 먹어야지"
            Hyunjae "오 피자 맛있겠다... 난 피자에 한표."
            Mirae "나도 피자!!!"
            Jangjung "아... 난 짬뽕 먹을래... "

            "친구들이 점심 메뉴를 두고 의견이 갈리고 있다."

            Hyunjae "지금 중식 아니면 피자 둘 중에 의견이 반반 갈리는데 어떡하지?"

            Jinil "뻔대가 남아있잖아. 넌 뭐먹을래? 너가 고르는 걸로 결정되겠다."


            menu:
                "짜장면, 짬뽕":
                    #장중이 + 삼용 파라미터 +
                    $ jangjung.parameter += 20
                    $ samyong.parameter += 20

                    show jjangge at truecenter
                    "중국집에서 음식을 시켰다."
                    "서비스로 탕수육과 군만두도 같이 와서 다양한 음식을 먹을 수 있었다."
                    "장중이는 어제 술을 마셨는지 짬뽕으로 해장을 하는 것 같다."
                    "삼용이도 오랜만에 중국 음식을 먹어서 그런지 기분이 좋은것 같다."
                    "아, 짜장면은 중국음식이 아니었나?"

                "피자":
                    #진일이 파라미터 ++
                    $ jinil.parameter += 40

                    show pizza at truecenter
                    "피자를 시켰다."
                    "여러 종류의 피자를 시켜 먹어서 다양하게 먹을 수 있었다."
                    "진일이는 앞으로 착하게 살기로 한다며 피자를 종류별로 1개씩만 먹는다고 한다."
                    "참고로 피자 종류는 5가지지만 한명당 3조각만 먹을수 있다."
                    "현재가 미래에게 피자를 먹여주는게 보인다. 이래서 피자를 시키자고 한건가? 눈에 습기가 찬다."

        "수업을 듣는다":
            return

    return
