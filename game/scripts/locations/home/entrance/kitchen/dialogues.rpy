label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Hey, sweetie!"
    deb "Hungry for some breakfast?"
    show debbie 51 at Position(xpos=1025)
    show player 10
    player_name "I don't know If I have time, {b}[deb_name]{/b}."
    if game.timer.is_weekend():
        player_name "I have to meet {b}Erik{/b} at his house..."
    else:
        player_name "I'm running late for school."
    show player 11
    show debbie 52
    deb "Honey, you have to eat!"
    show player 11
    if game.timer.is_weekend():
        deb "I don't care if your friend {b}Erik{/b} has to wait all day..."
    else:
        deb "I don't care if your school calls me to complain about you being late..."
    show player 1
    deb "You can't just go out on an empty stomach!"
    show player 14
    show debbie 51
    player_name "I guess I could take a few minutes to eat something..."
    show player 1
    show debbie 2
    deb "I prepared some cereal for you in the {b}dining room{/b}."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression game.timer.image("homekitchen{}")
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Good morning, sweetie! I made you some breakfast!"
    deb "I thought you'd like something special for your first day back at school."
    show player 2
    show debbie 1
    player_name "Thanks, {b}[deb_name]{/b} but I'm not really hungry and I'm running late for school. So..."
    show player 1
    show debbie 2
    deb "You're sure? I made your favorite..."
    deb "Happy face pancakes with three strips of baaaacon!"
    show debbie 1
    show player 10
    player_name "Oh man..."
    show player 11
    player_name "..."
    show player 10
    player_name "No, I really shouldn't..."
    player_name "I think {b}Erik{/b} overslept again and I don't wanna be late on my first day back."
    show player 11
    show debbie 3
    deb "Hah, again huh?"
    show player 1
    show debbie 2
    deb "Well I guess you'd better get a move on then."
    show player 2
    show debbie 1
    player_name "Yeah, thanks anyways, {b}[deb_name]{/b}!"
    show player 1f with dissolve
    show debbie 2
    deb "My pleasure, Sweet- Oh! Wait!"
    show player 1 with dissolve
    player_name "Hmm?"
    show debbie 3
    deb "I nearly forgot!"
    show debbie 2
    deb "I spoke with my friend {b}Diane{/b} yesterday and she mentioned that she could use some {b}help with her garden{/b} over the summer!"
    show player 10
    show debbie 1
    player_name "Hmm, I don't really know much about gardening {b}[deb_name]{/b}..."
    show player 11
    show debbie 3
    deb "Oh c'mon, It's easy! {b}Diane{/b} can teach you and if you do a good job she'll pay you as well!"
    show debbie 2
    deb "It could be a good way to {b}earn some money for college{/b}, don't you think?"
    show player 10
    show debbie 1
    player_name "Yeah, I guess you're right."
    show player 2
    player_name "I should go visit her and see what she wants me to do."
    show debbie 2
    deb "Atta' boy!"
    hide player
    show debbie 4b
    with dissolve
    deb "I know these last few weeks have been hard..."
    deb "But your {b}father{/b} would want you to carry on, you know?"
    deb "You'll get through this. I promise things will get better."
    show debbie 5b
    player_name "Yeah, I-I know. Thanks {b}[deb_name]{/b}..."
    deb "Chin up, sweetie! I'm here for you."
    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "There you are!"
    show debbie 3
    deb "I need your help with something..."
    show debbie 2
    show player 11
    deb "My friend {b}Diane{/b} is coming over for dinner tonight."
    deb "... And I need you to pick up some {b}Sea Trout{/b} down at the {b}Pier{/b}."
    deb "I want to cook her something special and it's her absolute favorite!"
    show debbie 1
    show player 2
    player_name "Oh, {b}Diane{/b} is coming over? That's a nice surprise!"
    player_name "It'll be good for her to get out of her house for awhile..."
    player_name "I worry about her sometimes... All alone over there."
    player_name "I'll swing by the {b}Pier{/b} and grab some {b}Sea Trout{/b} on my way home."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "{b}[firstname]{/b}, before you go, do you have a second to look at something?"
    show player 14
    show debbie 61
    player_name "Of course, {b}[deb_name]{/b}. What do you need?"
    show player 1
    show debbie 62
    deb "I have a new outfit for dinner tonight and I wanted to get your opinion."
    deb "Let me go put it on real fast."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "I'm excited to see {b}[deb_name]{/b} all dressed up!"
    show player 11
    deb "Sweetie!"
    deb "I'm ready!"
    show player 2
    player_name "Coming!"
    hide player with dissolve
    return

label kitchen_mom_dinner_fish:
    scene location_home_kitchen_day_blur
    show player 13 at left
    show debbie 1 at right
    with dissolve
    player_name "Hey, {b}[deb_name]{/b}. I have the {b}fish{/b} you wanted."
    show player 2
    deb "Thanks, sweetie! Now I can finish dinner."
    show debbie 2
    deb "I'll let you know when it's finished, okay?"
    show player 203

    scene expression L_home_entrance.background
    show diane 137 at right
    show debbie 91f
    with fade
    dia "Mmm, is that {b}Sea Trout{/b} I'm smelling?!"
    dia "You didn't?!"
    show diane 136
    show debbie 93f
    deb "Of course I did!"
    deb "I know how to treat my girl right!"
    show diane 138
    show debbie 91f
    dia "Oh my gosh, I could totally kiss you right now!"
    show player 203 at left with dissolve
    show diane 137
    show debbie 92f
    dia "There he is..."
    dia "... The {b}man of the house{/b}!"
    show diane 136
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 17
    player_name "That dress looks great on you!"
    show diane 138
    show player 203
    dia "Oh stop it, you!"
    show player 13
    show diane 136
    show debbie 93f
    deb "He's quite the little charmer isn't he?"
    show diane 137
    show debbie 91f
    dia "I don't know how you manage to keep your hands off him!"
    dia "Where's your other tenant? She going to join us tonight or did she have a Bitches of Summerville meeting to attend?"
    show player 10
    show diane 136
    player_name "No, she's gonna eat with us."
    show player 12
    player_name "... She's just upstairs getting ready."
    show player 203
    show diane 138
    dia "Typical princess..."
    show diane 137
    dia "Well, I'm not waiting for her! Not when {b}[deb_name]{/b}'s {b}Sea Trout{/b} is on the menu!"
    show debbie 92f
    show diane 136
    deb "Hey, be nice!"
    show debbie 93f
    deb "She's not as bad as you make her out to be..."
    show debbie 91f
    show diane 138
    dia "Heh, if you say so."
    show debbie 93f
    show diane 136
    deb "I do. Now both of you get in there and sit down while I scrounge up a bottle of wine!"
    show debbie 92f
    deb "I've got this new brand I want you to try."
    hide debbie
    hide diane
    with dissolve
    show player 24
    player_name "I should join them in the {b}Dining Room{/b}."
    player_name "{b}[deb_name]{/b}'s cooking smells delicious!"
    hide player
    with dissolve
    return

label kitchen_mom_debt_call:
    scene expression game.timer.image("homekitchen{}")
    show debbie 6 at right with dissolve
    deb "I've told you already! I don't {b}KNOW{/b} where the money is..."
    deb "I had no idea he was involved in any of this!"
    show debbie 7 at right
    deb "But-"
    show debbie 6 at right
    deb "I don't have it!!"
    show debbie 7 at right
    deb "..."
    show debbie 6 at right
    deb "Was that a {b}threat{/b}?!"
    deb "I'm hanging up now. Don't call back here again."
    show debbie 8 at right with hpunch
    deb "Just leave us {b}ALONE!!!{/b}"
    show debbie 9 at right
    show player 10 at left with dissolve
    player_name "..."
    player_name "...{b}[deb_name]{/b}?"
    player_name "...Are you okay?"
    show player 5 at left
    show debbie 11 at right
    deb "I'm alright, sweetie."
    show debbie 10 at right
    show player 10 at left
    player_name "Are you sure? It sounded pretty bad..."
    show player 5 at left
    show debbie 11 at right
    deb "It's nothing for you to worry about..."
    show debbie 10 at right
    show player 5 at left
    player_name "..."
    show player 10 at left
    player_name "I could try and find another job. Maybe I can come up with some money for you."
    show player 5 at left
    show debbie 11 at right
    deb "No."
    deb "Your {b}Father{/b} wouldn't want that, Sweetheart."
    deb "You need to keep your focus on school and {b}Save your money for tuition{/b}."
    show debbie 10 at right
    show player 10 at left
    player_name "Yeah, but {b}[deb_name]{/b}, I can help..."
    hide player 10 at left
    show debbie 12 at right
    with dissolve
    deb "Oh, sweetie..."
    deb "Just let me handle it and everything will be fine, okay? I promise."
    hide debbie with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "... I don't see the problem. Isn't it a good thing that he's helping you around the house?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "I know, it's just..."
    deb "He's been so... affectionate towards me lately..."
    show diane 122 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "That's not surprising, he just lost the only family he ever had..."
    show diane 121
    dia "He probably just needs someone he can feel close with..."
    dia "Especially with all this other stuff that's been happening to you guys."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "It's not that. There's more to it! It's the way he looks at me, you know?"
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    dia "..."
    show diane 121
    dia "What do you mean?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Well, a little while ago I.. I started noticing things..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "...Like?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Like how he's always getting hard around me..."
    deb "... And touching me... in certain ways."
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "..."
    show debbie 60f
    deb "... And the other day, I found him playing with himself; In my bed!"
    deb "... With my underwear!"
    show diane 121
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "What did you do?!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "We discussed it!"
    deb "I told him not to do that kind of stuff in my room, but..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "But, what?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "I caught him again! He apologized and started talking about urges that he couldn't control..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Okay, so what did you say to that?"
    show diane 124
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "... I kinda... Let him finish."
    show diane 121
    show debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    dia "You watched him masturbate?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "I didn't know what to do!"
    deb "I thought maybe if he just got it out of his system..."
    deb "... You know?"
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "That's so naughty..."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "There's more..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "More?!"
    dia "You're serious?!"
    dia "Tell me!"
    show diane 124
    show debbie 60f
    deb "Diane..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "{b}[deb_name]{/b}, tell me!"
    show diane 124
    show debbie 60f
    deb "... We've been taking showers together."
    show diane 121
    show debbie 59f
    dia "Wow..."
    show diane 125
    dia "... How is he?"
    show diane 124
    show debbie 60f
    deb "Diane!!"
    show diane 122
    show debbie 59f
    dia "What?!"
    show diane 123
    dia "Don't act like a prude! We both know you're dying to tell me!"
    show diane 124
    show debbie 60f
    deb "... {b}*Sigh*{/b}"
    show diane 125
    show debbie 59f
    dia "Did you... touch him?"
    show diane 126
    show debbie 60f
    deb "... Yes."
    deb "I kinda, jerked him off..."
    show diane 125
    show debbie 59f
    dia "All the way?"
    show diane 126
    show debbie 60f
    deb "... Until he came, yeah."
    show diane 125
    show debbie 59f
    dia "So how is it?"
    show diane 126
    show debbie 60f
    deb "... How is what?"
    show diane 125
    show debbie 59f
    dia "His {b}dick{/b}, {b}[deb_name]{/b}! Is it big?"
    show diane 126
    show debbie 60f
    deb "( !!! )"
    show debbie 59f
    deb "..."
    show diane 127
    dia "Don't get shy on me now, girl. Spit it out!"
    show debbie 60f
    show diane 126
    deb "{b}Diane{/b}, he's got the biggest... {b}Dick{/b} I've ever seen!"
    show diane 125
    show debbie 59f
    dia "... You don't say?!"
    show diane 122
    dia "I'm surprised you stopped at the handjob..."
    show diane 126
    show debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    deb "{b}Diane{/b}, he's just a kid!"
    show diane 125
    show debbie 15f
    dia "Pfft, he's in college!"
    show diane 126
    show debbie 16f
    deb "Yeah, but I'm old enough to be his {b}Mother{/b}!"
    show diane 122
    show debbie 15f
    dia "... But {b}you aren't{/b} his {b}Mother{/b}, {b}[deb_name]{/b}!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Oh, I dunno, {b}Diane{/b}..."
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "He obviously wants to."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Please, tell me I'm not doing something terribly wrong here..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "It's your decision, but..."
    dia "I think you should relax and enjoy it a little. Who care's about the age difference?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Really? You don't think it's wrong?"
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Nope. I don't see the harm in it!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "I suppose we aren't hurting anybody... And we're both consenting adults."
    show diane 122 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Plus this is all really {b}HOT{/b}!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "You are such a bad influence! I don't know why I listen to you!"
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "... Because you know I'm right! Just give it a chance. Who know's maybe it was meant to be?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 62f at Position(xpos=0.3318,ypos=1.000)
    deb "Yeah, I suppose anything is possible..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 61f
    dia "Alright, well I'd better head home. It's getting late."
    show diane 125
    dia "We'll continue this another time. I want all the juicy details for my spank bank!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 62f
    deb "{b}Diane{/b}! You're terrible!"
    deb "Why don't you come by for dinner sometime? I'd love to see you more often!"
    show debbie 61f
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    dia "I'm always down for dinner, {b}[deb_name]{/b}. Just as long as I'm not the one doing the cooking!"
    dia "Good luck, Honey."
    scene expression L_home_entrance.background
    show player 5
    player_name "( That... was a lot to take in. )"
    player_name "( {b}[deb_name]{/b} seemed really conflicted about all of this... )"
    show player 203
    player_name "( She said she's enjoying it, though. )"
    player_name "( Either way, I'm glad {b}Diane{/b} thinks it's okay for us to be doing these things! )"
    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show debbie 14b at right
    player_name "Aww, c'mon {b}[deb_name]{/b}!"
    player_name "You're the one who said I need to get out and start dating."
    player_name "It would definitely help if I knew how to kiss a girl properly, wouldn't it?"
    show player 1
    deb "..."
    show debbie 13
    deb "... Well."
    deb "Y-yeah, I suppose I could give you a few pointers."
    show debbie 14
    show player 2
    player_name "I would really appreciate it, {b}[deb_name]{/b}."
    show player 1
    show debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    deb "O-okay, umm... Come in close to me."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show debbie 72
    player_name "Alright."
    show player 227
    show debbie 73
    deb "Good. Now, lean in, that's it."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Okay."
    show player 227
    show debbie 73
    deb "... Close your eyes and gently press your lips against mine..."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    deb "Mmm."
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "How was that?"
    show player 227
    show debbie 77
    deb "... Wow."
    show player 227c
    show debbie 76
    player_name "Bad?"
    show player 227
    show debbie 73
    deb "N-no. That was quite good!"
    show player 227c
    show debbie 72
    player_name "Really?!"
    show player 227
    show debbie 73
    deb "Yeah. Are you sure this is your first time?"
    show player 227c
    show debbie 72
    player_name "Heh, yeah. Do you have any pointers?"
    show player 227
    deb "..."
    show debbie 73
    deb "Well, let's see..."
    deb "Oh, I know!"
    deb "Kiss me again and I'll show you a little trick!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80c
    player_name "( !!! )" with hpunch
    show debbie 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Whoa!"
    player_name "That thing you did with your tongue, that was so cool!"
    show player 227
    show debbie 75
    deb "Hehe, yeah."
    show debbie 73
    deb "It's just a little something I picked up awhile back..."
    show player 227c
    show debbie 72
    player_name "Hmm, can I try it?"
    show player 227
    show debbie 73
    deb "Oh... uh."
    show player 227c
    show debbie 72
    player_name "Please?"
    show player 227c
    show debbie 73
    deb "Y-yeah... Sure!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80b
    deb "( !!! )" with hpunch
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "How was that?!"
    show player 227
    deb "Mmm..."
    show player 227c
    player_name "{b}[deb_name]{/b}?"
    show player 227
    show debbie 77
    deb "Oh, sorry!"
    show debbie 75
    deb "That was REALLY good, sweetie!"
    deb "I mean, wow! You're gonna be quite the little heart breaker once you get out into the dating world!"
    show player 227c
    show debbie 76
    player_name "Really? Thanks {b}[deb_name]{/b}!"
    show player 227
    deb "Mmmhmm."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause 
    show debbie 77
    pause
    show debbie 74
    deb "Oh!"
    deb "Oh my..."
    show player 230
    player_name "..."
    show player 232
    player_name "Sorry, {b}[deb_name]{/b}."
    player_name "I didn't mean to..."
    show player 231
    show debbie 75
    deb "Hehe, it's okay, sweetie. It's perfectly understandable."
    show debbie 73
    deb "We'd better take a break though."
    show player 232
    show debbie 72
    player_name "... Yeah. O-okay."
    player_name "Do you think, maybe, we could do this again sometime?"
    show player 231
    deb "..."
    show player 232
    player_name "You know... Just for practice?"
    show player 231
    show debbie 73
    deb "I suppose that would be okay."
    deb "Just to practice though!"
    show player 232
    show debbie 72
    player_name "Yeah, of course!"
    show player 231
    show debbie 73
    deb "Alright. Feel free to ask me anytime."
    show player 232
    show debbie 72
    player_name "Thanks {b}[deb_name]{/b}!"
    show player 231
    show debbie 73
    deb "No problem, {b}[firstname]{/b}."
    show player 232
    show debbie 72
    player_name "See ya!"
    hide debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "That was awesome!"
    return

label kitchen_mom_dishes:
    scene location_home_kitchen_closeup
    show debbie 116 at right
    with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    show player 1 at left with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 119 at Position(xpos=1014)
    deb "Oh, hey, sweetie!"
    show debbie 120
    show player 14
    player_name "Hey, {b}[deb_name]{/b}!"
    show debbie 119
    show player 1
    deb "You need something?"
    deb "I'm just finishing up the dishes..."
    show debbie 120
    return

label kitchen_mom_dishes_yes:
    show debbie 118
    show player 14
    player_name "Why don't you take a break for awhile?."
    player_name "I'll dry the rest."
    show debbie 119
    show player 1
    deb "That's very sweet but you don't have to do that."
    show debbie 118
    show player 14
    player_name "Nah, it's fine. I'm bored anyways."
    show debbie 119
    show player 1
    deb "Heh, well alright. If you're bored anyways..."
    show player 272
    show debbie 62
    deb "Just dry and store them away in the cupboard."
    show player 273
    show debbie 61
    player_name "Will do."
    show debbie 63
    show player 272
    deb "Thanks for helping out around here, {b}[firstname]{/b}."
    show player 274
    show debbie 61
    player_name "My pleasure, {b}[deb_name]{/b}."
    show expression Cutscene("help_debbie_kitchen_cutscene", "I don't think {b}[deb_name]{/b} had ever had help with dishes before... \nShe told me her late husband never did any work around the house and my {b}Dad{/b} only really helped with yard work or broken appliances. \nShe stayed with me in the kitchen until I was finished and we had a nice long chat. \nIt was nice getting to know {b}[deb_name]{/b} better...") as cutscene with fade
    pause
    hide cutscene with dissolve
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show debbie 120 at Position(xpos=1014)
    player_name "Okay. I'll come back later, then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
