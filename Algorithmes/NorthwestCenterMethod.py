import numpy as np
import time
class NorthwestCenter:
    def __init__(self,list,demand,supply):
        self.list = np.copy(list)
        self.demand = np.copy(demand)
        self.supply = np.copy(supply)
        self.y,self.x = list.shape
        self.value_list = np.zeros((self.y,self.x) , dtype=int)

    def calculate_value_list(self):
        index_i = 0
        index_j = 0
        step = 0
        while(index_i < self.x and index_j < self.y):
            element_demand = self.demand[index_i]
            element_supply = self.supply[index_j]
            step += 1
            print('------------------------------step ', step, '------------------------------')
            print(self.value_list)
            print('demand: ', self.demand)
            print('supply: ', self.supply)
            if(element_supply > element_demand):
                self.value_list[index_j,index_i] = self.value_list[index_j,index_i] + element_demand
                self.demand[index_i] = self.demand[index_i] - element_demand
                self.supply[index_j] = self.supply[index_j] - element_demand
            else:
                self.value_list[index_j,index_i] = self.value_list[index_j,index_i] + element_supply
                self.demand[index_i] = self.demand[index_i] - element_supply
                self.supply[index_j] = self.supply[index_j] - element_supply

            if(self.demand[index_i] == 0):
                index_i += 1
            elif(self.supply[index_j] == 0):
                index_j += 1
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
                return_array[index_j,index_i] = self.list[index_j , index_i] * self.value_list[index_j,index_i]

        return np.sum(return_array)
