#이미지 선언
# image studentcenter = "club_first/studentcenter.jpg"
image prac = "club_first/1.png"
image clubroom = "club_first/clubroom.jpg"

# 3월 12일 저녁 동아리 첫 연습
# month1 week2 day4
label club_first :
    scene black
    "오늘은 동아리 첫 연습이 있는 날이다. 수업을 마친 동아와 만나 동아리 연습실로 찾아가게 되었다."

    show clubroom at truecenter
    "동아와 동아리 연습실에 들어갔다. 먼저 와 있는 선배들이 악기를 만지고 있는 모습이 보였다."

    "동아리 선배" "오~ 새내기들 오셨네요!! 반가워요!"
    Player "안녕하세요! 문정과 19학번 주인공입니다! 잘 부탁드려요!"
    Dongah "안녕하세요! 소비자아동학과 19학번 이동아입니다! 잘부탁드립니다!"
    "동아리 선배들" "와아~!"
    Player "앗 넵 좋아요!"
    "동아리 선배" "노래 한번 해볼까요??"
    
    show prac at truecenter
    "동아리원들과 즐겁게 합주를 하였다!"

    scene black

    return