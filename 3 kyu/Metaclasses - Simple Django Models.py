class Model:
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	# def validate(self):
	# 	print('validated')


# class User(Model):
#     # first_name = CharField(max_length=30)
#     # last_name = CharField(max_length=50)
#     # email = EmailField()
#     # is_verified = BooleanField(default=False)
#     # date_joined = DateTimeField(auto_now=True)
#     # age = IntegerField(min_value=5, max_value=120, blank=True)
#     pass

# user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
# # user1.validate()


'''
class CharField:

	@classmethod
	def classmethod(cls, min_length = 0, max_length = None):
		cls.min_length = min_length
		cls.max_length = max_length

	@classmethod
	def validate(cls, self):
		print(cls.min_length < len(self.))

'''


'''



print(user1.date_joined)  # prints date and time when the instance was created
print(user1.is_verified)  # prints False (default value)

user1.age = 256
user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and mandatory
'''