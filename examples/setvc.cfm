:setvc(p,c)
:Load_a_constant_%C%_into_%VREG%

:Ouput_initial_state
o

:Load_constant_into_spare_v.reg.%VREG%

s  :Swaps_focused_physical_register
:this_happens_every_inc_pass_below
:in_a_Counter_machine_language_without_a_relative_swap_command
:this_swap_would_have_to_be_performed_manually_using_an
:increment_decrement_loop.

repeat(%C%) { :incv0 s :incvv0 d_incv1 s repeat(%VREG%) { i } s _incvv0 }

:incv%C%

:Output_final_state_of_both_registers
oso

