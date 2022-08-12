#reminder setup

init 5 python in mas_bookmarks_derand:
    label_prefix_map["hyMod_reminder_"] = label_prefix_map["monika_"]


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_start",
            prompt="Can you remind me about drinking water?",
            category=["health"],
            conditional="seen_event('hyMod_topic_intro')",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
        )
    )

label hyMod_reminder_start:
    m 3sub "[player], of course! Thanks for asking me to!"
    m 3hublb "Your health is really important to me, you know that."
    m 4hubla "And this is a huge step on improving it!"

    m 4lubla "It's usually recommended to grab a glass of water every hour, is that okay with you?{nw}"
    menu:
        m "It's usually recommended to grab a glass of water every hour, is that okay with you?{fast}"

        "Yep!":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_1
            m 1dublb "Alrighty then! I'll be sure to remind you about it hourly, [mas_get_player_nickname()]~"
            jump .add_reminder

        "Maybe every 3 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_3

        "How about every 6 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_6

    m 1dublb "Alrighty then! I'll be sure to remind you about it every few hours, [mas_get_player_nickname()]~"

label .add_reminder:
    python:
        store.hyMod_reminder.addRecurringReminder(
            "hyMod_reminder_event",
            datetime.timedelta(seconds=3600), interval, store.hyMod_reminder_utils.LATENCY_HOURLY
        )

        mas_hideEVL("hyMod_reminder_start", "EVE", lock=True)
        mas_showEVL("hyMod_reminder_stop", "EVE", unlock=True)

    return "derandom"

#stop reminder
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_stop",
            prompt="You no longer need to remind me about hydration.",
            category=["health"],
            pool=True,
            rules={"no_unlock": None}
        )
    )

label hyMod_reminder_stop:
    m 7esb "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.hyMod_reminder.stopReminder("hyMod_reminder_event")
        mas_hideEVL("hyMod_reminder_stop", "EVE", lock=True)
        mas_showEVL("hyMod_reminder_start", "EVE", unlock=True)

    return


init 5 python:
    store.hyMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_reminder_event",
            conditional="store.hyMod_reminder.shouldTriggerReminder('hyMod_reminder_event')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None, "bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )

label hyMod_reminder_event:
    $ mas_display_notif(
        m_name,
        [
            "[player]! It's time to hydrate!",
            "[player], it's time to drink a cup of water!",
            "Drinking enough water every day keeps the doctor away!",
            "If there's something that makes you feel alive… that's water!",
            "Drink some water, [player]! Your body will thank you.",
            "Drink your way to better health, [player]! Drink water~",
            "Drinking water is like taking a shower on the inside!"
        ],
        "Window Reactions"
    )

    m 3subla "Hey, [player]! It's time to drink water~"
    m 3kubla "Try to drink a full cup, okay?"
    m 3lublb "Or at least half~"
    m 1dubla "Thank you for taking care of yourself, [mas_get_player_nickname()]!"

    # Do not move this anywhere, this must be above the return.
    $ store.hyMod_reminder.extendCurrentReminder()
    return