# Day One
from . import utils

def part1(input_):
  curr = 0
  for i in input_:
    curr += int(i)

  return curr


def part2(input_):
  history = set([0])
  curr = 0
  while True:
    for i in input_:
      curr += int(i)
      if curr in history:
        return curr
      history.add(curr)


def main():
  input_ = [int(l) for l in utils.get_input("1").split("\n")]
  print(part1(input_))
  print(part2(input_))

if __name__ == "__main__":
  main()