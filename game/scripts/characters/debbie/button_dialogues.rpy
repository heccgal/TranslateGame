label debbie_dialogue_mom_relaxing:
    scene location_home_kitchen_closeup
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Привет, милый! Разве ты не должен идти?"
    show player 2 at left
    show debbie 1 at right
    player_name "Да. Я был в пути."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    scene location_home_kitchen_closeup
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Милый, что ты там делаешь?"
    show debbie 50j
    player_name "Ммм, ничегооо..."
    show debbie 50k
    deb "Милый!"
    deb "Что мы будем делать, если {b}[jen_name]{/b} войдёт?"
    deb "Она будет неприятно удивлена!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    player_name "... И, кроме того..."
    player_name "... Это займет всего минуту."
    show debbie 50k
    deb "Ты такой плохой паре-"
    deb "Ахх!"
    deb "... Все в порядке! Только побыстрее!"
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 48c with dissolve
    deb "Ладно, ладно! Мы должны остановиться!"
    show debbie 50k
    deb "На этом всё, и мне придется сменить трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я еще могу тебе помочь?"
    show debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Ты нашёл мой {b}лосьон{/b} в {b}комоде спальни{/b}?"
    show debbie 1
    show player 10
    player_name "Нет, еще нет."
    show player 5
    show debbie 2
    deb "Ну, так чего же ты ждешь?"
    return

label debbie_dialogue_mom_car_condition:
    show player 10 at left
    show debbie 61 at right
    with dissolve
    player_name "Я выяснил, почему машина не заводится..."
    show player 5
    show debbie 63
    deb "Да?! Ты уже все исправила?"
    show debbie 61
    pause
    show player 25
    player_name "Это довольно ужастно, {b}[deb_name]{/b}... Не думаю, что смогу это исправить."
    show player 5
    show debbie 39
    deb "Ох."
    show debbie 38
    show player 10
    player_name "На самом деле, я думаю, нам придется заменить весь двигатель. На этом можно действительно разориться!"
    player_name "Это будет дорого..."
    show player 5
    pause
    show debbie 60
    deb "А что насчет страховки? Мы должны пойти и посмотреть, что {b}автосалон{/b} может сделать для нас."
    deb "Надеюсь, они покроют ремонт, в противном случае..."
    show debbie 39
    deb "... Мы останемся без машины на некоторое время."
    show debbie 38
    pause
    show player 10
    player_name "Уверен, все будет хорошо., {b}[deb_name]{/b}. Я пойду и поговорю с {b}дилерами авто{/b}."
    show player 5
    pause
    show player 14
    player_name "Я все исправлю."
    player_name "Так или иначе."
    show debbie 61
    show player 13
    pause
    show debbie 62
    deb "Я так рада, что ты рядом, дорогой!"
    deb "Спасибо тебе!"
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    show debbieobj 2 at Position(xpos=590,ypos=768)
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    scene location_home_kitchen_closeup
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Милый?"
    deb "Что ты там делаешь?"
    show debbie 50j
    player_name "Ммм, ничегооо..."
    show debbie 50k
    deb "Ахх..."
    deb "Что мы будем делать, если {b}[jen_name]{/b} войдёт?"
    deb "Она будет неприятно удивлена!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show debbie 50j with dissolve
    player_name "Ты хорошо себя чувствуешь?"
    show debbie 50k
    deb "Конечно..."
    deb "Ммм, ты делаешь меня такой мокрой.!"
    deb "Ахх!"
    show debbie 50j
    player_name "Что, если я стянул эти трусики и трахнул тебя прямо здесь?"
    show debbie 50k
    deb "Оо боже..."
    deb "Ладно, давай! Возьмите меня прямо здесь! Только побыстрее, дорогой!"
    show debbie 50j
    player_name "Ммм, держись крепче за этот шкаф!"
    show debbie 50c with dissolve
    pause
    show debbie 50d with dissolve
    pause
    hide debbie
    show debbie 50e at right
    with dissolve
    pause
    show debbie 50g with dissolve
    deb "Ох да!."
    hide debbie
    show debbies 164 at right
    with dissolve
    deb "Аххх!"
    player_name "Вау, с тебя капает..."
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies at right with dissolve
    deb "Ох, трахни меня!"
    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [164,165,166,167,168]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
        $ animcounter += 1
    call screen mom_kitchen_fuck_options

label debbie_kitchen_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            deb "ОХ!!!{p=1}{nw}"
        else:
            deb "АХХХ!!!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            deb "Ты кончил?{p=2}{nw}"
            player_name "Еще нет...{p=2}{nw}"
            deb "Поторопись, милый... Я не думаю, что... Я могу взять... Куда более!{p=3}{nw}"
    return

label mom_kitchen_fuck_cum:
    call expression game.dialog_select("mom_kitchen_fuck_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["09_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label mom_kitchen_fuck_cum_dialogue:
    player_name "( !!! )"
    player_name "Ох, {b}[deb_name]{/b}!"
    player_name "Я-"
    deb "Шшшш!"
    show debbies 169 with flash
    player_name "Ухх!!!"
    hide debbies
    show debbie 50h at right
    with dissolve
    pause
    deb "Обожаю, когда ты за главного!"
    player_name "Ты кончил?"
    deb "Ох, да!"
    show debbie 50i at right
    show player 434 at left
    with dissolve
    deb "{b}*Фуф*{/b}, мои ноги все еще дрожат..."
    deb "... Ничего себе, вы тебе много!"
    pause
    show debbie 61 with dissolve
    show player 10
    player_name "Прости."
    show player 13
    show debbie 62
    deb "Нет, мне это нравится! Внутри меня так хорошо."
    show debbie 61
    show player 14
    player_name "Мне нравится, когда ты так говоришь"
    show player 13
    show debbie 62
    deb "Хе-хе, ну это правда..."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene location_home_kitchen_closeup
    hide debbieobj
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 50k at Position(xpos=660,ypos=768) with dissolve
    deb "Ну привет тебе, дорогой...."
    show debbie 50j
    player_name "Хей, {b}[deb_name]{/b}..."
    show debbie 50k
    deb "Просто будь осторожен..."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 50k with dissolve
    deb "Ладно, ладно! Мы должны остановиться!"
    deb "На этом всё, и мне придется сменить трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я еще могу тебе помочь?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene location_home_kitchen_closeup
    hide debbieobj
    show debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Привет {b}[deb_name]{/b}, есть минутка?"
    show debbie 2
    show player 1
    deb "Что-то нужно, {b}[firstname]{/b}?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        deb "Вот мой большой человек..."
    elif randomizer() <= 20:
        deb "Привет, дорогая."
        deb "Что я могу для тебя сделать?"
    elif randomizer() <= 30:
        deb "Эмм..."
        deb "Без приветствия?"
    elif randomizer() <= 70:
        deb "В поисках меня, надеюсь."
    elif randomizer() <= 80:
        deb "Тебе что-то нужно, милый?"
        deb "Или я могу сделать что-нибудь для тебя?"
    elif L_home_shower.is_here(M_jenny):
        deb "{b}[jen_name]{/b} находится в душе."
        deb "В случае, если ты нуждаешься во мне в течение секунды."
    else:
        deb "Я надеялась, что увижу тебя сегодня."
    show debbie 1
    show player 14
    if randomizer() <= 50:
        player_name "Привет, {b}[deb_name]{/b}."
    else:
        player_name "Ты сегодня хорошо выглядишь."
    show player 13
    return

label debbie_dialogue_mom_not_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Привет, милый!"
    deb "В школе все в порядке?"
    show player 14 at left
    show debbie 1 at right
    player_name "Да..."
    show player 13 at left
    show debbie 13 at right
    deb "Надеюсь, ты не зашел слишком далеко, со всем этим?"
    show debbie 14 at right
    show player 14 at left
    player_name "нет, я догоню."
    show player 13 at left
    show debbie 13 at right
    deb "Просто дайте мне знать, если есть что-нибудь я могу сделать, чтобы помочь?"
    show player 21 at left
    show debbie 14 at right
    player_name "Хорошо, {b}[deb_name]{/b}..."
    player_name "Я должен идти."
    show player 13 at left
    show debbie 3 at right
    deb "Не задерживайся до поздна!"
    show debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show debbie 1 at right
    player_name "{b}[deb_name]{/b}, Ты знаете, что случилось с моим {b}Отцом{/b}?"
    show player 11
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Ох... Милый, Я..."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Пожалуйста, я хочу знать правду!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Прости, милый. У меня нет ничего для тебя."
    deb "Полицейское расследование ничего не дало..."
    deb "На самом деле, я понимаю, что дело приостановлено из-за отсутствия доказательств."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Да, но они найдут что-нибудь, не так ли? Я имею в виду, что это их работа!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Мы можем только надеяться."
    show debbie 59 at Position (xoffset=-28)
    pause
    show debbie 60 at Position (xoffset=-28)
    deb "Милый..."
    deb "Я тоже хочу закрыть все это..."
    deb "... Но твой {b}Отец{/b} не хотел бы, чтобы мы были одержимы этим."
    show debbie 63 at Position (xoffset=-28)
    deb "Ты молод, и тебе необходимо сосредоточиться на том, чтобы жить своей жизнью"
    deb "Сделай это для своего {b}Отца{/b}."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Да. Я попробую."
    show player 14
    show debbie 61 at Position (xoffset=-28)
    player_name "Спасибо, {b}[deb_name]{/b}."
    show player 1
    show debbie 2 with dissolve
    deb "Ещё что-то нужно?"
    show debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show debbie 1
    show player 10
    player_name "{b}[deb_name]{/b}, о том, что ты сказала по телефону..."
    show debbie 13
    show player 11
    deb "Я сказала тебе не беспокоиться об этом."
    deb "Все будет хорошо!"
    show debbie 14
    show player 14
    player_name "Хорошо, но что, если я хочу помочь тебе?"
    player_name "Что если у меня будет настоящая работа?"
    show player 10
    player_name "Я чувствую себя несколько ответственным за весь этот стресс..."
    show debbie 52 at Position (xoffset=1)
    show player 11
    deb "Ты можешь помочь мне, оставаясь в школе!"
    deb "Твой {b}Отец{/b} перевернется в могиле, если я позволю тебе пойти на полный рабочий день..."
    deb "Он хотел, чтобы ты закончил свою учёбу."
    show debbie 51 at Position (xoffset=1)
    show player 10
    player_name "... Но я могу работать после школы и по выходным?"
    show debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    deb "{b}*Вздох*{/b} Ты такой упрямый, как твой {b}Отец{/b}..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    deb "Хмм..."
    show debbie 63 at Position (xoffset=-28)
    deb "Почему бы тебе не пойти проверить {b}почтовый ящик{/b}?"
    deb "Кажется, я видела там объявления о работе.."
    deb "Возможно, одно из объявлений заитересует тебя?"
    show debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Хорошо, я посмотрю."
    show debbie 62 at Position (xoffset=-28)
    show player 1
    deb "Это всё, о чем ты хотел поговорить со мной, дорогой?"
    show debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, Я хотел бы поговорить о тех парнях в костюме..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Был ли мой {b}папа{/b} связан с ними?"
    show player 11
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*Вздох({/b} Наверное, я не смогу вечно держать это в секрете..."
    deb "Твой {b}Отец{/b} был хорошим человеком, {b}[firstname]{/b}."
    deb "... Но у него была слабость к азартным играм."
    deb "He always told me it was nothing to concern myself over and that he had it all in hand."
    deb "... But now he's gone and it seems there's a lot he didn't share with me."
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Your {b}Father{/b} owed those men a lot of money and they are still trying to collect."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "We should just tell the police about this!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "NO! I'm afraid of what might happen if I involve the authorities in this!"
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "So what, you're just going to pay those scumbags?!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "I've done my best but I'm afraid I just don't have the money to cover it all, sweetie."
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*Sigh({/b} Maybe you and I should just disappear and start over somewhere else."
    show player 1
    show debbie 63 at Position (xoffset=-28) with dissolve
    deb "Heh, that would be an adventure, wouldn't it?"
    show debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Yeah, I suppose."
    show debbie 2 with dissolve
    show player 1
    deb "Is there anything else you wanted to talk about?"
    show debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Wasn't there some paint in the garage?"
    show player 5
    show debbie 13
    deb "Paint? What do you want with old paint?"
    show debbie 1
    show player 10
    player_name "I was going to try and make... something."
    show player 5
    show debbie 2
    deb "Oh, well, {b}Diane{/b} said she'd get rid of them for me."
    show debbie 1
    show player 12
    player_name "Really?"
    player_name "Well, I'd better see if I can pick them up before she throws them away!"
    player_name "Thanks, {b}[deb_name]{/b}! Bye, {b}[deb_name]{/b}!"
    hide player with dissolve
    show debbie 2
    deb "Bye!"
    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Did you need help with anything?"
    show player 5
    show debbie 2
    deb "Did you finish mowing the yard?"
    show debbie 1
    show player 10
    player_name "Oh, right!"
    player_name "I'll get on that."
    show player 13
    show debbie 2
    deb "I'd really appreciate it, sweetie."
    show debbie 1
    show player 14
    player_name "No problem!"
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "( I gotta fix the {b}bathroom sink{/b} somehow... )"
    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "Anything else you need help with?"
    show player 13
    show debbie 2
    return

label debbie_dialogue_help_chores_later:
    deb "No. Not right now, sweetie."
    deb "Maybe later, if you're still available."
    return

label debbie_dialogue_help_chores_tomorrow:
    deb "No. Not today, sweetie."
    deb "Maybe tomorrow, if you're still available."
    return

label debbie_dialogue_help_chores_after:
    show debbie 3
    deb "Thanks for asking!"
    show debbie 1
    show player 14
    player_name "You're welcome, {b}[deb_name]{/b}."
    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "( I should go check the {b}car{/b} like {b}[deb_name]{/b} asked me to. )"
    return

label debbie_dialogue_help_fix_car:
    show player 4
    player_name "( I have to visit the {b}car dealership{/b}. Maybe they can fix {b}[deb_name]{/b}'s car... )"
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Hey, {b}[deb_name]{/b}, anything I can do to help around the house?"
    show player 1
    deb "Hmm..."
    show debbie 2
    deb "Nothing I can think of right now, no."
    show debbie 1
    show player 2
    player_name "Cool. Let me know if something comes up."
    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Need me to rub some more lotion on...your legs?"
    show player 13
    show debbie 2
    deb "That sounds wonderful, sweetie."
    deb "I could really use your gentle touch right about now."
    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Need me to rub some more lotion on... your legs?"
    show player 5
    show debbie 13
    deb "Oh... again? Well, I..."
    show debbie 14
    show player 10
    player_name "Did I do a bad job?"
    show player 5
    show debbie 13
    deb "Oh, no, sweetie. It was... really good."
    show debbie 14
    pause
    show debbie 13
    deb "Sure, I guess I could use a break."
    show debbie 1
    show player 14
    player_name "Great!"
    show player 13
    show debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    deb "Go and grab the {b}lotion from my bedroom dresser{/b}."
    show debbie 1
    show player 14
    player_name "Alright!"
    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show debbie 1 at right
    player_name "Remember when you asked me to go shopping with you?"
    show player 1
    show debbie 2
    deb "Yeah."
    show player 2
    show debbie 1
    player_name "Well I'm free now. Do you still wanna go?"
    show player 1
    show debbie 3
    deb "Really?! Great!"
    show debbie 2
    deb "Just let me get ready and I'll meet you in the car, okay?!"
    show debbie 1
    show player 2
    player_name "Alright."
    return

label debbie_dialogue_shower_basement:
    show player 2
    show debbie 1
    player_name "So uhh.."
    player_name "I was thinking we could maybe... Take a shower together?"
    show player 13
    show debbie 2
    deb "Right now?"
    show debbie 1
    deb "Hmm..."
    show debbie 3
    deb "I suppose I could go for a shower."
    show debbie 2
    deb "Let me just finish putting this load of laundry in and I'll meet you upstairs."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Hope you're not almost done..."
    deb "I was hoping we could spend some time in here."
    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show debbie 1
    player_name "Hey, {b}[deb_name]{/b}!"
    player_name "I was wondering..."
    show player 21
    player_name "Would you like to take a shower with me?"
    show player 14
    show debbie 2
    deb "It is getting pretty hot in the house..."
    show debbie 3
    deb "Sure! A shower sounds lovely right now."
    show debbie 2
    deb "Give me a minute. I'll join you after I'm done here."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Sorry to keep you waiting, sweetie..."
    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Would you like to join me in your room?"
    show player 13
    show debbie 3
    deb "Right now?"
    show debbie 1
    show player 10
    player_name "Absolutely!"
    show player 5
    show debbie 2
    deb "Heh, alright..."
    show player 13
    deb "... Just make sure, {b}[jen_name]{/b} doesn't see us."
    show debbie 1
    show player 14
    player_name "I will."
    show player 13
    show debbie 2
    deb "Hehehe..."
    deb "You're going to wear me out!"
    show debbie 1
    show player 14
    player_name "I'm just making sure you get plenty of exercise!"
    show player 13
    show debbie 3
    deb "Ha Ha Ha."
    show debbie 2
    deb "Get your butt upstairs and get those clothes off!"
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_1:
        show debbie 86 at left
        show player 434f at right
        with dissolve
        deb "The bed sheets are so nice and soft... Why don't you come lay with me..."
        show debbie 84
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show debbie 85
        show player 263 with dissolve
        deb "Naughty boy."
        show debbie 84
        show player 262
        player_name "What?"
        show player 263
        show debbie 85
        deb "You truly are insatiable."
        show debbie 84
        show player 262
        player_name "You can just lay on your back and I can do the rest."
        show player 263
        show debbie 86
        deb "Well where's the fun in that?"
        show debbie 84
        show player 262
        player_name "Heh, don't worry. I'll make it fun!"
        show player 263
        show debbie 84
        deb "Mmm, I have no doubt about that!"
        show debbie 89 with dissolve
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_kitchen:
    show player 14
    player_name "Would you like to join me in your room?"
    show player 13
    show debbie 2
    deb "Right now?"
    deb "Absolutely!"
    deb "Let's just make sure, {b}[jen_name]{/b} doesn't see us."
    show debbie 1
    show player 14
    player_name "Yup."
    show player 13
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_2:
        show player 434f at right
        show debbie 86 at left
        with dissolve
        deb "I was hoping you'd bring me in here for this today!"
        show debbie 84
        show player 435f
        player_name "You were really thinking about it?"
        show player 434f
        show debbie 86
        deb "Does that really surprise you?"
        deb "I'm always thinking about that big cock of yours..."
        show debbie 84
        show player 435f
        player_name "Heh, I think about it a lot too... Especially when you're wearing that robe of yours."
        show player 434f
        show debbie 89 with dissolve
        deb "You mean this old thing?"
        show debbie 90
        show player 435f
        player_name "... Oh, yeah."
        show player 434f
        show debbie 89
        deb "Hehe, why don't you take off those clothes and come play with me?"
        show debbie 90
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show player 263
        show debbie 102
        with dissolve
        deb "Mmmm..."
        show debbie 103
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_after:
    deb "Come and get me, big boy!"
    hide player
    show debbie 104 at left
    with dissolve
    pause
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_sex_in_my_room:
    show player 2
    player_name "You wanna sleep in my room tonight?"
    show player 1
    show debbie 2
    deb "Mmm, I would love that, sweetie."
    show player 2
    show debbie 1
    player_name "Great! I'll wait up for you then."
    show player 1
    show debbie 2
    deb "Can't wait!"
    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, would you come with me for a second?"
    show player 13
    show debbie 2
    deb "Hmm?"
    show debbie 1
    show player 14
    player_name "Just follow me."
    show player 13
    show debbie 2
    deb "Hehe, What are you up to?"
    show debbie 2
    deb "..."
    show debbie 3
    deb "You're planning something!"
    show debbie 2
    deb "Hehe!"
    deb "Is it a surprise?"
    deb "... I love surprises!"
    show debbie 1
    show player 14
    player_name "Heh, I know you do."
    player_name "I wouldn't really call it a surprise though..."
    show player 13
    show debbie 3
    deb "Hehe!"
    show debbie 2
    deb "Well what would you call it then?"
    show debbie 1
    deb "..."
    show debbie 2
    deb "Is this something naughty?"
    deb "..."
    show debbie 1
    show player 14
    player_name "Maaaaybe."
    show debbie 2
    deb "Hehe, Alright. Let's go quickly while {b}[jen_name]{/b} is upstairs."
    hide player
    hide debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "I was thinking, maybe we should watch another movie tonight. Interested?"
    show player 1
    show debbie 2
    deb "Mmm, a movie night, huh?"
    deb "That sounds like a great idea, Sweetheart!"
    show player 2
    show debbie 1
    player_name "Awesome!"
    player_name "I'll see you {b}tonight{/b} in the {b}living room{/b} then?"
    show player 1
    show debbie 2
    deb "I can't wait..."
    return

label debbie_dialogue_laundry_sex_basement:
    scene home_basement
    show debbie 122 at right
    show player 14 at left
    player_name "Are you almost done with the laundry?"
    show player 13
    show debbie 123
    deb "Almost. I just have to move this load into the dryer."
    deb "Why, what's up, sweetie?"
    show player 14
    show debbie 122
    player_name "I just thought you might like to go for a ride?"
    show player 13
    show debbie 123
    deb "Oh, feeling a bit naughty are we?"
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show debbie 123
    deb "Hehe, I'll take that as a yes!"
    show player 263f with dissolve
    deb "..."
    show debbie 121
    show player 432
    player_name "Absolutely!"
    show player 431
    pause
    show debbie 123
    deb "Get those clothes off and get on the washer!"
    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show debbie 108
    deb "My turn..."
    deb "Mmm, I've been waiting all morning for this!"
    show debbie 109
    pause
    show debbie 110
    pause
    show debbie 111
    pause
    show debbie 112
    pause
    show debbie 113
    pause
    show debbie 114
    pause
    player_name "You look beautiful, {b}[deb_name]{/b}."
    show debbie 115
    deb "Just sit back and relax, sweetie."
    deb "I'll take care of everything..."
    deb "...Just make sure you hold on to me."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655)
    pause
    show debbies 126f with dissolve
    deb "Oh!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    return

label debbie_dialogue_laundry_sex_basement_random_true:
    deb "Mmmm..."
    deb "I can barely fit you all in."
    return

label debbie_dialogue_laundry_sex_basement_random_false:
    deb "Ahh..."
    player_name "( !!! )"
    player_name "You're so warm..."
    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Hey, {b}[deb_name]{/b}... Do you want to hang out in the basement for some quick fun?"
    show player 13
    show debbie 2
    deb "Oh?"
    show debbie 1
    show player 14
    player_name "I figured we could turn on the dryer and you could be as loud as you wanted..."
    show player 13
    show debbie 3
    deb "Ha Ha."
    show debbie 2
    deb "That's quite naughty, sweetie."
    show debbie 1
    pause
    show debbie 2
    deb "Hmm... Alright!"
    deb "I have some free time and I could use some... attention."
    show debbie 1
    show player 14
    player_name "Really?"
    show player 13
    show debbie 2
    deb "Sure!"
    deb "Just meet me down there in a minute..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show debbie 1 at right
    player_name "Hey... Umm, {b}[deb_name]{/b}?"
    show player 5
    show debbie 2
    deb "Yes, sweetie?"
    show player 10
    show debbie 1
    player_name "Could I ask you something?"
    show player 5
    show debbie 3
    deb "Of course! You can ask me anything."
    show player 10
    show debbie 1
    player_name "Well, it's kinda... Embarrassing."
    show player 5
    show debbie 13
    deb "Oh? Well that's okay, {b}[firstname]{/b}."
    deb "There's no need to feel embarrassed."
    deb "Not with me..."
    show debbie 14
    show player 10
    player_name "Okay."
    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show debbie 14 at right
    player_name "I was wondering if you could..."
    player_name "Well..."
    show player 5
    show debbie 13
    deb "If I could what, Sweetheart?"
    show player 10
    show debbie 14
    player_name "Err... Remember the other day at the mall?"
    show player 5
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "... Yes?"
    show player 10
    show debbie 14b
    player_name "Well... I was hoping you could teach me more, you know, about kissing?"
    show player 5
    show debbie 13
    deb "What?!"
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "That was a mistake, sweetie. I should never have..."
    deb "What are you hoping I'd teach you anyways?"
    show player 10
    show debbie 14b
    player_name "You know, like, how to do it."
    player_name "I thought, maybe, you could show me what women like?"
    show player 5
    show debbie 13
    deb "Hmm, well I could certainly tell you what women like."
    deb "... But I don't think showing you is a good idea. It would be kind of inappropriate..."
    show debbie 14b
    return

label debbie_dialogue_kiss_teach_stat_fail:
    show player 10 at left
    show debbie 14b at right
    player_name "[chr_warn]Are you sure?"
    player_name "[chr_warn]I'd really like to practice with you."
    show player 5
    deb "..."
    show debbie 13
    deb "It's just not a good idea, sweetie."
    show player 10
    show debbie 14b
    player_name "[chr_warn]Oh... A-alright."
    show player 5
    show debbie 13
    deb "Sorry, Sweetheart."
    show player 10
    show debbie 14b
    player_name "[chr_warn]It's okay, {b}[deb_name]{/b}."
    return

label debbie_dialogue_kiss_leave:
    show player 10 at left
    show debbie 14 at right
    player_name "... Actually."
    player_name "Never mind."
    show debbie 13
    show player 5
    deb "Are you sure?"
    deb "You can always talk to me, {b}[firstname]{/b}."
    show player 10
    show debbie 14
    player_name "Yeah, it's nothing."
    player_name "Sorry to bug you."
    show player 5
    show debbie 13
    deb "You never bug me, sweetie."
    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show debbie 1 at right
    player_name "Do you think we could practice again?"
    player_name "You know... Kissing?"
    show player 1
    show debbie 13
    deb "Again?"
    show player 2
    show debbie 14b
    player_name "Y-yeah. I think I'm getting better!"
    show player 1
    show debbie 13
    deb "... Alright."
    deb "But just a little!"
    show player 2
    show debbie 14
    player_name "Okay, sure."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    deb "Mmm..."
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show debbie 77
    deb "Wow... I'd say you're definitely getting better."
    deb "... and you were already so good to begin with!"
    show player 232
    show debbie 76
    player_name "Thanks {b}[deb_name]{/b}!"
    show player 231
    show debbie 74
    pause
    show player 230
    pause
    show player 232
    show debbie 76
    player_name "Sorry about the... You know."
    show player 231
    show debbie 75
    deb "Hehe, it's alright, Sweetheart."
    deb "Perfectly natural."
    deb "The girls in this town are in trouble."
    show player 232
    show debbie 72
    player_name "Hah, you bet!"
    show player 231
    show debbie 73
    deb "Go get em, sweetie!"
    show player 232
    show debbie 72
    player_name "Yes, ma'am!"
    return

label debbie_dialogue_leave:
    show player 2
    player_name "Actually, nevermind, see you later, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
