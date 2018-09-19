label pizza_exterior_dialogue:
    $ player.go_to(L_pizzeria_exterior)
    if L_pizzeria_exterior.first_visit:
        call expression game.dialog_select("pizza_exterior_first_visit")
        $ L_pizzeria_exterior.visited()
    $ game.main()

label pizza_interior_dialogue:
    $ player.go_to(L_pizzeria_interior)
    if M_tony.is_state(S_tony_start):
        call expression game.dialog_select("pizza_interior_pizza_count_0")
        $ M_tony.trigger(T_tony_intro)
    $ game.main()

label pizzeria_kitchen_dialogue:
    $ player.go_to(L_pizzeria_kitchen)
    $ game.main()

label pizzeria_storage_dialogue:
    $ player.go_to(L_pizzeria_storage)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
