#How are you today?, dialogue submod by my-otter-self and IsabellaLikesCandy on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_topic_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_howareyou_BELLA",
            category=["莫妮卡"],
            prompt="你今天怎么样, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_howareyou_BELLA:
    m 3hubsb "我很高兴我能在这儿和你在一起, [mas_get_player_nickname()]!"
    m 3hua "谢谢你的问候!"
    m 1eka "你真的是我的阳光，你知道的?"
    m 1huu "诶嘿嘿~"
    m 1eub "我希望你也过得不错!"
    m 1rksdla "即使你马上就要走了..."
    m 1hubsb "就跟我在这里呆一会儿!"
    m 2eubsu "我相信这会让你过得更好~"
    m 2kubsa "我会尽我最大的努力让每一天都成为你生命中最美好的一天."
    m 2ekbsb "啊哈哈~ 我爱你, [player]!"
return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
