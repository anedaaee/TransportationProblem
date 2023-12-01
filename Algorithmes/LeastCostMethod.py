import numpy as np
import time
class LeastCost :
    def __init__(self, list, demand, supply):
        self.list = np.copy(list)
        self.init_list = np.copy(list)
        self.demand = np.copy(demand)
        self.supply = np.copy(supply)
        self.y, self.x = list.shape
        self.value_list = np.zeros((self.y, self.x), dtype=int)

    def calculate_value_list(self):
        step = 0
        while(np.sum(self.demand) != 0 and np.sum(self.supply) != 0):
            step += 1
            print('------------------------------step ', step, '------------------------------')
            print(self.value_list)
            print('demand: ', self.demand)
            print('supply: ', self.supply)
            while True:
                min_j , min_i = np.unravel_index(np.argmin(self.list), self.list.shape)
                max_value = np.max(self.list)
                self.list[min_j,min_i] = max_value + 1
                if(self.supply[min_j] == 0 or self.demand[min_i] != 0):
                    break;

            element_demand = self.demand[min_i]
            element_supply = self.supply[min_j]

            if (element_supply > element_demand):
                self.value_list[min_j, min_i] = self.value_list[min_j, min_i] + element_demand
                self.demand[min_i] = self.demand[min_i] - element_demand
                self.supply[min_j] = self.supply[min_j] - element_demand
            else:
                self.value_list[min_j, min_i] = self.value_list[min_j, min_i] + element_supply
                self.demand[min_i] = self.demand[min_i] - element_supply
                self.supply[min_j] = self.supply[min_j] - element_supply
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
