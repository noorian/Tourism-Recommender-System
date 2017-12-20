import pickle as pk
with open('bs_id_set.pkl', 'rb') as f:
    bs_id_set = pk.load(f)

print(len(bs_id_set))