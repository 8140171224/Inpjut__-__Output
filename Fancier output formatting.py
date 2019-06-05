#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = 2019
event = 'Referendum'


# In[3]:


f'Result of the {year} {event}'


# In[4]:


#NEXT


# In[5]:


yes_votes = 42_85_999
no_votes = 43_56_956


# In[6]:


percentages = yes_votes / (yes_votes + no_votes)


# In[8]:


'{:-9} YES votes {:2.2%}'.format(yes_votes, percentages)


# In[9]:


#NEXT


# In[10]:


s = 'Hello, World.'
str(s)


# In[11]:


repr(s)


# In[12]:


str(1/7)


# In[14]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ',and y is ' + repr(y)


# In[15]:


print(s)


# In[16]:


hello = 'Hello, world\n'
hellos = repr(hello)
print(hellos)


# In[17]:


repr((x, y, ('spam', 'eggs')))


# In[ ]:




