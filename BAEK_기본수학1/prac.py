# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first - self.second
#         return result
#     def sub(self):
#         result = self.first * self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# class MoreFourcal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = MoreFourcal(2,4)
# print(a.pow())
graph = []
for i in range(5):
    graph.append(list(map(int, input())))
print(len(graph))