﻿# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#start 함수에서 넘어옴
label sunday_room:
    scene sunday_room_image at truecenter

    # sunday_room_screen에 있는 핸드폰, 플래너 아이콘을 보여주는 스크린
    show screen phone_icon
    show screen planner_icon

    "일요일이 되었습니다.\n"
    extend "핸드폰을 이용해 SNS를 확인하거나,\n"
    extend "플래너를 이용해 다음주 일정을 짜세요."
    call hide_dialouge_box

    return

label planner:
    # 일요일 화면의 핸드폰, 플래너 아이콘 숨기기
    hide screen phone_icon
    hide screen planner_icon

    # 플래너 배경 ON
    show planner_background
    show planner_schedule_list

    # 형광색 하이라이트 창
    show screen schedule_highlight

    # 스케줄러 속 월화수목금토 '공부'~'휴식' 아이콘 띄우기
    show screen schedule_icon_show
    # 그 위에 투명한 수정 버튼
    show screen schedule_revise_button

    # 오른쪽 스케줄 창
    show screen schedule_button

    if day < 7 :
        "[day]일차 일정을 선택하세요."
        window hide
        pause

    # 뒤로가기 버튼을 눌러 for_day_schedule_select가 5가 되었을 시
    # 플래너 버튼을 숨기고 일요일로 간다.
    if for_day_schedule_select == 5:
        call hide_planner_button
        $ for_day_schedule_select = 0
        jump sunday_room

    $ day_schedule[day] = for_day_schedule_select
    $ for_day_schedule_select = 0

    # day_schedule[day]가 선택되어 있다면,day를 늘려 다음 날로 넘어간다.
    while day_schedule[day] != 0:
#    if for_day_schedule_select != 0:
        if day <= 6:
            $ day += 1

    # 토요일까지 선택을 완료하고 day가 7이 되면,
    if day == 7:
        hide screen schedule_highlight
        "일주일 일정을 실행하시겠습니까?"
        menu:
            "실행한다":
                jump weekday_run
            "수정한다":
                $ day = 1
                while day_schedule[day] != 0:
                #    if for_day_schedule_select != 0:
                    if day <= 6:
                        $ day += 1
                window hide
                pause

    jump planner

    return

label hide_planner_button :
    hide planner_background

    hide screen schedule_button
    hide screen schedule_highlight

    hide screen schedule_icon_show

    return

label button_reset(number) :
    if day_schedule[number] != 0:
        $ day_schedule[number] = 0
        $ day = number
#    while day_schedule[day]
#    if day_schedule[day] != 0
#        $ day += 1
    return

label phone:
    hide screen phone_icon
    hide screen planner_icon
    "핸드폰 화면이 구현되지 않았습니다."
    "일요일 화면으로 돌아갑니다"

    jump sunday_room
    return
