import re
#bir dizeden maksimum sayı değerini çıkartan algoritma
def extractMax(input):

	numbers = re.findall('\d+',input)

	numbers = map(int,numbers)

	print (max(numbers))

if __name__ == "__main__":

	input = 'kajdkjla921398asd19sdadads8123adjsk'

	extractMax(input)
