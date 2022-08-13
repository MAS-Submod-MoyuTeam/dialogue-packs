default persistent._hy_mod_active_reminders = dict()

init 4 python in hyMod_reminder_utils:

    import datetime

    INTERVAL_HOURLY_1 = datetime.timedelta(seconds=3600)
    INTERVAL_HOURLY_3 = datetime.timedelta(seconds=3600 * 3)
    INTERVAL_HOURLY_6 = datetime.timedelta(seconds=3600 * 6)

    LATENCY_HOURLY = datetime.timedelta(seconds=3600)


init 4 python in hyMod_reminder:

    import store
    import datetime

    ### Workaround for handling action/conditional reassignments ###

    _reminderEvents = dict()

    def addReminderEvent(event):
        _reminderEvents[event.eventlabel] = (event, event.conditional, event.action)
        store.addEvent(event)


    ### Assertions ###

    def _assertReminderActive(ev_label):
        if not isReminderActive(ev_label):
            raise AssertionError("expected reminder to be active")

    def _assertReminderInactive(ev_label):
        if isReminderActive(ev_label):
            raise AssertionError("expected reminder to be inactive")


    ### Public methods ###

    def addRecurringReminder(ev_label, delay, delta, latency):
        _assertReminderInactive(ev_label)

        store.persistent._hy_mod_active_reminders[ev_label] = (
            datetime.datetime.now() + delay,  # datetime to trigger after
            delta,  # time between triggers
            latency  # time after which reminder should not trigger
        )

    def isReminderActive(ev_label):
        return ev_label in store.persistent._hy_mod_active_reminders

    def shouldTriggerReminder(ev_label):
        if not isReminderActive(ev_label):
            return False

        trigger, delta, latency = store.persistent._hy_mod_active_reminders[ev_label]

        return trigger <= datetime.datetime.now() <= trigger + latency

    def isReminderMissed(ev_label):
        trigger, delta, latency = store.persistent._hy_mod_active_reminders[ev_label]

        return trigger + latency <= datetime.datetime.now()

    def extendCurrentReminder():
        ev_label = store.mas_globals.this_ev.eventlabel

        extendReminder(ev_label)

    def extendReminder(ev_label, keep_up=False):
        _assertReminderActive(ev_label)

        now = datetime.datetime.now()

        while True:
            trigger, delta, latency = store.persistent._hy_mod_active_reminders[ev_label]

            store.persistent._hy_mod_active_reminders[ev_label] = (
                trigger + delta,  # ensure we base new trigger datetime off the initial trigger timedelta
                delta, latency
            )

            if keep_up:
                if store.persistent._hy_mod_active_reminders[ev_label][0] <= now:
                    continue
                else:
                    break
            else:
                break

        # HACK: workaround so that MAS doesn't strip conditional and action from reminder event.
        ev, conditional, action = _reminderEvents[ev_label]
        ev.conditional, ev.action = conditional, action

    def stopReminder(ev_label):
        _assertReminderActive(ev_label)

        del store.persistent._hy_mod_active_reminders[ev_label]


init 7 python in hyMod_reminder:

    import store

    ### Event properties unlock ###

    for ev_label in _reminderEvents.keys():
        ev = store.mas_getEV(ev_label)
        store.Event.unlockInit("conditional", ev)
        store.Event.unlockInit("action", ev)

        _ev, conditional, action = _reminderEvents[ev_label]
        _reminderEvents[ev_label] = (ev, conditional, action)

    ### Missed reminder handling ###

    def _handleMissedReminders():
        for ev_label in store.persistent._hy_mod_active_reminders.keys():
            trigger, delta, latency = store.persistent._hy_mod_active_reminders[ev_label]
            if isReminderMissed(ev_label):
                extendReminder(ev_label, keep_up=True)

    _handleMissedReminders()
    store.mas_submod_utils.registerFunction("ch30_hour", _handleMissedReminders)