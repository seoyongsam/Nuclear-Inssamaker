image friend_2 = "fun_mt/friend_2.jpg"
image friend_3 = "fun_mt/friend_3.jpg"
image friend_4 = "fun_mt/friend_4.jpg"
image friend_5 = "fun_mt/friend_5.jpg"

label friend_2:
    "삼용이와 술을 마시기로 결정했다."

    scene friend_2 at truecenter
    "삼용" "오오~ 고생한 우리뻔대! 술이라도 한 잔 받어~"
    "주인공" "ㅎㅎㅎ 고마워! 너도 많이 고생했으니 너도 한 잔 받아"
    "주인공" "후 그래도 걱정 나름 많았는데, 다들 뻔엠 즐기고 있는 것 같아서 다행이다.."
    "삼용" "뭐 전부 너가 뒤에서 열심히 해서 그런거 아닐까"
    "삼용" "진짜 고생 많았어!!"
    "주인공" "에이 나 혼자만 한 건 아니지..너나 장중이나 진일이처럼 꾸준히 도와준 애들이 있어서 그랬던 거니까.."
    "주인공" "진짜 너희한테는 고마움 밖에 없다.."
    "주인공" "앞으로도 잘 부탁해!"
    "삼용" "ㅋㅋㅋ그래 언제든 맡겨만 줘"
    "삼용" "열심히 도와줄게~"

    scene black
    "삼용이와 얘기를 하며 소주 1병 정도를 더 비웠다."

    #삼용이와 파라미터 +
    return

label friend_3:
    "장중이와 술을 마시기로 결정했다."

    scene friend_3 at truecenter
    "장중" "예에 문정과에서 제일 고생하는 뻔대~ 술 한 잔 해야지!"
    "장중" "넌 진짜 나 없었으면 어쩔 뻔 했냐? ㅋㅋㅋ"
    "주인공" "ㅋㅋㅋ 진짜로 맞는 말이다"
    "주인공" "너 처럼 과에 일 있을 때마다 도와주는 애들 있어서 힘낼 수 있는 듯"
    "장중" "에이 과찬이야~ 일단 짠하자 짠!"
    "주인공" "짠!"
    "장중" "캬~ 오늘 따라 술이 다네"
    "주인공" "진짜 달다! 재밌어서 그런가 봐"
    "장중" "ㅋㅋㅋㅋ 맞음 맞음 더 마시자, 짠!"
    "주인공" "짠!"

    scene black
    "장중이와 이야기를 하며 소주 1병 정도를 더 비웠다."

    #장중이와 파라미터 +
    return

label friend_4:
    "진일이를 찾으러 나가기로 결정했다."
    "다행히 진일이는 숙소 바로 앞에 있었다."

    scene friend_4 at truecenter
    "주인공" "야 김진일! 또 사라져서 깜짝 놀랐잖아!"
    "진일" "아 뻔대냐? 아 그냥 바람 좀 쐬러 나왔지."
    "주인공" "어디 딴 데 가지말고 이 주변에만 있어랔ㅋㅋㅋ"
    "진일" "에이 이제 딴 데 안가지. 나온 김에 나랑도 한 잔 마셔야지, 잔 들고 와라"
    "주인공" "엌ㅋㅋㅋ 그 소주는 어디서 나온거냐. 잠시만 기다려봐"
    "진일" "아 아니다 여기 잔 많이 남아있네, 여기서 마시자, 자 잔 드시고~"
    "주인공" "엌ㅋㅋ 감사 감사~"
    "진일" "크~ 술 맛 좋다~ 뻔엠 준비하느라 고생많았다 뻔대야. 학기 초에 행사 많아서 바빴을텐데 항상 열심히 하더라."
    "주인공" "아냐 너 없었으면 진짜 힘들었을 걸...애들도 투표 잘 안하고..."
    "진일" "크 그래그래 너도 이 형님이 고생하는 거 아네, 일단 한 잔 더 짠!"
    "주인공" "엌ㅋㅋㅋㅋㅋ"
    "진일" "뭐 앞으로도 과에 일 생기거나 하면 편하게 말해. 계속 도와줄거니까."
    "주인공" "크~ 앞으로는 갓 진일이라고 부를게. 잘 부탁함!"
    "진일" "그래그래."

    scene black
    "진일이와 말을 주고 받으면서 소주 1병 정도를 더 비웠다."
    #진일이와 파라미터 +
    return

label friend_5:
    "장중, 진일, 용삼의 술자리에 합류하기로 결정했다."
    "...뭔가 땅이 흔들리는 것 같다."

    scene friend_5 at truecenter
    "주인공" "으어..얘들아 여기서 뭐하고 있었냐..."
    "장중" "엌ㅋㅋㅋㅋㅋㅋ 이 친구 많이 취했네, 야 괜찮냐?"
    "주인공" "어...아마도 괜찮은듯??"
    "진일" "아니 전혀 안 괜찮아 보이는데, 아 뻔대 많이 약하네;;"
    "삼용" "조절해 가면서 마셔야지.."
    "주인공" "앗! 누가 술을 남기냐~ 내가 마셔야지?"
    "장중" "엇"
    "진일" "하..."
    "주인공" "크으~ 맛있다!!"
    "삼용" "어휴..뭐 이런 거 하루이틀 보는 것도 아니고 적당히 마셔주자"
    "장중" "오키오키"
    "진일" "뭐 애들도 거의 자러 간 거 같고, 뻔대는 우리가 챙겨야지"
    "주인공" "...웁!"
    "장중" "야야야!!! 여기서 토하면 안 됨!!!"
    "삼용" "화장실! 화장실!!"
    "진일" "하...."

    scene black
    "애들이 내 몸을 씻겨주는 것 같다...이후 정신을 잃었다."
    #개별 파라미터 변화 없음
    $rest_point -= 1
    return