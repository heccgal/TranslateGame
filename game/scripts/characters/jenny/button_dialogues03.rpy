label jenny_dialogue_make_deal_alright_repeat:
    show player 12 at left
    show jenny 82 at Position(xpos=937)
    player_name "Хорошо..."
    show player 41 at Position(xpos=38) with fastdissolve
    pause
    show player 11 at left
    show jenny 80 at Position(xpos=945)
    jen "Подожди, я пересчитываю сначала." with fastdissolve
    show jenny 14
    jen "Хмм..."
    $ player.spend_money(500)
    play audio coins2
    show player 1
    show jenny 12 at Position(xpos=937)
    jen "Хорошо. Это все здесь." with fastdissolve
    show jenny 10
    show player 21
    player_name "Так... Прямо как в прошлый раз?"
    show player 11
    show jenny 7 at right
    jen "Да, никаких прикосновений без моего разрешения!"
    show player 21
    show jenny 8
    player_name "Окей..."
    show jenny 161 at Position(xpos = 943) with fastdissolve
    pause
    show jenny 162 with fastdissolve
    pause
    show jenny 91 at right with fastdissolve
    show player 1
    jen "Ты можешь коснуться одной рукой..."
    hide player
    show jenny 92
    with fastdissolve
    pause
    show jenny 94 with fastdissolve
    pause
    show jenny 93_94
    pause 8
    show jenny 95_94
    pause 8
    show jenny 95
    jen "Почему ты так сжимаешь мой сосок?"
    show jenny 94
    jen "Ты не можешь просто потрогать нормально?"
    show jenny 95
    pause
    show jenny 96
    jen "Хахх..."
    return

label jenny_dialogue_make_deal_continue:
    show jenny 93_94
    pause 8
    show jenny 95_94
    pause 8
    show jenny 95
    pause
    show jenny 96
    jen "Хахх..."
    return

label jenny_dialogue_make_deal_suck_stat_fail:
    show jenny 97 at Position(xpos=1008) with fastdissolve
    pause
    show jenny 98
    jen "[dex_warn]Какого хрена?!" with hpunch
    show jenny 102
    show player 5 at left
    with dissolve
    jen "[dex_warn]Я никогда не говорила, что ты можешь {b}сосать{/b} их, идиот!"
    show jenny 103
    show player 10
    player_name "Прости меня!"
    player_name "Я думал, все в порядке!"
    show jenny 102
    show player 5
    jen "Я же говорила, только рукой!!!"
    jen "Убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_suck_stat_pass:
    show jenny 99 at Position(xpos=1008) with hpunch
    jen "Аххх!!"
    show jenny 100
    jen "Что ты делаешь?!"
    show jenny 99_100_101
    pause 8
    show jenny 101
    return

label jenny_dialogue_make_deal_suck_continue:
    show jenny 99_100_101
    pause 8
    show jenny 101
    return

label jenny_dialogue_make_deal_suck_stop:
    show jenny 98 at Position(xpos=1008)
    jen "Какого хрена?!" with hpunch
    show jenny 102
    show player 5 at left
    with dissolve
    jen "Я никогда не говорила, что ты можешь сосать их! Идиот!!"
    show player 10
    show jenny 103
    player_name "Прости меня!"
    player_name "Я думал, тебе понравилось!"
    show jenny 102
    show player 5
    jen "Я... Я этого не делал, понятно?! Я просто притворялась!!"
    jen "На этот раз я позволила тебе зайти слишком далеко..."
    jen "Убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_stop:
    show jenny 91 at right
    show player 1 at left
    with fastdissolve
    jen "Довольный?"
    show jenny 89
    show player 21
    player_name "Да... Спасибо."
    show player 1
    show jenny 90
    jen "Нет... Спасибо тебе, {b}[firstname]{/b}!"
    jen "Возвращайся в любое время. Если ты хочешь большего... Ты знаешь условия сделки."
    show player 21
    show jenny 89
    player_name "Окей."
    show player 11
    show jenny 91
    jen "А теперь убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_not_yet:
    show player 12
    show jenny 10
    player_name "Вообще-то, ничего страшного."
    player_name "Мне нужно ещё подумать над этим."
    show player 11
    show jenny 7 at right
    jen "Тогда убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_not_enough:
    show player 10
    show jenny 10 at Position(xpos=937)
    player_name "У меня сейчас не так много денег..."
    show player 11
    show jenny 9
    jen "Ты на мели?! Это просто печально..."
    show player 14
    show jenny 10
    player_name "Но скоро должно быть больше."
    show player 5
    show jenny 9
    jen "Тьфу... Возвращайся, когда будут деньги."
    jen "Убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_cam_show_pre:
    show player 2
    show jenny 11 at Position(xpos=937)
    player_name "Нужен ли я тебе... для {b}показа{/b}?"
    show player 1
    show jenny 12
    jen "Кто-то чувствует себя {b}возбужденным{/b}."
    jen "Хочешь почувствовать, как моя мокрая киска обвивается вокруг твоего члена?"
    show player 13
    show jenny 11
    player_name "..."
    show player 21
    player_name "Ну, если тебе нужна моя помощь, я думаю..."
    show player 1
    show jenny 19 at right
    jen "Ладно, подожди здесь, маленький извращенец."
    jen "Позвольте мне взять мой {b}реквизит{/b}, а потом я объясню, что делать."
    scene black with fade
    return

label jenny_dialogue_cam_show_pre_inside:
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 1 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Тьфу... эта штука такая тугая!"
    show player 21
    show jenny 167
    player_name "Я думаю, что это выглядит хорошо..."
    show player 11
    show jenny 166
    jen "Прекрати свою дешевую лесть."
    show jenny 167
    player_name "..."
    show jenny 109
    jen "Так... знаешь, как я сказал тебе, что кончать внутрь-плохо?"
    jen "Получается, что мои поклонники любят {б}кончание во внутрь{/в}. Я получил абсолютную тонну новых подписчиков из-за этого."
    show jenny 108
    show player 21
    player_name "Подожди... Что?"
    show player 1
    show jenny 166
    jen "Я хочу сказать, что ты можешь продолжать делать это, идиот! Я не возражаю!"
    show player 21
    show jenny 167
    player_name "Охх..."
    show jenny 166
    show player 11
    jen "А теперь сядь на мою кровать и ничего не говори, пока я готовлю шоу..."
    jen "Просто сиди сложа руки, и держи, своего петуха хорошо и жестко, и дайте мне знать, когда ты собираешься кончить."
    jen "Поняла, придурок?"
    show jenny 109
    jen "Мы должны продолжать в том же духе, пока нас снимают."
    show jenny 108
    show player 21
    player_name "Окей..."
    return

label jenny_dialogue_cam_show_pre_outside:
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 1 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Тьфу... эта штука такая тугая!"
    show player 21
    show jenny 167
    player_name "Я думаю, что это выглядит хорошо..."
    show player 11
    show jenny 166
    jen "Прекрати свою дешевую лесть."
    show jenny 166
    show player 11
    jen "А теперь сядь на мою кровать и ничего не говори, пока я готовлю шоу..."
    jen "Просто сиди сложа руки, и держи, своего петуха хорошо и жестко, и дайте мне знать, когда ты собираешься кончить."
    jen "Поняла, придурок?"
    show jenny 109
    jen "Они должны думать, что ты мой парень."
    show jenny 108
    show player 21
    player_name "Окей..."
    return

label jenny_dialogue_cam_show_pre_after:
    scene jenny_webcam2
    show jenny 151 zorder 2 at Position(xpos=407,ypos=748)
    show jenny_cheer1 zorder 3 at Position(xpos=439,ypos=724)
    show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
    show xtra 20 zorder 4 at left
    with fade
    jen "Хорошо, мы в прямом эфире!"
    show jenny 155
    jen "Эй ребята!"
    show jenny 151
    jen "Извините, что заставила вас ждать! Я должна была позвать своего парня!"
    jen "Он был очень плох, и теперь я должна преподать ему урок!"
    jen "Давайте приступим?"
    hide jenny
    hide jenny_cheer1
    show jennysex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
    show playersex 116b
    with fastdissolve
    jen "Просто нужно сделать несколько вещей..."
    hide jennysex
    show jennysex 104 zorder 1 at Position(xpos=122,ypos=540)
    show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
    with fastdissolve
    jen "Сначала я сниму эту юбку..."
    show jennysex 105 at Position(xpos=144,ypos=544) with fastdissolve
    pause
    show jennysex 106 at Position(xpos=170,ypos=542) with fastdissolve
    jen "Теперь давай используем это, чтобы убедиться, что он никуда не уйдет, пока я выебу его мозги..."
    show jennysex 106b
    show playersex 120
    player_name "Ты на самом деле не собираешься-"
    show jennysex 107 zorder 2 at Position(xpos=300,ypos=542)
    show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
    with fastdissolve
    pause
    show playersex 125
    show jennysex 109 at Position(xpos=357,ypos=620)
    with fastdissolve
    jen "Что вы скажете, ребята? Должны ли мы выяснить, что скрывается под его шортами?"
    show jennysex 108
    player_name "..."
    show jennysex 111 at Position(xpos=375,ypos=634) with fastdissolve
    jen "О, вау..."
    show jennysex 112 at Position(xpos=374,ypos=674)
    show playersex 127
    jen "Посмотрите на этот красивый, толстый, длинный член..." with vpunch
    show jennysex 113 with fastdissolve
    jen "Давай сделаем это красиво и жестко."
    show jennysex 115b with fastdissolve
    pause
    show jennysex 114b_115b
    pause 8
    show jennysex 114
    jen "Интересно, поместится ли это внутри меня..."
    show jennysex 115b
    player_name "!!!"
    show playersex 126
    player_name "Подожди... Ты принимаешь таблетки, верно?"
    show jennysex 110b at Position(xpos=423,ypos=674)
    show playersex 127b
    jen "Шшш!!!" with hpunch
    jen "Тебе не нужно беспокоиться об этом!!"
    jen "Просто сделай то, что сделал в прошлый раз, и все будет хорошо!"
    show jennysex 114 at Position(xpos=374,ypos=674)
    show playersex 127
    with fastdissolve
    jen "Извините за это, ребята!"
    show jennysex 115
    jen "Мой парень просто... застенчивый."
    show jennysex 114
    jen "Теперь давайте дадим вам то, чего вы все так долго ждали..."
    show jennysex 116 at right with dissolve
    pause
    show jennysex 119b at Position(xpos = 939, ypos = 674) with fastdissolve
    jen "О, да!!"
    show jennysex 117b with fastdissolve
    jen "Это так... {b}глубоко{/b}!!"
    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
    pause 8
    show jennysex 117b
    jen "Его член намного лучше, чем любая из моих игрушек..."
    show jennysex 118b
    jen "Это действительно растягивает меня..."
    show jennysex 119
    pause
    show jennysex 120
    pause
    show jennysex 121
    pause
    return

label sis_cheerleader_fuck_looprep:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not sis_cheerleader_sex2_menu:
                show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
            else:

                show expression AnimatedImage("jennysex", [123,124,125,126,127], M_jenny) as jennysex at Position(xpos = 986, ypos = 768)
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_cheerleader_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if not sis_cheerleader_sex2_menu:
                $ pose_list = [117,118,119,120,121]
                $ xpos_list = [939]
                $ ypos_list = [674]
            else:

                $ pose_list = [123,124,125,126,127]
                $ xpos_list = [986]
                $ ypos_list = [768]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex at Position(xpos = xpos_list[0],ypos = ypos_list[0])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_cheerleader_hscene_dialog")
        $ animcounter += 1
    call screen sis_cheerleader_sex_options

label jenny_cheerleader_hscene_dialog:
    if animcounter == 1:
        jen "Ахххх!!!{p=1}{nw}"

    elif animcounter == 3:
        jen "Ох!!!{p=1}{nw}"
        player_name "Уххх...{p=1}{nw}"
    return

label sis_cheerleader_fuck_cum_outside:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_manual")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_after")
    if store._in_replay == None and sister.completed(sis_final2):
        call expression game.dialog_select("sis_cheerleader_fuck_after_repeat")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_after_initial")
    $ renpy.end_replay()
    $ sis_final_cum = "Outside"
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_outside_animation:
    jen "( Я чувствую его член... )"
    jen "( ... он пульсирует, как сумасшедший... )"
    jen "( ... он собирается кончить?! )"
    pause
    show jennysex 130b
    with vpunch
    return

label sis_cheerleader_fuck_cum_outside_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    jen "( Я чувствую его член... )"
    show jennysex 118
    jen "( ... он пульсирует, как сумасшедший... )"
    show jennysex 119
    jen "( ... он собирается кончить?! )"
    show jennysex 120
    pause
    show jennysex 130b at Position(xpos=939,ypos=674)
    with vpunch
    return

label sis_cheerleader_fuck_cum_outside_after:
    jen "Ахх!!"
    show jennysex 130
    show white zorder 5
    show playersexc 129 zorder 4 at Position(xpos=560,ypos=377)
    hide white with dissolve
    pause
    show playersexc 130 at Position(xpos=609,ypos=423) with fastdissolve
    pause
    show jennysex 130b
    jen "Вау..."
    jen "Ребята, вы видите мою зияющую киску?"
    jen "И вся эта горячая сперма бежит по моей спине..."
    jen "Надеюсь, вам понравилось!"
    return

label sis_cheerleader_break_free_fail:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_break_free_fail_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_break_free_fail_manual")
    call screen sis_cheerleader_sex_options

label sis_cheerleader_break_free_fail_animation:
    player_name "[str_warn]( Эй, эти наручники не такие крепкие... )"
    player_name "[str_warn]( Давай... )"
    player_name "[str_warn]( Черт возьми, я не могу вырваться. )"
    player_name "[str_warn]( Я недостаточно силён... )"
    return

label sis_cheerleader_break_free_fail_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    player_name "[str_warn]( Эй, эти наручники не такие крепкие... )"
    show jennysex 118
    player_name "[str_warn]( Давай... )"
    show jennysex 119
    player_name "[str_warn]( Черт возьми, я не могу вырваться. )"
    show jennysex 120
    player_name "[str_warn]( Я недостаточно силён... )"
    show jennysex 121
    return

label sis_cheerleader_break_free_pass:
    $ sis_cheerleader_sex2_menu = True
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_break_free_pass_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_break_free_pass_manual")
    call expression game.dialog_select("sis_cheerleader_break_free_pass_after")
    jump expression game.dialog_select("sis_cheerleader_fuck_looprep")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
