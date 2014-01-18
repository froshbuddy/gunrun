class Area:
	productCodes = {
		'sidearm': 0,
		'ballistic': 1,
		'ammo': 2,
		'explosives': 3,
		'laser': 4,
		'chemicals': 5
	};
	product = [
		1,#sidearm
		3,#ballistic
		1,#ammo
		3,#explosive
		15,#laser
		8,#chemical
	];

	def __init__(self,priceMod):
		for i in range(len(self.product)):
			self.product[i] += priceMod[i];
		print self.product;



if __name__ == "__main__":
	area = Area([0,3,0,5,150,30]);