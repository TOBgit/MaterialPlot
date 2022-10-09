# -*- coding:utf-8 -*-
import pandas as pd
from typing import List



def evaluation(syntax: str, original_data_features: List):
    from SyntaxReader.lexer import LexerForData
    from SyntaxReader.parser_ import Parser
    from SyntaxReader.Interpreter import meanInterpreter
    lexer = LexerForData(syntax, original_data_features)
    tokens = lexer.generate_token()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree:
        return False
    meanInt = meanInterpreter()
    value = meanInt.visit(tree)
    return value


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

    def tryReplaceFeatureValue(self, syntaxStr, suffix):
        outstr = syntaxStr
        success = False
        for featurekey, value in self.features.items():
            if not isinstance(value, str) and value is not None:
                if suffix in featurekey:
                    realfeature = featurekey.replace(suffix, "")
                    if realfeature in outstr:
                        outstr = outstr.replace(realfeature, str(value))
                        success = True
        if not success:
            return None
        else:
            return outstr

    def findRelevantFeature(self, syntaxStr, suffix):
        for featurekey, value in self.features.items():
            if not isinstance(value, str) and value is not None:
                if suffix in featurekey:
                    realfeature = featurekey.replace(suffix, "")
                    if realfeature in syntaxStr:
                        return featurekey

    def get(self, feature_name, suffix):
        fullname = feature_name + suffix
        if fullname in self.features:
            return self.features[fullname]
        elif fullname in self.baked_features:
            return self.baked_features[fullname]
        else:
            if suffix == "_sd":
                # todo: don't know how to calculate yet, get origin sd
                fullname = self.findRelevantFeature(feature_name, suffix)
                if fullname:
                    return self.features[fullname]
            elif suffix == "_mean":
                strout = self.tryReplaceFeatureValue(feature_name, suffix)
                if strout is not None:
                    value = evaluation(strout, self.features)
                    self.baked_features[fullname] = value.value
                    return value.value
                else:
                    pass


class MatPlotModel(object):
    def __init__(self, filename: str):
        self.numeric_columns = []
        self.string_columns = []
        self.data = self.initFromData(filename)
        print(self.data)

    def getMaterialFamily(self, key_name = "Type"):
        if key_name not in self.data:
            return []
        return list(self.data[key_name].unique())

    def getItemByType(self, typestr: str):
        return self.getItemsByFamily("Type", typestr)

    def initFromData(self, filename: str):
        df = pd.DataFrame()
        if filename:
            temp_df = pd.read_csv(filename)
            # Find the numerical and string columns.
            for column in temp_df.columns:
                if isinstance(temp_df[column][0], float):
                    self.numeric_columns.append(column)
                else:
                    self.string_columns.append(column)
            # Use the first column to group different samples from the same material.
            for name, sub_df in temp_df.groupby(temp_df.columns[0]):
                # Calculate the mean among all numeric columns.
                avg_series = sub_df.loc[:, self.numeric_columns].mean(axis=0, skipna=True)
                # Take the first row to capture descriptive features in string columns.
                avg_series = avg_series.append(sub_df[self.string_columns].iloc[0].squeeze())
                df = df.append(avg_series.to_frame().T)
            # Remove name from the string columns.
            self.string_columns.remove("Name")

        # Remove na for compatibility now!
        df.dropna(inplace=True)
        return df

    #TODO(team): handle more complex semantic expression.
    def addProperty(self, new_column_info: List):
        '''
        Manipulate to calculate additional terms from the data. Return the name of the new term.
        New column info is descried as [numerator, order_of_numerator, denominator, order_of_denominator].
        '''
        new_str = new_column_info[0] + '^' + str(new_column_info[1]) + '/' + new_column_info[2] + '^' + str(new_column_info[3])
        if new_str not in self.data.columns:
            self.data[new_str] = (self.data[new_column_info[0]] ** new_column_info[1] / self.data[new_column_info[2]] ** new_column_info[3])
        return new_str


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
