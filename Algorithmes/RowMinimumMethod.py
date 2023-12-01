import numpy as np
import time
class RowMinimum :
    def __init__(self, list, demand, supply):
        self.list = np.copy(list)
        self.init_list = np.copy(list)
        self.demand = np.copy(demand)
        self.supply = np.copy(supply)
        self.y, self.x = list.shape
        self.value_list = np.zeros((self.y, self.x), dtype=int)

    def calculate_value_list(self):
        index_j = 0
        step = 0
        while(np.sum(self.demand) != 0 or np.sum(self.supply) != 0):
            step += 1
            print('------------------------------step ', step, '------------------------------')
            print(self.value_list)
            print('demand: ', self.demand)
            print('supply: ', self.supply)
            if self.supply[index_j] != 0:
                row = self.list[index_j]
                while(True):
                    min_index = np.argmin(row)
                    max_value = np.max(row)
                    self.list[index_j,min_index] = max_value + 1

                    if(self.demand[min_index] != 0):
                        break;

                element_demand = self.demand[min_index]
                element_supply = self.supply[index_j]
                if (element_supply > element_demand):
                    self.value_list[index_j, min_index] = self.value_list[index_j, min_index] + element_demand
                    self.demand[min_index] = self.demand[min_index] - element_demand
                    self.supply[index_j] = self.supply[index_j] - element_demand
                else:
                    self.value_list[index_j, min_index] = self.value_list[index_j, min_index] + element_supply
                    self.demand[min_index] = self.demand[min_index] - element_supply
                    self.supply[index_j] = self.supply[index_j] - element_supply

            index_j += 1

            if(index_j == self.y):
                index_j = 0
            time.sleep(7)
        print('------------------------------finaly------------------------------')
        print(self.value_list)
        print('demand: ', self.demand)
        print('supply: ', self.supply)
        time.sleep(7)

    def clculate_result(self):
        return_array = np.zeros((self.y,self.x) , dtype=int)
        for index_j in range(self.y):
            for index_i in range(self.x):
                return_array[index_j,index_i] = self.init_list[index_j , index_i] * self.value_list[index_j,index_i]

        return np.sum(return_array)
