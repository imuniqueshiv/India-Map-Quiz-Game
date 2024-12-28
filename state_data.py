# import pandas
#
# india_dict = {
#     "indian_states": [
#         "Andhra Pradesh",
#         "Arunachal Pradesh",
#         "Assam",
#         "Bihar",
#         "Chhattisgarh",
#         "Goa",
#         "Gujarat",
#         "Haryana",
#         "Himachal Pradesh",
#         "Jharkhand",
#         "Karnataka",
#         "Kerala",
#         "Madhya Pradesh",
#         "Maharashtra",
#         "Manipur",
#         "Meghalaya",
#         "Mizoram",
#         "Nagaland",
#         "Odisha",
#         "Punjab",
#         "Rajasthan",
#         "Sikkim",
#         "Tamil Nadu",
#         "Telangana",
#         "Tripura",
#         "Uttar Pradesh",
#         "Uttarakhand",
#         "West Bengal"
#     ],
#     'x': [-54.0, 199.0, 167.0, 53.0, -1.0, -135.0, -177.0, -101.0, -83.0, 27.0, -115.0, -102.0, -64.0, -121.0, 188.0,
#           135.0, 168.0, 198.0, 28.0, -111.0, -153.0, 98.0, -69.0, -57.0, 148.0, -30.0, -51.0, 85.0],
#     'y': [-125.0, 108.0, 72.0, 59.0, -2.0, -122.0, 18.0, 119.0, 175.0, 20.0, -123.0, -193.0, 14.0, -47.0, 37.0, 54.0,
#           19.0, 62.0, -31.0, 149.0, 75.0, 87.0, -189.0, -81.0, 20.0, 77.0, 138.0, 17.0]
#
# }
#
# df = pandas.DataFrame(india_dict)
# df.to_csv("india_states_data.csv", index=False)
#
# data = pandas.read_csv("india_states_data.csv")
# print(len(data))