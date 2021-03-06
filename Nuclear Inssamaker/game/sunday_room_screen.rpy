image planner_background = "planner_background.png"
image planner_schedule_list = "planner_schedule_list.png"
#image highlight = im.Scale("highlight.png",100,100)
image highlight = "highlight.png"

image sel_study = "sel_study.png"
image sel_club = "sel_club.png"
image sel_gwa = "sel_gwa.png"
image sel_rest = "sel_rest.png"

## 일요일 방에서 핸드폰 아이콘
screen phone_icon():
    vbox :
        xalign 0.34 yalign 0.7
        imagebutton:
            idle "phone_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("phone_icon.png",2)
            # 클릭시 phone label을 실행함
            action Jump("phone")

## 일요일 방에서 플래너 아이콘
screen planner_icon():
    vbox xalign 0.64 yalign 0.7 :
        imagebutton:
            idle "planner_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover im.Alpha("planner_icon.png",2)
            # 클릭시 planner label을 실행함
            action Jump("planner")

## 스케줄러에서 선택화면이 나타나는 노란색 테두리 하이라이트 화면
screen schedule_highlight():
    if day < 7:
        vbox:
            xpos (32 + 128*(day-1)) ypos 180
            add "highlight"

## 플래너를 눌렀을 때 나오는 일정짜기 버튼
screen schedule_button():
    ## 일단 여기다가 background 때려 박았음"
    add "hp_background.png"
    add "mental_background.png"
    add "to_do_list.png"
    ##

    frame:
        xpos 986 ypos 450
        xsize 260
        vbox:
            spacing 10
            xalign 0.5

            textbutton "공부하기":
                action SetVariable("for_day_schedule_select", 1)

            textbutton "동아리":
                action SetVariable("for_day_schedule_select", 2)
#                action Notify("동아리 활동했다")

            textbutton "과활동":
                action SetVariable("for_day_schedule_select", 3)
#                action Notify("과활동했다")

            textbutton "휴식":
                action SetVariable("for_day_schedule_select", 4)
#                action Notify("쉬었다")

            textbutton "뒤로가기":
#               $ for_day_schedule_select = 5
                action SetVariable("for_day_schedule_select", 5)
                #text_align 0.5

screen schedule_icon_show():
    # 월요일
    if day_schedule[1] != 0:
        hbox:
            xpos 32 ypos 180
            if day_schedule[1] == 1:
                add "sel_study"

            elif day_schedule[1] == 2:
                add "sel_club"

            elif day_schedule[1] == 3:
                add "sel_gwa"

            elif day_schedule[1] == 4:
                add "sel_rest"

    # 화요일
    if day_schedule[2] != 0:
        hbox:
            xpos 160 ypos 180
            if day_schedule[2] == 1:
                add "sel_study"

            elif day_schedule[2] == 2:
                add "sel_club"

            elif day_schedule[2] == 3:
                add "sel_gwa"

            elif day_schedule[2] == 4:
                add "sel_rest"

    if day_schedule[3] != 0:
        hbox:
            xpos 288 ypos 180
            if day_schedule[3] == 1:
                add "sel_study"

            elif day_schedule[3] == 2:
                add "sel_club"

            elif day_schedule[3] == 3:
                add "sel_gwa"

            elif day_schedule[3] == 4:
                add "sel_rest"

    if day_schedule[4] != 0:
        hbox:
            xpos 416 ypos 180
            if day_schedule[4] == 1:
                add "sel_study"

            elif day_schedule[4] == 2:
                add "sel_club"

            elif day_schedule[4] == 3:
                add "sel_gwa"

            elif day_schedule[4] == 4:
                add "sel_rest"

    if day_schedule[5] != 0:
        hbox:
            xpos 544 ypos 180
            if day_schedule[5] == 1:
                add "sel_study"

            elif day_schedule[5] == 2:
                add "sel_club"

            elif day_schedule[5] == 3:
                add "sel_gwa"

            elif day_schedule[5] == 4:
                add "sel_rest"

    if day_schedule[6] != 0:
        hbox:
            xpos 672 ypos 180
            if day_schedule[6] == 1:
                add "sel_study"

            elif day_schedule[6] == 2:
                add "sel_club"

            elif day_schedule[6] == 3:
                add "sel_gwa"

            elif day_schedule[6] == 4:
                add "sel_rest"

screen schedule_revise_button():
    hbox:
        xpos 32 ypos 180
        spacing -4
        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 1)

        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 2)

        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 3)

        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 4)

        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 5)

        imagebutton :
            idle im.Alpha("sel_study.png",0)
            hover im.Alpha("sel_study.png",0)
            action Call("button_reset", number = 6)
