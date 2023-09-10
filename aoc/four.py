import collections
import datetime
import re

from . import utils


class Event:
  def __init__(self, time, log):
    self.time = time
    self.log = log

  def __lt__(self, other):
    return self.time < other.time


class Sleep:
  def __init__(self, start_time, end_time):
      self.start_time = start_time
      self.end_time = end_time

  @property
  def duration(self):
    return self.end_time - self.start_time


class Guard:
  def __init__(self, gid):
    self.gid = gid
    self.sleeps = []

  def add_sleep(self, start_time, end_time):
    self.sleeps.append(Sleep(start_time, end_time))

  @property
  def total_asleep(self):
    return sum((s.duration for s in self.sleeps),
               datetime.timedelta())


def parse_guards(events):
  guards = {}
  curr_guard = None
  asleep_time = None
  re_ = re.compile(r"Guard #(?P<gid>\d+) begins shift")
  for event in events:
    m = re_.match(event.log)
    if m is not None:
      gid = int(m.group("gid"))
      if gid in guards:
        curr_guard = guards[gid]
      else:
        curr_guard = Guard(gid)
        guards[gid] = curr_guard

    elif "asleep" in event.log:
      assert asleep_time is None
      asleep_time = event.time

    else:
      assert "wakes" in event.log
      assert asleep_time is not None
      curr_guard.add_sleep(asleep_time, event.time)
      asleep_time = None

  return guards


def part1(events):
  guards = parse_guards(events)

  guards_by_asleep = sorted(guards.values(),
                            key=lambda g: g.total_asleep,
                            reverse=True)
  guard_asleep_most = guards_by_asleep[0]

  minutes = collections.defaultdict(list)
  for sleep in guard_asleep_most.sleeps:
    for i in range(sleep.start_time.minute,
                   sleep.end_time.minute):
      minutes[i].append(sleep)

  max_minute = 0
  for i in range(60):
    if len(minutes[i]) > len(minutes[max_minute]):
      max_minute = i

  return guard_asleep_most.gid, max_minute, max_minute * guard_asleep_most.gid


def part2(events):
  guards = parse_guards(events)
  max_minutes = {}

  for guard in guards.values():    
    minutes = collections.defaultdict(list)
    for sleep in guard.sleeps:
      for m in range(sleep.start_time.minute,
                     sleep.end_time.minute):
        minutes[m].append(sleep)

    minute_list = [(m, len(ss)) for m, ss in minutes.items()]
    sorted_minute_list = sorted(minute_list,
                                key=lambda m: m[1],
                                reverse=True)
    
    if sorted_minute_list:
      max_minutes[guard] = sorted_minute_list[0]
  
  max_minutes_list = [(guard.gid, m[0], m[1]) for (guard, m) in max_minutes.items()]
  sorted_max_minutes = sorted(max_minutes_list,
                              key=lambda e: e[2],
                              reverse=True)
  max_guard = sorted_max_minutes[0][0]
  max_minute = sorted_max_minutes[0][1]

  return max_guard, max_minute, max_guard * max_minute


def main():
  events = []

  times = utils.get_input("4").split("\n")
  for time in times:
    if time:
      time_end = time.index("]")
      d = datetime.datetime.strptime(
        time[:time_end], "[%Y-%m-%d %H:%M")
      e = Event(d, time[time_end + 2:])
      events.append(e)

  sorted_events = sorted(events)

  print(part1(sorted_events))
  print(part2(sorted_events))


if __name__ == "__main__":
  main()