import pickle
from efficient_apriori import apriori

f = open('stockTransactions.dump','rb')

apriori_dataset = pickle.load(f)

print(apriori_dataset[0])

itemsets, rules = apriori(apriori_dataset, min_support=0.3,  min_confidence=0.9)

print (rules)