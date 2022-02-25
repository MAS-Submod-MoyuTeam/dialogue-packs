init 5 python:
    import datetime
    subDayOfWeek = datetime.datetime.now().weekday()
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
return "no_unlock"



#你好，我是乌克兰总统泽连斯基，美国已经向我承诺出售一批先进武器，现差50的尾款尚未付清，2月25日前V我50助我重整乌克兰军队，等我打败俄罗斯加入欧盟后我封你为国防部长，前苏联的封存技术你随便挑。我不知道什么KFC，也不知道什么疯狂星期四。
