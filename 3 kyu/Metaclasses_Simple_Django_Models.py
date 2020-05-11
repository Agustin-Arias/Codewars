import datetime
import re

class ValidationError(Exception):
	pass

class Model:
	# add try except so that when fewer arguments
	# are passed to Model, it trows a ValidationError.
	def __init__(self, first_name, last_name, email):
		self.first_name.string = first_name
		self.last_name.string = last_name
		self.email.string = email


	def validate(self):
		self.first_name.validate()
		self.last_name.validate()
		self.email.validate()
		self.is_verified.validate()
		self.age.validate()


class CharField:
	string = None
	def __init__(self, min_length = 0, max_length = None, blank = False, default = None):
		self.min_length = min_length
		self.max_length = max_length

	def validate(self):
		#include blank and default
		if type(self.string) == str:
			length = len(self.string)
			mini = self.min_length
			maxi = self.max_length
			if not self.string.isalpha():
				print(f"{self.string} must be of alphabetical type.\n")
			elif (length < mini):
				print(f"Length of {self.string} is too short! Minimum {mini} characters.\n")
				raise ValidationError
			elif (length > maxi):
				print(f"Length of {self.string} is too long! Maximum {maxi} characters.\n")
				raise ValidationError
		else:
			print(f"Type of name was not correct, {type(self.string)} must be of type str.\n")
			raise ValidationError

class EmailField:
	string = None
	def __init__(self, min_length = 0, max_length = None, blank = False, default = None):
		self.min_length = min_length
		self.max_length = max_length

	def validate(self):
		#include blank and default
		string = self.string
		if type(string) == str:
			words = re.findall(r"[\w']+" , string)
			if all(word.isalpha() and self.min_length <= len(word) <= (self.max_length if self.max_length else len(word)) for word in words):
				pass
			else:
				print(f"Email {string} was not valid")
				print("Email should be in the format: \n"
					"address@subdomain.domain where address, subdomain, and domain are sequences of alphabetical characters.\n"
					f"with length above {self.min_length}", end = "")
				if self.max_length:
					print(f" and below {self.max_length}")
				else:
					print(".")
				ṕrint()
				raise ValidationError
		else:
			print(f"Type of email \"{string}\" was not correct, type should be str.")

class DateTimeField:
	def __init__(self, auto_now = False, blank = False, default = None):
		self.auto_now = auto_now
		self.default = default

	def __repr__(self):
		if self.default == None:
			return str(datetime.datetime.now())
		else:
			return str(self.date_time)

class BooleanField:
	def  __init__(self, blank = False, default = None):
		self.default = default

	def __repr__(self):
		return str(self.default)

	def validate(self):
		if type(self.default) == bool:
			pass
		else:
			print(f"Type was not correct, {type(self.default)} must be of type bool")

#unfinished
class IntegerField:
	def __init__(self, min_value = None, max_value = None, blank = False, default = None):
		self.min_value = min_value
		self.max_value = max_value
	
	def validate(self):		
		#unfinished
		pass

class User(Model):
	first_name = CharField(max_length=30)
	last_name = CharField(max_length=50)
	email = EmailField()
	date_joined = DateTimeField(auto_now=True)	
	is_verified = BooleanField(default=False)
	age = IntegerField(min_value=5, max_value=120, blank=True)

user1 = User(first_name='Liam', last_name='Smith', email="liam@example.com")
# user1.validate()
# print(user1.date_joined)  # prints date and time when the instance was created
# print(user1.is_verified)  # prints False (default value)

# print(user1.age)
# user1.age = 256
# print(user1.age)
# user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and mandatory
