label bedroom_mc_start_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 8
    player_name "Ugh... I hate getting up early."
    show player 9
    player_name "( No text messages from {b}Erik{/b}. Maybe he's still sleeping. )"
    player_name "( I'll stop by his house on the way to school. )"
    hide player 9 with dissolve
    return

label bedroom_mc_weekday_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( I should get ready for school... )"
    hide player with dissolve
    return

label bedroom_mc_weekend_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( What should I do this weekend... )"
    hide player with dissolve
    return

label bedroom_erik_bullying:
    scene black with fade
    deb "Sweetie?"
    pause
    deb "Wake up, sweetie."
    scene expression game.timer.image("bedroom{}") with fade
    show debbie 14f at left
    show player 101bf at right
    with dissolve
    player_name "Huh? {b}[deb_name]{/b}? What time is it?"
    show player 100bf
    show debbie 13f
    deb "{b}Mrs. Johnson{/b} is at the door asking to see you."
    show debbie 14f
    show player 101bf
    player_name "{b}Mrs. Johnson{/b}? For me?"
    show player 100bf
    show debbie 13f
    deb "She hasn't said much, but she wants to talk with you before you head out for the day."
    show debbie 14f
    show player 101bf
    player_name "Oh. Ok. Let me get dressed and I'll be down soon."
    show player 100bf
    show debbie 13f
    deb "Alright..."
    show debbie 14f
    pause
    show debbie 13f
    deb "Is there anything I need to know about, {b}[firstname]{/b}?"
    show debbie 14f
    player_name "..."
    show player 101bf
    player_name "I have no idea why she's here either, {b}[deb_name]{/b}."
    show player 100bf
    deb "..."
    show debbie 13f
    deb "Ok, sweetie."
    hide debbie
    hide player
    with dissolve
    return

label bedroom_mia_tattoo_help:
    scene expression game.timer.image("bedroom{}")
    show player 35 with dissolve
    player_name "( I have to make something nice for her tattoo idea. )"
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "( Perhaps, I can use one of the {b}easels in art class{/b}! )"
    show player 33
    player_name "( I can use it to come up with a nice design for her. )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 101 with dissolve
    player_name "I should sleep."
    hide player with dissolve
    show unlock53 at truecenter with dissolve
    pause
    hide unlock53 with dissolve
    return

label bedroom_mia_strip_aftermath_grounded:
    scene expression game.timer.image("bedroom{}")
    show player 24 with dissolve
    player_name "( I can't believe I won't be able to see {b}Mia{/b} anymore. )"
    show player 25
    player_name "( Her parents don't trust me. )"
    show player 35
    player_name "( Perhaps I can make it up to them somehow... )"
    hide player with dissolve
    return

label bedroom_mia_concerning_visit:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    pause
    show player 30 at Position (xoffset=-6) with dissolve
    player_name "( I wonder how {b}Mia{/b} is doing. )"
    show player 12 at Position (xoffset=-6)
    player_name "( It's been a few days, and I haven't heard anything from her... )"
    player_name "( ...Perhaps I should visit her and see how she's doing... )"
    hide player with dissolve
    return

label bedroom_mia_urgent_message:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Huh?"
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 14 with dissolve
    player_name "( Looks like I got a text message... )"
    hide player with dissolve
    return

label bedroom_mia_angelicas_impatience:
    scene expression game.timer.image("bedroom{}")
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Yawn*"
    show player 56f with dissolve
    player_name "( I should get ready for- )"
    show player 11f
    "*Knock knock*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Hun?"
    deb "There's someone downstairs who's here for you."
    show debbie 1f
    show player 30f
    player_name "{b}Erik{/b}?"
    show player 11f
    show debbie 2f
    deb "No, sweetie. It's a lady!"
    deb "She says you two have spoken before..."
    show debbie 1f
    show player 10f
    player_name "What?"
    player_name "But who-"
    show player 5f
    show debbie 2f
    deb "She's waiting downstairs. Why don't you {b}get dressed and come down{/b}."
    hide debbie with dissolve
    show player 12f player_name "A lady?!"
    show player 4f at Position (xoffset=-6) with dissolve
    player_name "Huh..."
    hide player with dissolve
    return

label bedroom_mia_angelicas_home_visit:
    scene expression game.timer.image("bedroom{}")
    show player 13f at right
    show debbie 2f at left
    deb "Sweetie?"
    show debbie 1f
    show player 17f
    player_name "Good morning, {b}[deb_name]{/b}."
    show player 13f
    show debbie 2f
    deb "Morning."
    deb "That nice lady from the other day is downstairs again."
    show debbie 1f
    show player 11f
    player_name "..."
    show player 12f
    player_name "Who?"
    show player 5f
    show debbie 3f
    deb "Come on now, sleepyhead. The nun is here again."
    show debbie 1f
    show player 22f
    player_name "!!!"
    deb "Hurry up so you can meet her downstairs."
    hide debbie with dissolve
    show player 10f
    player_name "What is she going to want now?"
    hide player with dissolve
    return

label bedroom_mia_angelicas_final_home_visit:
    scene expression game.timer.image("bedroom{}") with fade
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Yawn*"
    show player 56f with dissolve
    player_name "I should get ready for-"
    show player 11f
    "*Knock knock*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Hun?"
    deb "That nun is here again..."
    show debbie 1f
    show player 30f
    player_name "Again?"
    show player 24f
    pause
    show debbie 13f
    deb "I've been meaning to ask..."
    deb "What exactly are you doing for the church?"
    show debbie 14f
    show player 11f
    player_name "..."
    show debbie 13f
    deb "I mean, I'm surprised to see a nun visiting so much..."
    show debbie 14bf
    show player 29f at Position (xoffset=-35) with dissolve
    player_name "Yeah, um... everything is... fine."
    player_name "She's just... got me running errands."
    player_name "( Yeah, heh... heh... )"
    show player 3f at Position (xoffset=-35)
    show debbie 14f
    deb "..."
    show debbie 13f
    deb "Well, at least you're doing something good for the community..."
    show player 5f with dissolve
    show debbie 2f
    deb "I suppose I shouldn't be worried."
    show debbie 3f
    deb "What harm could come from you spending time at church?"
    hide debbie with dissolve
    show player 11f
    player_name "..."
    show player 37f at Position (xoffset=-41) with dissolve
    player_name "( You have no idea... )"
    hide player with dissolve
    return

label bedroom_mom_overheard:
    scene expression game.timer.image("bedroom{}")
    show player 34 with dissolve
    player_name "...{b}*distant voice*{/b}..."
    show player 35
    player_name "( Is that {b}[deb_name]{/b} on the phone? )"
    show player 12
    player_name "( ...She sounds like she's mad... Is she yelling? )"
    show player 10
    player_name "( I should go see if she's okay. )"
    hide player with dissolve
    return

label bedroom_mom_doorbell:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Doorbell's ringing, someone's at the door. )"
    player_name "( Must be {b}Erik{/b} or something... )"
    hide player with dissolve
    return

label bedroom_mom_movie_afterthoughts:
    scene expression game.timer.image("bedroom{}")
    show player 5
    player_name "Well that was super awkward!"
    player_name "There is no way she didn't notice..."
    player_name "I mean, she didn't say anything."
    player_name "... but it definitely got uncomfortable."
    show player 11
    player_name "I hope {b}[deb_name]{/b} isn't upset with me..."
    player_name "..."
    show player 24
    player_name "Ugh, I'll worry about it tomorrow. Right now, I need some sleep."
    hide player with dissolve
    return

label bedroom_mom_afterthoughts_two:
    scene location_home_bedroom_night_blur
    show player 13
    player_name "( That was really hot! )"
    player_name "( {b}[deb_name]{/b}'s nipples taste so good... )"
    player_name "( ... And she got wet enough to soak through onto my shorts! )"
    show player 5
    player_name "( ... )"
    player_name "( She kinda freaked out there at the end though. )"
    player_name "( Should I have apologized more? )"
    player_name "( ... )"
    show player 13
    player_name "( No sense worrying about it now. I should get some sleep. )"
    hide player with dissolve
    return

label bedroom_mom_note:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 101 with dissolve
    player_name "I should sleep."
    hide player with dissolve
    return

label bedroom_mom_note_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Someone left a {b}note{/b} on my computer screen?"
    hide player with dissolve
    return

label bedroom_mom_chores:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    if randomizer() < 50:
        player_name "I wonder if {b}[deb_name]{/b} needs help around the house."
        player_name "I should go ask her..."
    else:
        player_name "I wonder if {b}[deb_name]{/b} needs my help with anything else..."
    hide player with dissolve
    return

label bedroom_mom_search_panties:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( I can't stop thinking about the other day down in the basement... )"
    player_name "( {b}[deb_name]{/b} really seemed to be enjoying that massage. )"
    player_name "( Her legs are so soft and shapely... )"
    show player 11
    player_name "( Come to think of it. The lotion was in her panty drawer. )"
    player_name "( I'd like to take a closer look at that! )"
    show player 13
    player_name "( Maybe now is a good time. )"
    hide player with dissolve
    return

label bedroom_mom_kissing_practice:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "I keep having naughty dreams involving {b}[deb_name]{/b}."
    player_name "It's driving me nuts!"
    show player 5
    player_name "..."
    player_name "I should probably {b}talk to her{/b} about it..."
    hide player with dissolve
    return

label bedroom_bissette_french_food_assignment:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "I should do my French assignment."
    show player 14
    player_name "I have everything I need to finish it, now."
    hide player with dissolve
    return

label bedroom_sis_couch_1:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I hear someone in the hallway... Is that {b}[jen_name]'s{/b} door? )"
    show player 4
    player_name "( I wonder if she's up to something. )"
    hide player with dissolve
    return

label bedroom_sis_couch_3:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( I wonder if there's a {b}new porn video{/b} on TV tonight. )"
    show player 26
    player_name "( I should try and check it out while everyone's sleeping... )"
    hide player with dissolve
    return

label bedroom_study01:
    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment_after")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()

    elif M_bissette.is_state(S_bissette_do_poem_assignment):
        call expression game.dialog_select("bedroom_bissette_do_poem_assignment")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()
    else:

        scene expression game.timer.image("bedroom{}")
        if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]):
            call expression game.dialog_select("bedroom_bissette_find_books")
        else:

            call expression game.dialog_select("bedroom_no_school_work")
    $ game.main()

label bedroom_bissette_french_food_assignment_after:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "The book was everything someone would ever want to know about cheese.\nEverything from making, to preparing, cooking and eating all kings of cheeses...\n...But I eventually managed to piece a few paragraphs together that should please {b}Ms. Bissette{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_bissette_do_poem_assignment:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "Writing that poem proved to be quite difficult.\n...I seemed to be having a hard time keeping my focus.\nBut after a several hours and few... breaks. I finally managed to put something on paper!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide studybedroom01
    hide studybedroom02
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 511 with dissolve
    player_name "Finally!"
    player_name "I hope this is good enough to impress {b}Ms. Bissette{/b}..."
    player_name "I just need to {b}print it{/b} in the {b}computer lab{/b} and hand it in."
    hide player with dissolve
    return

label bedroom_bissette_find_books:
    show player 73 with dissolve
    player_name "( I first need to get the right school {b}textbook{/b} before I can finish my {b}homework{/b}... )"
    player_name "( I can probably find it at the local {b}library{/b}. )"
    hide player with dissolve
    return

label bedroom_no_school_work:
    show player 1 with dissolve
    player_name "( I don't have any school work. )"
    hide player with dissolve
    return

label mia_midnight_text:
    call expression game.dialog_select("mia_midnight_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_midnight_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 442 with dissolve
    player_name "{b}Mia{/b}!? Asking...for help?"
    player_name "What is this all about?"
    player_name "Is she in trouble?"
    show player 443
    player_name "..."
    show player 442
    player_name "Maybe I should {b}go see her now{/b}... Just to make sure she's alright."
    hide player with dissolve
    return

label mia_urgent_text:
    call expression game.dialog_select("mia_urgent_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_urgent_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "She can't find her dad?"
    player_name "I'd better go see what's going on..."
    hide player with dissolve
    return

label bed_locked:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I still have something I need to do before I can sleep... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_check_on_mom:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( I should really go check on {b}[deb_name]{/b}... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_sleeping_jerk_off_roxxy:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875)
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show roxxy dream 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show roxxy dream 2 with dissolve
    rox "Mmm, hello {b}[firstname]{/b}..."
    rox "I'm so happy you came to watch me cheer!"
    show roxxy dream 1 with dissolve
    player_name "..."
    show roxxy dream 2 with dissolve
    rox "I just can't keep my mind off you lately..."
    rox "You've been so helpful, I think you deserve a reward!"
    rox "I know, how about a special routine, for your eyes only?"
    rox "Would you like that, {b}[firstname]{/b}?"
    show roxxy dream 1 with dissolve
    $ M_player.set("sex speed", .3)
    show player 496c_496d_496e_496d_496c
    player_name "You bet I would!"
    show roxxy dream 2 with dissolve
    rox "Hehe, well you just lay back and enjoy the show!"
    rox "Keep stroking that big cock for me, {b}[firstname]{/b}!"
    show roxxy dream 3 with dissolve
    $ M_player.set("sex speed", .2)
    show player 496c_496d_496e_496d_496c
    rox "Gimme a C!"
    "C!"
    rox "Gimme a U!"
    "U!"
    rox "Gimme a M!"
    "M!"
    show player 496f
    rox "What's that spell?!"
    show player 496g
    player_name "HNNGGG!!!" with flash
    rox "Yay!!!"
    show player 496h
    hide jerkbubble
    hide roxxy dream
    player_name "Haah... Haaa..."
    player_name "Uuuhh man, I'm covered..."
    pause
    player_name "{b}Roxxy{/b} is so hot!"
    return


label bedroom_sleeping_jerk_off_debbie:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "... {b}[deb_name]{/b} is so beautiful."
    player_name "I just can't stop thinking about it."
    player_name "... about her."
    player_name "Mmm, God, I want her so bad!"
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show debbied 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show debbied 2
    deb "Well Hello there..."
    show debbied 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    show debbied 2
    deb "Oh gosh... Is that for me?"
    deb "... It's so big!"
    show debbied 1
    pause
    show debbied 2
    deb "... and thick."
    show debbied 3 with dissolve
    deb "Mmm, are you gonna give it to me?"
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    deb "Give it to me, {b}[firstname]{/b}!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1)
    show debbied 4_5
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show player 496f
    player_name "OH!"
    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"
    show player 496h
    hide jerkbubble
    hide debbied
    player_name "Haaaah... Haaaah..."
    player_name "Uuuhh man, I'm covered..."
    return

label bedroom_sleeping_jerk_off_mia:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "{b}Mia{/b} is so cute!"
    player_name "I can't wait to see her again..."
    pause
    player_name "... That cute body of hers."
    player_name "Mmm..."
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
    pause
    show miad 2
    mia "Hey, {b}[firstname]{/b}!"
    show miad 1
    pause
    show miad 2
    mia "Wow, I've never seen one of those before!"
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    mia "Are they all that big?!"
    show miad 1
    pause
    show miad 2
    mia "I was really hoping you would be my first, {b}[firstname]{/b}."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "Do you think it will fit?"
    mia "... In my..."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "...In my pussy?"
    show player 496f
    player_name "OH!"
    show player 496g with flash
    player_name "HHHNNNGGGG, HHuuuUUHH!!"
    show player 496h
    hide jerkbubble
    hide miad
    player_name "Haaaah... Haaaah..."
    player_name "Uuuhh man, I'm covered..."
    return

label bedroom_sleeping_debbie_movie_night:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "I think I heard {b}[deb_name]{/b} doing something downstairs."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_sleepover:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Maybe I should could sleep next to {b}[deb_name]{/b} tonight."
    player_name "She did say I could go visit her at night if I wanted to..."
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_pre:
    scene location_home_bedroom_cutscene01 with fade
    pause
    "{b}*Thump*{/b}"
    scene bedroom_cs03 with dissolve
    "{b}*Thump Thump*{/b}"
    player_name "..."
    scene bedroom_cs04 with dissolve
    player_name "What is that noise?"
    scene bedroom_night with fade
    show player 101bf
    player_name "( Sounds like it's coming from outside. )"
    player_name "( ... From {b}Erik{/b}'s yard, maybe? )"
    show player 100bf
    return

label bedroom_sleeping_erik_thief_use_telescope:
    show player 101bf
    player_name "( I should probably go have a look. )"
    show player 100f
    player_name "Hmm..."
    show player 101bf
    player_name "( I'll just take a quick peek through my telescope. )"
    hide player

    scene windowbackyardnight02a
    player_name "!?!"
    player_name "What the..."
    scene windowbackyardnight02b
    player_name "( Is that someone sneaking into {b}Erik's{/b} yard?! )"
    player_name "( That's the {b}burglar{/b} I've been hearing about in the news! )"
    scene windowbackyardnight02c
    player_name "..."
    player_name "( Is he going into {b}Erik's{/b} house?! )"

    scene bedroom_night with fade
    show player 101bf with dissolve
    player_name "( This is bad! )"
    player_name "( What if {b}Erik{/b} and {b}Mrs. Johnson{/b} are in danger? )"
    player_name "( I should go outside and see what he's doing in {b}Erik{/b}'s yard. )"
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_sleep:
    show player 101f
    player_name "( It's probably just some animal. )"
    player_name "( I need to get to sleep... )"
    hide player
    return

label bedroom_sleeping_erik_bullying_3_started:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Man... What a day. )"
    show player 17
    player_name "( I guess the training at the gym is starting to pay off! )"
    pause
    show player 12
    player_name "( {b}Dexter{/b} is never going to let this go. )"
    player_name "(... I'm gonna need all the training I can get! )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 101 with dissolve
    player_name "( I'd better get some sleep. )"
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_eve_karaoke:
    scene expression game.timer.image("bedroom{}")
    show player 14 with dissolve
    player_name "I'm supposed to meet {b}Eve{/b} over at {b}Erik's{/b} house tonight!"
    show player 30
    player_name "Sleep will have to wait."
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_school_sneak_mission:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Tonight, I was going to sneak into school with {b}Erik{/b}."
    player_name "I can't go to bed yet."
    hide player with dissolve
    return

label bedroom_sleeping_mia_midnight_call:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    "{b}Bzzt{/b}!"
    player_name "..."
    "{b}Bzzzzzzt{/b}!"
    scene bedroom_cs04 with dissolve
    player_name "Huh?"
    player_name "Is that my phone?"
    scene black with fade
    pause
    scene bedroom_night
    show player 7 with dissolve
    pause
    show player 101
    player_name "Someone's texting me?"
    player_name "I should see who it is..."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_solo_dream:
    scene dream_debbie_04 with fade:
        ypos -707
        linear 4.0 ypos 0
    deb "Mmm..."
    deb "Oh, that feels wonderful, sweetie."
    player_name "..."
    player_name "Oh, {b}[deb_name]{/b}..."
    deb "I want you {b}[firstname]{/b}!"
    deb "I want you inside me so bad!"
    player_name "{b}*Gulp*{/b}"
    player_name "Really?"
    deb "You have no idea! Give me that big, hard cock, {b}[firstname]{/b}!"
    deb "Please, I need it!"
    player_name "..."
    deb "Do it now! Hurry! I can't wait any longer!"
    scene dream_debbie_05 with dissolve:
        ypos 0
    pause
    player_name "Hnnggg!!" with flash
    pause
    scene dream_debbie_05 with flash:
        ypos 0
        linear 4.0 ypos -475
    player_name "... Oooooh..."
    pause

    scene location_home_bedroom_cutscene06 with fade
    pause
    scene location_home_bedroom_cutscene07
    player_name "..."
    scene location_home_bedroom_cutscene08
    player_name "Oh man..."
    pause
    scene location_home_bedroom_cutscene09
    pause
    player_name "I made a mess..."
    player_name ".. But holy crap, that was intense..."
    player_name "It all felt so real!"
    player_name "Arrgghh, I'm really losing it!"
    player_name "I just can't stop thinking about her!"
    player_name "I want to hold her and kiss her so bad..."
    player_name "Maybe I should try {b}talking to {b}[deb_name]{/b} about kissing{/b}?"
    player_name "She seemed kind of into it at first, when I kissed her in the Mall..."
    player_name "Hmm, it's risky but I think it's worth a shot!"
    player_name "I might go nuts if I don't do something..."
    player_name "... But first I should clean up and get some more sleep."
    return

label bedroom_sleeping_debbie_night_visit:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    deb "( ... )"
    deb "( I can’t fall asleep. )"
    deb "( Ever since I watched him masturbate... )"
    deb "( I can’t stop thinking about his- )"
    deb "( I just... )"
    deb "( ... )"
    define fadehold = Fade(0.5, 1.0, 0.5)

    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( I can't believe I'm having these thoughts... )"
    deb "( It's one thing for him to be having them. He's just a young man. )"
    deb "( ... But I'm old enough know better! )"
    show debbies 2
    deb "( He doesn't really want me! It's just a silly crush! )"
    deb "( I'm old enough to be his {b}Mother{/b}! )"
    deb "( ... But the way he makes me feel. )"
    show debbies 3
    deb "( The way he looks at me with those hungry eyes... )"
    show debbies 4
    deb "( ... Mmm, I need to see it... )"
    show debbies 5
    deb "( Just a peek. )"
    show debbies 6
    deb "( ... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( It's just so big... )"
    show debbies 7_8
    deb "( ... And it's getting bigger. )"
    deb "( Mmm... )"
    show debbies 9
    pause
    show debbies 10
    deb "( I have to see it! )"
    deb "( Oh, it's so thick... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "{b}*Gasp*{/b}!"
    deb "( It's so unbelievable! )"
    deb "( {b}*Sigh*{/b} What am I going to do? )"
    deb "( I just can't get this cock out of my head! )"
    deb "( ... )"
    deb "( It's been so long since I've felt one... )"
    deb "( ... And I miss it so much. )"
    deb "( It's not so bad for me to touch it... Just a little bit. Right? )"
    deb "( Surely, it's uncomfortable for him. Just look at how hard it is! )"
    show debbies 13
    pause
    show debbies 14
    pause
    deb "( ... So hard... )"
    deb "( ... And thick. )"
    show debbies 13
    deb "..."
    show debbies 13_14
    pause
    deb "( Oh, god. What am I doing?! )"
    deb "..."
    deb "( I'm stroking his cock! )"
    deb "( Hah... His big, juicy- )"
    deb "( Just like he was stroking it for me earlier. )"
    pause
    deb "( He says he wants me... He wants me so bad that he masturbates while thinking about me! )"
    deb "( Mmm... )"
    deb "( He wants to fuck me with this- )"
    show debbies 12
    deb "( ... )"
    show debbies 20
    deb "( What's wrong with me!? "
    show debbies 21
    deb "( Oh, god! )"
    deb "( I need to get out of here! )"
    deb "( ... Walk away, {b}[deb_name]{/b}! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"
    show debbies 23
    player_name "Whats-?"
    player_name "( Was that? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( Hmm, it's nothing. )"
    return

label bedroom_sleeping_debbie_night_visit_two:
    label mom_night_suck:
        scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( What am I doing here again?! )"
    deb "( Why can't I stop thinking about his cock! )"
    deb "( I just keep imagining it inside me! )"
    show debbies 2
    deb "( ... )"
    deb "( ... Maybe Diane is right; Perhaps I should just relax and let myself go. )"
    deb "( Those hungry looks he gives me... )"
    deb "( Mmm, I'm getting wet just thinking about it... )"
    show debbies 3
    deb "( I have to see it again! )"
    show debbies 4
    deb "( ... )"
    show debbies 5
    deb "( Oh, this is so wrong... What are you doing, {b}[deb_name]{/b}? )"
    show debbies 6
    deb "( It's even bigger than I remember... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( Mmm and it's growing again... )"
    show debbies 7_8
    deb "( ... So {b}hard{/b}. )"
    deb "( ... )"
    deb "( ... Maybe I could just take a peak... )"
    show debbies 9
    pause
    show debbies 10
    deb "( ... I mean it has to be uncomfortable for him. )"
    deb "( I'm just helping him relax... That's all. )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Oh, Lord help me! )"
    deb "( Mmm... )"
    show debbies 13
    deb "( I just can't resist touching it! )"
    deb "( It feels so good in my hands... )"
    show debbies 13_14
    deb "( It's so thick... )"
    deb "( ... and juicy. )"
    deb "( ... )"
    deb "( It's been so long... )"
    deb "( I want... )"
    deb "( I want to taste it! )"
    show debbies 15
    deb "( I {b}NEED{/b} to taste it! )"
    deb "( Just for a second! That couldn't hurt, right? )"
    show debbies 16_17
    deb "( Yes!! )"
    deb "( Oh God, I've missed this so much! )"
    deb "( I'm so horny! )"
    show debbies 18
    player_name "{b}*Moan*{/b}"
    show debbies 19
    deb "( !!! )" with hpunch
    deb "( Oh crap! He's waking up... )"
    deb "( ... )"
    show debbies 20
    deb "( What am I doing?! )"
    deb "( I can't let him see me like this! )"
    show debbies 21
    deb "( I have to get out of here! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Hmm?"
    show debbies 23
    player_name "What's-"
    player_name "( Was that? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( ... )"
    player_name "( I guess it was nothing... )"
    $ renpy.end_replay()
    return

label bedroom_sleeping_debbie_midnight_noises:
    scene bedroom_cs01 with fade
    "Ha ha ha..."
    "{b}*SPLASH*{/b}"
    scene bedroom_cs03 with dissolve
    player_name "..."
    scene bedroom_cs04
    player_name "Who is making all that noise outside?"
    scene bedroom_cs03
    player_name "..."
    player_name "......"
    scene bedroom_cs01 with dissolve
    pause
    "{b}*SPLASH*{/b}"
    scene bedroom_cs04 with dissolve
    player_name "What is going on?"

    scene bedroom_night
    show player 101b
    with dissolve
    player_name "Maybe, I should go check to see what's going on."
    player_name "Sounds like whoever is outside isn't going to stop any time soon."
    show player 8 with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three:
    $ M_mom.set("sex speed", .175 / .75)
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Oh... )"
    deb "( I'm here... )"
    show debbies 3
    deb "( What am I doing! )"
    show debbies 4
    deb "( WHAT AM I DOING!!! )"
    show debbies 5
    deb "( Mmm! )"
    deb "( There it is! )"
    show debbies 6
    deb "( Oh, I want it so bad... )"
    show debbies 7_8
    deb "( Get hard for me, sweetie... )"
    deb "( Please... )"
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Oh, I'm burning up... I need it!!! )"
    show debbies 15
    deb "( Mmm. )"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .75)
    show debbies 16_17
    deb "( Oh! So good! )"
    deb "( I miss this taste so much! )"
    player_name "( Mmm. )"
    deb "{b}*Slurp*{/b}"
    show debbies 19
    player_name "Hmm?"
    show debbies 20b
    player_name "What's-"
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    show debbies 20d
    deb "It's alright, {b}[firstname]{/b}, it's me."
    show debbies 20c
    player_name "... Okay."
    player_name "But what's going-"
    show debbies 20d
    deb "Shhh..."
    show debbies 20c
    player_name "{b}[deb_name]{/b}? What are you-"
    show debbies 20e with dissolve
    deb "Hush, sweetie, just relax and let yourself go..."
    player_name "..."


    deb "Oh, I need it, {b}[firstname]{/b}!"
    deb "I need that big cock inside of me!!!"
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "{b}*Gulp*{/b}"
    deb "I tried..."
    deb "I tried so hard to resist."
    deb "... But I just can't!"
    show debbies 20g with dissolve
    deb "Please, don't think less of me..."
    pause
    show debbies 20h with hpunch

    player_name "... Ooohh!!"
    deb "Haaaaaaaah!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.75)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Oh God!!"
    pause
    deb "Oh, it's even better than I imagined!"
    player_name "Oh, {b}[deb_name]{/b} this feels so good!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 2)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Haah! {b}[firstname]{/b}! Oh, {b}[firstname]{/b}!"
    deb "I'm gonna cum!"
    show debbies 20h with flash
    deb "AAHHH!!"

    player_name "... You're shaking! Are you alright, {b}[deb_name]{/b}?!"
    deb "Haaah... Haaaah..."
    deb "... Don't worry, sweetie."
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Keep going! Fuck, this is so good!"
    player_name "..."
    deb "Give it to me!!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.5)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "OOOH YES!!!"
    deb "That's it, Baby!!"
    deb "Give me that fat cock!"
    return

label bedroom_sleeping_debbie_night_visit_three_loop:
    menu:
        "Keep going." if keep_going < 2:
            $ keep_going += 1
            if M_mom.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")

        "Change Angle." if keep_going < 2:
            $ keep_going += 1
            if not M_mom.get("change angle"):
                $ M_mom.set("sex speed", .15)
                $ M_mom.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                with fade
            else:

                $ M_mom.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_mom.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                with fade
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")
        "Cum.":

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_pre")


            if M_player.is_set("pet cat"):
                scene location_home_bedroom_sleeping4 with fade
            else:
                scene location_home_bedroom_sleeping2 with fade

            if store._in_replay == None:
                show unlock11 at truecenter with dissolve
                $ renpy.pause()
                hide unlock11

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["10_unlocked"] = True
    $ M_mom.trigger(T_mom_midnight_fun)
    $ Sleep()
    $ game.main()

label bedroom_sleeping_debbie_night_visit_three_cum_pre:
    player_name "Oh, {b}[deb_name]{/b}... I'm gonna..."
    player_name "... I'm gonna!!"
    deb "Don't stop!! Don't-"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "HHNNGGG!!!!!"

    deb "AAAAAAAAHHHH!!!"
    pause
    show debbies 20h

    player_name "{b}*Panting*{/b}"

    deb "Mmm..."
    show debbies 20r with dissolve
    deb "..."
    show debbies 20s with dissolve
    deb "Oh gosh..."
    show debbies 20t
    player_name "That was incredible!"
    show debbies 20s
    deb "Hehe, it really was..."
    deb "..."
    deb "I'm so sorry, Sweetheart!"
    deb "I shouldn't have done this..."
    show debbies 20t
    player_name "What!? No, don't say that!"
    deb "..."
    player_name "I wanted this too!"
    show debbies 20s
    deb "... You did?"
    show debbies 20t
    player_name "You have no idea! It's practically all I can think about!"
    show debbies 20s
    deb "... Really?"
    show debbies 20t
    player_name "Yeah!"
    player_name "I love you, {b}[deb_name]{/b}!"
    show debbies 20s
    deb "I... I love you too, {b}[firstname]{/b}!"
    deb "..."
    deb "Nobody has ever made me cum like that before!"
    show debbies 20t
    player_name "Never?"
    show debbies 20s
    deb "Never. That orgasm was crazy!"
    show debbies 20t
    player_name "Sorry I didn't last very long..."
    show debbies 20s
    deb "No, you did great, Sweetheart! Especially for our first time!"
    show debbies 20t
    player_name "... First time?"
    deb "..."
    player_name "Can we do this again, {b}[deb_name]{/b}?"
    show debbies 20s
    deb "Oh, sweetie, are you sure that's what you want?"
    show debbies 20t
    player_name "Of course!!!"
    player_name "{b}[deb_name]{/b}, I've never wanted anything more!"
    show debbies 20s
    deb "Oh gosh..."
    deb "I hate to admit it but I feel the same way!"
    deb "..."
    deb "Alright, sweetie..."
    deb "... But we can only be naughty when no one else is around!"
    deb "And you can't tell {b}ANYBODY{/b}! Especially not {b}[jen_name]{/b}!"
    deb "Do you understand?!"
    show debbies 20t
    player_name "Yes."
    show debbies 20s
    deb "{b}[firstname]{/b}, I'm serious! You cannot tell a soul about this!"
    show debbies 20t
    player_name "I won't, {b}[deb_name]{/b}. I promise."
    show debbies 20s
    deb "Good boy."
    deb "{b}*Yawn*{/b}"
    deb "Oh, I'm exhausted now."
    show debbies 20t
    player_name "Yeah, me too."
    show debbies 20s
    deb "Mmm, I could fall asleep right here."
    show debbies 20t
    player_name "You should, {b}[deb_name]{/b}."
    show debbies 20s
    deb "I guess it would be alright. So long as I get out of here before {b}[jen_name]{/b} wakes up."



    scene location_home_bedroom_cutscene_sleep
    with fade
    show text "{b}[deb_name]{/b} and I had finally slept together." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "It had been spectacular! All of our pent up anxieties evaporated in an instant!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Our worries disappeared as she drifted off to sleep in my arms." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... We awoke the next morning feeling better than either of us could ever remember." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three_cum_after:

    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "{b}[deb_name]{/b}?"
    show debbies 20u
    player_name "..."
    show debbies 20v
    player_name "{b}[deb_name]{/b}, wake up."
    show debbies 20u
    deb "Hmm?"
    show debbies 20x
    deb "{b}*Yawn*{/b} Is it morning already?"
    show debbies 20w
    player_name "I'm afraid so."
    show debbies 20x
    deb "Oh, I slept like a log..."
    show debbies 20w
    player_name "Heh, yeah, me too."
    show debbies 20x
    deb "Mmm, alright. I suppose I'd better get out of here before {b}[jen_name]{/b} wakes up."
    show debbies 20w
    player_name "You sure you don't want to fool around a bit more?"
    show debbies 20x
    deb "Hehe, don't tempt me, sweetie. That cock of yours is hard to say no to."
    show debbies 20w
    player_name "I'll never get tired of hearing that!"
    show debbies 20x
    deb "Come and find me later, okay?"
    scene black with fade
    return

label bedroom_sleeping_debbie_smith_dream:
    scene dream_debbie 1 at Position(ypos=1475) with fade
    deb "Good morning, sweetie."
    deb "It's me, {b}[deb_name]{/b}."
    player_name "{b}[deb_name]{/b}?"
    player_name "Where are we?"
    deb "It's okay. Everything will be alright..."
    deb "Let me take care of you."
    scene dream_debbie 1_2:
        linear 5.0 ypos -707
    player_name "{b}[deb_name]{/b}..."
    player_name "What are you doing..."
    deb "- It's okay... I just want you to feel good..."
    player_name "{b}[deb_name]{/b}... That feels amazing!"
    scene dream_debbie 3
    player_name "( !!! )" with hpunch
    smi "{b}[firstname]{/b}!!!"
    scene dream_debbie 3:
        ypos -707
        linear 1.0 ypos 0
    smi "What are you doing here???"
    smi "Are you... SLEEPING?!"

    smi "Get to class NOW or I'm sending your ass to {b}DETENTION{/b}!"
    scene black with fade
    pause .2
    scene expression game.timer.image("bedroom{}")
    show player 264
    with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 265 with dissolve
    player_name "( !!! )"
    show player 266
    player_name "( That was such a strange dream! )"
    player_name "( {b}[deb_name]{/b} and I were doing things and she was naked! )"
    player_name "( Then {b}Principal Smith{/b}... )"
    show player 267 with hpunch
    player_name "( !!! )"
    show player 268
    player_name "( Is this normal?! )"
    player_name "( I've never had those kinds of dreams with {b}[deb_name]{/b} before... )"
    hide player with dissolve
    return

label bedroom_debbie_sleepover_pre:
    $ M_mom.set("sex speed", .175)
    scene location_home_bedroom_sex01 with fade
    show debbies 1
    player_name "( ... )"
    deb "Sweetie?"
    deb "Aww, did you fall asleep waiting on me?"
    player_name "( ... )"
    show debbies 3
    pause
    show debbies 4
    pause
    show debbies 5
    pause
    show debbies 6
    deb "... Wake up, sweetie."
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .75)
    show debbies 7_8
    deb "Mmm..."
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    pause
    show debbies 20b
    deb "{b}[firstname]{/b}?"
    player_name "... Hmm?"
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    player_name "Crap, I fell asleep didn't I?"
    show debbies 20d
    deb "Hehe, that's okay, sweetie."
    show debbies 20c
    player_name "Did you still wanna- ?"
    show debbies 20e with dissolve
    deb "Shh, we don't want to wake {b}[jen_name]{/b}!"
    player_name "Oh! ... Yeah, sorry."
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    deb "Hehe..."
    deb "It's alright, you're just excited. I'm excited too!"
    deb "I could hardly wait for {b}[jen_name]{/b} to get in bed."
    show debbies 20g with dissolve
    player_name "Oh wow, {b}[deb_name]{/b}, you're sopping wet!"
    deb "I told you I was excited."
    show debbies 20h with dissolve
    deb "Mmm..."
    deb "Now, let's not waste time... Give it to me, sweetie!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 3)
    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
    return

label bedroom_debbie_sleepover_random_33:
    deb "Ahh!!!"
    deb "Oh {b}[firstname]{/b}, it's so deep!"
    deb "You like it when I squeeze you with my pussy?"
    player_name "Oh God, yes!"
    deb "{b}[firstname]{/b}!"
    return

label bedroom_debbie_sleepover_random_66:
    deb "Oh yes!!!"
    deb "That's it, Baby! Fuck my pussy!"
    deb "Mmm, you like that?"
    player_name "Oh yeah, {b}[deb_name]{/b}!"
    deb "Faster, Baby!"
    return

label bedroom_debbie_sleepover_random_100:
    deb "Oh God, that's good!"
    deb "Who's my naughty boy?"
    player_name "Mmm, I am..."
    deb "That's right, Baby! Fuck me harder!"
    player_name "Uuhh!! You like this hard cock, {b}[deb_name]{/b}?"
    deb "Aaahh!! Yes! Yesss! YESSSSSS!!"
    deb "Give it to meeeeee!"
    return

label bedroom_debbie_sleepover:
    call expression game.dialog_select("bedroom_debbie_sleepover_pre")
    if randomizer() < 33:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_33")

    elif randomizer() < 66:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_66")

    elif randomizer() < 100:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_100")

    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.5)
    pause
    $ M_mom.set("change angle", False)

    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_loop:
    menu:
        "Keep going.":
            if M_mom.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
        "Change Angle.":

            if not M_mom.get("change angle"):
                $ M_mom.set("sex speed", .15)
                $ M_mom.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                with fade
            else:

                $ M_mom.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_mom.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                with fade
        "Cum.":

            jump expression game.dialog_select("bedroom_debbie_sleepover_cum")
    pause
    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_cum:
    call expression game.dialog_select("bedroom_debbie_sleepover_cum_dialogue")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping4 with fade
    else:
        scene location_home_bedroom_sleeping2 with fade

    show unlock11 at truecenter with dissolve
    pause
    $ Sleep()
    hide unlock11 with dissolve
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and not M_mom.is_state(S_mom_note):
        call expression game.dialog_select("bedroom_debbie_sleepover_after_random_70")
    else:

        call expression game.dialog_select("bedroom_debbie_sleepover_after_not_random")
        if not M_mom.is_set("basement sex"):
            call expression game.dialog_select("bedroom_debbie_sleepover_after_not_basement_sex")
            $ M_mom.trigger(T_mom_delay)
        hide player with dissolve
    $ game.main()

label bedroom_debbie_sleepover_cum_dialogue:
    player_name "... Oh!"
    player_name "{b}[deb_name]{/b}, I'm gonna..."
    deb "Do it, Baby! Come inside me!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "Uhhhuh!!!"
    deb "Hnnngg!!"
    deb "AAAAHHhh!!!"
    player_name "Shh! You're gonna wake {b}[jen_name]{/b}!"
    player_name "..."
    show debbies 20h with dissolve
    deb "Huhhh, huhhh, huhhh..."
    show debbies 20r with dissolve
    pause
    show debbies 20s with dissolve
    deb "Oh {b}[firstname]{/b}... That was..."
    show debbies 20t
    player_name "Mindblowing?"
    show debbies 20s
    deb "Phew... Yes!"
    deb "Mmm, I can't feel my legs."
    pause
    deb "... I love you, {b}[firstname].{/b}"
    show debbies 20t
    player_name "I love you too, {b}[deb_name]{/b}. You're the best!"
    show debbies 20s
    deb "Hah, thanks, sweetie."
    return

label bedroom_debbie_sleepover_after_random_70:
    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "Wake up, {b}[deb_name]{/b}."
    show debbies 20u
    deb "Mmm..."
    show debbies 20w
    player_name "The sun is up."
    show debbies 20x
    deb "Good morning, sweetie."
    show debbies 20w
    player_name "You sleep alright?"
    show debbies 20x
    deb "... You kidding? After getting fucked like that, I slept great!"
    show debbies 20w
    player_name "Heh, me too..."
    deb "..."
    show debbies 20x
    deb "I should probably get out of here before {b}[jen_name]{/b} gets up."
    show debbies 20w
    player_name "Yeah..."
    show debbies 20x
    deb "Thanks for a great night, {b}[firstname]{/b}! I love you!"
    show debbies 20w
    player_name "I love you too, {b}[deb_name]{/b}!"
    scene black with fade
    return

label bedroom_debbie_sleepover_after_not_random:
    scene location_home_bedroom_day_blur
    show player 7
    pause
    show player 8
    pause
    show player 1
    player_name "..."
    show player 2
    player_name "Hmm, {b}[deb_name]{/b} must have woken before me and snuck out..."
    player_name "Phew, what a night! I slept like a baby..."
    return

label bedroom_debbie_sleepover_after_not_basement_sex:
    show player 10
    player_name "Hmm, what is that note on my computer monitor?"
    player_name "... Did {b}[deb_name]{/b} leave that?"
    return

label sleeping_locked:
    scene expression player.location.background_blur
    show player 35 at left
    if not erik.over(erik_intro):
        player_name "( Can't sleep right now. I should go to school before I'm late. )"
    else:
        player_name "(I still have some things to do today...)"
    $ game.main()

label tired_bedroom_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 55 with dissolve
    player_name "{b}*yawn*{/b}"
    show player 56
    player_name "( I'm too tired for that... )"
    hide player 56
    $ game.main()

label M6_note:
    call expression game.dialog_select("M6_note_dialogue")
    $ M_mom.trigger(T_mom_read_note)
    $ game.main()

label M6_note_dialogue:
    scene expression game.timer.image("bedroom{}")
    show debbienote at Position (ypos=650) with dissolve
    pause
    hide debbienote with dissolve
    show player 11 with dissolve
    player_name "( {b}[deb_name]{/b} needs help with the laundry? )"
    player_name "( I should go see what it's about. )"
    hide player with dissolve
    return

label pet_cat:
    scene expression game.timer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Hey there, [cat]!"
    show cat 12
    if randomizer() < 33:
        cat "Meow"
    elif randomizer() < 66:
        cat "Prrrr"
    else:
        cat "Brrrep"
    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Who's a good Kitty?!"
    elif randomizer() < 30:
        player_name "You just gonna sleep all day?"
    elif randomizer() < 45:
        player_name "What did you do today, huh?"
    elif randomizer() < 60:
        player_name "You cute little fuzz ball."
    elif randomizer() < 75:
        player_name "Aww, snuggles for Kitty!"
    elif randomizer() < 85:
        player_name "Hey, watch it with those claws!"
    elif randomizer() < 93:
        player_name "I should get you a toy, huh?"
    else:
        player_name "I just love petting my pussy..."
    show cat 16
    pause
    hide cat with dissolve
    $ game.main()

label cookies:
    scene expression game.timer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( A box of my favorite cookies! )"
    player_name "( I should keep them in my backpack in case I get hungry. )"
    hide expression "objects/closeup_cookies.png" with dissolve
    show expression "boxes/popup_cookies.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_cookies.png" with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
