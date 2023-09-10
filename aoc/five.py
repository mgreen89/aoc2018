from . import utils


def react(input_str):
  buf = []
  for c in input_str:
    if buf and buf[-1].swapcase() == c:
      buf.pop()
    else:
      buf.append(c)

  return buf


def part1(input_str):
  reacted = react(input_str)
  return len(reacted)


def part2(input_str):
  reagents = set(c.lower() for c in input_str)
  lengths = [(c, len(react(input_str.replace(c, "").replace(c.upper(), ""))))
             for c in reagents]
  sorted_lengths = sorted(lengths, key=lambda l: l[1])
  return sorted_lengths[0][1]


def main():
  input_str = utils.get_input("5")

  print(part1(input_str))
  print(part2(input_str))


if __name__ == "__main__":
  main()