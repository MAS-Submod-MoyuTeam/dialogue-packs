label fucking_weekend:
    m "嘿, [player]!"
    m "今天是疯狂星期四!来和我一起吃小汉堡!"
    m "啊哈哈...肯X基什么的没有给我广告费啦...只是随口一说."
    m "不过我或许能在今天为你做点什么..."
    m "等我一下..."
    #换上带有DATE的衣服
    python:
        store.ahc_utils.changeHairAndClothes(
            _day_cycle="day",
            _hair_random_chance=1,
            _clothes_random_chance=1,
            _exprop="date"
        )
    m "好了~"