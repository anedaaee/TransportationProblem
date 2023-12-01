import numpy as np
import copy
import time
from collections import deque


class Node:
    def __init__(self, y, x, step, full_flag, start_flag):
        self.y = y
        self.x = x
        self.step = step
        self.full_flag = full_flag
        self.start_flag = start_flag

    def __str__(self):
        return '{y: ' + str(self.y) + ',x : ' + str(self.x) + ', step : ' + str(self.step) + '}'

    def setIsNegative(self,isNegative):
        self.isNegative = isNegative

    def setValue(self,value):
        self.value = value
class ModifiedDistribiution:

    def __init__(self, list, value_list):
        self.list = np.copy(list)
        self.value_list = np.copy(value_list)
        self.y, self.x = list.shape
        self.empty_value = np.zeros((self.y, self.x))
        self.U = np.full((self.y,), None)
        self.V = np.full((self.x,), None)
        self.U[0] = 0

    def initUV(self):
        self.empty_value = np.zeros((self.y, self.x))
        self.U = np.full((self.y,), None)
        self.V = np.full((self.x,), None)
        self.U[0] = 0
    def chekcUVComplete(self):
        flag = False
        for index_j in range(self.y):
            if (self.U[index_j] == None):
                flag = True
        for index_i in range(self.x):
            if (self.V[index_i] == None):
                flag = True
        return flag

    def calculateUV(self):
        while (self.chekcUVComplete()):
            for index_j in range(self.y):
                for index_i in range(self.x):
                    if self.value_list[index_j, index_i] != 0:
                        if self.U[index_j] == None and self.V[index_i] == None:
                            continue
                        elif (self.U[index_j] != None):
                            self.V[index_i] = round(self.list[index_j, index_i] - self.U[index_j], 1)

                        elif (self.V[index_i] != None):
                            self.U[index_j] = round(self.list[index_j, index_i] - self.V[index_i], 1)

    def calculateEmptyValue(self):
        for index_j in range(self.y):
            for index_i in range(self.x):
                if (self.value_list[index_j, index_i] == 0):
                    self.empty_value[index_j, index_i] = round(self.list[index_j, index_i] - self.U[index_j] - self.V[index_i], 1)

    def findInputVariable(self):
        self.input_variable_row_index, self.input_variable_col_index = np.unravel_index(np.argmin(self.empty_value),
                                                                                        self.empty_value.shape)

    def checkNodeExistInPath(self, input_node, path):
        copy_path = copy.deepcopy(path)
        first_node = copy_path[0]
        copy_path.remove(first_node)
        for node in copy_path:
            if node.y == input_node.y and node.x == input_node.x and node.full_flag:
                return True
        return False

    def find_path(self):
        paths = []
        result = []
        for j in range(self.y):
            for i in range(self.x):
                if (self.value_list[j, i] == 0):
                    start_right_node = Node(j, i, 'r', False, True)
                    path = []
                    path.append(start_right_node)
                    paths.append(path)
                    start_left_node = Node(j, i, 'l', False, True)
                    path = []
                    path.append(start_left_node)
                    paths.append(path)
                    start_up_node = Node(j, i, 'u', False, True)
                    path = []
                    path.append(start_up_node)
                    paths.append(path)
                    start_down_node = Node(j, i, 'd', False, True)
                    path = []
                    path.append(start_down_node)
                    paths.append(path)

        while len(paths) != 0:
            path = paths.pop()
            last_node = path[-1]
            fist_node = path[0]
            if fist_node.x == last_node.x and fist_node.y == last_node.y and len(path) > 3:
                result.append(path)
            elif last_node.x < 0 and last_node.x >= self.x and last_node.y < 0 and last_node.y >= self.y:
                continue
            else:
                if not last_node.full_flag:
                    if last_node.step == 'r':
                        full_flag = True
                        if 0 <= last_node.x + 1 < self.x and 0 <= last_node.y < self.y:
                            if (self.value_list[last_node.y, last_node.x + 1] == 0):
                                full_flag = False
                            new_node = Node(last_node.y, last_node.x + 1, 'r', full_flag, False)
                            if (not self.checkNodeExistInPath(new_node, path)):
                                path.append(new_node)
                                paths.append(path)
                    elif last_node.step == 'l':
                        full_flag = True
                        if 0 <= last_node.x - 1 < self.x and 0 <= last_node.y < self.y:
                            if (self.value_list[last_node.y, last_node.x - 1] == 0):
                                full_flag = False
                            new_node = Node(last_node.y, last_node.x - 1, 'l', full_flag, False)
                            if (not self.checkNodeExistInPath(new_node, path)):
                                path.append(new_node)
                                paths.append(path)
                    elif last_node.step == 'u':
                        full_flag = True
                        if 0 <= last_node.x < self.x and 0 <= last_node.y - 1 < self.y:
                            if (self.value_list[last_node.y - 1, last_node.x] == 0):
                                full_flag = False
                            new_node = Node(last_node.y - 1, last_node.x, 'u', full_flag, False)
                            if (not self.checkNodeExistInPath(new_node, path)):
                                path.append(new_node)
                                paths.append(path)
                    elif last_node.step == 'd':
                        full_flag = True
                        if 0 <= last_node.x < self.x and 0 <= last_node.y + 1 < self.y:
                            if (self.value_list[last_node.y + 1, last_node.x] == 0):
                                full_flag = False
                            new_node = Node(last_node.y + 1, last_node.x, 'd', full_flag, False)
                            if (not self.checkNodeExistInPath(new_node, path)):
                                path.append(new_node)
                                paths.append(path)
                else:
                    if 0 <= last_node.x + 1 < self.x and 0 <= last_node.y < self.y:
                        full_flag = True
                        if (self.value_list[last_node.y, last_node.x + 1] == 0):
                            full_flag = False
                        new_node_right = Node(last_node.y, last_node.x + 1, 'r', full_flag, False)
                        right_path = copy.deepcopy(path)
                        if (not self.checkNodeExistInPath(new_node_right, right_path)):
                            right_path.append(new_node_right)
                            paths.append(right_path)
                    if 0 <= last_node.x - 1 < self.x and 0 <= last_node.y < self.y:
                        full_flag = True
                        if (self.value_list[last_node.y, last_node.x - 1] == 0):
                            full_flag = False
                        new_node_left = Node(last_node.y, last_node.x - 1, 'l', full_flag, False)
                        left_path = copy.deepcopy(path)
                        if (not self.checkNodeExistInPath(new_node_left, left_path)):
                            left_path.append(new_node_left)
                            paths.append(left_path)
                    if 0 <= last_node.x < self.x and 0 <= last_node.y - 1 < self.y:
                        full_flag = True
                        if (self.value_list[last_node.y - 1, last_node.x] == 0):
                            full_flag = False
                        new_node_up = Node(last_node.y - 1, last_node.x, 'u', full_flag, False)
                        up_path = copy.deepcopy(path)
                        if (not self.checkNodeExistInPath(new_node_up, up_path)):
                            up_path.append(new_node_up)
                            paths.append(up_path)
                    if 0 <= last_node.x < self.x and 0 <= last_node.y + 1 < self.y:
                        full_flag = True
                        if (self.value_list[last_node.y + 1, last_node.x] == 0):
                            full_flag = False
                        new_node_down = Node(last_node.y + 1, last_node.x, 'd', full_flag, False)
                        down_path = copy.deepcopy(path)
                        if (not self.checkNodeExistInPath(new_node_down, down_path)):
                            down_path.append(new_node_down)
                            paths.append(down_path)
        return result

    def checkNegetiveEmptyValue(self):
        for j in range(self.y):
            for i in range(self.x):
                if (self.empty_value[j, i] < 0):
                    return True

        return False
    def findFistPath(self,step_stone_paths):
        for path in step_stone_paths:
            start_node = path[0]
            if (self.input_variable_row_index == start_node.y and self.input_variable_col_index == start_node.x):
                return path
    def cleen_path(self,path):
        first_node = path[0]
        result = []
        result.append(first_node)
        for node in path:
            if self.value_list[node.y,node.x] != 0:
                result.append(node)

        return result
    def clculate_result(self):
        return_array = np.zeros((self.y,self.x) , dtype=int)
        for index_j in range(self.y):
            for index_i in range(self.x):
                return_array[index_j,index_i] = self.list[index_j , index_i] * self.value_list[index_j,index_i]

        return np.sum(return_array)
    def main(self):

        global first_path
        first_path = None
        self.calculateUV()
        self.calculateEmptyValue()
        step = 0
        while (self.checkNegetiveEmptyValue()):
            step += 1
            print('------------------------------step ', step, '------------------------------')
            print('Enpty value set:')
            print(self.empty_value)
            print('value set:')
            print(self.value_list)
            step_stone_paths = self.find_path()
            self.findInputVariable()

            first_path = self.findFistPath(step_stone_paths)
            if(first_path):
                first_path = first_path[::-1]

                first_path.pop()
                first_path = self.cleen_path(first_path)

                for i in range(len(first_path)):
                    if i % 2 == 1:
                        first_path[i].setIsNegative(True)
                        first_path[i].setValue(- (self.value_list[first_path[i].y,first_path[i].x]))
                    else :
                        first_path[i].setIsNegative(False)
                        first_path[i].setValue(self.value_list[first_path[i].y,first_path[i].x])

                negative_path = []

                for node in first_path :
                    if(node.value < 0):
                        negative_path.append(node)

                max_negative_index = 0
                for i in range(1,len(negative_path)):
                    if negative_path[i].value > negative_path[max_negative_index].value:
                        max_negative_index = i

                output_variable = negative_path[max_negative_index].value
                for node in first_path:
                    if node.isNegative:
                        self.value_list[node.y,node.x] = self.value_list[node.y,node.x] + output_variable
                    else:
                        self.value_list[node.y,node.x] = self.value_list[node.y,node.x] - output_variable
                self.initUV()
                self.calculateUV()
                self.calculateEmptyValue()
            time.sleep(7)
        print('------------------------------finaly------------------------------')
        print('Enpty value set:')
        print(self.empty_value)
        print('value set:')
        print(self.value_list)
        time.sleep(7)
        return self.clculate_result()
