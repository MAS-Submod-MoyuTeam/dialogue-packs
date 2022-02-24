init 5 python:
    import datetime
    subDayOfWeek = datetime.now().weekday()
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="fucking_weekend",
            conditional="subDayOfWeek == 3 and store.mas_submod_utils.isSubmodInstalled(\"Auto Outfit Change\")",
            random=False,
            action=EV_ACT_PUSH
        )
    )

label fucking_weekend:
    m "嘿, [player]!"
    m "今天是疯狂星期四!来和我一起吃小汉堡!"
    m "啊哈哈...肯X基什么的没有给我广告费啦...只是随口一说."
    m "不过我或许能在今天为你做点什么..."
    m "等我一下..."
    #换上带有DATE的衣服
    call mas_transition_to_emptydesk
    python:
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop="date"
        )
    with Pause(5)
    call mas_transition_from_emptydesk
return "no_unlock"