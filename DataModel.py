# -*- coding:utf-8 -*-
from typing import List

import pandas as pd
import numpy as np

from SyntaxReader.interpreter import evaluateWithData

class MaterialItem(object):
    """
    Use it to describe your Material
    """

    def __init__(self, data: pd.Series):
        self.label = data["Name"]
        self.color_r = int(data["Color_R"])
        self.color_g = int(data["Color_G"])
        self.color_b = int(data["Color_B"])
        if "rotation" in data.keys():
            self.rotation = data["rotation"]
        else:
            self.rotation = 0.0
        # All other string columns are family info and stored in a dict for reference.
        # TODO(tienan): might need to specifically handle the case when family feature cell is empty.
        self.family_info = {}
        family_feature_keys = []
        for feature in data.keys():
            if isinstance(data[feature], str):
                family_feature_keys.append(feature)
                self.family_info[feature] = data[feature]
        # All other features of the material are stored in a dict allowing for flexible extension.
        self.features = {}
        self.baked_features = {}
        for feature in data.keys():
            if feature in ["Name", "Color_R", "Color_G", "Color_B", "rotation"] + family_feature_keys:
                continue
            self.features[feature] = data[feature]

    def get(self, feature_name, suffix):
        fullname = feature_name + suffix
        if fullname in self.features:
            return self.features[fullname]
        elif fullname in self.baked_features:
            return self.baked_features[fullname]
        else:
            new_mean, new_sd = evaluateWithData(feature_name, self.features)
            self.baked_features[feature_name + "_mean"] = new_mean
            self.baked_features[feature_name + "_sd"] = new_sd
            return self.baked_features[fullname]

class MatPlotModel(object):
    def __init__(self, filename: str):
        self.numeric_columns = []
        self.string_columns = []
        self.raw_data = self.loadData(filename)
        self.data = self.initFromData()
        print(self.data)

    def getMaterialFamily(self, key_name="Type"):
        if key_name not in self.data:
            return []
        return list(self.data[key_name].unique())

    def getItemByType(self, typestr: str):
        return self.getItemsByFamily("Type", typestr)
    
    def loadData(self, filename: str):
        df = pd.DataFrame()
        if filename:
            df = pd.read_csv(filename)
        return df
    
    def onRawDataUpdate(self):
        self.data = self.initFromData()

    def initFromData(self):
        df = pd.DataFrame()
        if len(self.raw_data) > 0:
            # Find the numerical and string columns.
            self.numeric_columns = list(self.raw_data.columns[self.raw_data.dtypes == np.float])
            self.string_columns = list(self.raw_data.columns[self.raw_data.dtypes == np.dtype('O')])
            def groupData(df):
                # Calculate the mean among all numeric columns.
                avg_series = df.loc[:, self.numeric_columns].mean(axis=0, skipna=True)
                # Take the first row to capture descriptive features in string columns.
                # avg_series = avg_series.append(df[self.string_columns].iloc[0].squeeze())
                avg_series = pd.concat([df[self.string_columns].iloc[0].squeeze(), avg_series])
                return avg_series
            df = self.raw_data.groupby(self.raw_data.columns[0]).apply(groupData)
            # Remove name from the string columns.
            self.string_columns.remove("Name")

        # Remove na for compatibility now!
        df.dropna(inplace=True)
        return df

    def addMaterial(self):
        pass

    def getStringColumns(self):
        '''
         Returns the candidate columns for users to select the family category.
         Note that the Name column is not included.
        '''
        return self.string_columns

    def getNumericColumns(self):
        return self.numeric_columns

    @staticmethod
    def convertToItem(df):
        items = {}
        for idx, row in df.iterrows():
            items[row.Name] = MaterialItem(row)
        return items

    def getAllItems(self):
        return self.convertToItem(self.data)

    def getSelectedItems(self, selection):
        return self.convertToItem(self.data[self.data.Name.isin(selection)])

    def getItem(self, label):
        return self.convertToItem(self.data[self.data.Name == label])

    def getItemsByFamily(self, column: str, label: str):
        return self.convertToItem(self.data[self.data[column] == label])

    def getItemsByFamilyAndSelected(self, column: str, label: str, selection):
        return self.convertToItem(self.data[(self.data[column] == label) & self.data.Name.isin(selection)])

    def provideFamilyCandidateByColumn(self, column_name: str):
        candidate = self.data[column_name].drop_duplicates()
        return candidate.values

    def getColumns(self):
        return self.data.columns

    def getCount(self):
        return len(self.data)

    @staticmethod
    def getMeanColor(items: List[MaterialItem]):
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for item in items:
            r = item.color_r
            g = item.color_g
            b = item.color_b
            sum_r += r
            sum_g += g
            sum_b += b
        meanR = float(sum_r) / float(len(items))
        meanG = float(sum_g) / float(len(items))
        meanB = float(sum_b) / float(len(items))
        return meanR, meanG, meanB
