init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_salad",category=['food'],prompt="Salad",random=True))

label monika_salad:
    m 1eua "[player], do you like salad?"
    m 1hua "I enjoy the delicacy a lot!"
    m 1hub "It's a healthy dish where you can mix almost anything together!"
    m 4rub "From tomatoes, lettuce, spinach, cheese, dressing, vinegar-"
    m 1sua "And so much more!"
    m 1eub "It's a great for a healthy diet."
    m 1nub "Something I hope your doing."
return
