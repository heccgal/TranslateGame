label button_grace_mia_get_tattoo:
    scene tattoo_indoor_c
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace 2 at right
    show tattoo_desk at right
    with dissolve
    grace "Эй там!"
    grace "Вы здесь для встречи?"
    return

label button_grace_generic:
    show player 13 at left
    show grace 2 at right
    show tattoo_desk at right
    with dissolve
    grace "Эй там!"
    grace "Вы здесь для встречи?"
    return

label button_grace_tattoo:
    show mia 10f
    mia "Я бы хотела сделать татуировку... Сейчас."
    show mia 7f
    show grace 2
    grace "Сейчас? Я вижу..."
    show grace 3
    grace "Вы имеете в виду дизайн?"
    show grace 1
    show mia 30f at Position (xoffset=64) with dissolve
    mia "Мой друг нарисовал это для меня, и я хочу сделать это сегодня!"
    show mia 7f
    show grace 5
    with dissolve
    grace "Хмм..."
    show grace 6
    grace "Ты уверена, что хочешь этого?"
    grace "Татуировки постоянны, так что я должна убедиться, что мои клиенты знают, во что ввязываются!"
    show grace 7
    show mia 10f
    mia "Я думала об этом долгое время... Да, я действительно этого хочу."
    show mia 7f
    show grace 6
    grace "Хорошо, дорогая. Но, это не дешево!"
    show grace 7
    show player 14
    player_name "Сколько это будет стоить?"
    show player 13
    show grace 5
    grace "Для такого размера... с цветами... Около {b}$400{/b}."
    show grace 7
    show player 22
    show mia 12f
    mia "!!!"
    mia "Черт... Я думаю, что у меня есть только {b}$200{/b}..."
    show mia 8f
    show player 11
    player_name "..."
    show player 10
    player_name "Тебе не хватает?"
    show player 5
    show mia 12 with dissolve
    mia "Нет, это все, что мне удалось накопить."
    mia "Как ты думаешь, что мне делать?"
    show mia 8
    return

label button_grace_tattoo_help:
    show player 14
    player_name "Я позабочусь об остальном."
    show player 13
    show mia 12
    mia "Серьёзно?!"
    show mia 7
    show player 14
    player_name "Почему нет."
    player_name "Я работаю в последнее время, так что у меня есть немного денег..."
    show player 17
    player_name "...И это ради благого дела!"
    show player 13
    show mia 10
    mia "Это очень мило с твоей стороны..."
    mia "...И я позабочусь о том, чтобы вернуть тебе долг!"
    show mia 7
    show player 17
    player_name "Все в порядке, ха-ха."
    show player 13
    show grace 6
    grace "Так?"
    show mia 7f with dissolve
    grace "Готовы начать?"
    show grace 7
    show mia 10f
    mia "Я готова!"
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve

    scene tattoo_cs01
    show text "Потребовалось некоторое время, чтобы закончить работу.\nЯ очень нервничал за {b}Мию{/b}...\n...Но, оказалось, она была в порядке все время!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide tattoo_cs01
    with dissolve

    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace 2 at right
    with dissolve
    grace "Все сделано!"
    grace "Надеюсь, вам понравится."
    show grace 1
    show mia 10f
    mia "Это здорово! И это было не так больно, как я думала..."
    show mia 7f
    show grace 2
    grace "Убедитесь, что вы оставите повязку на нем, по крайней мере, на несколько дней."
    show grace 1
    show mia 10f
    mia "Хорошо, спасибо вам!"
    show mia 7f
    show grace 2
    grace "Пока, ребята."
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 7 right
    with dissolve
    show player 14
    player_name "Каково это?"
    show player 13
    show mia 12
    mia "Татуировка?"
    show mia 7
    show player 14
    player_name "Да."
    show player 13
    show mia 12
    mia "Все нормально... У него просто покалывание."
    show mia 10
    mia "И я рада, что сделала это... Наконец-то я могу сказать, что сделала то, что хотела."
    show mia 7
    show player 10
    player_name "Ты боишься, что твоя мама может узнать?"
    show player 5
    show mia 9
    mia "Надеюсь, нет, но это в хорошо скрытом месте, ха-ха."
    show mia 7
    show player 17
    player_name "Я думаю, это круто, что ты это сделала."
    show player 18
    show mia 10
    mia "Спасибо, {b}[firstname]{/b}. Я рада, что ты пошёл со мной."
    show player 13
    mia "Я должна идти. Пока моя мама не начала что-то подозревать..."
    show mia 7
    show player 14
    player_name "Ладно, увидимся в школе!"
    show player 13
    show mia 10
    mia "Пока."
    hide player
    hide mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    show player 10
    player_name "Может, нам стоит зайти попозже?"
    show player 5
    mia "..."
    show mia 12
    mia "Полагаю, мы должны это сделать."
    show mia 8
    show player 10
    player_name "Все нормально. Мы всегда можем вернуться в другой раз."
    show player 5
    show mia 12
    mia "Ты прав."
    show mia 8
    show player 10
    player_name "Прости, что не смогли сделать татуировку сегодня..."
    show player 5
    show mia 12
    mia "Все нормально. Я должна вернуться домой."
    show mia 8
    show player 10
    player_name "Хорошо, увидимся позже."
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene location_tattoo_indoor_closeup
    show player 10 zorder 3 at left
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace 1 zorder 0 at right
    player_name "Могу я спросить тебя кое о чем?"
    show player 11
    show grace 2
    grace "Конечно!"
    show player 10
    show grace 1
    player_name "Ну, вы видите..."
    show player 11
    pause
    show player 10
    player_name "Дело..."
    show player 11
    grace "..."
    show player 10
    player_name "... Вот в чем дело..."
    show player 11
    show eve 2f zorder 2 at Position(xpos=0.35, ypos=1.0) with dissolve
    eve "Господи, выкладывай уже, {b}[firstname]{/b}!"
    show eve 1bf with dissolve
    eve "Что, Раггеди Энн?"
    show eve 5f with dissolve
    show grace 4
    grace "Хех, не много."
    show grace 2
    grace "Держишься подальше от неприятностей, сопляк?"
    show eve 6bf
    show grace 1
    eve "Конечно, нет."
    show player 1
    show eve 5f
    show grace 4
    grace "Хехе."
    show eve 2f
    show grace 1
    eve "Смотри, {b}[firstname]{/b} здесь нужны чернила."
    show eve 5f
    show grace 2
    grace "О, ты думаешь сделать там татуировку, жеребец?"
    show player 11
    show grace 1
    player_name "..."
    show eve 1bf with dissolve
    eve "Нет, нет, нет. Ему нужны настоящие чернила! Как в бутылках, дура!"
    show eve 6bf
    eve "Извини, она может быть немного медленной."
    show eve 5f
    show grace 3
    grace "Эй! Я слышал это!"
    show eve 6f
    show grace 1
    eve "Да, я сказал это громко..."
    show eve 5f
    show grace 4
    grace "Ха-ха, умная задница."
    show eve 6f
    show grace 1
    eve "Любуйся, сестренка!"
    show eve 5f
    show grace 2
    grace "Да, конечно. Тебе повезло, что ты симпатичный."
    show player 1
    show grace 1
    show eve 1bf with dissolve
    eve "Да, не так ли?"
    show grace 2
    show eve 5f with dissolve
    grace "Итак, сколько чернил вам нужно, {b}[firstname]{/b}?"
    show player 2
    show grace 1
    player_name "Ммм, я не уверен."
    player_name "Достаточно, чтобы сделать одну картинку."
    show player 1
    show grace 2
    grace "Ахххх, художник, да?"
    show grace 4
    grace "Figures, the first guy {b}Eve{/b} brings home is an artist."
    show player 11
    show grace 1
    show eve 6bf
    eve "Tch, better than that biker freak you had hanging around here in high school."
    show eve 1f
    show grace 4
    grace "Хех, вы не получите никаких аргументов..."
    show grace 2
    grace "Будет ли достаточно одной бутылки каждого основного цвета?"
    show grace 3
    grace "Полагаю, ты умеешь смешивать?"
    show player 10
    show grace 1
    player_name "Смешивать?"
    show player 11
    show eve 2f
    eve "Да, ты понимаешь? Синий и красный дают пурпурный."
    eve "Желтый и синий дают зеленый."
    show player 2
    show eve 1f
    player_name "О да, как цветное колесо, правильно?"
    show player 1
    show grace 2
    grace "Да, именно."
    show grace 3
    grace "Я думаю, единственный вопрос сейчас, что ты собираешься сделать для меня?"
    show grace 1
    show player 10
    player_name "Ох, ох. Не знаю. Что ты хочешь от меня?"
    show grace 3
    show player 11
    grace "Вы случайно не заметили граффити на стене здания, когда вошли?"
    show player 10
    show grace 1
    player_name "... Да, это довольно трудно пропустить."
    show player 11
    show grace 2
    grace "Я дам тебе краски, если ты сможешь смыть их для меня."
    show grace 1
    show eve 2f
    eve "Серьёзно?"
    show player 2
    show eve 1f
    player_name "Я могу это сделать!"
    show player 1
    show eve 6bf
    grace "Пффф, какая трата времени!"
    show eve 1f
    show player 11
    player_name "..."
    show eve 1bf with dissolve
    eve "Это снова будет помечено..."
    show eve 1f
    show grace 8
    with dissolve
    grace "Ну, это твои тупые гребаные друзья, которые продолжают это делать!"
    grace "Ты должен сказать этим маленьким сучкам, что я надеру им задницы, если это повторится!"
    show grace 9
    show player 10
    player_name "Мда, я не знал, что твоя {b}сестра{/b} была такой плохой задницей!"
    show eve 6f
    show player 11
    eve "Хех, ты понятия не имеешь."
    show eve 5f
    show grace 8
    grace "Я не знаю, почему ты тусуешься с этими придурками в любом случае..."
    show eve 2f
    show grace 9
    eve "... Если вы собираешься шантажировать {b}[firstname] {/b} работой по дому. Ты могла бы, по крайней мере, заставить его сделать что-то полезное."
    eve "Как, может, ты переместила все это тяжелое дерьмо, которое ты заказала в задней комнате?"
    show eve 6bf
    show grace 1 with dissolve
    eve "Я не хочу трахаться с этим дерьмом!"
    show eve 5f
    show grace 3
    grace "Хм, я полагаю, что это неплохая идея."
    show grace 4
    grace "... Особенно, если это заставит тебя заткнуться о своей вагине! Ух!"
    show grace 1
    show eve 6bf
    eve "... Сука."
    show eve 5f
    show grace 4
    grace "Хахаха, не притворяйся, что тебе не нравится насилие."
    show grace 1
    show eve 6bf
    eve "Да, да..."
    show eve 2f
    eve "Если ты простишь меня, {b}[firstname]{/b}."
    show player 1
    eve "Я лучше пойду предупрежу ребят, что {b}Грейс{/b} снова на пути войны."
    show eve 1f
    show grace 4
    grace "Чертовски верно!"
    show grace 1
    show eve 6f
    eve "Увидимся, сестренка!"
    hide eve
    with dissolve
    show grace 2
    grace "Ящики {b}находятся прямо перед счетчиком{/b}. Просто передвинь их назад для меня, и краска твоя."
    show grace 1
    show player 2
    player_name "Звучит неплохо!"
    return

label button_grace_you_look_familiar:
    show player 10
    player_name "Ты знаешь... Я думаю..."
    show player 12
    player_name "Ухх."
    show player 34
    show grace 3
    grace "Все в порядке?"
    show grace 1
    show player 30
    player_name "Извините, но вы выглядите... знакомой."
    show player 5
    show grace 3
    grace "Да?"
    show grace 2
    grace "Хм... Может, ты думаешь о моей сестре?"
    show grace 1
    show player 12
    player_name "Сестре?"
    show player 11
    show grace 3
    grace "Моя маленькая сестренка? {b}Ева{/b}?"
    show grace 1
    show player 38 with dissolve
    player_name "О! Ну конечно!"
    show player 14 with dissolve
    player_name "Теперь я вижу связь."
    show player 13
    show grace 4
    grace "Ха-ха."
    show grace 2
    grace "В любом случае, я могу что-нибудь для тебя сделать?"
    return

label button_grace_nothing:
    show player 14
    player_name "Я просто осматриваюсь."
    show player 13
    show grace 2
    grace "Круто! Взглянуть."
    grace "Я делаю все стили и проекты, представленные в моем магазине!"
    grace "Просто дай мне знать, если ты когда-нибудь подумаешь о чем-нибудь, и мы договоримся о встрече!"
    show grace 1
    show player 14
    player_name "Хорошо, спасибо!"
    show player 13
    show grace 2
    grace "Увидимся."
    hide grace
    hide mia
    hide player
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
