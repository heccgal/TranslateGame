label helen_dialogue_mia_route:
    show helen 50 at right
    show player 14 at left
    with dissolve
    player_name "Привет, {b}Хелен{/b}."
    show player 13
    show helen 51
    helen "Привет, {b}[firstname]{/b}."
    show helen 50
    show player 14
    player_name "Как дела в последнее время?"
    show player 13
    show helen 51
    helen "Намного лучше."
    helen "Так приятно осознавать, что я очистилась."
    helen "Церковное таинство действительно помогло улучшить мои отношения с {b}Гарольдом{/b}."
    show helen 24
    helen "Но ... никто больше не должен об этом знать."
    show helen 50
    show player 21
    player_name "Хех... Да, я предполагаю."
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "Для меня это немного размыто..."
    show player 13
    hide xtra 21
    with dissolve
    show helen 51
    helen "Еще раз спасибо за помощь. Наша семья ценит то, что ты сделал... и не сделал этого."
    helen "Я должна тебя отпустить. Ты, наверное, хочешь потусоваться с {b}Мией{/b}."
    show helen 50
    show player 14
    player_name "Да."
    show player 36 with dissolve
    player_name "Увидимся позже!"
    return

label helen_dialogue_helen_end_intro:
    show player 13 at left
    show helen 63 at right
    with dissolve
    helen "Привет, {b}[firstname]{/b}."
    show helen 62
    show player 14
    player_name "Привет, {b}Хелен{/b}."
    show player 13
    show helen 63
    helen "Ты пришел очистить моё грешное тело?"
    show helen 62
    return

label helen_dialogue_helen_end_leave:
    show player 10
    player_name "Спасибо {b}Хелен{/b}..."
    player_name "Может, в другой раз."
    show player 12
    player_name "У меня есть...другие вещи, которые нужно сделать."
    show player 5
    show helen 48
    helen "Ох..."
    helen "Я действительно надеялась служить тебе..."
    helen "Не стесняйтесь навещать меня чаще."
    show helen 47
    show player 12
    player_name "Конечно... Я дам тебе знать., {b}Хелен{/b}."
    return

label helen_dialogue_helen_end_sex:
    show player 26
    player_name "Да."
    show player 13
    show helen 63
    helen "Спасибо {b}Господу{/b}!"
    helen "Я была занята молитвой о твоем скором возвращении."
    helen "Снимай одежду и я впущу немного света."
    helen "Теперь ложись на спину, чтобы я мог позволить свету {b}бога{/b} сиять на меня."
    hide helen
    scene mia_house_helen_window1
    show player helen_sex 59
    with fade
    pause
    scene mia_house_helen_window2
    show player helen_sex 59
    pause
    scene mia_house_helen_window3
    show player helen_sex 59
    show helen 54 with dissolve
    return

label helen_dialogue_change_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Хелен{/b}!"
    show player 5
    helen "..."
    show helen 3
    helen "Привет, {b}[firstname]{/b}."
    show helen 1
    show player 12
    player_name "Кажется, ты в лучшем настроении, чем обычно!"
    show player 5
    show helen 2
    helen "Я стараюсь быть таким человеком... открытым... даже с такими людьми, как вы."
    show helen 1
    show player 14
    player_name "Это здорово."
    show player 13
    show helen 2
    helen "Чего именно вы хотите добиться?"
    show helen 1
    return

label helen_dialogue_change_harold:
    show player 10
    player_name "Вы говорили с {b}Гарольдом{/b}?"
    show player 11
    show helen 4
    helen "Нет..."
    show helen 3
    helen "...Все находится в руках {b}Бога{/b}."
    show helen 1
    show player 12
    player_name "Да?"
    show player 5
    show helen 4
    helen "Вы должны уйти сейчас..."
    return

label helen_dialogue_change_mia_clues:
    show player 10
    player_name "Где, вы сказали, я могу найти подсказки о местонахождении {b}Гарольда{/b}?"
    show player 5
    show helen 24 with dissolve
    helen "Начните с допроса его коллег в {b}полицейском участке{/b}..."
    helen "...И найди {b}руководителя{/b} возле его рабочего места."
    show helen 23
    show player 12
    player_name "Полагаю, я могу поспрашивать, где он может быть..."
    show player 5
    show helen 24
    helen "Спасибо тебе..."
    return

label helen_dialogue_change_corset:
    show player 10
    player_name "Еще раз, какое белье ты искала?"
    show player 5
    show helen 28
    helen "Я всегда хотела носить корсет... и {b}Гарольд{/b} любит видеть меня в красном."
    show helen 23
    show player 12
    player_name "Тогда {b}красный корсет{/b}?"
    show player 5
    show helen 24
    helen "Если сможешь найти, принеси мне его сюда."
    show helen 23
    show player 10
    player_name "Я постараюсь..."
    show player 5
    show helen 28
    helen "Спасибо тебе, {b}[firstname]{/b}."
    return

label helen_dialogue_change_angelica:
    show player 10
    player_name "Как проходит причастие?"
    player_name "Ты и {b}Сестра Анджелика {/b}, есть какой-то прогресс?"
    show player 5
    show helen 27
    helen "..."
    show helen 24
    helen "Я... Думаю, у нас все хорошо..."
    show helen 28
    helen "...{b}Сестра Анжелика{/b} очень... основательна и более осведомленна, чем я."
    show helen 23
    show player 10
    player_name "Я вижу..."
    player_name "Дайте мне знать, если вам понадобится моя помощь!"
    return

label helen_dialogue_change_whipping:
    show player 10
    player_name "Ты в порядке? До сих пор не могу поверить, что видела, как {b}Сестра Анжелика{/b} хлестала тебя."
    show player 5
    show helen 25
    helen "..."
    show helen 28
    helen "Немного побаливает, но..."
    show helen 24
    helen "...Я грешница {b}[firstname]{/b}. И... Мне это нужно."
    show helen 28
    helen "Если это поможет мне избавиться от греховности, я должена это сделать."
    show helen 27
    show player 37 with dissolve
    player_name "..."
    show player 10 with dissolve
    player_name "Хорошо, я полагаю."
    player_name "Если вам нужна помощь или вы хотите, дайте мне знать."
    player_name "Я сделаю все возможное, чтобы помочь вам."
    show player 5
    show helen 24
    helen "Спасибо, {b}[firstname]{/b}. Ты мне очень помогаешь."
    helen "{b}Сестра Анжелика{/b} помогает мне понять, что именно моя греховность привела ко всем моим проблемам в жизни."
    helen "Мне нужно закончить это обучение и, возможно, я буду такой же полезной и милой...как ты."
    show helen 27
    show player 37 with dissolve
    player_name "{b}Хелен{/b}..."
    show helen 23
    show player 10 with dissolve
    player_name "Я не думаю, что ты плохая."
    show player 5
    show helen 28
    helen "Спасибо, {b}[firstname]{/b}."
    return

label helen_dialogue_change_ritual:
    show player 10
    player_name "Вы знаете... В последнее время я все больше времени провожу в церкви..."
    show player 5
    show helen 2
    helen "...У вас есть?"
    show helen 1
    show player 14
    player_name "Да!"
    show player 10
    player_name "Я пытаюсь узнать больше... вы знаете... о {b}Боге{/b} и все такое!"
    show player 5
    show helen 2
    helen "Хмм... Серьёзно?"
    show helen 1
    show player 12
    player_name "Знаете ли вы, что, подстраховаться... есть причастие поздней ночью?"
    show player 5
    show helen 4
    helen "Ночные службы?"
    show helen 1
    show player 10
    player_name "Да! Они похожи... ритуалы?"
    show player 5
    show helen 4
    helen "Я никогда не знала об этом, и я посещаю нашу церковь уже более 20 лет."
    show helen 2
    helen "Почему я никогда не слышала о таком... причастие?"
    show helen 1
    return

label helen_dialogue_change_ritual_stat_fail:
    show player 10
    player_name "[chr_warn]Я не уверена, что знаю, Эмм... Я не могу объяснить..."
    show player 5
    show helen 4
    helen "[chr_warn]Похоже, это не очень серьезно..."
    show helen 1
    show player 24
    player_name "[chr_warn]..."
    show player 25
    player_name "[chr_warn]Ну, я тоже еще не ушел, так что я не знаю много о том, что это включает."
    show player 24
    show helen 4
    helen "[chr_warn]Я не уверен, что я вполне понимаю цель всего этого..."
    show helen 2
    helen "[chr_warn]...Но удачи с вашей волонтерской работой и дайте мне знать, когда у вас будет больше деталей."
    show helen 1
    show player 25
    player_name "[chr_warn]Ох... Окей."
    return

label helen_dialogue_change_ritual_stat_pass:
    show player 12
    player_name "{b}Сестра Анжелика{/b} за главного!"
    player_name "Она сказала, что я должен распространить информацию и найти... Эхх... верные последователи присоединиться к нам!"
    show player 14
    player_name "Я знаю, что ты очень надёжная..."
    show player 33
    player_name "И за 20 лет в церкви, я удивлен, что ты никогда не посещала вечерние таинства. Может быть, я-"
    show helen 4
    helen "Подожди."
    show helen 1
    show player 13
    player_name "..."
    show helen 4
    helen "Ты присутствуешь на этом?"
    show helen 1
    show player 14
    player_name "Давайте просто скажем, что эмм... Мне нравится заниматься волонтерской работой для церкви!"
    show player 13
    show helen 2
    helen "Должна сказать, Я приятно удивлена вашей преданностью нашей Церкви..."
    show helen 4
    helen "...Я просто не уверена, что понимаю цель всего этого."
    show helen 1
    show player 14
    player_name "{b}Сестра Анжелика{/b}, кажется, думает, что это отличный способ отпустить грехи и очистить душу..."
    show player 13
    show helen 3
    helen "Хмм..."
    show helen 2
    helen "Вы говорите, это ночью?"
    show helen 1
    show player 14
    player_name "Да, мэм! Это Эхх... в монашеской палате!"
    show player 13
    show helen 3
    helen "Хорошо, ты убедил меня."
    show helen 2
    helen "Я пойду с тобой в гости к {b}Сестре Анжелике{/b} ночью и посмотрю, что это такое..."
    show helen 1
    show player 14
    player_name "Звучит здорово!"
    return

label helen_dialogue_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Хелен{/b}!"
    show player 5
    show helen 4
    helen "Опять ты."
    helen "Чего именно вы хотите добиться?!"
    show helen 1
    return

label helen_dialogue_harold:
    show player 10
    player_name "Вы говорили с {b}Гарольдом{/b}?"
    show player 11
    show helen 5
    helen "Наша ситуация вас не касается."
    show helen 4
    helen "Кроме того, сейчас мы ничего не можем сделать..."
    show helen 3
    helen "...все находится в руках {b}Бога{/b}!"
    show helen 1
    show player 12
    player_name "Да?"
    show player 5
    show helen 4
    helen "Вы должны уйти сейчас..."
    return

label helen_dialogue_leave:
    show player 5 at left
    show helen 2 at right
    with dissolve
    helen "!!!"
    show helen 4
    helen "Что ты здесь делаешь?!"
    show player 22
    helen "Это и есть моя спальня! Убирайся!!"
    show helen 6
    show player 10
    player_name "Простите!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
