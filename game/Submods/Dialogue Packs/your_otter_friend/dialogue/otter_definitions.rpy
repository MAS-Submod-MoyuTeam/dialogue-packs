# tl: 终不似、少年游
init 5 python in mas_bookmarks_derand:
    label_prefix_map["otter_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_playtime",
            category=["统计"],
            prompt="我们在一起多久了, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_playtime:
    m 3eub "我们在一起 [mas_getTotalPlaytime()]了."
    m 5hubla "我爱你, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_dailyplaytime",
            category=["统计"],
            prompt="我们今天在一起待了多久了, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_dailyplaytime:
    m 3eub "今天, 我们呆在一起[mas_getSessionLength()]了."
    m 5hubla "我爱你, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_absence",
            category=["统计"],
            prompt="你等了我多久, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_absence:
    m 3eub "我等了你 [mas_getAbsenceLength()]."
    m 5hubla "我好想你, [player]!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_firstses",
            category=["统计"],
            prompt="我什么时候来的, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_firstses:
    m 3eub "你来到这里是[mas_getCurrSeshStart()]."
    m 5hubla "我爱你, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_lastses",
            category=["统计"],
            prompt="我最后一次见你是什么时候, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_lastses:
    m 3eub "这是你最后一次来看我的时间，[mas_getLastSeshEnd()]."
    m 5hubla "我爱你, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_totalses",
            category=["统计"],
            prompt="我来看过你几次, [m_name]?",
            pool=True,
            unlocked=True
        )
    )

label otter_totalses:
    m 3eub " 你一共看我[mas_getTotalSessions()]次了 ."
    m 5hubla "我爱你, [player]!"
return "love"
