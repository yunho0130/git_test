
# coding: utf-8

# * Markdown Test

# In[1]:

class Duck:
        def quack(self): print u"꽥꽥!"
        def feathers(self): print u"오리에게 흰색, 회색 깃털이 있습니다."

class Person:
        def quack(self): print u"이 사람이 오리를 흉내내네요."
        def feathers(self): print u"사람은 바닥에서 깃털을 주어서 보여 줍니다."

def in_the_forest(duck):
        duck.quack()
        duck.feathers()

def game():
        donald = Duck()
        john = Person()
        in_the_forest(donald)
        in_the_forest(john)


# In[2]:

game()


# In[4]:

import platform
platform.python_version()

