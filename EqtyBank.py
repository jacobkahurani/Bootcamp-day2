class Counter(object):
	number = 0
	def __init__(self):
		Counter.number +=1
	def __del__(self):
		Counter.number -=1
class Account(Counter):
	def __init__(self, holder, number, balance, credit_line=1500):
		Counter.__init__(self) #call method defined in another class.
		self.__Holder = holder
		self.__Number = number
		self.__Balance = balance
		self.__CreditLine = credit_line
	def deposit(self, amount):
		self.__Balance = amount
	def withdraw(self, amount):
		if(self.__Balance - amount <- self.__CreditLine):
			#coverage insufficient
			return False
		else:
			self.__Balance -=amount
			return True
	def balance(self):
		return self.__Balance
	def transfer(self, target, amount):
		if(self.__Balance - amount <-self.__CreditLine):
			#coverage insufficient
			return False
		else:
			self.__Balance -= amount
			target.__Balance += amount
			return True
