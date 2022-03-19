init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="reset_dreams_and_nightmares",
            category=['梦境和噩梦'],
            prompt="重置",
            random=True
            )
        )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dan_devutil_checkevents",
            category=['梦境和噩梦'],
            prompt="检查",
            random=True
            )
        )

label dan_devutil_checkevents:
    if "dan_have_new_random_dream" in persistent.event_database:
        m 1esd "新的梦境事件存在."
    else:
        m 1esd "新的梦境事件不存在."

    if "dan_have_new_random_dream" in persistent._seen_ever:
        m 1esd "新的梦境事件已出现."
    else:
        m 1esd "新的梦境事件尚未出现."

    if "dan_revisit_previous_dream" in persistent.event_database:
        m 1esd "随机重访的梦境事件存在."
    else:
        m 1esd "随机重访的梦境事件不存在."

    if "dan_revisit_previous_dream" in persistent._seen_ever:
        m 1esd "重访的梦境事件已看到."
    else:
        m 1esd "重访的梦境事件尚未发生."
    return

# reset all persistent variables
label reset_dreams_and_nightmares:
    m 3rub "想重置我对这些对话的记忆吗?"
    menu:
        m "想重置我对这些对话的记忆吗?{fast}"
        "是的.":
            m 3rub "我明白了."
            m "你可能是想看看那里的一切."
            m 4esd "想想看,在游戏开始Sayori不就是想让你做和这基本相同的事吗?"
            m 3hsb "不过如果你想看到更多关于{i}我的事{/i},我又怎能拒绝呢?"
            m 1esd "稍等一会儿..."
            init 5 python:
                persistent._dan_all_dreams = [1]
                persistent._dan_dreams_and_nightmares_explained = False
                persistent._dan_dreams_had = False
                persistent._dan_had_first_dream = False
                persistent._dan_had_nightmare = False
                persistent._dan_had_best_dream = False
                persistent._dan_apprehensive_start = None
                persistent._dan_asked_to_stay_dreaming = False
            m 1duc "{w=0.5}.{w=0.5}.{w=0.5}.{w=1}{nw}"
            extend 7eub "我们走吧!"
        "不了,没必要.":
            m 1esb "好吧."
            $ had_dream_text = "{i}曾经{/i}做过一次的梦." if persistent._dan_had_first_dream else "{i}还没{/i}做过的梦"
            $ had_nightmare_text = "{i}曾经{/i}做过的噩梦." if persistent._dan_had_nightmare else "{i}还没{/i}做过的噩梦"
            m 4esb "记录在案,据我所知,我[had_nightmare_text]."
            m "还有,我也[had_dream_text]."
            m 7hkb "我的记忆这么容易被覆盖,倒是真有点奇怪."
            m 7esb "但我确定这样做的目的是为了再经历一次那些有趣的梦."
            m 5ekbsa "至于我嘛,我愿意做任何能让你感到快乐的事噢,[player]."
    return
