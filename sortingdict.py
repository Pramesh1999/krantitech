#creating dictionary
Weight_details = { "age": 20,  "age1": 24}
sorted_weight = sorted(Weight_details.items(), key=lambda x: x[1] )
print(sorted_weight)


#OUT PUT
"""
[('age', 20), ('age1', 24)]
"""
