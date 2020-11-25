grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

i = 0
j = 0

for j in range(len(grid)):
  for i in range(len(grid)):
    print(grid[i][j], end = '')
    if i == 8:
      print('\n')
      break
  if j == 5:
    break

print('\nDone.')

import os
os.system("pause")