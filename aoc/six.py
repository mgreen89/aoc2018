from . import utils


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.area = 0
    self.infinite = False

  def dist(self, x, y):
    """Manhattan distance to (x, y)."""
    return abs(self.x - x) + abs(self.y - y)


def part1(points):
  def find_closest(x, y):
    pds = sorted(((p, p.dist(x, y)) for p in points),
                 key=lambda x: x[1])
    
    if pds[0][1] == pds[1][1]:
      # Equidistant
      return None
    return pds[0][0]

  min_x = min(p.x for p in points)
  max_x = max(p.x for p in points)
  min_y = min(p.y for p in points)
  max_y = max(p.y for p in points)

  for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
      p = find_closest(i, j)

      if p:
        if i in (min_x, max_x) or j in (min_y, max_y):
          p.infinite = True
      
        else:
          p.area += 1

  return max(p.area for p in points if not p.infinite)


def part2(points):
  safe_dist = 10000
  
  min_x = min(p.x for p in points)
  max_x = max(p.x for p in points)
  min_y = min(p.y for p in points)
  max_y = max(p.y for p in points)

  safe_area_size = 0
  for i in range(min_x, max_x):
    for j in range(min_y, max_y):
      if sum(p.dist(i, j) for p in points) < safe_dist:
        safe_area_size += 1

  return safe_area_size


def main():
  points = []
  for line in utils.get_input("6").split("\n"):
    (x, y) = line.split(",")
    points.append(Point(int(x), int(y)))

  print(part1(points))
  print(part2(points))


if __name__ == "__main__":
  main()