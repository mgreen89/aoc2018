def get_power_level(x, y, serial):
  rack_id = x + 10
  pl = rack_id * y
  pl += serial
  pl *= rack_id

  # Keep the hundreds digit.
  hd = pl // 100 % 10
  return hd - 5


def get_sq_level(cells, left_x, top_y, size):
  total = 0
  for i in range(left_x, left_x + size):
    for j in range(top_y, top_y + size):
      total += cells[(i, j)]

  return total


def part1(serial):
  cells = {}
  for x in range(1, 301):
    for y in range(1, 301):
      cells[(x, y)] = get_power_level(x, y, serial)

  sqs = {}
  for x in range(1, 298):
    for y in range(1, 298):
      sqs[(x, y)] = get_sq_level(cells, x, y, 3)

  return max(sqs, key=sqs.get)


def part2(serial):
  cells = {}
  for x in range(1, 301):
    for y in range(1, 301):
      cells[(x, y)] = get_power_level(x, y, serial)

  all_sqs = {}
  for size in range(1, 301):
    sqs = {}
    for x in range(1, 301 - size):
      for y in range(1, 301 - size):
        sqs[(x, y)] = get_sq_level(cells, x, y, size)

    all_sqs[size] = max(sqs, key=sqs.get)

    print("{}   {}  {}".format(
      size, all_sqs[size],
      sqs[(all_sqs[size][0], all_sqs[size][1])]))

  max_pwr_size = max(all_sqs, sqs.get)
  return max_pwr_size, all_sqs[max_power_size]


def main():
  serial_number = 3463

  print(part1(serial_number))
  print(part2(serial_number))

if __name__ == "__main__":
  main()