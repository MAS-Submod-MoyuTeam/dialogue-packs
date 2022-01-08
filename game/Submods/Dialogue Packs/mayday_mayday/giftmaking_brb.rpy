init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="giftmaking_brb",
            category=['马上回来'],
            prompt="我要去为你的现实做一点东西",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label giftmaking_brb:
    $ ev = mas_getEV("giftmaking_brb")

    if ev.shown_count == 0:
        m 6sublb "真的吗? 你要这么做了吗!?"
        m 1skbla "听到你说这话意义重大, [player]."
        m 1fublb "我等不及要看你做的东西了~!"
        m 1hublb "好运哦~!"
        

    elif ev.shown_count == 2:
        m 1eublb "好的, [player]."
        m 1sublb "我等不及去看到你这次的作品了!"
        m 3hsblb "只要确保你不要过度劳累， 好吗?"
        m 1hublb "好运~!"

    elif ev.shown_count == 4:
        m 1wubld "天呐, 你为了做了这么多东西, 真是把我宠坏了!"
        m 1lksdlu "我不禁感觉有些难过, 我还没有什么可以为你做的这些表示回报."
        m 1hkblsdlu "我很快就会想出一个办法的, 但你现在必须听我说."
        m 5ekbfu "我希望你知道, 我很感谢你为了做的每一件事, [player]."
        m 5ekbfb "好运~!"

    else:
        m 2esbla "好的, [player]."
        m 2fkbla "你想帮助我的现实变好这让我真的很开心."
        m 4nublb "只是确保在你工作时有足够的休息时间, 好吗?"
        m 1hublb "好运~!"

#...
$ mas_idle_mailbox.send_idle_cb("giftmaking_brb_callback")
return "idle"

label giftmaking_brb_callback:

    m 1eua "现在都完成了吗?"
    m 2wub "我可以看看你你到目前为止都做了些什么吗?"
    m 5ftblu "还是说你要给我个惊喜~?"
    m 5kublb "啊哈哈~"
