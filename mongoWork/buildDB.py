from pymongo import MongoClient
import json

data=json.load(open("../data/nasa.json"))

client=MongoClient('ds131729.mlab.com:31729')
client.crumbs.authenticate('Ghouse', 'llokumi.!@#$')

db=client.crumbs
number = 0
for d in data['dataset']:
	print number
	db.datasets.insert(d)
	number += 1