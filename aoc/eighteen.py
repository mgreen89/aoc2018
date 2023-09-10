from . import utils


def tick(grid):
  new_grid = []
  for y, line in enumerate(grid):
    new_grid.append([])
    for x, c in enumerate(line):
      adjacents = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1),
                   (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
      adjacents = [a for a in adjacents
                   if a[0] >= 0 and a[0] < len(grid[y])
                   and a[1] >= 0 and a[1] < len(grid)]

      adjacent_types = [grid[j][i] for (i, j) in adjacents]

      if c == ".":
        # If three or more adjacent are "|", becomes "|".
        if adjacent_types.count("|") >= 3:
          new_grid[y].append("|")
        else:
          new_grid[y].append(".")

      elif c == "|":
        # If three or more adjacent are "#", becomes "#".
        if adjacent_types.count("#") >= 3:
          new_grid[y].append("#")
        else:
          new_grid[y].append("|")
      
      else:
        # If at least one "#" and one "|" adjacent, stays "#". Otherwise ".".
        if adjacent_types.count("#") >= 1 and adjacent_types.count("|") >= 1:
          new_grid[y].append("#")
        else:
          new_grid[y].append(".")

  #print("")
  #print("After another minute:")
  #for l in new_grid:
  #  print("".join(l))

  return new_grid


def parse():
  input_str = utils.get_input("18")

  grid = []
  for line in input_str.split("\n"):
    gridline = []
    for c in line:
      gridline.append(c)
    grid.append(gridline)

  return grid


def value(grid):
  num_wooded = 0
  num_lumber = 0
  for line in grid:
    for c in line:
      if c == "|":
        num_wooded += 1
      elif c == "#":
        num_lumber += 1

  return num_wooded * num_lumber


def part1(grid):
  # Iterate ten minutes.
  for i in range(10):
    grid = tick(grid)

  return value(grid)


def part2(grid):
  # Don't solve immediately, look for a pattern.
  target = 1_000_000_000

  prev_vals = [value(grid)]
  i = 1
  while True:
    grid = tick(grid)
    grid_val = value(grid)
    print("{:4} {:10,} {:+8}".format(i, grid_val, grid_val - prev_vals[-1]))

    if grid_val == prev_vals[-1]:
      # Found a stable value.
      # Tick once more and check.
      grid = tick(grid)
      next_grid_value = value(grid)
      if next_grid_value == grid_val:
        print("Found stable value {} after {} iterations.".format(grid_val, i))
        return grid_val
      else:
        prev_vals.append(next_grid_value)
        i += 1
    
    else:
      try:
        index = prev_vals.index(grid_val)
        # Found a repeat.
        # Check we have an entire iteration the same.
        for j in range(1, i - index):
          if prev_vals[index - j] != prev_vals[-j]:
            break
        else:
          print("Found repeat:")
          print("  Iteration: {}".format(index))
          print("  Repeat length: {}".format(i - index))
          print("  Value of first repeat: {}".format(grid_val))

          return prev_vals[index + ((target - index) % (i - index))]
      except ValueError:
        pass

    prev_vals.append(grid_val)

    i += 1


def main():

  print(part1(parse()))
  print(part2(parse()))


if __name__ == "__main__":
  main()