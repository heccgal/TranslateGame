label diane_triggers_init:
    return

label diane_fsm_init:
    python:

        S_aunt_start = State("start")



        M_aunt.add(S_aunt_start)
    return

label diane_machine_init:
    python:
        M_aunt = Machine("aunt",default_loc=[[L_diane_garden, L_diane_garden, L_diane_shed, L_diane_bedroom]],
                         vars={'sex speed': .4},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
