import collections
import re

from . import utils


class Claim:
  """A fabric rectangle claim."""

  def __init__(self, cid, left, top, width, height):
    self.cid = cid
    self.left = left
    self.top = top
    self.width = width
    self.height = height

  @property
  def right(self):
    return self.left + self.width

  @property
  def bottom(self):
    return self.top + self.height

  def covers(self, from_left, from_top):
    """Does the claim cover a square?"""
    return (from_left >= self.left and
            from_left < self.right and
            from_top >= self.top and
            from_top < self.bottom)


def part1(claims):
  m = collections.defaultdict(list)
  for claim in claims:
    for x in range(claim.left, claim.right):
      for y in range(claim.top, claim.bottom):
        m[(x, y)].append(claim.cid)

  return sum(1 for i in m if len(m[i])> 1)


def part2(claims):
  m = collections.defaultdict(list)
  overlaps = {}
  for claim in claims:
    overlaps[claim.cid] = set()
    for x in range(claim.left, claim.right):
      for y in range(claim.top, claim.bottom):
        for cid in m[(x, y)]:
          overlaps[cid].add(claim.cid)
          overlaps[claim.cid].add(cid)
        m[(x, y)].append(claim.cid)

  no_overlaps = [cid for cid in overlaps if len(overlaps[cid]) == 0]
  assert len(no_overlaps) == 1
  return no_overlaps[0]


def main():
  re_str = r"""\#(?P<cid>[0-9]+)\ @\               # claim id
               (?P<left>[0-9]+),(?P<top>[0-9]+):\  # left, top coords
               (?P<wide>[0-9]+)x(?P<tall>[0-9]+)   # width, height len
            """

  re_ = re.compile(re_str, re.VERBOSE)

  claims = []
  for line in utils.get_input("3").split("\n"):
    if line:
      m = re_.match(line)
      assert m is not None
      claims.append(Claim(int(m.group("cid")),
                          int(m.group("left")),
                          int(m.group("top")),
                          int(m.group("wide")),
                          int(m.group("tall"))))

  print(part1(claims))
  print(part2(claims))

if __name__ == "__main__":
  main()