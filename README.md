# CurrencyTools

## *Description*
Just fun Scripts to help when investing in CryptoCurrencies

## Dependencies

*Connection to the internet*

Python2
sys `https://docs.python.org/2/library/sys.html`
requests `http://docs.python-requests.org/en/master/`
json `https://docs.python.org/2/library/json.html`


## *Files*

### default.json
Allows you to store a purchase price of your currency and how much you possess.  

### bitcoin.py 
Calculates your gain/loss against a set purchase price and quantity of bitcoin against the current market value which it gets via get request of `https://coinmarketcap.com/`

There are 3 accepted command line arguements for bitcoin.py. 
	
A single float/double/int which will be interpreted as the purchase price.
which would look like `python bitcoin.py 5000`

Two floats/doubles/ints which will be interpreted as the purchase price and then quantity of currency.
which would look like `python bitcoin.py 5000 3.78`

specify to use the `default.json` file where you can set your purchase price and amount.
which would look like `python bitcoin.py default`


### ethereum.py
Calculates your gain/loss against a set purchase price and quantity of ethereum against the current market value which it gets via get request of `https://coinmarketcap.com/`

There are 3 accepted command line arguements for ethereum.py. 
	
A single float/double/int which will be interpreted as the purchase price.
which would look like `python ethereum.py 200`

Two floats/doubles/ints which will be interpreted as the purchase price and then quantity of currency.
which would look like `python ethereum.py 200 3.78`

specify to use the `default.json` file where you can set your purchase price and amount.
which would look like `python ethereum.py default`


### litecoin.py
Calculates your gain/loss against a set purchase price and quantity of litecoin against the current market value which it gets via get request of `https://coinmarketcap.com/`

A single float/double/int which will be interpreted as the purchase price.
which would look like `python litecoin.py 200`

Two floats/doubles/ints which will be interpreted as the purchase price and then quantity of currency.
which would look like `python litecoin.py 200 3.78`

specify to use the `default.json` file where you can set your purchase price and amount.
which would look like `python litecoin.py default`

## *Alias*
	If you care to make an alias for these scripts I recommend using something like
	
alias `bitcoin`="python $(echo(find ~/ -name bitcoin.py 2>dev/null) | head -n1) default"
alias `ethereum`="python $(echo(find ~/ -name ethereum.py 2>dev/null) | head -n1) default"
alias `litecoin`="python $(echo(find ~/ -name litecoin.py 2>dev/null) | head -n1) default"
