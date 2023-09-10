import collections
import difflib

from . import utils


def part1(box_ids):
  twos = set()
  threes = set()

  for bid in box_ids:
    count_ = collections.Counter(bid)
    if any(c == 2 for l, c in count_.items()):
      twos.add(bid)
    if any(c == 3 for l,c in count_.items()):
      threes.add(bid)

  return len(twos) * len(threes)


def part2(box_ids):
  ratio = 25/26
  for i, bid in enumerate(box_ids):
    s = difflib.SequenceMatcher(a=bid)
    for nbid in box_ids[i+1:]:
      s.set_seq2(nbid)
      if s.ratio() == ratio:
        r = ""
        for c1, c2 in zip(bid, nbid):
          if c1 == c2:
            r += c1
        return r


def main():
  box_ids = [line for line in utils.get_input("2").split()]
  print(part1(box_ids))
  print(part2(box_ids))


if __name__ == "__main__":
  main()