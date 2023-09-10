from . import utils


def part1(nos):
  meta_sum = 0

  def recurse(index):
    nonlocal meta_sum

    # Call on the start of each child.
    child_count = int(nos[index])
    meta_count = int(nos[index + 1])

    i = index + 2
    for child in range(child_count):
      i = recurse(i)

    for meta in range(meta_count):
      meta_sum += int(nos[i])
      i += 1

    return i

  recurse(0)

  return meta_sum


class Node:
  def __init__(self, children, metadata):
    self.children = children
    self.metadata = metadata

  @property
  def value(self):
    if self.children:
      val = 0
      for m in self.metadata:
        try:
          val += self.children[m - 1].value
        except IndexError:
          pass
      return val
    
    return sum(self.metadata)


def part2(nos):

  def recurse(index):
    # Call on the start of each child.
    child_count = int(nos[index])
    meta_count = int(nos[index + 1])
    i = index + 2

    children = []
    for child in range(child_count):
      i, child_node = recurse(i)
      children.append(child_node)

    metadata = []
    for meta in range(meta_count):
      metadata.append(int(nos[i]))
      i += 1

    return i, Node(children, metadata)

  _, root = recurse(0)

  return root.value


def main():
  nos = utils.get_input("8").split()
  
  print(part1(nos))
  print(part2(nos))


if __name__ == "__main__":
  main()