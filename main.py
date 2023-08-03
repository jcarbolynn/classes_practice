class User:
  # can have an empty class by using pass
  # use 
  # pass

  # self is the object being created
  # def __init__(self):
  #   print("Hello")

  def __init__(self, username, user_id):
    # use what is passed in to set object's attributes
    # convention that name of parameter matches name of attribute
    self.username = username
    self.id = float(user_id)
    self.followers = 0
    self.following = 0

    # when each object is created you MUST provide this information for the attributes
    # can create default values and do not need to provide this information when creating the object

  # needs a self parameter, lets you know the object that called it
  def follow(self, user):
    self.following += 1
    user.followers += 1
    
# 0o because leading zeroes not ok, or make them stings
user_1 = User("hello", 0o001)
user_2 = User("goodbye", 0o007)


user_1.follow(user_2)
print(user_1.following)
print(user_2.following)
print(user_2.followers)
