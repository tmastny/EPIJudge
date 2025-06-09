import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from pydoc import help

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle_old(r1: Rect, r2: Rect) -> Rect:
    r2x_in_r1 = r1.x <= r2.x <= r1.x + r1.width
    r1x_in_r2 = r2.x <= r1.x <= r2.x + r2.width
    x_intersect = r2x_in_r1 or r1x_in_r2

    r2y_in_r1 = r1.y <= r2.y <= r1.y + r1.height
    r1y_in_r2 = r2.y <= r1.y <= r2.y + r2.height
    y_intersect = r2y_in_r1 or r1y_in_r2
    if not (x_intersect and y_intersect):
        return Rect(0, 0, -1, -1)

    if r2x_in_r1:
        x = r2.x
        width = min(r1.x + r1.width - x, r2.width)
    else:
        x = r1.x
        width = min(r2.x + r2.width - x, r1.width)

    if r2y_in_r1:
        y = r2.y
        height = min(r1.y + r1.height - y, r2.height)
    else:
        y = r1.y
        height = min(r2.y + r2.height - y, r1.height)

    return Rect(x, y, width, height)

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if (
        r1.x + r1.width < r2.x or
        r2.x + r2.width < r1.x or
        r2.y + r2.height < r1.y or
        r1.y + r1.height < r2.y
    ):
        return Rect(0, 0, -1, -1)

    x = max(r1.x, r2.x)
    y = max(r1.y, r2.y)
    return Rect(
        x,
        y,
        min(r1.x + r1.width - x, r2.x + r2.width - x),
        min(r1.y + r1.height - y, r2.y + r2.height - y)
    )


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
