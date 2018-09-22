label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Что я должен был снова сделать?"
    show player 5
    show teacher 5
    bis "{i}Вы забыли{/i}?"
    bis "Вы должны убедить {b}Рокси{/b} показать экзамены."
    bis "В противном случае средняя точка уклона всего класса будет страдать."
    show teacher 4
    show player 14
    player_name "Ох, хорошо!"
    player_name "Не переживайте, {b}Мисс биссетта{/b}!"
    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Мисс биссетта{/b}?"
    show player 13
    show teacher 5
    bis "{i}Да{/i}?"
    show teacher 4
    show player 14
    player_name "Я убедил {b}Рокси{/b} показать мне тест!"
    show player 13
    show teacher 2
    bis "{i}Точно{/i}!?"
    show teacher 1
    show player 17
    player_name "Да!"
    show teacher 25 zorder 1 with dissolve

    bis "{i}Ты спасаешь мою жизнь{/i}!"
    show teacher 26 with dissolve
    bis "Что бы я без тебя делала?!"
    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "Хех, это не большое дело..."
    show player 13
    show teacher 16
    with dissolve
    bis "Теперь не забудьте изучить слова, которые мы узнали за наши прошлые задания, хорошо?"
    show teacher 17
    show player 14
    player_name "Хорошо! Не переживайте!"
    show player 13
    show teacher 16
    bis "{i}Очень хорошо{/i}! На следующем уроке у нас будет тест."
    show teacher 17
    show player 14
    player_name "Хорошо, {b}Мисс биссетта{/b}!"
    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bis "{i}Привет{/i}, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Привет, {b}Мисс биссетта{/b}."
    show player 13
    show teacher 2
    bis "С чем я могу вам помочь?"
    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "Я взволнован пробовать вино, {b}Мисс биссетта{/b}."
    show player 13
    show teacher 12
    bis "{i}О да, мой красивый мужчина{/i}!"
    bis "Мы сегодня вечером будем дегустировать многое, правда?"
    show teacher 13
    show player 29 with dissolve
    player_name "*Глоток* Д-да..."
    show player 14
    show teacher 3
    bis "{i}Очень хорошо{/i}, Я хочу видеть вас в моем кабинете сегодня вечером."
    show teacher 13
    show player 14 with dissolve
    player_name "Хорошо!"
    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "Я не думаю, что мне нужно что-нибудь прямо сейчас."
    show player 13
    show teacher 2
    bis "{i}Очень хорошо{/i}!"
    show teacher 1
    show player 36 with dissolve
    player_name "Пока!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
