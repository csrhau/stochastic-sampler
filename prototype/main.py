#!/usr/bin/env python

from __future__ import print_function
from collections import namedtuple

Instruction = namedtuple('Instruction', ['name', 'time', 'energy'])

class BasicBlock:
  def __init__(self, instructions, targets):
    self.instructions = instructions
    self.targets = targets

class InstructionIterator:
  def __init__(self, cpu, max_cycles):
    self._cpu = cpu
    self._max_cycles = max_cycles

  def __iter__(self):
    return self

  def next(self):
    if self._cpu.cycles < self._max_cycles:
      self._cpu.advance()
      return self._cpu.cycles
    else:
      raise StopIteration()

class CPU:
  def __init__(self):
    pass

  def advance(self):
    self._cycles += 1

  @property
  def cycles(self):
    return self._cycles

  @property
  def instruction_iterator(self):
    return self._instruction_iterator

  def invocation(self):
    cycle = 0
    cycles = 100
    while cycle < cycles:
      cycle += 1
      yield cycle

def main():
  processor = CPU()
  for i in processor.invocation():
    print(i)

if __name__ == '__main__':
  main()
