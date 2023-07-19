from models.event import Event
import datetime

event1 = Event("Mob Programming", datetime.date(2023, 6, 19), 14, "The Classroom", "try and mob this lab!!", True)
event2 = Event("Glastonbury", datetime.date(2023, 6, 10), 10000, "The South", "Madness, Music, Mugs", False)
event3 = Event("E3", datetime.date(2023, 9, 30), 8000, "LA", "Games", False)

events = [event1, event2, event3]