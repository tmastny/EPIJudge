from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    COLOR = image[x][y]
    
    def dfs(x, y):
        if (
            x < 0 or x >= len(image) or
            y < 0 or y >= len(image[0]) or 
            image[x][y] != COLOR
        ):
            return
        
        image[x][y] = not COLOR 
        for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            dfs(nx, ny)
    
    dfs(x, y)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
