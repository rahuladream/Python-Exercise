import pickle

def storeData():
	omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
	rahul = {'key': 'Rahul', 'name': 'Rahul Singh', 'age': 23, 'pay': 50000}

	db = {}
	db['omkar'] = omkar
	db['rahul'] = rahul

	dbfile = open('examplePickle', 'ab')

	pickle.dump(db, dbfile)
	dbfile.close()

	def loadData():
		dbfile = open('examplePickle', 'rb')
		db.pickle.load(dbfile)

		for keys in db:
			print(keys, '=>', db[keys])
		dbfile.close()

	if __name__ == '__main__':
		storeData()
		loadData()