﻿# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_run:
    $ i = 0
    while i < 6:
        $ tmp_2 = i + 1
        "[tmp_2]일차 일정은\n"
        if day_schedule[i] == 1:
            extend "공부했다"
        elif day_schedule[i] == 2:
            extend "동아리 연습했다"
        elif day_schedule[i] == 3:
            extend "과활동했다"
        elif day_schedule[i] == 4:
            extend "휴식했다"
        else :
            extend "에러"
        $ i += 1

    "일요일 화면으로 돌아갑니다."
    call weekday_schedule_reset
    jump go_sunday_room
    return

label weekday_schedule_reset:
    $ i = 0
    while i < 6:
        $ day_schedule[i] = 0
        $ i += 1

    $ day = 1
    return