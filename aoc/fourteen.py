def part1(tgt_recipes):
  recipes = bytearray([3, 7])

  elf1 = 0
  elf2 = 1

  while len(recipes) < tgt_recipes + 10:
    recipe1 = recipes[elf1]
    recipe2 = recipes[elf2]

    new_recipe = recipe1 + recipe2
    d1, d2 = divmod(new_recipe, 10)
    if d1 != 0:
      recipes.append(d1)
    recipes.append(d2)

    elf1 = (elf1 + 1 + recipe1) % len(recipes)
    elf2 = (elf2 + 1 + recipe2) % len(recipes)

  return "".join(str(int(x)) for x in recipes[tgt_recipes:])


def part2(tgt_recipes):
  tgt = bytearray(int(x) for x in str(tgt_recipes))
  recipes = bytearray([3, 7])

  elf1 = 0
  elf2 = 1

  while True:
    if len(recipes) % 1_000_000 == 0:
      try:
        return(recipes.index(tgt))
      except ValueError:
        print("Not found after {:,} recipes".format(len(recipes)))

    recipe1 = recipes[elf1]
    recipe2 = recipes[elf2]

    new_recipe = recipe1 + recipe2
    d1, d2 = divmod(new_recipe, 10)
    if d1 != 0:
      recipes.append(d1)
    recipes.append(d2)

    elf1 = (elf1 + 1 + recipe1) % len(recipes)
    elf2 = (elf2 + 1 + recipe2) % len(recipes)
  

def main():
  tgt_recipes = 652601

  print(part1(tgt_recipes))
  print(part2(tgt_recipes))