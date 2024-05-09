#!/usr/bin/python3
'''Task Island Perimeter'''


def island_perimeter(grid):
    '''returns perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    last_max = len(grid[0]) - 1  # index of the last square in list

    for last_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == last_max:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # top and down
                if last_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[last_idx + 1][land_idx] == 0:
                        counter += 1
                elif last_idx == grid_max:
                    # top side
                    if grid[last_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[last_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[last_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
