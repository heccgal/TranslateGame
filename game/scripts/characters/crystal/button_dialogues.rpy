label button_crystal_preamble:
    show player 5 at left
    show crystal 3 at right
    with dissolve
    crys "Это парень моей маленькой девочки, снова."
    show crystal 1 with dissolve
    show player 10
    player_name "Я говорил вам, что мы не-"
    show player 5
    show crystal 2
    crys "Как скажете, молодой человек."
    show crystal 4 with dissolve
    crys "*Глоток*"
    show crystal 2 with dissolve
    crys "Так чего же вы хотите?"
    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "Где {b}Рокси... Отец{/b}?"
    show player 11
    show crystal 2
    crys "Ха! У нее нет отца!"
    crys "Я сама её вырастила.."
    show crystal 1
    show player 10
    player_name "Я вижу."
    show player 11
    show crystal 2
    crys "Честно говоря, я не помню, какой из них был..."
    show crystal 4 with dissolve
    crys "*Глоток*"
    show crystal 2 with dissolve
    crys "...Так что ее папа может быть кем угодно, потому что я знаю."
    show crystal 1
    show player 22
    player_name "!!!"
    show crystal 2
    crys "Что-нибудь еще, о чем бы вы хотели поговорить?"
    show player 5
    show crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Вы знаете, где я могу найти {b}Рокси{/b}?"
    show player 5
    show crystal 3 with dissolve
    crys "Хах! Ты думаешь, я знаю где моя дочка?"
    show crystal 1 with dissolve
    show player 10
    player_name "Хмм..."
    show player 5
    show crystal 2
    crys "Она всегда чем-то занимается..."
    crys "...Но, как правило, она находится в {b}школе{/b} или на {b}пляже{/b}."
    show crystal 1
    show player 14
    player_name "Ох. Я вижу. Спасибо!"
    show player 13
    show crystal 2
    crys "Что-нибудь ещё?"
    show crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "Ох, ничего."
    player_name "Я просто проходил мимо..."
    show player 11
    show crystal 2
    crys "Ну, скоро приедет посетитель, так почему бы тебе не двигаться, дальше."
    show crystal 1
    show player 10
    player_name "Прости. Я тогда пойду."
    player_name "Пока!"
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_closeup_night.jpg"
    show player 5 at left
    show player_wet at left
    show crystal 3 at right
    with dissolve
    crys "Ммм, ты же знаешь, я могу помочь тебе с мокрой одеждой, если хочешь?"
    show crystal 1 with dissolve
    show player 10
    player_name "Ухх... Я..."
    show player 5
    player_name "..."
    show crystal 2
    crys "Не стесняйся."
    crys "Ты красивый мужчина. Ты заслуживаешь особого внимания, не так ли?"
    show crystal 1
    show player 3 with dissolve
    player_name "..."
    rox "{b}Мама{/b}, оставь {b}[firstname]{/b} наедине!"
    show crystal 2
    crys "Хехехе, я просто немного дразню мальчика."
    show crystal 1
    rox "Ну, хватит!"
    show crystal 4 with dissolve
    rox "{b}[firstname]{/b}, иди сюда!"
    show crystal 1
    player_name "..."
    hide crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show crystal 6 at right
    with dissolve
    crys "Ты проиграл, красавчик?"
    show crystal 5
    show player 10
    player_name "Что?!"
    show player 5
    show crystal 6
    crys "Ох, ты у {b}Рокси{/b} новый парень."
    show crystal 5
    show player 12
    player_name "Н-нет, Я-"
    show player 5
    show crystal 6
    crys "Она внутри."
    show crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show crystal 2 at right
    with dissolve
    crys "Ты проиграл, красавчик?"
    show crystal 1
    show player 10
    player_name "Да?!"
    show player 5
    show crystal 2
    crys "Ох, ты у {b}Рокси{/b} новый парень."
    show crystal 1
    show player 10
    player_name "Н-нет, Я-"
    show player 5
    show crystal 2
    crys "Ее здесь нет."
    show crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Ммм, теперь есть хороший способный человек!"
    show crystal 5
    show player 14
    player_name "Хех, Привет {b}Кристи{/b}..."
    show player 13
    show crystal 6
    crys "Почему бы тебе не выпить пива и посидеть со мной?"
    crys "Вы можете показать этот серебряный язык еще немного..."
    show crystal 5
    show player 14
    player_name "О, я не знаю... {b}Рокси{/b} не буде-"
    show player 5
    show crystal 6
    crys "Позвать {b} Рокси{/b}?"
    show crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show crystal 2 at right
    with dissolve
    crys "Ммм, теперь есть хороший способный человек!"
    show crystal 1
    show player 14
    player_name "Хех, Привет {b}Кристи{/b}..."
    show player 13
    show crystal 2
    crys "Почему бы тебе не выпить пива и посидеть со мной?"
    crys "Вы можете показать этот серебряный язык еще немного..."
    show crystal 1
    show player 14
    player_name "О, я не знаю... {b}Рокси{/b} не буде-"
    show player 5
    show crystal 2
    crys "{b}Рокси{/b} здесь нет."
    show crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Извините за беспокойство."
    show player 5
    show crystal 6
    crys "Пш, поговори, не утруждай меня ничем..."
    crys "На самом деле, почему бы тебе не сбегать в магазин и не купить мне свежую упаковку двенадцати?"
    crys "Ты сделаешь это, и мы сможем поговорить, пока твои уши не отвалятся."
    show crystal 5
    show player 17
    player_name "Хех, Неа, все в порядке."
    player_name "Я должен зайти внутрь и посмотреть на {b}Рокси{/b}."
    show player 13
    show crystal 6
    crys "Поступай как знаешь."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show crystal 1 with dissolve
    show player 10
    player_name "Ты знаешь, где она?"
    show player 5
    show crystal 2
    crys "Пф, я не знаю где она..."
    crys "Я никогда не смогу уследить за этой девчонкой."
    show crystal 1
    show player 10
    player_name "Серьёзно?"
    show player 5
    show crystal 2
    crys "Неблагодарное отродье, не говори мне ничего."
    crys "Её нужно похвалить! Что ей нужно..."
    show crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show crystal 4 with dissolve
    show player 12
    player_name "Где она?"
    show player 5
    show crystal 2 with dissolve
    crys "Черт, если я знаю."
    crys "Если она не {b}в школе{/b}, то я полагаю, что она вероятно {b}на пляже{/b}."
    crys "Клянусь, эта девушка наполовину русалка!"
    show crystal 1
    show player 17
    player_name "Хех, может быть..."
    show player 13
    return

label button_crystal_roxxys_mom:
    show crystal 1 with dissolve
    show player 10
    player_name "Так вы {b}Мама Рокси{/b}?"
    show player 5
    show crystal 2
    crys "Это верно."
    crys "Разве ты не видишь сходство?"
    show crystal 1
    menu:
        "Да, я полагаю.":
            show player 12
            player_name "Теперь, когда вы упомянули об этом, вы двое очень похожи."
            show player 5
            show crystal 2
            crys "Да, ей очень повезло, что она пошла за мной."
            crys "Ее отец был уродлив, как грех!"
            show crystal 1
            player_name "..."
            show crystal 2b
            crys "Хахаха!"
            show crystal 1
            jump roxmom_dialogue_repeat
        "Ты выглядишь такой молодой!":
            show player 12
            player_name "Я вижу сходство, но ты выглядишь слишком молодой, чтобы быть мамой Рокси."
            show player 10
            player_name "Ты уверен, что ты не ее сестра?"
            show player 5
            show crystal 2
            crys "Ну что ж, если у тебя нет серебряного языка!"
            crys "Думаю, именно так ты привлек внимание моей дочери?"
            show crystal 1
            show player 10
            player_name "Ну, Я-"
            show player 5
            show crystal 2
            crys "Не хочу тебя расстраивать, слизняк... Но чтобы удержать ее, нужно больше, чем просто болтовня."
            crys "Я воспитала ее правильно, ты заметил?"
            crys "Показала ей, что ценность мужчины в его действиях, а не в его словах!"
            show crystal 1
            player_name "..."
            show crystal 2
            crys "Если ты не можешь должным образом заботиться о моей девочке, тогда тебе лучше двигаться дальше, детка."
            show crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "А {b}Рокси{/b} занята?"
    show player 3
    show crystal 6
    crys "Пф, я сомневаюсь..."
    crys "Вероятно, она просто сидит на этом чертовом телефоне."
    show crystal 5
    show player 12 with dissolve
    player_name "Так что я могу просто зайти и увидеть ее?"
    show player 5
    show crystal 11
    crys "... Ты ждешь, что я тебя остановлю или что-то вроде того?"
    show crystal 10
    show player 10
    player_name "Я не-"
    show player 11
    show crystal 6
    crys "Боже правый, малыш."
    crys "Выразите пару и заходите туда уже!"
    hide crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Ты счастливы быть дома?"
    show player 5
    show crystal 2
    crys "Черт возьми я!"
    crys "Это место может быть дерьмовой дырой, но оно чертовски лучше тюремной камеры, я скажу тебе это бесплатно!"
    crys "Думаю, я должна поблагодарить тебя за то, что ты вытащил меня оттуда?"
    show crystal 4 with dissolve
    show player 14
    player_name "О, нет необходимости благодарить. Я был просто счастлив помочь."
    show player 13
    show crystal 2 with dissolve
    crys "Хех, да... Окей."
    crys "Если ты так говоришь, Слик."
    crys "Предложение стоит, если вы передумаете..."
    crys "Я могу РЕАЛЬНО поблагодарить ... Знаешь, что я имею в виду?"
    show crystal 1
    show player 5
    player_name "... {b}*Глоток*{/b}"
    show crystal 2
    crys "Хехехе."
    return

label button_crystal_should_go_evening:
    show player 14
    player_name "Я, вероятно, должен идти..."
    show player 13
    show crystal 6
    crys "Да, думаю, ты права насчет этого.."
    crys "Позаботься о моей девочке, слышишь?"
    show crystal 5
    show player 14
    player_name "Да, мэм."
    hide player with dissolve
    pause
    show crystal 6
    crys "Хахаха, \"мэм...\""
    crys "Это убивает меня каждый раз!"
    hide crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "Наверное, мне стоит пойти и найти {b}Рокси{/b}."
    show player 13
    show crystal 2
    crys "Ну, тебе не обязательно убегать сейчас...."
    crys "Я с радостью составлю тебе компанию, пока она не вернется."
    show crystal 1
    show player 14
    player_name "Хех, нет, все в порядке. Я бы не хотел вас беспокоить."
    show player 13
    show crystal 2
    crys "Пф, не беспокоить."
    crys "Я знаю несколько способов скоротать время...."
    show crystal 1
    show player 3 with dissolve
    player_name "{b}*Глоток*{/b}"
    show player 29
    player_name "Я... я... .. Увидимся, {b}Кристи{/b}."
    show player 3
    show crystal 2
    crys "Поступай как знаешь."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Да, она здесь?"
    show player 13
    show crystal 6
    crys "О, да, она там..."
    show crystal 11
    crys "Наверное, треплется по телефону, как обычно."
    crys "Если бы я знала, я клянусь, это не было бы приковано к моей девочке..."
    show crystal 5
    show player 17
    player_name "Хех, да."
    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
