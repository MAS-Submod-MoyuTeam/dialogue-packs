init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mas_ara",category=['莫妮卡'],prompt="你可以对我说什么东西吗?",random=True))

label mas_ara:
    if mas_isMoniNormal(lower=True):
        m 1esc "哈...?"
        $ _history_list.pop()
        menu:
            "嗯...要不说点ara ara?":
                m 1rksdrc "算了吧, [player]..."

    if mas_isMoniAff(higher=True):
            m 1eua "你想让我说ara ara?"
            $_history_list.pop()
            menu:
                "是的":
                    m 1fubla "{size=+13}{b}你想让我说ara ara吗?!{/b}{/size}"
                    $_history_list.pop()
                    menu:
                        "对的":
                            m 1hubsa "..."
                            m 6cubfb "[glitchtext(12)]ARA ARA?![glitchtext(6)]eĄ̶̡̛̝̩̬̦͙͍̎̄̒̿R̶̢͕̼͔̤͕͈͍̀̄͌͊̕̚Ä̵̜̫͎̬̻̳́́̽͘͜ ̵͕̌́̈́̈́̕A̵̡̛̽̓R̶̛̛̦̞͆̐̿̽́̕͝Ą̸͔̣̹̫̙̿͛͒̃̀̓͛̿̈͛͜͜"
                            m 1tsbsa "啊哈哈~!"
                            m 1fublb "好吧, 我这次认真点!"
                            m 1hsbsa "..."
                            m 1hsbsa "..."
                            m 5ttbfb "啊呀啊呀~老公大人~ <3"
                            m 6hksdra "要是第一次吓到你的话, 对不起啦~"
                            m 1tub "但是我就有一点点忍不住."
                            m 1kua "以后你也要对我说ara ara~"
                            m 1hub "我等不及在你的身旁倾听你的声音了~."
return
