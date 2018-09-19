label consumr_quest10_not_completed:
    scene consumr
    show player 4 with dissolve
    player_name "( There must quite a few types of pesticides in here. )"
    show player 10
    player_name "( I'm not sure what kind I need. )"
    player_name "( I should probably ask the {b}store clerk{/b} like {b}Diane{/b} suggested. )"
    hide player with dissolve
    return

label consumr_okita_get_ingredients:
    call expression game.dialog_select("consumr_okita_get_ingredients_pre")
    if M_okita.get("talked with veronica"):
        call expression game.dialog_select("consumr_okita_get_ingredients_talked_with_veronica")
    return

label consumr_okita_get_ingredients_pre:
    scene location_mall_consumr_day_blur
    show player 2
    with dissolve
    player_name "Okita said that {b}Vegetable Stock{/b} would work best as the base liquid."
    return

label consumr_okita_get_ingredients_talked_with_veronica:
    show player 10
    player_name "... But they only have {b}Chicken Stock{/b}."
    player_name "I guess we'll have to make do with the {b}Chicken Stock{/b}."
    show player 2
    player_name "I should {b}buy{/b} some and get it back to Okita."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
