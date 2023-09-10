import copy
import re

from . import utils


class Step:
  def __init__(self, id):
    self.id = id
    self.prereqs = set()


def part1(steps):
  sorted_steps = sorted(list(steps.values()),
                        key=lambda s: s.id)
  step_order = []
  
  while sorted_steps:
    for step in sorted_steps:
      if not step.prereqs:
        # Do it, and remove it from all pre-reqs.
        step_order.append(step)
        for other in sorted_steps:
          if other is not step:
            other.prereqs.discard(step)
    
        sorted_steps.remove(step)
        break

  return "".join(s.id for s in step_order)


def part2(steps):
  sorted_steps = sorted(list(steps.values()),
                        key=lambda s: s.id)

  class Worker:
    def __init__(self):
      self.step = None
      self.remaining = 0

    def start(self, step):
      self.step = step
      # ord("A") = 65
      self.remaining = ord(step.id) - 4

    def tick(self):
      if self.remaining > 0:
        self.remaining -= 1

    @property
    def idle(self):
      return self.remaining == 0

    @property
    def step_id(self):
      if self.step is not None:
        return self.step.id
      else:
        return "-"

  ticks = 0
  workers = [Worker(), Worker(), Worker(), Worker(), Worker()]
  def tick():
    nonlocal ticks
    ticks += 1
    for w in workers:
      w.tick()

    #print("{:4}   {} {} {} {} {}".format(ticks, *[w.step_id for w in workers]))

    for w in workers:
      if w.idle and w.step is not None:
        # Step has finished.
        for other in sorted_steps:
          if w.step is not other:
            other.prereqs.discard(w.step)
        w.step = None

  while sorted_steps:
    idle_workers = [w for w in workers if w.idle]
    for step in sorted_steps.copy():
      if not idle_workers:
        break

      if not step.prereqs:
        idle_workers[0].start(step)
        sorted_steps.remove(step)
        idle_workers.pop(0)

    tick()

  while any(not w.idle for w in workers):
    tick()

  return ticks

def main():
  re_ = re.compile(r"Step (?P<prereq>[A-Z]) must be finished before step (?P<step>[A-Z]) can begin.")

  steps = {}
  for line in utils.get_input("7").split("\n"):
    m = re_.match(line)
    assert m is not None
    step_id = m.group("step")
    prereq_id = m.group("prereq")
    
    if prereq_id in steps:
      prereq = steps[prereq_id]
    else:
      prereq = Step(prereq_id)
      steps[prereq_id] = prereq

    if step_id in steps:
      step = steps[step_id]
    else:
      step = Step(step_id)
      steps[step_id] = step
    
    step.prereqs.add(prereq)

  print(part1(copy.deepcopy(steps)))
  print(part2(copy.deepcopy(steps)))


if __name__ == "__main__":
  main()
