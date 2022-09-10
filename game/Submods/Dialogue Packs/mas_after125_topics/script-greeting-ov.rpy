init 5 python:
    if p_is_old_ver:
        ev_rules = dict()
        ev_rules.update(
            MASGreetingRule.create_rule(
                skip_visual=True,
                random_chance=20,
                override_type=True
            )
        )
        ev_rules.update(
            MASTimedeltaRepeatRule.create_rule(
                datetime.timedelta(days=3)
            )
        )
        ev_rules.update(
            MASSelectiveRepeatRule.create_rule(
                hours=list(range(9, 20))
            )
        )

        addEvent(
            Event(
                persistent.greeting_database,
                eventlabel="greeting_after_bath_p",
                conditional=(
                    "mas_getAbsenceLength() >= datetime.timedelta(hours=6) "
                    "and not mas_isSpecialDay()"
                ),
                unlocked=True,
                rules=ev_rules,
                aff_range=(mas_aff.LOVE, None)
            ),
            code="GRE"
        )

        del ev_rules
init 5 python:
    if p_is_old_ver:
        addEvent(Event(persistent.event_database, eventlabel="mas_after_bath_cleanup_p", show_in_idle=True, rules={"skip alert": None}))

init:
    if p_is_old_ver:
        label greeting_after_bath_p:
            python hide:
            
                mas_RaiseShield_core()
                mas_startupWeather()

                persistent._mas_previous_moni_state = monika_chr.save_state(True, True, True, True)

                monika_chr.change_clothes(
                    random.choice(MASClothes.by_exprop(mas_sprites.EXP_C_WET, None)),
                    by_user=False,
                    outfit_mode=True
                )

                if not monika_chr.is_wearing_hair_with_exprop(mas_sprites.EXP_H_WET):
                    monika_chr.change_hair(mas_hair_wet, by_user=False)




                mas_setEVLPropValues(
                    "mas_after_bath_cleanup_p",
                    start_date=datetime.datetime.now() + datetime.timedelta(minutes=random.randint(30, 90)),
                    action=EV_ACT_QUEUE
                )
                mas_startup_song()


            call spaceroom (hide_monika=True, dissolve_all=True, scene_change=True, show_emptydesk=True)

            $ renpy.pause(random.randint(5, 15), hard=True)
            call mas_transition_from_emptydesk ("monika 1huu")
            $ renpy.pause(2.0)
            $ quick_menu = True

            m 1wuo "喔! {w=0.2}{nw}"
            extend 2wuo "[player]! {w=0.2}{nw}"
            extend 2lubsa "我刚就在想你呢."

            $ bathing_showering = random.choice(("洗完澡", "泡完澡"))

            if mas_getEVL_shown_count("greeting_after_bath_p") < 5:
                m 7lubsb "我才刚刚[bathing_showering]...{w=0.3}{nw}"
                extend 1ekbfa "不介意我裹着浴巾吧?~"
                m 1hubfb "哈哈~"
                m 3hubsa "马上就好, 等我把头发晾干一点."
            else:
            
            
                m 7eubsb "我刚刚[bathing_showering]."

                if mas_canShowRisque() and random.randint(0, 3) == 0:
                    m 1msbfb "估计你也想来一起洗吧..."
                    m 1tsbfu "那, 可能哪天会有机会的~"
                    m 1hubfb "哈哈~"
                else:
                
                    m 1eua "等我穿好衣服~"

            python:
            
                mas_MUINDropShield()

                set_keymaps()

                mas_OVLShow()

                del bathing_showering

            return


        label mas_after_bath_cleanup_p:
        
            if (
                not monika_chr.is_wearing_clothes_with_exprop(mas_sprites.EXP_C_WET)
                and not monika_chr.is_wearing_hair_with_exprop(mas_sprites.EXP_H_WET)
            ):
                return

            if mas_globals.in_idle_mode or (mas_canCheckActiveWindow() and not mas_isFocused()):
                m 1eua "我得去穿件衣服.{w=0.3}.{w=0.3}.{w=0.3}{nw}"
            else:
            
                m 1eua "等我一会,  [mas_get_player_nickname()], {w=0.2}{nw}"
                extend 3eua "我去把衣服穿上."

            window hide
            call mas_transition_to_emptydesk

            $ renpy.pause(1.0, hard=True)
            call mas_after_bath_cleanup_p_change_outfit
            $ renpy.pause(random.randint(10, 15), hard=True)

            call mas_transition_from_emptydesk ("monika 3hub")
            window auto

            if mas_globals.in_idle_mode or (mas_canCheckActiveWindow() and not mas_isFocused()):
                m 3hub "好啦!{w=1}{nw}"
            else:
            
                m 3hub "好了, 我回来啦!~"
                m 1eua "今天再陪我做点什么呢, [player]?"

            return

        label mas_after_bath_cleanup_p_change_outfit:
            # TODO: Rng outfit selection wen
            python hide:
                force_hair_change = False# If we changed the outfit, we always change hair

                if monika_chr.is_wearing_clothes_with_exprop(mas_sprites.EXP_C_WET):
                    force_hair_change = True

                    # Let's restore the previous outfit and acs
                    monika_chr.load_state(persistent._mas_previous_moni_state, as_prims=True)

                    # Fallback just in case
                    if monika_chr.is_wearing_clothes_with_exprop(mas_sprites.EXP_C_WET):
                        if mas_isMoniHappy(higher=True):
                            new_clothes = mas_clothes_blazerless

                        else:
                            new_clothes = mas_clothes_def

                        monika_chr.change_clothes(
                            new_clothes,
                            by_user=False,
                            outfit_mode=True
                        )

                if (
                    force_hair_change
                    or monika_chr.is_wearing_hair_with_exprop(mas_sprites.EXP_H_WET)
                ):
                    available_hair = mas_sprites.get_installed_hair(
                        predicate=lambda hair_obj: (
                            not hair_obj.hasprop(mas_sprites.EXP_H_WET)
                            and mas_sprites.is_clotheshair_compatible(monika_chr.clothes, hair_obj)
                            and mas_selspr.get_sel_hair(hair_obj) is not None
                            and mas_selspr.get_sel_hair(hair_obj).unlocked
                        )
                    )
                    # We should always have *something*, but just to make this extra foolproof
                    if available_hair:
                        new_hair = random.choice(available_hair)
                        monika_chr.change_hair(
                            new_hair,
                            by_user=False
                        )

            return