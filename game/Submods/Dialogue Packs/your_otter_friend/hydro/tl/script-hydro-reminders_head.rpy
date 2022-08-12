#reminder setup
# 翻译：@终不似、少年游

translate chinese python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_start",
            prompt="你能提醒我喝水的事吗?",
            category=["健康"],
            conditional="seen_event('hyMod_topic_intro')",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
        )
    )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_stop",
            prompt="你不用再提醒我要补水了，我喝过了，爱你.",
            category=["健康"],
            pool=True,
            rules={"no_unlock": None}
        )
    )
    store.hyMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_event",
            conditional="store.hyMod_reminder.shouldTriggerReminder('hyMod_reminder_event')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None, "bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )
