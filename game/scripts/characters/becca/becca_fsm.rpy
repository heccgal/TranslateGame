label becca_triggers_init:
    python:

        T_becca_beach_sex = Trigger("beach sex", "Только что был секс с Беккой на пляже.")
    return

label becca_fsm_init:
    python:
        M_becca.add_action(T_becca_beach_sex, ["inc", "Секс на пляже с Бекка",])
    return

label becca_machine_init:
    python:
        M_becca = Machine("becca", default_loc = [[L_basketball_court, L_basketball_court, L_NULL, L_NULL]],
                          vars = {"sex speed": .3,
                                  "becca beach sex": 0,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
