label dianes_shed_diane_breeding_help_started:
    scene shed_night with None
    show diane 89 at right
    show player 11 at left
    dia "I have a {b}little request{/b} to ask of you."
    show diane 88
    player_name "..."
    show player 21
    player_name "Sure! What can I do for you?"
    show diane 87
    show player 13
    dia "I have, this... {b}Package{/b}, I'd like you to pickup for me."
    show diane 88
    show player 10
    player_name "Oh, okay."
    player_name "Where is it?"
    show diane 89
    show player 13
    dia "You'll have to pick it up at the {b}mall{/b}..."
    show diane 90
    show player 11
    dia "...It's at a shop, called {b}Pink{/b}."
    dia "It should be under my name!"
    show diane 88
    show player 29
    player_name "At the {b}Pink{/b} store?!"
    show player 21
    player_name "..."
    player_name "But, what is it?"
    show diane 87
    show player 13
    dia "It's a little something for you... But it's a {b}surprise{/b}!"
    show diane 88
    show player 11
    player_name "!!!"
    show player 21
    player_name "Really?"
    show player 108f
    player_name "The mall is closed right now, though..."
    show player 21
    player_name "I'll have to go tomorrow."
    show diane 90
    show player 13
    dia "That's my good boy..."
    show diane 89
    return

label dianes_shed_shed_dialouge_0:
    show player 35 at left with dissolve
    player_name "Woah..."
    show player 34
    player_name "...What a strange looking shed."
    player_name "What's up with all the containers... And those chains?!"
    show player 43
    player_name "Anyway, let's try and {b}find that pump{/b}..."
    hide player 43 with dissolve
    return

label dianes_shed_shed_dialouge_1_intro:
    scene shed_blur_night
    show diane 57 at right with dissolve
    window hide
    pause
    show diane 58 at right
    window hide
    pause
    show diane 57 at right
    window hide
    pause
    show diane 58 at right
    window hide
    pause
    show diane 57 at right
    show player 11 at left with dissolve
    player_name "..."
    show player 23 at left
    player_name "{b}Diane{/b}!??"
    show diane 59 at right with hpunch
    show player 22 at left
    dia "!!!"
    show diane 60 at right
    dia "What are you doing here??!"
    show diane 64 at right
    show player 29 at left
    player_name "I saw the door was open! And-"
    show player 3 at left
    player_name "..."
    show player 21 at left
    player_name "...Is that a {b}breast pump{/b}?"
    show diane 61 at right
    show player 5 at left
    dia "{b}*Sigh*{/b}"
    show diane 62 at right
    show player 11 at left
    dia "Yes, {b}[firstname]{/b}... I... like to milk myself sometimes..."
    show diane 64 at right
    show player 12 at left
    player_name "Wait..."
    if M_player.get("drank milk"):
        player_name "Is that the milk you had me drink the other day?!"
    else:
        player_name "Is that the milk you gave me to drink the other day?!"
    show diane 61 at right
    show player 11 at left
    dia "I know... I should have told you..."
    show diane 60 at right
    show player 5 at left
    dia "But it's all natural, and I had no one else to try it with!!"
    show diane 61 at right
    dia "I hope you can forgive me?"
    return

label dianes_shed_shed_dialouge_1_okay:
    show diane 64 at right
    show player 21 at left
    player_name "It's fine, {b}Diane{/b}."
    player_name "You don't have to be sorry..."
    show diane 63 at right
    show player 17 at left
    if M_player.get("drank milk"):
        player_name "...I actually liked it!"
    else:

        player_name "...I'm glad you offered me some!"
    show diane 62 at right
    show player 13 at left
    dia "That's... very sweet of you to say..."
    show diane 63 at right
    show player 29 at left
    player_name "I... should go home now."
    show diane 62 at right
    show player 3 at left
    dia "Yeah, I'm going inside now..."
    dia "And can you please-"
    show diane 64 at right
    show player 21 at left
    player_name "I'll keep this to myself. Don't worry."
    show diane 63 at right
    show player 13 at left
    dia "Thanks."
    hide player 13 at left with dissolve
    hide diane 63 at right with dissolve
    return

label dianes_shed_shed_dialouge_1_wrong:
    show diane 64 at right
    show player 12 at left
    player_name "I don't know, {b}Diane{/b}."
    if M_player.get("drank milk"):
        player_name "It's pretty messed up that you tricked me into drinking your breast milk..."
    else:

        player_name "That was pretty wrong to offer me that..."
    show diane 61 at right
    show player 90 at left
    dia "I know..."
    dia "I'm so sorry!"
    show diane 64 at right
    show player 12 at left
    player_name "I'm going {b}home{/b} now..."
    show diane 60 at right
    show player 13 at left
    dia "But-"
    show diane 64 at right
    show player 24 at left
    player_name "Bye..."
    hide diane 64 at right with dissolve
    hide player 24 at left with dissolve
    return

label dianes_shed_seen_shed_locked:
    show player 34 with dissolve
    player_name "Hmm..."
    show player 35
    player_name "The door's locked."
    hide player 35 with dissolve
    return

label dianes_shed_not_seen_shed_locked:
    show player 35 at left with dissolve
    player_name "Hmm.. The shed is locked. I wonder what's in there?"
    show diane 8 at right with dissolve
    show player 22 at left
    dia "Are you snooping around?"
    show diane 9 at right
    show player 10 at left
    player_name "Uhh, sorry. I was just looking for tools..."
    show diane 10 at right
    show player 11 at left
    dia "It's okay. Perhaps one day I'll give you a little tour..."
    show player 21 at left
    show diane 9 at right
    player_name "Sure, {b}Diane{/b}..."
    hide player 21 at left with dissolve
    hide diane 9 at right with dissolve
    return

label dianes_shed_dianes_dialogue:
    scene location_diane_shed01_night_closeup
    show player 1 at left with dissolve
    show diane 89 at right with dissolve
    dia "Hey there, Handsome."
    dia "Ready to learn how to milk?"
    show diane 88
    show player 17
    player_name "Sure! I'd love to help!"
    show diane 89
    show player 1
    dia "That's my good boy..."
    return

label dianes_shed_dianes_dialogue_not_package:
    show diane 88
    show player 10
    player_name "I forgot where to pick up the {b}package{/b}."
    show player 29
    player_name "How do I find it again?"
    show diane 89
    show player 13
    dia "You'll have to pick it up at the {b}mall{/b}."
    show diane 87
    dia "It's at a shop called {b}Pink{/b}."
    show diane 89
    dia "It should be under my name!"
    show diane 88
    show player 21
    player_name "Oh. All right. gotcha!"
    show diane 89
    show player 13
    dia "Is there anything else you want to talk about?"
    return

label dianes_shed_dianes_dialogue_package:
    show player 239_240
    pause
    show diane 88
    show player 170
    player_name "I have the {b}package{/b} you asked for!"
    show diane 90
    show player 169
    dia "Excellent!"
    label aunt_shed_replay_1:
        show diane 119
        show player 11
        dia "Now, stay right here..."
        dia "...I'll be right back with a surprise for you."
        scene black with dissolve
        pause 0.5

        scene shed_night
        show diane 113 at right
        show player 23 at left
        with dissolve
        player_name "!!!" with hpunch
        show diane 114
        show player 22
        dia "So?"
        show diane 115
        dia "...You like it?"
        show diane 113
        show player 29
        player_name "That's... really sexy, {b}Diane{/b}."
        show diane 114
        show player 13
        dia "I always wanted to wear this... I just never had anyone to wear it for..."
        show diane 113
        show player 11
        player_name "..."
        show diane 116
        show player 23
        dia "I like the way my breasts can hang naturally, like this..."
        show player 22
        player_name "..."
        show diane 114
        dia "I figured it would help you get in the mood for... {b}milking{/b}..."
        show diane 113
        show player 29
        player_name "Well, it's working! Haha..."
        show diane 114
        show player 13
        dia "So... Uhm..."
        dia "What do you feel like doing, now?"
    return

label dianes_shed_dianes_dialogue_not_lets_milk:
    show diane 88
    show player 21
    player_name "I'm ready to start if you want."
    show diane 87
    show player 11
    dia "Not just yet!"
    show diane 89
    show player 13
    dia "You need to {b}take care of the few things{/b} I asked you about earlier, before we get started..."
    show diane 88
    show player 21
    player_name "Oh, right!"
    show player 17
    player_name "My bad, I'll tend to those first..."
    show diane 90
    show player 13
    dia "Don't worry. We'll be having fun, soon..."
    return

label dianes_shed_dianes_dialogue_lets_milk_no_sex:
    show diane 113
    show player 17
    player_name "Let's make some milk!"
    show diane 114
    show player 2
    dia "I was hoping you'd say that..."
    show diane 112
    dia "But before we start, I have to prepare for the milk extraction!"
    show diane 113
    show player 12
    player_name "How do you do that?"
    show diane 117
    show player 11
    dia "With these!"
    dia "I have to attach these suction pumps..."
    player_name "!!!"
    show diane 113
    show player 21
    player_name "Do they... hurt?"
    show diane 115
    show player 13
    dia "Haha. Not really..."
    show diane 114
    dia "It feels a bit strange when it pumps, but I kind of like it!"
    show diane 113
    show player 21
    player_name "Cool!"
    show diane 114
    show player 11
    dia "You know, they say that cows lactate more when they are... {b}Fertilized{/b}..."
    show diane 113
    player_name "..."
    show player 29
    player_name "I... I don't understand-"
    show diane 112
    show player 13
    dia "I'm just saying... Pregnant cows produce a lot more milk!"
    show player 11
    show diane 114
    dia "... And {b}this cow isn't pregnant yet{/b}. Is her {b}bull{/b} ready to {b}breed{/b} her?"
    show diane 113
    show player 23
    player_name "!!!"
    show diane 114
    show player 22
    dia "Breed me, {b}[firstname]{/b}! Claim my womb as yours!"
    show diane 113
    show player 29
    player_name "...Yeah, I... I'd like to..."
    show diane 114
    show player 13
    dia "That's my good boy!"
    show player 11
    return

label dianes_shed_dianes_dialogue_lets_milk_had_sex:
    show diane 113
    show player 17
    player_name "Let's make some milk!"
    show diane 114
    show player 2
    dia "I was hoping you'd say that..."
    dia "I couldn't wait for you to come back!"
    show diane 112
    show player 11
    dia "But before we start, let me get into character!"
    show player 11
    show diane 116
    dia "How do I look?"
    show player 21
    player_name "You're beautiful, {b}Diane{/b}!"
    show player 13
    show diane 112
    dia "Now, when you mount me on the chair..."
    dia "Make sure you cum {b}deep{/b} inside me...."
    show player 11
    show diane 113
    player_name "!!!"
    show player 23
    show diane 114
    dia "I need my bull to.... {b}breed{/b} me good..."
    show diane 112
    show player 22
    dia "...You think you could help me with that?"
    show diane 113
    show player 29
    player_name "...Yeah, I... I can do that for you..."
    show diane 115
    show player 13
    dia "That's my good boy!"
    show player 11
    show diane 114
    return

label dianes_shed_dianes_dialogue_lets_milk:
    dia "Let's get set up on the {b}breeding chair{/b}..."
    scene shed_closeup 1
    show dianesex 36
    with dissolve
    dia "Now just slide it in nice and slow..."
    dia "...And don't let go until you finish {b}deep{/b} inside..."
    show dianesex 38
    dia "That's it..."
    show dianesex 40
    dia "{b}*Moan*{/b}"
    return

label shed_sex_loop:
    if shed_sex_action == 0:
        if shed_sex_angle == 0:
            if not renpy.showing("shed_closeup 1"):
                scene shed_closeup 1
                show expression AnimatedImage("dianesex", [38,40], M_aunt) as dianesex
        else:
            if not renpy.showing("shed_closeup 2"):
                scene shed_closeup 2
                show expression AnimatedImage("dianesex", [50,52], M_aunt) as dianesex at right

    elif shed_sex_action == 1:
        if not renpy.showing("shed_closeup 3"):
            scene shed_closeup 3
            show dianesex 54
            player_name "You're so wet, {b}Diane{/b}."
            dia "I just love the feeling of my clit against your hard cock, sweetie."
            dia "Stay still..."

    elif shed_sex_action == 2:
        if previous_shed_sex_action != shed_sex_action:
            show dianesex 56
            dia "I want it inside me now..."
    show screen sex_xray_anim_buttons 
    pause
    hide screen sex_xray_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if shed_sex_action == 0:
                if shed_sex_angle == 0:
                    show expression AnimatedImage("dianesex", [38,40], M_aunt) as dianesex
                else:
                    show expression AnimatedImage("dianesex", [50,52], M_aunt) as dianesex at right

            elif shed_sex_action == 1:
                show expression AnimatedImage("dianesex", [54,55], M_aunt) as dianesex

            elif shed_sex_action == 2:
                show expression AnimatedImage("dianesex", [58,59,58,57], M_aunt) as dianesex

            elif shed_sex_action == 3:
                show expression AnimatedImage("dianesex", [61,60], M_aunt) as dianesex
            pause 8
        else:

            $ pose_counter = 0
            if shed_sex_action == 0:
                if shed_sex_angle == 0:
                    $ pose_list = [38,40]
                else:
                    $ pose_list = [50,52]

            elif shed_sex_action == 1:
                $ pose_list = [54,55]
            elif shed_sex_action == 2:
                $ pose_list = [58,59,58,57]

            elif shed_sex_action == 3:
                $ pose_list = [61,60]
            $ poses_done = []
            while poses_done != pose_list:
                if shed_sex_action == 0 and shed_sex_angle == 1:
                    show expression "dianesex {}".format(pose_list[pose_counter]) as dianesex at right
                else:

                    show expression "dianesex {}".format(pose_list[pose_counter]) as dianesex
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1

    if shed_sex_action == 3:
        $ persistent.cookie_jar["Diane"]["unlocked"] = True
        $ persistent.cookie_jar["Diane"]["gallery"]["06_unlocked"] = True
        pause .3
        show dianesex 62
        player_name "Woa..."
        player_name "It squirted so much!"
        dia "{b}*Panting*{/b}"
        dia "You milked me..."
        if not store._in_replay == None:
            jump expression game.dialog_select("after_milk_replay")
    $ previous_shed_sex_action = shed_sex_action
    call screen shed_sex_options

label shed_sex_cum:
    call expression game.dialog_select("shed_sex_cum_dialouge")
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label shed_sex_cum_dialouge:
    dia "Don't hold back..."
    dia "Cum deep inside me..."
    dia "Breed me!!!"
    if shed_sex_angle == 0:
        show dianesex 40
        if xray:
            show expression "characters/player/char_player_sex_44.png" as playersex_cum
    else:

        show dianesex 52 at right
        if xray:
            show expression "characters/player/char_player_sex_48.png" as playersex_cum at right
    dia "{b}AAaaahh!!{/b}"
    if shed_sex_angle == 0:
        show dianesex 36
        show expression "characters/player/char_player_sex_45.png" as playersex_cum
    else:

        show dianesex 48
        show expression "characters/player/char_player_sex_49.png" as playersex_cum at right
        pause
        show dianesex 46
        show expression "characters/player/char_player_sex_50.png" as playersex_cum
    dia "That was... So much cum..."
    player_name "I did okay?"
    dia "You bred me well."
    dia "Thank you..."
    hide playersex_cum
    label after_milk_replay:
        scene shed_night
    show player 1 at left
    show diane 89 at right
    with dissolve
    dia "Thank you so much for your help..."
    show diane 87
    dia "Pretty soon I'll have the finest milk in town!"
    show player 2
    show diane 88
    player_name "I really enjoyed this. I hope I can help you again soon!"
    show player 1
    show diane 89
    dia "I plan on expanding my milk business, so..."
    show diane 90
    dia "There's plenty of work to be done around here!"
    show diane 89
    dia "I can always use a hand..."
    show player 17
    show diane 88
    player_name "That would be amazing!"
    show player 1
    show diane 89
    dia "It's getting late. You should probably get going..."
    show diane 92
    dia "You don't want to keep {b}[deb_name]{/b} waiting!"
    show player 21
    show diane 91
    player_name "Yeah."
    show player 13
    show diane 87
    dia "Remember: We have to keep this our little secret."
    show player 21
    show diane 88
    player_name "Don't worry, {b}Diane{/b}, I won't tell anyone."
    show player 13
    show diane 90
    dia "That's my handsome boy!"
    show diane 111 at left
    dia "We're gonna have a lot of {b}fun{/b} together..."
    hide diane 111 at left
    $ renpy.end_replay()
    return

label dianes_shed_dianes_dialogue_leave:
    show diane 88 at right
    show player 10 at left
    player_name "I'd love to stay here and milk with you..."
    show diane 91
    player_name "But It's getting late and {b}[deb_name]'s{/b} gonna be worried."
    show diane 92
    show player 5
    dia "That's too bad."
    dia "I was looking forward to getting help with my milk..."
    show diane 91
    show player 10
    player_name "I'm sorry... Maybe another night?"
    show diane 87
    show player 13
    dia "Sure... You know where to find me."
    show diane 88
    show player 21
    player_name "Okay!"
    hide diane 88 at right with dissolve
    hide player 21 at left with dissolve
    return

label dianes_shed_dewitt_paint:
    scene location_diane_shed01_night_closeup
    show player 588
    with dissolve
    player_name "Finally found the paint!"
    player_name "If I bring this and some {b}lumber{/b} to the {b}work bench{/b} in the {b}garage{/b}, I can make a fake guitar, no problem."
    hide player with dissolve
    $ M_dewitt.trigger(T_dewitt_shed_find_paint)
    if not player.has_item("paint"):
        $ player.get_item("paint")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
