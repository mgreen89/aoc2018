import operator

from . import utils


class Processor:

  def __init__(self):
    self.registers = [0, 0, 0, 0]

    self.fns = [
      self.addr,
      self.addi,
      self.mulr,
      self.muli,
      self.banr,
      self.bani,
      self.borr,
      self.bori,
      self.setr,
      self.seti,
      self.gtir,
      self.gtri,
      self.gtrr,
      self.eqir,
      self.eqri,
      self.eqrr,
    ]

  def _r_cmd(self, fn, a, b, c):
    res = self.registers.copy()
    res[c] = int(fn(self.registers[a], self.registers[b]))
    return res

  def _i_cmd(self, fn, a, b, c):
    res = self.registers.copy()
    res[c] = int(fn(self.registers[a], b))
    return res

  def addr(self, a, b, c):
    return self._r_cmd(operator.add, a, b, c)

  def addi(self, a, b, c):
    return self._i_cmd(operator.add, a, b, c)

  def mulr(self, a, b, c):
    return self._r_cmd(operator.mul, a, b, c)

  def muli(self, a, b, c):
    return self._i_cmd(operator.mul, a, b, c)

  def banr(self, a, b, c):
    return self._r_cmd(operator.and_, a, b, c)

  def bani(self, a, b, c):
    return self._i_cmd(operator.and_, a, b, c)

  def borr(self, a, b, c):
    return self._r_cmd(operator.or_, a, b, c)

  def bori (self, a, b, c):
    return self._i_cmd(operator.or_, a, b, c)

  def setr(self, a, b, c):
    res = self.registers.copy()
    res[c] = self.registers[a]
    return res

  def seti(self, a, b, c):
    res = self.registers.copy()
    res[c] = a
    return res

  def gtir(self, a, b, c):
    # Test value A > reg B
    # N.B. === reg B < value A
    return self._i_cmd(operator.lt, b, a, c)

  def gtri(self, a, b, c):
    # Test reg A > value B
    return self._i_cmd(operator.gt, a, b, c)

  def gtrr(self, a, b, c):
    return self._r_cmd(operator.gt, a, b, c)

  def eqir(self, a, b, c):
    # Test value A == reg B
    return self._i_cmd(operator.eq, b, a, c)

  def eqri(self, a, b, c):
    return self._i_cmd(operator.eq, a, b, c)

  def eqrr(self, a, b, c):
    return self._r_cmd(operator.eq, a, b, c)

  def multi_fns(self, fns, a, b, c):
    return [fn(a, b, c) for fn in fns]

  def all_fns(self, a, b, c):
    return self.multi_fns(self.fns, a, b, c)


def parse():
  input_str = utils.get_input("16")

  cmd_history = []
  prog = []

  input_lines = input_str.split("\n")
  i = 0
  while i < len(input_lines):
    if input_lines[i].startswith("Before"):
      # Trust it's safe.
      pre_state = eval(input_lines[i][len("Before: "):])
      cmd = [int(x) for x in input_lines[i + 1].split(" ")]
      post_state = eval(input_lines[i + 2][len("After:  "):])

      cmd_history.append((cmd, pre_state, post_state))
      i += 3

    elif input_lines[i]:
      # Start of mini program.
      while i < len(input_lines):
        prog.append([int(x) for x in input_lines[i].split(" ")])
        i += 1

    else:
      i += 1
      
  return cmd_history, prog


def part1(cmd_history):
  three_or_more = 0
  for cmd in cmd_history:
    proc = Processor()
    proc.registers = cmd[1]
    all_fns_output = proc.all_fns(cmd[0][1], cmd[0][2], cmd[0][3])
    if all_fns_output.count(cmd[2]) >= 3:
      three_or_more += 1

  return three_or_more


def part2(cmd_history, prog):
  opcode_to_fns = {}

  proc = Processor()
  remaining_fns = proc.fns.copy()

  while len(opcode_to_fns) < len(proc.fns):
    for cmd in cmd_history.copy():
      if cmd[0][0] in opcode_to_fns:
        cmd_history.remove(cmd)
        continue

      proc.registers = cmd[1]
      all_fns_output = proc.multi_fns(
        remaining_fns, cmd[0][1], cmd[0][2], cmd[0][3])
      
      if all_fns_output.count(cmd[2]) == 1:
        fn = remaining_fns[all_fns_output.index(cmd[2])]
        opcode_to_fns[cmd[0][0]] = fn
        remaining_fns.remove(fn)

  # All opcodes found.
  proc.registers = [0, 0, 0, 0]
  for line in prog:
    proc.registers = opcode_to_fns[line[0]](line[1], line[2], line[3])

  return proc.registers


def main():
  cmd_history, prog = parse()

  print(part1(cmd_history))
  print(part2(cmd_history, prog))


if __name__ == "__main__":
  main()