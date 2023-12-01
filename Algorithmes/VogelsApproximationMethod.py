import numpy as np
import time
import copy

class VogelsApproximation:
    def __init__(self, list, demand, supply):
        self.column_penalty = None
        self.row_penalty = None
        self.list = np.copy(list)
        self.init_list = np.copy(list)
        self.demand = np.copy(demand)
        self.supply = np.copy(supply)
        self.y, self.x = list.shape
        self.value_list = np.zeros((self.y, self.x), dtype=int)

    def find_max_index(self):
        max_index_row_penalty = np.argmax(self.row_penalty)
        max_index_column_penalty = np.argmax(self.column_penalty)
        if (self.row_penalty[max_index_row_penalty] > self.column_penalty[max_index_column_penalty]):
            return {
                "kind": "row",
                "index": max_index_row_penalty
            }
        else:
            return {
                "kind": "column",
                "index": max_index_column_penalty
            }

    def checkFinish(self):
        if np.sum(self.demand) == 0 and np.sum(self.supply) == 0:
            return True
        return False

    def calculate_value_list(self):
        step = 0
        while(not self.checkFinish()):
            step += 1
            print('------------------------------step ',step,'------------------------------')
            print(self.value_list)
            print('demand: ',self.demand)
            print('supply: ',self.supply)
            print('row penalty: ',self.row_penalty)
            print('column penalty: ',self.column_penalty)
            self.find_penalty()

            max_obj = self.find_max_index()

            if max_obj['kind'] == 'row':
                row = self.list[max_obj['index'],:]
                row_index = max_obj['index']
                minimum_index = np.argmin(row)
                if self.supply[row_index] > self.demand[minimum_index]:
                    self.value_list[row_index,minimum_index] += self.demand[minimum_index]
                    max_arg = np.max(self.list)
                    self.list[row_index,minimum_index] = max_arg + 1
                    self.supply[row_index] -= self.value_list[row_index,minimum_index]
                    self.demand[minimum_index] -= self.value_list[row_index,minimum_index]
                else:
                    self.value_list[row_index,minimum_index] = self.supply[row_index]
                    max_arg = np.max(self.list)
                    self.list[row_index,minimum_index] = max_arg + 1
                    self.supply[row_index] -= self.value_list[row_index, minimum_index]
                    self.demand[minimum_index] -= self.value_list[row_index, minimum_index]

            elif max_obj['kind'] == 'column':
                column = self.list[:,max_obj['index']]
                column_index = max_obj['index']
                minimum_index = np.argmin(column)
                if self.supply[minimum_index] > self.demand[column_index]:
                    self.value_list[minimum_index, column_index] += self.demand[column_index]
                    max_arg = np.max(self.list)
                    self.list[minimum_index,column_index] = max_arg + 1
                    self.supply[minimum_index] -= self.value_list[minimum_index, column_index]
                    self.demand[column_index] -= self.value_list[minimum_index, column_index]
                else:
                    self.value_list[minimum_index, column_index] = self.supply[minimum_index]
                    max_arg = np.max(self.list)
                    self.list[minimum_index,column_index] = max_arg + 1
                    self.supply[minimum_index] -= self.value_list[minimum_index, column_index]
                    self.demand[column_index] -= self.value_list[minimum_index, column_index]
            time.sleep(7)
        print('------------------------------finaly------------------------------')
        print(self.value_list)
        print('demand: ', self.demand)
        print('supply: ', self.supply)
        print('row penalty: ', self.row_penalty)
        print('column penalty: ', self.column_penalty)
        time.sleep(7)
    def find_penalty(self):
        self.row_penalty = np.zeros(self.y, dtype=int)
        self.column_penalty = np.zeros(self.x, dtype=int)
        for index_j in range(self.y):
            row = self.list[index_j, :]
            row = copy.deepcopy(row)
            row = row[row>0]
            #print(row)
            if self.supply[index_j] == 0:
                self.row_penalty[index_j] = -1
            else:
                if len(row) == 1 :
                    self.row_penalty[index_j] = row[0]
                elif len(row) == 2 :
                    self.row_penalty[index_j] = abs(row[0] - row[1])
                elif len(row) > 2:
                    firstMinIndex = np.argmin(row)
                    first_min = row[firstMinIndex]
                    row = np.concatenate((row[:firstMinIndex] , row[firstMinIndex + 1:]))
                    secondMinIndex = np.argmin(row)
                    second_min = row[secondMinIndex]
                    self.row_penalty[index_j] = abs(first_min-second_min)

        for index_i in range(self.x):

            column = self.list[:, index_i]
            column = copy.deepcopy(column)
            column = column[column > 0]
            #print(column)
            if self.demand[index_i] == 0:
                self.column_penalty[index_i] = -1
            else:
                if len(column) == 1:
                    self.column_penalty[index_i] = column[0]
                elif len(column) == 2:
                    self.column_penalty[index_i] = abs(column[0] - column[1])
                elif len(column) > 2:
                    firstMinIndex = np.argmin(column)
                    first_min = column[firstMinIndex]
                    column = np.concatenate((column[:firstMinIndex], column[firstMinIndex + 1:]))
                    secondMinIndex = np.argmin(column)
                    second_min = column[secondMinIndex]
                    self.column_penalty[index_i] = abs(first_min - second_min)

    def clculate_result(self):
        return_array = np.zeros((self.y, self.x), dtype=int)
        for index_j in range(self.y):
            for index_i in range(self.x):
                return_array[index_j, index_i] = self.init_list[index_j, index_i] * self.value_list[index_j, index_i]

        return np.sum(return_array)
