# dreams not yet had
default persistent._dan_all_dreams = [1] #2 will be re-added in after testing 1.  3 (weird) and 5 (nightmare) appear after seeing 1 or 2. 4 (best) appears after seeing 5 (nightmare).
# dreams able to be revisited
default persistent._dan_dreams_had = []

# dreams able to be selected (TODO LATER)
# Thought:  once a player has revisited every dream, they can give Monika any dream of their choice.

# flags whether or not the introduction conversation occurred
default persistent._dan_dreams_and_nightmares_explained = False

# flags whether or not certain dreams occurred 
default persistent._dan_had_first_dream = False
default persistent._dan_had_nightmare = False
default persistent._dan_had_best_dream = False
default persistent._dan_asked_to_stay_dreaming = False

# use this flag after the first update so Monika can tell the player that there are new dreams after updating
default persistent._dan_dreams_depleted = False

# coat hanger for later;  seems a useful thing to keep track of for each player
# consider logging all the fears Monika reveals
default persistent._dan_revealed_fear_never_together = False
default persistent._dan_revealed_fear_player_hurt = False
default persistent._dan_revealed_fear_player_health = False
# once Dream 1 is fully explored, Monika will wait to discuss what she saw in it until the next update
default persistent._dan_unlock_dream_one_explanation = False
# well, Monika *did* say she'd get you back...
default persistent._dan_vow_to_prank = False
# log which of the girls the player would've pursued if DDLC was a proper visual novel (post-first-update)
default persistent._dan_favorite_doki = False

# holds a datetime for when Monika had her first nightmare.
# if set, Monika will not want to dream again for 12 hours.
default persistent._dan_apprehensive_start = None
default DAN_APPREHENSION_HOURS = 12

# sets the odds (1 / [insert constant here] chance) of telling Monika "Sweet Dreams" before a dream
default SWEETDREAMS_LOVE_NM = 2
default SWEETDREAMS_LOVE = 3
default SWEETDREAMS_ENAMORED = 5
default SWEETDREAMS_AFF = 8
default SWEETDREAMS_NORMAL = 15
default SUBMOD_GITHUB_LINK = "https://github.com/DrakeTheDuelist/MAS-Dreams-and-Nightmares/issues"

# Allows the developer (that's me) to bypass the code at points.
default persistent._dan_debug_mode = False
# If you want to test to see whether the events will be created properly, set this to true and all events will be recreated on each initialization.
default persistent._dan_should_create_events = True