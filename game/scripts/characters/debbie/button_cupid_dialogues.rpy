label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Дорогой, ты что-нибудь нашёл?"
    show player 10
    show debbie 164
    player_name "Я все еще ищу."
    show player 5
    show debbie 166
    deb "Хехе, хорошо!"
    show debbie 165
    deb "Не смотри так серьезно. Это просто! Просто найди что-нибудь, что мне понравится..."
    show debbie 164
    pause
    hide debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Что-то {b}[deb_name]{/b} хочет? )"
    player_name "( Может, ожерелье? )"
    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Ладно, {b}[deb_name] {/b}. Как насчет этого?"
    hide xtra
    show player 1 with dissolve
    show debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show debbie 172
    deb "Ох, {b}[firstname]{/b}... Какое красивое {b}ожерелье{/b}."
    show debbie 170
    show player 14
    player_name "Тебе очень нравится?"
    show player 13
    show debbie 171
    deb "Я! У тебя отличный вкус, дорогой."
    show debbie 170
    show player 14
    player_name "Хех, спасибо {b}[deb_name]{/b}!"
    show player 13
    show debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show debbie 175
    pause 2
    show debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show debbie 165
    deb "Ну?"
    show player 14
    show debbie 164
    player_name "... хмм?"
    show player 13
    show debbie 166
    deb "Как я выгляжу?"
    show player 14
    show debbie 164
    player_name "Ты выглядишь прекрасно, {b}[deb_name]{/b}!"
    show player 13
    show debbie 166
    deb "Ох... Спасибо, Милый."
    show debbie 164
    deb "Хмм..."
    show debbie 165
    deb "Где зеркало, когда оно так нужно?"
    show debbie 164
    player_name "..."
    show player 14
    player_name "Наверное, в раздевалке..."
    show player 13
    show debbie 165
    deb "Хорошая мысль, милый!"
    deb "Я сейчас вернусь."
    hide debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Хорошо."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
