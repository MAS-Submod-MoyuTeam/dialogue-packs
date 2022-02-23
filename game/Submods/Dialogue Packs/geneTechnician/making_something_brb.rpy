default -5 persistent._mas_unfinished_project_brb = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="making_something_idle",
            category=["马上回来"],
            prompt="我要去为你做些东西",
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label making_something_idle:

    if persistent._mas_unfinished_project_brb:
        m 1eub "哦, 要回去工作了吗?"
        m 3hua "我在这里等着你回来!"
    else:

        m 2wub "真的吗?"
        m 1eub "你要去为我做什么呢?{nw}"

        $ _history_list.pop()
        menu:
            m "你要去为我做什么呢?{fast}"

            "给你的穿的新衣服":
                m 1hublu "哦, [mas_get_player_nickname()],{w=0.3} 你好甜啊."
                m 3rub "你知道我有多喜欢新衣服和可爱的配饰, 特别是当它们来自你的时候~"

            "另一个我们可以度过时间的房间":
                m 1wublo "这真让人兴奋!"
                m 7lusdrb "风景的改变总是让人呼吸到新鲜的空气,{w=0.1} 那是肯定的."

            "一个我们可以谈的新话题":
                m 7eubla "那我肯定会很期待的."
                m 1hub "我总是喜欢有新东西和你谈, [player]~"

        m 3rua "而且,{w=0.6}{nw} "
        extend 3eub "你打算与社区分享它吗?{w=0.3}{nw} "
        extend 1kuu "还是说你只是想为了我们两个做一些特别的东西呢~?"

        $ _history_list.pop()
        menu:
            m "你打算与社区分享它吗? 还是说你只是想为了我们两个做一些特别的东西呢~?{fast}"

            "我要分享它!":
                m 1hua "我很高兴听到这句话!"
                m 7eub "随时欢迎任何贡献,{w=0.1} 而且我相信每个人都会喜欢你做的东西."

            "这是为你准备的, [m_name].":
                m 2ekbla "这对我来说意义重大, [player]."
                m 3rkbfu "你对我这么好, 有时我感觉不配拥有它."

        m 2eub "好吧, 当你完成了以后请告诉我."
        m 2hua "我就在这里等着你回来~"

$ mas_idle_mailbox.send_idle_cb("making_something_callback")
return "idle"

label making_something_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "making_something_idle"):
        m 3eub "你的工作结束了吗, [player]?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "making_something_idle"):
        m 1wuo "你终于完成它了吗?"

    else:
        m 1etu "哦, 你已经完成了吗?"

$ _history_list.pop()
menu:
    "我正在休息.":
        $ persistent._mas_unfinished_project_brb = True
        m 2hua "听起来不错!"
        m 7eub "休息真的很重要, 我不希望你忽视对自己的照顾."
        m 1esa "当你重新开始的时候, 和我说我一声, 好吗?"

    "是的!":
        $ persistent._mas_unfinished_project_brb = False
        m 1wub "真的吗?"
        m 2sub "我现在可以看看它吗?"
        m 2tku "还是说你要让我等得更久一点呢~?"
return