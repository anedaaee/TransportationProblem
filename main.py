import numpy as np
import pandas as pd
from Algorithmes.NorthwestCenterMethod import NorthwestCenter
from Algorithmes.RowMinimumMethod import RowMinimum
from Algorithmes.LeastCostMethod import LeastCost
from Algorithmes.VogelsApproximationMethod import VogelsApproximation
from Algorithmes.ModifiedDistribution import ModifiedDistribiution
import time

csv_data = pd.read_csv('./csv/transportationProblem.csv')
supplys = csv_data['supply'].to_numpy()
supplys = supplys[:-1]

demand = csv_data.loc[csv_data['warehouses\projects'] == 'demand', '1':'3'].values.flatten()



csv_data = csv_data.drop(columns='warehouses\projects')
numpy_list = csv_data.to_numpy()
i, j = numpy_list.shape
numpy_list = np.delete(numpy_list,i - 1,axis=0)
numpy_list = np.delete(numpy_list,j - 1,axis=1)

supplys_sum = np.sum(supplys)
demand_sum = np.sum(demand)

if(demand_sum == supplys_sum):
    numpy_list = numpy_list

elif(demand_sum < supplys_sum):
    x , y = numpy_list.shape
    numpy_list = np.pad(numpy_list, [(0, 0), (0, 1)], mode='constant')
    demand = np.append(demand , supplys_sum - demand_sum)
else:
    x, y = numpy_list.shape
    numpy_list = np.pad(numpy_list, [(0, 1), (0, 0)], mode='constant')
    supplys = np.append(supplys, demand_sum - supplys_sum )


print('------------------------------Northwest Center method------------------------------')
nw = NorthwestCenter(list = numpy_list , demand=demand , supply=supplys)
print('input: ,',numpy_list)
print('demand: ',demand)
print('supplys: ',supplys)
time.sleep(7)
nw.calculate_value_list()
time.sleep(7)
print('------------------------------Northwest Center method result------------------------------')
print('The basic answer of the elementary reason Northwest Center method: ',nw.clculate_result())
print()
time.sleep(7)


print('------------------------------Row Minimum method------------------------------')
rm = RowMinimum(list = numpy_list , demand=demand , supply=supplys)
print('input: ,',numpy_list)
print('demand: ',demand)
print('supplys: ',supplys)
time.sleep(7)
rm.calculate_value_list()
time.sleep(7)
print('------------------------------Row Minimum method result------------------------------')
print('The basic answer of the elementary reason Row Minimum method: ',rm.clculate_result())
print()
time.sleep(7)

print('------------------------------Least Cost method------------------------------')
lc = LeastCost(list = numpy_list , demand=demand , supply=supplys)
print('input: ,',numpy_list)
print('demand: ',demand)
print('supplys: ',supplys)
time.sleep(7)
lc.calculate_value_list()
time.sleep(7)
print('------------------------------Least Cost method result------------------------------')
print('The basic answer of the elementary reason Least Cost method: ',lc.clculate_result())
print()
time.sleep(7)

print('------------------------------vogel method------------------------------')
print('input: ,',numpy_list)
print('demand: ',demand)
print('supplys: ',supplys)
time.sleep(7)
va = VogelsApproximation(list = numpy_list , demand=demand , supply=supplys)
va.calculate_value_list()
time.sleep(7)
print('------------------------------vogel method result------------------------------')
print('The basic answer of the elementary reason vogel method: ',va.clculate_result())
print()
time.sleep(7)

# list = np.array([
#     [2.2,2.1,2.4],
#     [1.8,1.9,2.1],
#     [3,3.2,3.6]
# ])
#
# value_list = np.array([
#     [0,40,210],
#     [190,0,110],
#     [0,200,0]
# ])
#
print('------------------------------Modified Distribiution method------------------------------')
print('input: ,',numpy_list)
print('demand: ',demand)
print('supplys: ',supplys)
time.sleep(7)
md = ModifiedDistribiution(list=numpy_list,value_list=va.value_list)
print('------------------------------Modified Distribiution method result------------------------------')
print('The basic answer of the elementary reason Modified Distribiution method: ',md.main())
print()
time.sleep(7)

