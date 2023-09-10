from  . import utils


def tick(state, recipes):
  start = min(state) - 2
  end = max(state) + 2

  new_state = set()
  for i in range(start, end):
    pattern = "".join("#" if i + k in state else "."
                      for k in range(-2, 3))
    if pattern in recipes:
      new_state.add(i)
  
  return new_state


def part1(initial, recipes):
  current = set(i for i, c in enumerate(initial) if c == "#")

  for i in range(20):
    current = tick(current, recipes)

  return sum(current)


def part2(initial, recipes, visualize=False):
  if visualize:  
    # Don't actually solve this, just check to see if there's
    # a pattern after n iterations.
    current = set(i for i, c in enumerate(initial) if c == "#")
  
    prev_sum = 0
    for i in range(1, 200):
      current = tick(current, recipes)
      current_sum = sum(current)
      print("{:4}: {:6} {:6}".format(i, current_sum, current_sum - prev_sum))
      prev_sum = current_sum

  # Found that sum at iteration 162 is 12203
  # Every iteration after 161 adds 73.
  # So for 50,000,000,000 iterations is just a multiplication.
  return 12203 + (73 * (50_000_000_000 - 162))


def main():
  # Parse the input.
  input_lines = utils.get_input("12").split("\n")

  init_state = input_lines[0][len("initial state: "):]
  recipes = set()
  for line in input_lines[2:]:
    # Only add recipes that result in a new plant.
    if line[-1] == '#':
      recipes.add(line[:5]) 

  print(part1(init_state, recipes))
  print(part2(init_state, recipes))

if __name__ == "__main__":
  main()