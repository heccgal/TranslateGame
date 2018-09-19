label veronica_dialogue_pre:
    scene location_mall_consumr_closeup
    show player 1 at left
    show veronica 2 at right
    with dissolve
    vero "Welcome to {b}CONSUM-R{/b}! My name is {b}Veronica{/b}."
    show veronica 4
    vero "Is there anything I can help you with today?"
    show veronica 1
    return

label veronica_dialogue_vegatable_stock:
    show player 2
    player_name "I'm looking for {b}Vegetable Stock{/b}. Do you guys carry it?"
    show player 1
    show veronica 2
    vero "I'm afraid we're all sold out at the moment."
    show player 10
    show veronica 1
    player_name "Oh man..."
    show player 11
    show veronica 2
    vero "Would {b}Chicken Stock{/b} work? We have plenty of that."
    show player 10
    show veronica 1
    player_name "I don't know..."
    player_name "Is there a delivery coming soon or something?"
    show player 11
    show veronica 2
    vero "We get deliveries daily but I have no idea when that particular item will be restocked."
    show player 10
    show veronica 1
    player_name "Crap..."
    player_name "Alright, thank you."
    hide veronica with dissolve
    show player 10 with dissolve

    player_name "Hmm, I guess {b}Chicken Stock{/b} will have to do."
    show player 2
    player_name "I should buy some and take it to Okita."

    return

label veronica_dialogue_bug_spray:
    show player 4
    player_name "Uh..."
    show player 12
    player_name "I'm looking for pesticide?"
    show veronica 4
    show player 1
    vero "Ah, yes! We have a variety of pest repellent products!"
    show veronica 1
    show player 2
    player_name "Hmm... How about for insects?"
    show veronica 3
    show player 1
    vero "Well... There are many types of pesticides for insects..."
    show veronica 2
    show player 11
    vero "Do you know what type of bug you're dealing with?"
    show veronica 1
    show player 10
    player_name "I'm not quite sure what kind it is..."
    show veronica 3
    show player 13
    vero "Well, what does it {b}look like{/b}?"
    show veronica 1
    return

label veronica_dialogue_bug_spray_large_wings:
    show player 35
    player_name "It had a set of large wings..."
    show veronica 3
    show player 11
    vero "Hmm... Could be {b}grasshoppers{/b}..."
    show veronica 4
    show player 1
    vero "Get the spray can with a {b}red cap{/b}. It's called the {b}Bug Exterminator{/b}."
    show veronica 2
    vero "It should do the trick!"
    show veronica 1
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_bug_spray_pincers:
    show player 35
    player_name "It had large pincers..."
    show veronica 3
    show player 11
    vero "Hmm... Could be {b}earwigs{/b}... Nasty buggers!"
    show veronica 4
    show player 1
    vero "Get the spray can with a {b}green cap{/b}. It's called the {b}Bug Annihilator{/b}."
    show veronica 2
    vero "It should do the trick!"
    show veronica 1
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_bug_spray_white_spots:
    show player 35
    player_name "It had white spots on its shell..."
    show veronica 3
    show player 11
    vero "Hmm... Could be {b}beetles{/b}..."
    show veronica 4
    show player 1
    vero "Get the spray can with a {b}blue cap{/b}. It's called the {b}Bug Eradicator{/b}."
    show veronica 2
    vero "It should do the trick!"
    show veronica 1
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_leave:
    show player 2
    player_name "Uhm..."
    show player 17
    player_name "I think I'm fine, thanks!"
    show veronica 4
    show player 1
    vero "No problem!"
    show veronica 2
    vero "Just let me know if you need anything."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
