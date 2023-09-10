import operator

from . import utils


class Processor:

  def __init__(self, ip_reg, program):
    self.registers = [0, 0, 0, 0, 0, 0]
    self.ip_reg = ip_reg
    self.ip = 0
    self.program = program

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

  def run(self):
    self.ip = 0
    while self.ip >= 0 and self.ip < len(self.program):
      self.registers[self.ip_reg] = self.ip
      inst = getattr(self, self.program[self.ip][0])
      a, b, c = self.program[self.ip][1:]
      self.registers = inst(a, b, c)
      self.ip = self.registers[self.ip_reg]
      self.ip += 1


def part1(ip_reg, prog):
  proc = Processor(ip_reg, prog)
  proc.run()

  return proc.registers[0]


def main():
  input_str = utils.get_input("19")
  input_lines = input_str.split("\n")

  ip_reg = int(input_lines[0][len("#ip "):])
  prog = []
  for line in input_lines[1:]:
    cmd = line.split()
    prog.append((cmd[0], int(cmd[1]), int(cmd[2]), int(cmd[3])))

  print(part1(ip_reg, prog))


if __name__ == "__main__":
  main()