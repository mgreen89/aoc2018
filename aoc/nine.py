import collections
import re

from . import utils


def old_part1(num_players, max_val):
  # Set up initial marbles
  marbles = [0]
  current_i = 0
  marble_count = 1

  players = [0] * num_players
  curr_player = 1

  for i in range(1, max_val + 1):
    if i % 23 == 0:
      players[curr_player] += i
      remove_i = (current_i - 7) % marble_count
      players[curr_player] += marbles.pop(remove_i)
      current_i = remove_i
      marble_count -= 1
    else:
      insert_i = (current_i + 2) % marble_count
      marbles.insert(insert_i, i)
      current_i = insert_i
      marble_count += 1
    
    curr_player += 1
    curr_player %= num_players

  return max(players)


def part1(num_players, max_val):
  scores = [0] * num_players
  circle = collections.deque([0])

  for marble in range(1, max_val + 1):
    if marble % 23 == 0:
      circle.rotate(7)
      scores[marble % num_players] += marble + circle.pop()
      circle.rotate(-1)
    else:
      circle.rotate(-1)
      circle.append(marble)

  return max(scores)


def part2(num_players, orig_max_val):
  return part1(num_players, orig_max_val * 100)


def main():
  re_ = re.compile(r"(?P<players>[0-9]+) players; last marble is worth (?P<maxval>[0-9]+) points")
  
  input_str = utils.get_input("9")

  m = re_.match(input_str)
  assert m is not None

  num_players = int(m.group("players"))
  max_val = int(m.group("maxval"))

  print(part1(num_players, max_val))
  print(part2(num_players, max_val))
