#random quip for when the player comes back and it calmed down, if they decide to
#not vent/rant to Monika
init python:
    RandomCalmDownWelcome = ["让我们花更多时间在一起吧!",
        "让我们把今天剩下的时间全变成快乐吧.",
        "接下来想做什么呢？"]
    RandomCalmDownWelcomeQuip = random.choice(RandomCalmDownWelcome)
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mental_calmdown_idle",
            prompt="我要去冷静一下",
            category=['马上回来'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label mental_calmdown_idle:
    m 1euc "你需要冷静，[player]？"
    m "希望不是我扫了你的兴！"
    m 3euc "嗯...可以告诉我你为什么难过吗，[player]？"
    menu:
        "好":
            $ PlayerAskedMonikaToVent = True
            m 1eua "那就继续说说你为什么难过吧，[player]。"
            m "我会给你一个按钮，这样你就可以在我说完后告诉我，我也不会在期间打断你了"
            menu:
                "莫妮卡，我说完了...":
                    jump mental_calmdown_idle_callback
        "不用了谢谢":
            $ PlayerAskedMonikaToVent = False
            m 1euc "哦，好吧。"
            m 3hub "我在这等着你哦，[player]！"

    #Set up the callback label
    $ mas_idle_mailbox.send_idle_cb("mental_calmdown_idle_callback")
    #Then the idle data
    $ persistent._mas_idle_data["mental_idle_calmdown"] = True
    return "idle"

label mental_calmdown_idle_callback:

    m 3eud "你冷静下来了吗，[player]？"
    menu:
        "是的":
            if PlayerAskedMonikaToVent == True:
                m 1eua "很高兴我能帮你冷静一点，[player]。"
            else:
                m 1eua "很高兴你冷静下来了，[player]。"
        "还没":
            m 1euc "如果你没法完全冷静的话，去一个更平静的地方可能会有所帮助。"
            m 3eub "就像在这！"
    m 1eub "你知道的，我真的希望我能帮到更多..."
    m 3euc "即使我不能亲自去到你身边。"
    extend 3eua "我也会永远在电脑里陪着你！"
    m 1rusdlc "除非我能找到办法离开这台电脑。"
    m 1eua "总之，[RandomCalmDownWelcomeQuip]"

    return