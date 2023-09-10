from . import utils


class Toon:
  health = 200
  attack_power = 3

  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.hp = Toon.health
    self.ap = Toon.attack_power


class Elf(Toon):
  pass


class Goblin(Toon):
  pass


def tick(walls, toons):
  toons.sort(key=lambda t: (t.y, t.x))
  for toon in toons:
    # 1. Check if adjacent to any toons of the other type.
    #    - If so, don't move.
    #    - Otherwise:
    #      - Find all the toons of the other type.
    #      - Find all the empty adjacent squares to the toons.
    pass


def part1(walls, toons):
  ticks = 0
  while not all(isinstance(t, tt)
                for t in toons
                for tt in [Elf, Goblin]):
    pass


def parse():
  input_str = utils.get_input("15")

  walls = set()
  toons = []
  for y, line in enumerate(input_str.split("\n")):
    for x, c in enumerate(line):
      if c == "#":
        # Wall.
        walls.add((x, y))

      elif c == "G":
        # Goblin.
        toons.append(Goblin(x, y))

      elif c == "E":
        # Elf.
        toons.append(Elf(x, y))

  return walls, toons


def main():
  print(part1(*parse()))


if __name__ == "__main__":
  main()