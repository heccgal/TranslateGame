label job_done_dialogue(earnings):
    $ renpy.checkpoint()
    if quest10 in quest_list and not infestation_done and player.has_item("annihilator"):
        scene black with dissolve
        with Pause(0.5)
        show expression Cutscene("garden_event01", "I began to spray the whole lot with green napalm...\n Emptied the entire can of spray on the nasty buggers...\nUntil nothing remained!") as cutscene with dissolve
        $ player.remove_item("annihilator")
        if player.has_item("exterminator"):
            $ player.remove_item("exterminator")

        if player.has_item("eradicator"):
            $ player.remove_item("eradicator")
        pause
        hide cutscene with dissolve

        scene black with dissolve
        with Pause(0.5)
        scene black
        with Dissolve(0.5)
        show unlock27 at truecenter with dissolve
        pause
        $ infestation_done = True
        $ aunt_dialogue_advance = True
        hide unlock27 with dissolve
        hide black
        $ game.main()

    if not garden_firsttime:
        scene black
        with Pause(0.5)
        call expression game.dialog_select("garden_firsttime_text")
        pause
        scene black with dissolve
        with Pause(0.5)
        $ garden_firsttime = True
    if quest10 in quest_list and not infestation_done:
        scene garden_dead
    else:

        scene garden
    if earnings > 0:
        show player 1 at left with dissolve
        show diane 2 at right with dissolve
        dia "Oh, wow! My garden looks absolutely gorgeous, {b}[firstname]{/b}!"
        show player 1 at left
        show diane 9 at right
        player_name "Yeah... I had to get rid of a lot of stuff..."
        show diane 15 at right
        show player 11 at left
        dia "Just look at that big, hard cucumber!"
        show diane 16 at right
        player_name "..."
        show diane 5 at right
        show player 13 at left
        dia "Thanks, Handsome! And come back soon!"
        hide player 13 at left with dissolve
        hide diane 5 at right with dissolve
    else:

        call expression game.dialog_select("garden_firsttime_fail")
    $ game.timer.tick()
    if earnings < 0:
        $ earnings = 0
    $ player.get_money(earnings)
    $ after_minigame = True
    $ garden_done += 1
    show unlock7 at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide unlock7
    with dissolve
    $ in_garden = True
    call expression game.dialog_select("garden_dialogue")

label garden_firsttime_text:
    show expression Cutscene("garden_firsttime_01", "{b}Diane{/b} went to lie down as I began digging up her garden.\n It was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    scene black with dissolve
    with Pause(0.5)
    show expression Cutscene("garden_firsttime_02", "As I worked, I noticed {b}Diane{/b} was watching me intently...\nI suppose she was just trying to make sure I did a good job.\nWe exchanged a few words here and there but mostly just small talk.\nHer eyes seemed fixed upon my sweat soaked body.") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    return

label garden_firsttime_fail:
    show player 5 at left with dissolve
    show diane 23 at right with dissolve
    dia "Hmm... There's some room for improvement."
    show diane 24 at right
    show player 24 at left
    player_name "Yeah... I didn't do too well. Sorry {b}Diane{/b}!"
    show diane 3 at right
    show player 13 at left
    dia "It's okay... You're new at this..."
    show diane 2 at right
    dia "And I'm sure you'll get better at it!"
    dia "I always need fresh vegetables..."
    show diane 1 at right
    show player 10 at left
    player_name "I guess so..."
    show diane 14 at right
    show player 11 at left
    dia "Just make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
    show diane 1 at right
    show player 13 at left
    player_name "I'll do better next time..."
    player_name "Thanks {b}Diane{/b}!"
    hide player 13 at left with dissolve
    hide diane 1 at right with dissolve
    return

label garden_listing:
    call screen garden_minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
