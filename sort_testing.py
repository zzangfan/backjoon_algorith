input_list = ["alice,20,800,mtv","alice,50,1200,mtv"]
trans_list = [i.split(",") for i in input_list]
trans_list.sort(key=lambda x: int(x[1]),reverse=True)
print(trans_list)