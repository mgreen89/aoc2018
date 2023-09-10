import collections
import matplotlib as mpl
import matplotlib.pyplot as plt

from . import utils


class Point:
  def __init__(self, start_x, start_y, vel_x, vel_y):
    self.start_x = start_x
    self.start_y = start_y
    self.vel_x = vel_x
    self.vel_y = vel_y
    
  @classmethod
  def from_line(cls, line):
    start_x, start_y = map(int, line[10:24].split(","))
    vel_x, vel_y = map(int, line[36:42].split(","))
    return cls(start_x, start_y, vel_x, vel_y)

  def pos_after(self, ticks):
    return (self.start_x + self.vel_x * ticks,
            self.start_y + self.vel_y * ticks)


def part1(points):
  areas = collections.defaultdict(lambda x:0)

  local_min = 100000
  for scale in [10000, 1000, 100, 10, 1]:
    start = local_min - (10 * scale)
    end = local_min + (10 * scale)
    for i in range(start, end, scale):
      new_points = [p.pos_after(i) for p in points]
      min_x = min(p[0] for p in new_points)
      max_x = max(p[0] for p in new_points)
      min_y = min(p[1] for p in new_points)
      max_y = max(p[1] for p in new_points)
      areas[i] = (max_x - min_x) * (max_y - min_y)
      #print("{:7}: {}".format(i, areas[i]))

    local_min = min(areas, key=areas.get)

  # At the minimum area, print a representation.
  minimum_points = [p.pos_after(local_min) for p in points]
  min_x = min(p[0] for p in new_points)
  max_x = max(p[0] for p in new_points)
  min_y = min(p[1] for p in new_points)
  max_y = max(p[1] for p in new_points)

  # Coords are from left, from top, so:
  #  - zero all coords based on the minimums
  #  - flip the Y values
  plotting_points = [(p[0] - min_x, max_y - p[1]) for p in minimum_points]

  mpl.use("Agg")
  plt.scatter([p[0] for p in plotting_points],
              [p[1] for p in plotting_points])
  plt.savefig("aoc/outputs/ten.png")

  return "Number of ticks: {}".format(local_min)

def main():
  input_lines = utils.get_input("10").split("\n")
  points = [Point.from_line(line) for line in input_lines]

  print(part1(points))

if __name__ == "__main__":
  main()