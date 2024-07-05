# list practice

"""
Note on Pythons different loops
`for n in nodes`: Iterates over the elements of the list nodes.
`for i in range(len(nodes))`: Iterates over the indices of the list nodes.
`for index, value in enumerate(nodes)`: Iterates over both the indices and the elements of the list nodes.
"""

nodes1 = ["id", "5", "left", "10", "right", "15", "value", "5" ]
num_node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# this type of loops prints value/element `for [value] in lst``
for n in nodes1:
    print(n)

# --------------------------------------------- #

print("# --------------------------------------------- #")

nodes2 = ["id", "5", "left", "10", "right", "15", "value", "5"]

# Iterate over a range of indices from 0 to len(nodes) - 1
for i in range(len(nodes2)):
    print(nodes2[i])

# --------------------------------------------- #

print("# --------------------------------------------- #")

nodes3 = ["id", "5", "left", "10", "right", "15", "value", "5"]

for i, v in enumerate(nodes3):
    print(nodes3) # ['id', '5', 'left', '10', 'right', '15', 'value', '5']
    print(v) # id
    print(nodes3[i]) # id
