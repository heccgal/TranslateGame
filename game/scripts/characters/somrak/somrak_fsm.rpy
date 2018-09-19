label somrak_triggers_init:
    python:

        T_perv_visit = Trigger("Visit", "Visit Somrak at the gym")
        T_perv_pay = Trigger("Pay", "Pay Somrak a pair of panties")
        T_perv_train = Trigger("Train", "Somrak teaches a lesson")
        T_perv_finish = Trigger("Finish", "Somrak has finished a set of lessons")
    return

label somrak_fsm_init:
    python:

        S_perv_start = State("start")
        S_perv_wait_clean = State("waiting","Waiting for clean panties")
        S_perv_teach_1 = State("teaching","Level one")
        S_perv_wait_used = State("waiting","Waiting for used panties")


        S_perv_start.add(T_perv_visit, S_perv_wait_clean,
                         actions=['clear','need_rest',
                                  'trigger', T_jenny_panty_raid,
                         ])
        S_perv_wait_clean.add(T_perv_pay, S_perv_teach_1,
                              actions=['assign',('session',2)])
        S_perv_teach_1.add(T_perv_train,S_perv_teach_1,
                           actions=['set','need_rest',
                                    'triggerOnZero',('session',T_perv_finish)])
        S_perv_teach_1.add(T_perv_finish,S_perv_wait_used)
        S_perv_teach_1.add(T_all_sleep,S_perv_teach_1,
                           actions=['clear','need_rest',])

        M_perv.add(S_perv_start, S_perv_wait_clean, S_perv_teach_1, S_perv_wait_used)
    return

label somrak_machine_init:
    python:
        M_perv = Machine("Somrak",default_loc=[[L_gym, L_gym, L_gym, L_NULL]])
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
