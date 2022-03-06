# class syntax
# an attribute ius a variable that is associated with an object
# constructor, allow to specific action also know as initialize a object
""" __init__ special method use to initialize a attributte
Adding Methods to a class
When a functions is attack to an object is called a method
"""

class User:
      def __init__(self, user_id, username): # This function is going to be call everytime you create a new object
          self.id = user_id
          self.username = username
          self.followers = 0 # this is a default value therefore it doesnt need to be part of the parameters
          self.following = 0
      def follow(self, user):
          user.followers += 1
          self.following += 1

user_1 = User("001", "Lilibeth")
user_2 = User("1995", "Montano")
# print(user_1.id)
# print(user_2.username)
# print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)