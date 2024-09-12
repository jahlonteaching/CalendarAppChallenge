from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
class Reminder:
    EMAIL: str = "email"
    SYSTEM: str = "system"

    date_time: datetime 
    type: str 
    
    def __str__(self):
      return  f"Reminder on {self.date_time} of type {self.type}"

# TODO: Implement Event class here
class Event:
   
   title: str = title
   description: str 
   date_: date
   start_at: time 
   end_at: time 
   id: str = field(default_factory=generate_unique_id)

   def add_reminder(self):
       reminder = Reminder(date_time=self.date_time, type=self.type_)
       self.reminders.append(reminder)

   def delete_reminder(self, reminder_index: int):
      if 0 <= reminder_index < len(self.reminders):
        del self.reminders[reminder_index]
      else:
        reminder_not_found_error()

   def __str__(self):
        return (f"Event '{self.title}' on {self.date_} from {self.start_at} to {self.end_at} "
              f"with {len(self.reminders)} reminders.")
class Schedule:
    def __init__(self, date_: date):
            self.date_ = date_
            self.slots = {}
            self._init_slots()

    def _init_slots(self):
         current_time = time(0, 0)
         while current_time < time(23, 45):
              self.slots[current_time] = None
              current_time = (datetime.combine(date.today(), current_time) + timedelta(minutes=15)).time()
              self.slots[time(23, 45)] = None
             







# TODO: Implement Day class here


# TODO: Implement Calendar class here
