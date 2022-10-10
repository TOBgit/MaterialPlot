from math import log10
from typing import List

from AlgorithmUtils import ellipseHull, simpleEllipse
from DataModel import MaterialItem
from PySide2.QtWidgets import QMessageBox
from View.ErrorWidget import simpleErrorPopUp

class GraphicConfig():
    '''
    Describe the plot features.
    '''

    def __init__(self):
        self._configGetters = {}
        self._configs = {}

        self.expend_ratio = 2.
        self.hull_sampling_step = 200
        self.log_scale = True
        self.x_axis = "Modulus"
        self.y_axis = "Strength"

    def __getattribute__(self, key):
        """
        By this, you can read config either by self.getConfig("expend_ratio") or self.expend_ratio.
        The value in self._config has priority
        :param key:
        :return:
        """
        config = super(GraphicConfig, self).__getattribute__("_configs")
        if key in config:
            return config[key]
        else:
            return super(GraphicConfig, self).__getattribute__(key)

    def updateFromUI(self):
        for key, getter in self._configGetters.items():
            if callable(getter):
                self._configs[key] = getter()

    def registerConfigGetter(self, key, getter):
        self._configGetters[key] = getter

    def getConfig(self, key):
        return self._configs.get(key, None)


class GraphicTransformer():
    '''
    Converts the coordinate-related features to the appropriate plot scale based on the config.
    Note the final Qt objects have negative y values to fit the y-axis style in the plot.
    '''

    def __init__(self, config: GraphicConfig):
        self.config = config

    def matToSquare(self, mat_item: MaterialItem):
        elps = self.convertMatToSimpleEllipse(mat_item)
        return elps.upper_left_x, elps.upper_left_y, elps.w, elps.h

    def matUpperLeftPoint(self, mat_item: MaterialItem):
        elps = self.convertMatToSimpleEllipse(mat_item)
        return elps.upper_left_x, elps.upper_left_y

    def matCenterPoint(self, mat_item: MaterialItem):
        elps = self.convertMatToSimpleEllipse(mat_item)
        return elps.x, elps.y

    def matRotation(self, mat_item: MaterialItem):
        elps = self.convertMatToSimpleEllipse(mat_item)
        return elps.rotation

    def getEllipseHull(self, items: List[MaterialItem]):
        return ellipseHull([self.convertMatToSimpleEllipse(item) for item in items],
                           self.config.expend_ratio,
                           self.config.hull_sampling_step)

    #
    # Private
    #
    def convertMatToSimpleEllipse(self, mat_item: MaterialItem):
        '''
        Convert an material item to a pure geometry object.
        '''
        width = mat_item.get(self.config.x_axis, "_sd")
        height = mat_item.get(self.config.y_axis, "_sd")
        upper_left_x = mat_item.get(self.config.x_axis, "_mean") - width * 0.5
        upper_left_y = mat_item.get(self.config.y_axis, "_mean") + height * 0.5
        if self.config.log_scale:
            # The ellipse/square in log scale is defined by the log of the original four corner points.
            # Use the diff between the lower-right point and upper-left point to re-calculate
            # the width and height.
            try:
                width = log10(upper_left_x + width) - log10(upper_left_x)
            except:
                simpleErrorPopUp(f"The feature ({self.config.x_axis}) of material ({mat_item.label}) has its std larger than its mean. "
                                 f"Cannot be drawn on log scale.")
                return None
            try:
                height = log10(upper_left_y) - log10(upper_left_y - height)
            except:
                simpleErrorPopUp(
                    f"The feature ({self.config.y_axis}) of material ({mat_item.label}) has its std larger than its mean. "
                    f"Cannot be drawn on log scale.")
                return None
            upper_left_x = log10(upper_left_x)
            upper_left_y = log10(upper_left_y)

        center_x = upper_left_x + width / 2.
        center_y = upper_left_y - height / 2.
        return simpleEllipse(center_x, center_y, width, height, mat_item.rotation)
