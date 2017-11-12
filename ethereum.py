import sys
import requests
import json

#Pablo Alguindigue
'''First input is purchase price'''
'''Second input is quantity of currency'''

'''New line spacing for printing'''
def header(x):
	print'\n'*x

'''returns boolean'''
def isNotEmpty(x):
	return len(x)>0

'''trys to cast x to a float, else quits'''
def castToFloat(x):
	try:
		return float(x)
	except Exception:
		print 'Could not cast {} to float'.format(x)
		sys.exit()

'''returns only the current price of currency'''
def getCurrentPrice():
	r = requests.get('https://coinmarketcap.com/currencies/ethereum/')
	transferrable = []

	if r.status_code ==200: 
		for charachter in r.text[r.text.index('quote_price')+13:r.text.index('quote_price')+24]:
			try:
				charachter = int(charachter)
			except Exception:
				pass
			if type(charachter) == int:
				transferrable.append(charachter)
			
			if charachter == '.':
				transferrable.append('.')
	

		currentPrice = str()
		for item in transferrable:
			currentPrice+=str(item)
		
		return currentPrice
	
	else:
		print 'Request to website did not succeed'


'''prints your gain or loss at the moment of your currency investment'''
def compute(quantity, purchasePrice, currentPrice):
	if isNotEmpty(quantity) and isNotEmpty(purchasePrice) and isNotEmpty(currentPrice):
		purchasePriceTotal = castToFloat(quantity)* castToFloat(purchasePrice)
		currentPriceTotal = castToFloat(quantity)*castToFloat(currentPrice)
		gain = currentPriceTotal-purchasePriceTotal
		header(1)
		
		print 'You have: {} ethereum'.format(quantity)
		print 'ethereum current price: ',currentPrice
		print 'Your purchase price: ',purchasePrice
		
		if gain > 0:
			print 'Your gain: ',gain
		else:
			print 'Your loss: ',gain
		header(2)

	else:
		print 'One of your variables is not set'

	sys.exit()










#Program start
####################################################

header(3)
purchasePrice =''
quantity = ''

#if input is default, try and read default.json
if len(sys.argv)==2 and sys.argv[1] =='default':
	try:
		with open('default.json','r') as default:
			default = json.load(default)
			
			#make sure there is value in vars
			if isNotEmpty(str(default['ethereum']['price'])) and isNotEmpty(str(default['ethereum']['amount'])):
				purchasePrice = str(default['ethereum']['price'])
				quantity = str(default['ethereum']['amount'])
			
			else:
				print 'I think your one of your values is empty in default.json'
				sys.exit()
	
	except Exception:
		print 'Could not find default.json'
		print 'Might have to set default.json location'


#if input is price, only return the price
elif len(sys.argv)==2 and sys.argv[1] =='price':
	print 'Current ethereum price is: ',getCurrentPrice()
	sys.exit()


#if the there was a single command line arguement passed
elif len(sys.argv)==2:
	purchasePrice = sys.argv[1]
	quantity = raw_input('Enter amount of ethereum: ')


#if the there was a both purchase price and quantity set as arguements
elif len(sys.argv)==3:
	purchasePrice = sys.argv[1]
	quantity = sys.argv[2]

#if nothing is specified, then ask
else:
	purchasePrice = raw_input('Enter Purchase Price: ')
	quantity = raw_input('Enter amount of ethereum: ')
	
compute(quantity, purchasePrice, getCurrentPrice())


