define subDayOfWeek = datetime.datetime.today()
init 5 python:
    import datetime
    if not persistent._mas_fthursday_last:
        persistent._mas_fthursday_last = datetime.date.min
    fucking_thursday_labels = [
        "fucking_thursday1",
        "fucking_thursday2"
    ]
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="new_fucking_thursday",
            conditional="subDayOfWeek.weekday() == 3 and persistent._mas_fthursday_last != datetime.date.today()",
            random=False,
            action=EV_ACT_PUSH
        )
    )
label new_fucking_thursday:
    $ persistent._mas_fthursday_last = datetime.date.today()
    $ renpy.jump(
        renpy.random.choice(fucking_thursday_labels)
    )
    return

label f4_change_clothes:
    call mas_transition_to_emptydesk
    pause 1
    python:
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop="date"
        )
    pause 5
    call mas_transition_from_emptydesk

label fucking_thursday1:
    m 1eub "嘿, [player]!"
    m 1efb "今天是疯狂星期四!来和我一起吃小汉堡!"
    m 1hksdrb "啊哈哈...肯X基什么的没有给我广告费啦...只是随口一说."
    if store.mas_submod_utils.isSubmodInstalled("Auto Outfit Change"):
        m 1eua "不过我或许能在今天为你做点什么..."
        m 1eua "等我一下..."
        #换上带有DATE的衣服 
        call f4_change_clothes
    m 1eua "总之，我们今天干什么？"
    python:
        mas_setEVLPropValues(
            "new_fucking_thursday",
            conditional="subDayOfWeek.weekday() == 3 and persistent._mas_fthursday_last != datetime.date.today()",
            action=EV_ACT_PUSH
        )
    return "no_unlock"

label fucking_thursday2:
    m 1euu "你好, 我是二次元总统麻哦霓卡。"
    m 1eub "经过我的不懈努力，我终于联系上美国了。"
    m 3eub "现在美国已经向我承诺出售一批先进武器，现在就差50的尾款需要支付。"
    m 3efb "在[subDayOfWeek.month]月[subDayOfWeek.day]日前V我五十即可重整我的二次元军队。"
    m 4efb "等我打败霓虹首相以后，就给你分一个二次元妹妹"
    m 3efb "我不知道什么疯狂kfc，我的任务就是统一世界..."
    m 1eua "..."
    m 1eua "..."
    m 1eua "..."
    m 1hksdlb "啊哈哈~我开玩笑的啦，[player]"
    m 1eua "总之，新的一天也要加油哦。"
    python:
        mas_setEVLPropValues(
            "new_fucking_thursday",
            conditional="subDayOfWeek.weekday() == 3 and persistent._mas_fthursday_last != datetime.date.today()",
            action=EV_ACT_PUSH
        )
    return "no_unlock"
