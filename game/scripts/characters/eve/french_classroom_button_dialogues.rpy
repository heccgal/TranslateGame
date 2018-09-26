label eve_classroom_dialogue_eve_intro:
    show evedesk 1 at left with dissolve
    eve "Поразительно... Я думала, что ты точно мертв!"
    show evedesk 2
    player_name "Что?... Что ты имеешь в виду?"
    show evedesk 1
    eve "Не знаю... Ты пропал на весь месяц, и люди начали выдумывать слухи о том, как твоя семья была убита или что-то вроде того..."
    show evedesk 3
    player_name "Тьфу... Ничего подобного!"
    show evedesk 4
    eve "Я так и думала. Люди просто любят поговорить, а эта школа - просто шутка."
    eve "Я рада, что наш последний год почти закончился..."
    show evedesk 5
    player_name "Да, я знаю, что ты имеешь в виду."
    show evedesk 6
    eve "Тебе стоит как-нибудь потусоваться с нами в парке... Избегать всех этих идиотов в школе и расслабляться, понимаешь?"
    show evedesk 5
    eve "Убедитесь, что ты придёшь в {b}ночь{/b}... обычно, когда мы выходим на улицу."
    player_name "Эхх... Думаю, я могу прийти как-нибудь вечером."
    show evedesk 6
    eve "Это зависит только от тебя. Делай все, что хочешь!"
    show evedesk 4
    eve "О, Эй, ты слышал объявление {b}Мисс Биссет{/b} о специальном вознаграждении?"
    show evedesk 1
    eve "Или ты проспала эту часть?"
    show evedesk 3
    player_name "Эй! Я проснулась... для той части."
    show evedesk 4
    eve "Интересно, какая будет награда."
    eve "Она не очень много об этом говорила. Наверное, что-то глупое."
    eve "Я уже делаю довольно хорошо, так что даже не стоит пытаться."
    show evedesk 2
    player_name "Почему нет?"
    show evedesk 6
    eve "Как переход от четверки к четверке значительно улучшился?"
    eve "Ты с большей вероятностью выиграешь..."
    show evedesk 5
    player_name "Я?"
    show evedesk 1
    eve "Ну, конечно... или я не права?"
    eve "У тебя есть много возможностей для улучшения."
    show evedesk 6
    eve "Плюс, {b}Мисс Биссетт{/b} в любом случае, даёт одолжение парням."
    eve "Тебе стоит серьезно подумать об этом."
    hide evedesk with dissolve
    return

label eve_classroom_dialogue_intro:
    show evedesk 4 at left with dissolve
    eve "Привет, {b}[firstname]{/b}."
    show evedesk 5
    player_name "Привет, {b}Ева{/b}."
    show evedesk 4
    eve "Что случилось?"
    return

label eve_classroom_dialogue_talent_show_help:
    show evedesk 5
    player_name "Ты играешь на каких-нибудь инструментах?"
    show evedesk 4
    eve "Нет, я не играю. Я всегда хотела научиться, но у меня просто не было времени, понимаешь?"
    show evedesk 5
    player_name "Хорошо, а как насчет пения?"
    show evedesk 1
    eve "Ох, эмм..."
    show evedesk 4
    eve "Да, мне нравится петь, наверное. Не знаю, насколько я хороша."
    show evedesk 5
    player_name "Бьюсь об заклад! Ты должна подписаться на шоу талантов со мной!"
    show evedesk 3
    player_name "Нам действительно не хватает добровольцев."
    show evedesk 1
    eve "... Да, я не знаю."
    eve "Ты хочешь, чтобы я пела перед всей школой? Звучит довольно неловко."
    eve "... И я не пела некоторое время. С тех пор, как сломалась моя караоке-машина."
    eve "У меня совсем нет практики."
    show evedesk 5
    player_name "Хмм..."
    player_name "Ты знаешь, я думаю, что мой друг {b}Эрик{/b} имеет {b}караоке{/b} в своем подвале."
    show evedesk 4
    eve "О, правда?"
    show evedesk 5
    player_name "Точно! Приходи как-нибудь и потренируйся!"
    show evedesk 4
    eve "Ты хочешь, чтобы я спела для тебя и твоего друга?"
    show evedesk 5
    player_name "Нет, мы можем петь все вместе! Давай, сделаем это сегодня вечером, будет весело!"
    eve "..."
    show evedesk 4
    eve "Ладно, думаю, я могу заехать ненадолго."
    show evedesk 5
    player_name "Потрясающе! {b}Я буду ждать тебя в доме Эрика {/b} сегодня вечером."
    return

label eve_classroom_dialogue_adehsive:
    show evedesk 5
    player_name "Какой был план?"
    show evedesk 4
    eve "Ты должен встретиться с {b}Кевином{/b} в {b}научной лаборатории после занятий{/b}."
    eve "Запомнил?"
    show evedesk 5
    player_name "Да, это верно. Спасибо, {b}Ева{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show evedesk 5
    player_name "Ты собираешься записаться на репетиторство к {b}Мисс Биссет{/b}?"
    show evedesk 4
    eve "Я уже делаю довольно хорошо, так что даже не стоит пытаться."
    show evedesk 2
    player_name "Почему нет?"
    show evedesk 6
    eve "Как переход от четверки к четверке значительно улучшился?"
    eve "Ты с большей вероятностью выиграешь..."
    show evedesk 5
    player_name "Я?"
    show evedesk 1
    eve "Ну, конечно... или я не права?"
    eve "У тебя есть много возможностей для улучшения."
    show evedesk 6
    eve "Плюс, {b}Мисс Биссетт{/b} в любом случае, даёт одолжение парням."
    eve "Тебе стоит серьезно подумать об этом."
    return

label eve_classroom_dialogue_hang_out:
    show evedesk 5
    player_name "Где, говоришь, ты проводишь время?"
    show evedesk 4
    eve "Мои друзья и я тусуемся в {b}парке{/b}."
    eve "Просто убедитесь, что ты придёшь {b}ночью{/b}... обычно, когда мы выходим на улицу."
    show evedesk 5
    player_name "Хорошо. Я могу заскочить на одну ночь."
    show evedesk 6
    eve "Это зависит только от тебя. Делайте все, что хочешь!"
    return

label eve_classroom_dialogue_leave:
    show evedesk 5
    player_name "Ничего, просто хотел поздороваться."
    show evedesk 4
    eve "О. Тогда поговорим позже."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
