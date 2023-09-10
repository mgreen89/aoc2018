# Utilities

def get_input(day):
  with open("./aoc/inputs/{}.txt".format(day)) as f:
    return f.read()
