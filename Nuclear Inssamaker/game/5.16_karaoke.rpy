image school2 = "karaoke/school.jpg"
image karaoke = "karaoke/karaoke.jpg"
image score_30 = "karaoke/score_30.jpg"
image score_83 = "karaoke/score_83.jpg"
image score_95 = "karaoke/score_95.jpg"
image score_100 = "karaoke/score_100.jpg"
image wild_flower = "karaoke/wild_flower.jpeg"
image are_you_happy = "karaoke/are_you_happy.jpg"
image sicha = "karaoke/sicha.jpg"
image kasi = "karaoke/kasi.jpg"

# 노래방 5월 16일 월요일 month == 5 and week == 3 and day == 1 저녁
label karaoke:
    show school2 at truecenter
    "주인공" "우리 오늘 공부도 안되는데 코노고?\n"
    "동삼용" "좋은데? 오랜만에 첨밀밀 한 번 불러봐야지\n"
    "김진일" "오... 나도 껴줘!"
    "유현재" "녹두 ㄱㄱ"

    show karaoke at truecenter
    "노래방 기계" "박효신 야생화 예약하셨습니다.\n"
    "친구들" "오오... 누구냐?\n"
    "주인공" "흠흠... 목 좀 풀어볼까?"
    "친구들" "노래방 점수로 밥 내기!"

    show wild_flower at truecenter
    "주인공" "나 피우리라.... 라.... 라..."

    show score_83 at truecenter
    "친구들" "이거 뭐냐 ㅋㅋㅋㅋㅋ"
    "주인공" "코노비 확정이네... 하..."
    "김진일" "다음에 나다!"
    "친구들" "오 뭔데뭔데"

    show are_you_happy at truecenter
    "김진일" "좋니 사랑해서~ 사랑을 시작할 떄~\n"
    extend "네가~ 얼.. (쿨럭) 마 ㄴr... 예쁜지 모르찌이이이~"
    "친구들" "ㅋㅋㅋㅋ 김진일 목 나갔다 ㅋㅋㅋㅋㅋ"

    show score_30 at truecenter
    "친구들" "ㅋㅋㅋㅋㅋㅋ 이게 뭐냐\n"
    extend "너 코노비 확정이다"
    "김진일" "와... 기계가 이상한 것 같은데"

    show sicha at truecenter
    "유현재" "Love & Peace"
    "친구들" "욜~ 힙찔이네"
    "유현재" "mic check 1,2... 1,2...\n"
    extend "그뤠이~\n"
    extend "밤새 모니터에 흐른 침이 마르기도 전에..."

    show score_95 at truecenter
    "유현재" "봤냐? 힙알못들아\n"
    extend "코노비 낼 준비나 해라"
    "동삼용" "노래가 뭔지 보여준다 기다려봐"

    show kasi at truecenter
    "동삼용" "제발 가라고~ 아주 가라고~ 했어도 나를 괴롭히는데에에~"
    "친구들" "오~~ 동삼용~~!!"

    show score_100 at truecenter
    "동삼용" "(거만한 표정)\n"
    extend "뭐 이 정도 ㅎ"
    "친구들" "어우 재수없어...\n"
    extend "벌써 세 시간이나 했네 ㅋㅋㅋ\n"
    extend "진일아 네가 코노비 해결해. 우리 먼저 나가있을게 ㅋㅋㅋㅋ"
    "김진일" "와... 진짜 그냥 간다고???"
    "친구들" "노래 못하면 조용히 하자"
    "김진일" "야 기계가 이상한거야"
    "친구들" "네 다음 음치"

    return