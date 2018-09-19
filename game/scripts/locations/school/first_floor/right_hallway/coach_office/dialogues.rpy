label coach_locker_dialogue:
    if player.has_picked_up_item("master_key"):
        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            if player.has_item("pompoms"):
                jump expression game.dialog_select("coachs_office_locker_peeking")
            else:

                call expression game.dialog_select("coachs_locker_bissette_roxxy_pom_poms")
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen coachs_locker
    else:

        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            call expression game.dialog_select("coachs_locker_locked_bissette_roxxy_pom_poms")
        else:

            call expression game.dialog_select("coachs_locker_locked")
    $ game.main()

label coachs_locker_bissette_roxxy_pom_poms:
    show coach_locker
    player_name "There they are!"
    return

label coachs_locker_locked_bissette_roxxy_pom_poms:
    show expression game.timer.image("coach_office{}_b")
    show player 12 with dissolve
    player_name "I bet they're in that locker."
    player_name "Looks like I'll need a key to get in."
    hide player with dissolve
    return

label coachs_locker_locked:
    show expression game.timer.image("coach_office{}_b")
    show player 1 with dissolve
    player_name "Coach Bridget's locker is locked. I can't open it as I don't have the key."
    hide player with dissolve
    return

label coachs_office_roxxy_pom_poms_right_time:
    show player 30 with dissolve
    player_name "Alright, she's not in here."
    show player 14
    player_name "This is my chance to find those {b}Pom Poms{/b}!"
    show player 3f with dissolve
    player_name "..."
    show player 38 at Position (xoffset=41) with dissolve
    player_name "Now where could they be?"
    hide coach
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms_wrong_time:
    show coach 8 at right
    show player 23 at left
    with dissolve
    player_name "Oh crap! She's in here!"
    show player 22
    show coach 10
    bri "Can I help you?"
    show coach 8
    show player 10
    player_name "Err, umm..."
    show player 11
    show coach 10
    bri "Yes?"
    show coach 8
    show player 21
    player_name "No, I was just..."
    show player 27
    show coach 9
    bri "..."
    show coach 8
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "Excuse me, I need to use the restroom!"
    hide player
    hide xtra
    with dissolve
    show coach 10
    bri "What a weirdo..."
    hide coach
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms:
    scene expression game.timer.image("coach_office{}_b")
    if game.timer.is_morning():
        call expression game.dialog_select("coachs_office_roxxy_pom_poms_right_time")
    else:

        call expression game.dialog_select("coachs_office_roxxy_pom_poms_wrong_time")
        $ player.go_to(L_school_righthallway)
    return

label coach_locker_pom_poms:
    show coach_locker
    player_name "Awesome!"
    call expression game.dialog_select("coach_locker_pom_poms_dialogue")
    $ player.get_item("pompoms")

    $ player.location.call_screen(False)

label coach_locker_pom_poms_dialogue:
    show expression "boxes/popup_item_pompom1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_pompom1.png" with dissolve

    scene expression game.timer.image("coach_office{}_b")
    show player 14 with dissolve
    player_name "Now I just need to get these back to {b}Rox{/b}-"
    show player 11
    bri "Yeah, Yeah! Just head to the track and I'll meet you there."
    bri "I need to change first."
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Oh crap! She's coming!"
    player_name "I'm so dead! What am I gonna do!?"
    player_name "I gotta hide somewhere!"
    hide player with dissolve
    return

label coachs_office_locker_hide_fail:
    call expression game.dialog_select("coachs_office_locker_hide_fail_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ player.go_to(L_school_righthallway)
    $ game.main()

label coachs_office_locker_hide_fail_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show coach 3 at Position (xpos=850)
    show player 22 at left
    with dissolve
    bri "What are you doing in here?"
    show coach 7
    show player 23
    player_name "I... Uh..."
    show player 29 with dissolve
    player_name "This... isn't the restroom?"
    show player 22 with dissolve
    show coach 4
    bri "Get your scrawny ass out of here!"
    show coach 7
    show player 23
    player_name "On my way!"
    hide player with dissolve
    show coach 10 at right with dissolve
    bri "Weirdo."
    hide coach with dissolve
    return

label coachs_office_locker_peeking:
    call expression game.dialog_select("coachs_office_locker_peeking_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ game.main()

label coachs_office_locker_peeking_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show player 10 with dissolve
    player_name "This is the only place to hide!"
    player_name "I just have to hope she doesn't look in here."
    hide player with dissolve

    scene coach_locker_cs1
    with fade
    show text "It was a tight fit but I managed to get inside the locker and close the door.\nJust in time too, {b}Coach Bridget{/b} had almost caught me!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_cs2
    with fade
    show text "All I could do now was keep quiet and hope she didn't find me." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_peek
    show coach 1
    show coach_locker_peek_overlay
    with dissolve
    player_name "( There she is! )"
    player_name "( Please don't look in here... )"
    pause
    show coach 2
    bri "Man, it sure is cookin' out there."
    bri "I'm sweating like a whore in church!"
    show coach 11 with dissolve
    player_name "( She's undressing! )"
    player_name "( I am so dead if she finds me! )"
    show coach 12 with dissolve
    pause
    show coach 13 at Position (xoffset=37) with dissolve
    bri "Mmm, I hope you're paying attention!"
    player_name "( Does she know?! )"
    pause
    show coach 14 at Position (xoffset=51) with dissolve
    bri "I'd hate for you to miss the gun show!"
    player_name "( ... )"
    pause
    bri "Damn girl!"
    bri "Better put those away before they hurt somebody."
    show coach 12 with dissolve
    player_name "( What a weirdo... )"
    show coach 11 with dissolve
    pause
    show coach 9 with dissolve
    pause
    show coach 10
    bri "Huh. Thought I heard something."
    bri "Must have been my imagination..."
    hide coach with dissolve
    pause
    pause
    player_name "( I think she's gone. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
