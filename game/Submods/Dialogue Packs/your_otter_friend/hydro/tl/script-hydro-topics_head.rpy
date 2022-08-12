#importance of drinking water
# 翻译：@终不似、少年游


translate chinese python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_intro",
            prompt="喝水的重要性",
            category=["健康"],
            random=True
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_tips",
            prompt="多喝水小贴士",
            category=["健康"],
            conditional="seen_event('hyMod_topic_intro')",
            action=EV_ACT_RANDOM
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_signs",
            prompt="有脱水的迹象",
            category=["健康"],
            conditional="seen_event('hyMod_topic_intro')",
            action=EV_ACT_RANDOM
        )
    )

