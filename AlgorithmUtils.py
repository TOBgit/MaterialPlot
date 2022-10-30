import numpy as np
from typing import List

from scipy.spatial import ConvexHull


class selectionLine:
    '''
    Used to describe a selection line on log-scale.
    # (a1 * (x ^ a2)) / (b1 * (y ^ b2)) = c
    '''
    def __init__(self, a1, a2, b1, b2, c):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c = c

class simpleEllipse:
    '''
    A class to describe the pure geometry information of an ellipse.
    '''
    def __init__(self, x, y, w, h, rotation):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotation = rotation
        # Describe the upper-left point of the bounding rectangle of the ellipse.
        # TODO(team): handle this when rotation is not zero.
        self.upper_left_x = x - w / 2.
        self.upper_left_y = y - h / 2.

def ellipseHull(ellipses: List[simpleEllipse], expand_ratio, step):
    if len(ellipses) == 0:
        return None
    pts = []
    for i, ellipse in enumerate(ellipses):
        t = np.linspace(0, 2 * np.math.pi, step)
        # Sample points along the surface of the ellipse.
        x = ellipse.w * np.sin(t) / 2 * expand_ratio + ellipse.x
        y = ellipse.h * np.cos(t) / 2 * expand_ratio + ellipse.y
        xy = np.stack((x, y)).T
        if ellipse.rotation is not None:
            # TODO(cow) rotation points
            pass
        pts.append(xy)
    pts = np.concatenate(pts, axis=0)
    hull = ConvexHull(pts)

    return pts[hull.vertices]
