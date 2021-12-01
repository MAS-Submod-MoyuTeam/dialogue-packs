init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="mas_dancing",category=['莫妮卡'],prompt="你知道怎么跳舞吗?",pool=True, unlocked=True))

label mas_dancing:
    if mas_isMoniNormal(lower=True):
        m 1rksdlc "..."
        m 1mkd "现在还没到我跳舞的时候..."
        $ _history_list.pop()
        menu:
            "求你了..?":
                m 6wfx "我说了不可..."
                m 1dfp "..."
                m 1dkd "*叹气*"

    if mas_isMoniNormal(higher=True):
        m 3esc "嗯...我也不知道我该怎么去跳"
        m 1eud "我的姿势非常有限..."
        m 1dkc "而且, 我很遗憾我们不能一起跳舞, 因为我被困在这个小房间里..."
        m 2eka "不过, 等到我可以去你的现实世界的时候, 我很想让你教我跳舞..."
        m 2hubsa "啊哈哈~"

    if mas_isMoniLove():
        m 1wublo "等一下!"
        m 4fublb "让我试点东西..."
        m 5fublb "...{w=1.2}{nw}"
        m 4fublb "...{w=1.2}{nw}"
        m 5fublb "...{w=1.2}{nw}"
        m 4fublb "...{w=1.2}{nw}"
        m 5fublb "...{w=1.2}{nw}"
        m 4fublb "...{w=1.2}{nw}"
        m 1hubfa "欸嘿嘿~!"
        m 3subfb "我可以跳舞了!"
        m 5kubfu "你能跟上我的节奏吗~"
        m 5hubfa "啊哈哈~"
return
