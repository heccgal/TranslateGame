label right_tombstone:
    scene location_church_graveyard_tombstone01
    if M_aqua.is_state(S_aqua_graveyard_search):
        call expression game.dialog_select("right_tombstone_aqua_graveyard_search")
        $ M_aqua.trigger(T_aqua_tomb_engraving)
    else:

        pause
    $ game.main()

label right_tombstone_aqua_graveyard_search:
    player_name "( The name on this tomb stone is Ben Dover! )"
    player_name "( This has to be the one. )"
    player_name "( But now that I've found it, I'm not sure what I'm supposed to be looking for... )"
    player_name "Hmm..."
    player_name "( Maybe there's a {b}clue{/b} somewhere? )"
    player_name "( This engraving stands out... )"
    player_name "( Maybe I should look for a large {b}bell{/b} somewhere in town? )"
    return

label stray_cat:
    scene location_church_graveyard_closeup
    if not M_player.is_set("found cat"):
        $ M_player.set("found cat", True)
        call expression game.dialog_select("stray_cat_first_pre")
        if player.has_item("cat_food"):
            call expression game.dialog_select("feed_cat")
            $ player.remove_item("cat_food")
            jump expression game.dialog_select("stray_cat_take_home")
        call expression game.dialog_select("stray_cat_first_after")

    elif not player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_no_food")

    elif player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_have_food_pre")
        $ player.remove_item("cat_food")
        menu stray_cat_take_home:
            "Take her home.":
                call expression game.dialog_select("stray_cat_have_food_take_her_pre")
                call screen cat_name_input
                if cat_name.strip() == "":
                    $ cat_name = "Pussywillow"
                $ cat = Character("[cat_name]", color = "#c87efe")
                call expression game.dialog_select("stray_cat_have_food_take_her_after")
                $ M_player.set("pet cat", True)
            "Leave her here.":

                call expression game.dialog_select("stray_cat_have_food_leave_her")

    hide cat
    hide player
    with dissolve
    $ game.main()

label stray_cat_first_pre:
    show player 11 at left with dissolve
    cat "Meow"
    show player 10
    player_name "Uhh, Hello?"
    show player 11
    cat "Meow"
    show player 10
    player_name "Where is that sound coming from?"
    cat "Groooour!"
    show player 11
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show player 1
    pause
    show player 2
    player_name "Aww."
    player_name "Well hey there little guy."
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 3
    player_name "What are you doing out here all by yourself?"
    player_name "Are you lost?"
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 3
    player_name "Poor little thing."
    player_name "I don't see a collar."
    show cat 3
    player_name "Must be a stray..."
    player_name "Where's your home boy?"
    show player 1
    show cat 4
    cat "Groooour!"
    show player 11
    show cat 3
    pause
    show player 10
    player_name "Well what's the matter?"
    show player 11
    show cat 4
    cat "Groooour!"
    show player 30
    show cat 3
    player_name "Hmm..."
    show player 2
    player_name "OH, I get it!"
    player_name "You're a little lady, aren't you?!"
    show player 1
    show cat 4
    cat "Brrrep"
    show cat 5 with dissolve
    cat "Prrrr"
    show player 2
    player_name "You look hungry."
    player_name "Are you hungry girl?"
    show player 1
    show cat 4
    cat "Meow"
    show player 2
    show cat 3
    return

label stray_cat_first_after:
    player_name "Hehe, alright. Well maybe I can find something for you."
    show player 4
    show cat 3
    player_name "(Hmm.)"
    player_name "(I should see about getting her something to eat.)"
    player_name "(I bet Consum-r has something.)"
    return

label stray_cat_no_food:
    show player 1 at left
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Meow"
    show player 2
    show cat 3
    player_name "Aww... Still hungry, huh?"
    show player 1
    show cat 4
    cat "Brrrep"
    show player 2
    show cat 5
    player_name "You're just so cute!"
    player_name "I'll try to find you something to eat, okay?"
    show player 1
    show cat 4
    cat "Prrrr"
    show player 2
    show cat 5
    player_name "You just hold on!"
    return

label stray_cat_have_food_pre:
    show player 1 at left with dissolve
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Meow"
    show player 2
    show cat 3
    player_name "Hello again little one."
    show player 1
    show cat 4
    cat "Meow"
    show player 2
    show cat 3
    label feed_cat:
        player_name "Guess what I've got for you?"
        show player 239_240
        pause
        hide player with dissolve
        show cplayer 1 at left with dissolve
        show cat 4
        cat "Brrrep"
        show cplayer 2
        show cat 3
        player_name "That's right! I brought you something yummy!"
        show cat 4
        cat "Meow"
        hide cat with dissolve
        show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
        pause



        hide cat with dissolve
        show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
        player_name "!!!" with hpunch
        hide cplayer with dissolve
        hide cat with dissolve
        show cat 8 at left with dissolve
        pause
        show cat 9
        cat "Prrrr"
        show cat 10
        player_name "Hehe, that's right."
        player_name "Nom noms for Kitty!"
        show cat 9
        cat "Brrrep"
        show cat 8

        scene black with fade
        scene location_church_graveyard_closeup with fade

        show cat 17 at left
        player_name "Wow, you really were hungry, weren't you?"
        show cat 18
        cat "Buuuuuurp!"
        show cat 17
        player_name "..."
        player_name "Hah, well I'm glad you enjoyed that..."
        hide cplayer with dissolve
        show player 2 at left
        show cat 3 at Position(xpos=0.57, ypos=0.77)
        with dissolve
        player_name "Now that's better isn't it girl?"
        show player 1
        show cat 4
        cat "Brrrep"
        show player 2
        show cat 5
        player_name "You're so sweet."
        show player 4
        player_name "( Hmm... )"
        player_name "( Maybe I should take you home with me. )"
        player_name "( I don't think {b}[deb_name]{/b} would mind... )"
    return

label stray_cat_have_food_take_her_pre:
    show player 2
    player_name "What do you say girl?"
    player_name "You wanna come home with me?"
    show player 1
    show cat 4
    cat "Brrrep!"
    hide cat with dissolve
    show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
    pause
    hide cat with dissolve
    show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
    player_name "!!!" with hpunch
    hide player
    hide cat
    with dissolve
    show cat 13 at left with dissolve
    pause
    show cat 16
    pause
    show cat 14
    player_name "Hehe, aww..."
    show cat 15
    pause
    show cat 14
    player_name "I'll take that as a yes!"
    show cat 12
    cat "Prrrr"
    show cat 14
    player_name "Well you're gonna need a name if you're coming home with me..."
    return

label stray_cat_have_food_take_her_after:
    player_name "How about... [cat]?"
    player_name "You like that?"
    show cat 12
    cat "Meow"
    show cat 14
    player_name "heh, alright. [cat] it is then!"
    show cat 15
    cat "Prrrr"
    show cat 16
    pause
    show cat 14
    player_name "C'mon [cat], Let's get you home!"
    show popup_cat at truecenter with dissolve
    pause
    hide popup_cat with dissolve
    return

label stray_cat_have_food_leave_her:
    show player 10 at left
    show cat 5
    player_name "Hmm, sorry girl."
    player_name "I don't think {b}[deb_name]{/b} would be very happy if I brought you home."
    show player 11
    show cat 4
    cat "Meow"
    show player 10
    show cat 5
    player_name "At least I got you some food..."
    show player 11
    show cat 4
    cat "Brrrep"
    show player 10
    show cat 5
    player_name "You're a good girl."
    player_name "Stay safe, okay?"
    show player 11
    show cat 4
    cat "Meow"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
