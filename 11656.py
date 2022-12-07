inputs = input()

answer_dict = [inputs[i:] for i in range(len(inputs))]
answer_dict.sort()
print("\n".join(answer_dict))