label tony_dialogue_pre:
    scene pizza_behind_c
    show xtra 12 zorder 2
    with None
    show maria 1 zorder 1 at left
    show tony 2 zorder 1 at Position(xpos=400)
    show player 1f zorder 3 at right
    with dissolve
    return

label tony_dialogue_deliver_pizzas_first:
    tony "Эй, малыш!"
    tony "Готов работать?"
    show tony 1
    show player 14f
    player_name "Конечно!"
    show tony 2
    show player 1f
    tony "Хорошо! Прежде чем мы начнем, убедитесь, что у вас есть велосипед или что - то еще, чтобы вы быстрее передвигались."
    tony "Затем возьмите эти коробки на прилавке, и доставить их по правильным адресам!"
    tony "О! Наши клиенты любят пиццу красивой и горячей."
    tony "Так что чем быстрее ты работаешь, тем больше я тебе плачу!"
    show tony 1
    show player 14f
    player_name "Звучит отлично, {b}Тони{/b}!"
    return

label tony_dialogue_deliver_pizzas_repeat:
    tony "Коробки прямо здесь, малыш!"
    return

label tony_dialogue_default:
    show tony 1f at right
    show player 10 at left
    tony "Тебе нужен велосипед для доставки пиццы, малыш!"
    show player 4
    player_name "( Бьюсь об заклад, я мог бы купить велосипед в {b}Консумере{/b}... )"
    show player 2
    player_name "Спасибо, Тони. Я возьму велосипед и вернусь!"
    show tony 2f
    tony "Ты сделаешь это, малыш!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
