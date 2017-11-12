import sys
import requests
import json

#Pablo Alguindigue
'''First thing is purchase price'''
'''Second thing is quantity of currency'''

def header(x):
	print'\n'*x

def isNotEmpty(x):
	return len(x)>0

def castToFloat(x):
	try:
		return float(x)
	except Exception:
		print 'Could not cast to float'

def logic(quantity, purchasePrice, currentPrice):
	if isNotEmpty(quantity) and isNotEmpty(purchasePrice) and isNotEmpty(currentPrice):
		purchasePriceTotal = castToFloat(quantity)* castToFloat(purchasePrice)
		currentPriceTotal = castToFloat(quantity)*castToFloat(currentPrice)
		gain = currentPriceTotal-purchasePriceTotal
		header(1)
		print 'You have: {} Eth'.format(quantity)
		print 'Ethereum current price: ',currentPrice
		print 'Your purchase price: ',purchasePrice
		
		if gain > 0:
			print 'Your gain: ',gain
		else:
			print 'Your loss: ',gain
		header(2)

	else:
		print 'One of your variables is not set'

header(3)
purchasePrice =''
quantity = ''

if len(sys.argv)==2 and sys.argv[1] =='default':
	try:
		with open('/Users/Lito/Desktop/currency/default.json','r') as default:
			default = json.load(default)
			purchasePrice = str(default['ethereum']['price'])
			quantity = str(default['ethereum']['amount'])
	
	except Exception:
		print 'Could not find defaut.json'
		sys.exit()

elif len(sys.argv)==2 and not isNotEmpty(quantity):
	purchasePrice = sys.argv[1]
	quantity = raw_input('Enter amount of Ethereum: ')

elif len(sys.argv)==3:
	purchasePrice = sys.argv[1]
	quantity = sys.argv[2]

elif len(sys.argv)>3:
	print 'Not sure what you\'re trying to do'
	header()
	sys.exit(1)

else:
	purchasePrice = raw_input('Enter Purchase Price: ')
	quantity = raw_input('Enter amount of Ethereum: ')


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
	
	logic(quantity, purchasePrice, currentPrice)

else:
	print 'Request to website did not succeed'
