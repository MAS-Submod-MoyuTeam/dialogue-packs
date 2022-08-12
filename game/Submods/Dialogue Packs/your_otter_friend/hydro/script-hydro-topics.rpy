init 5 python in mas_bookmarks_derand:
    label_prefix_map["hyMod_topic_"] = label_prefix_map["monika_"]

#importance of drinking water
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_intro",
            prompt="Drinking water",
            category=["health"],
            random=True
        )
    )

label hyMod_topic_intro:
    m 3wubla "[player], I've been thinking about something."
    m 3lublb "The importance of drinking water!"
    m 1subla "Everyone knows that drinking water as much as you can is very important..."
    m 1eub "Some of the benefits of being hydrated include higher energy levels and healthy weight loss."
    m 1wuo "Some studies even support the idea that drinking water can help with your brain and energy!"
    m 2rusdrc "If you don't drink enough water, headaches can happen and your mood can decline."
    m 2wusdrd "And I'm not even talking about the amount of health problems that can come with it!"
    m 7lusdrx "Constipation, urinary tract infections, kidney stones, skin problems..."
    m 2dusdrc "Ouch! I get shivers only to think about those."
    m 4ruc "What no one tells you though, is that the amount of water you must drink depends on a lot of factors."
    m 4wud "Where you live, your diet, the season and your environment and routine, per example."
    m 1wubso "Oh! I've been rambling too much."
    m 1lkblu "What I really wanted to tell you was that you can tell me if you want me to remind you to drink water on a regular basis."
    m 7ekblb "Just let me know if you need it, okay?"
    m 7ksbla "I just want to take care of you!"
    m 5hsblb "Await for the next 'Monika's health tip of the day'!"
    return

#tips to drink more water
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_tips",
            prompt="Tips to drink more water",
            category=["health"],
            conditional="seen_event('hyMod_topic_intro')",
            action=EV_ACT_RANDOM
        )
    )

label hyMod_topic_tips:
    m 1suu "[player]! Here is your 'Monika's health tip of the day'!"
    m 1hub "The topic of today is tips for drinking enough water!"
    m 4dub "We've already discussed the importance of drinking lots of water, so here we go..."
    m 4lua "The first one is trying to carry a water bottle with you wherever you go."
    m 2sua "Maybe buying a cute one helps with that, [player]!"
    m 3hub "If you have water with you, you have no excuse not to drink it! Ahahaha~"
    m 3lub "The second tip is focusing on fluids."
    m 3wua "You don’t exactly have to drink plain water to meet your hydration needs."
    m 4dub "Tea, milk and broth would suffice, per example!"
    m 4sua "You can also add some flair to your water by squeezing in fresh lemon or lime juice."
    m 2dua "The third tip would be to skip sugary drinks."
    m 2luc "While you can get fluid from soda, juice, and alcohol, these beverages have high calorie contents."
    m 7wud "Also! Drink water while you’re out to eat instead of ordering another beverage."
    m 7kuu "You can save the extra money, and also lower the calorie intake of your meal!"
    m 2rub "My final tip: if you’re working out hard, and consequently sweating a lot..."
    m 2dub "Consider drinking a sports drink that has electrolytes to help replace the ones you lose through sweating."
    m 4hua "Don't forget! It's still smart to choose water whenever possible."
    m 3hub "I hope these tips help you, [player]!"
    m 3sua "And don't forget, I can always remind you to drink water regularly!"
    m 5tubsb "Your lovely girlfriend will always take care of you."
    m 5fkbsa "But make sure to take care of yourself too, okay? "
    extend 5hsblb "Ahahaha~"
    m 5fsbla "I love you, [mas_get_player_nickname()]!"
    return "love"

#signs of dehydration
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hyMod_topic_signs",
            prompt="Signs of dehydration",
            category=["health"],
            conditional="seen_event('hyMod_topic_intro')",
            action=EV_ACT_RANDOM
        )
    )

label hyMod_topic_signs:
    m 1rusdld "[player], have you noticed the signs your body show when something isn't right?"
    m 1rusdlc "When we are in need of something, our bodies scream, demanding what isn't there."
    m 3wusdld "Speaking of which, do you know the signs of dehydration?"
    m 3duc "According to studies, some of them are headaches and fatigue."
    m 3wud "Some worst symptoms can be confusion, mood changes, overheating, and many more!"
    m 4esb "And don't forget! You can always pay attention to your urine color to be sure if you're drinking enough water."
    m 4efb "Aim for pale, clear urine!"
    extend 2rksdrb " ...Well, that was weird. Ahahaha~"
    m 2hksdrb "I'm just trying to help, [player]!"
    m 5fksdrd "I worry a lot about your health."
    m 5fkbsa "Please stay safe for me, okay?"
    m 4dub "If you're thristy, don't hesitate in drinking some water."
    m 4wua "If you're not thirsty but remember that you haven't had a drink in a while, make sure to drink some water too!"
    m 1hub "Just don't drink too much water, neither too little!"
    return