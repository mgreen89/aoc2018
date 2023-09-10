# N.B Throughout this solution the y direction is reversed.
# Therefore the turning multiplcation is opposite to normal,
# i.e. multiply by +j to turn right, multiply by -j to turn left.

import copy

from . import utils


class Cart:
  def __init__(self, pos, direction):
    # Position.
    self.pos = pos

    # Direction is a unit complex vector.
    #  * +1 : right
    #  * +j : down
    #  * -1 : left
    #  * -j : right
    self.direction = direction

    # Cross direction is between 0 and 2.
    # - 0 -> turn left, 1 -> straight on, 2 -> turn right 
    self.cross_dir = 0

    # Dead indicator
    self.dead = False

  def turn(self, track_section):
    if track_section == "\\":
        if self.direction.real == 0:
            self.direction *= -1j
        else:
            self.direction *= +1j

    elif track_section == "/":
        if self.direction.real == 0:
            self.direction *= +1j
        else:
            self.direction *= -1j

    elif track_section == "+":
        self.direction *= -1j * 1j ** self.cross_dir
        self.cross_dir = (self.cross_dir + 1) % 3


def parse():
  input_lines = utils.get_input("13").split("\n")

  cart_to_dir = {
    ">": 1,
    "v": 1j,
    "<": -1,
    "^": -1j,
  }

  tracks = {}
  carts = []

  for y, line in enumerate(input_lines):
    for x, c in enumerate(line):
      if c in ["/", "\\", "+"]:
        # Track sections of interest
        tracks[(x + y * 1j)] = c
      elif c in cart_to_dir:
        carts.append(Cart(x + y * 1j, cart_to_dir[c]))

  return tracks, carts


def part1(tracks, carts):
  while True:
    carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
    for cart in carts:
      cart.pos += cart.direction
      if any(cart2.pos == cart.pos
             for cart2 in carts if cart2 is not cart):
        return cart.pos

      # Turn the cart if necessary.
      if cart.pos in tracks:
        cart.turn(tracks[cart.pos])


def part2(tracks, carts):
  while len(carts) > 1:
    carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
    for cart in carts.copy():
      if cart.dead:
        continue

      cart.pos += cart.direction
      for cart2 in carts:
        if cart2.pos == cart.pos and cart2 is not cart and not cart2.dead:
          cart.dead = True
          cart2.dead = True
          break
      
      if not cart.dead and cart.pos in tracks:
        # Turn the cart if necessary.
        cart.turn(tracks[cart.pos])

    carts = [cart for cart in carts if not cart.dead]

  assert len(carts) == 1

  return carts[0].pos


def main():
  tracks, carts = parse()

  print(part1(tracks, copy.deepcopy(carts)))
  print(part2(tracks, copy.deepcopy(carts)))


if __name__ == "__main__":
  main()