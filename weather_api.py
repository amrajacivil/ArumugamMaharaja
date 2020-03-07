#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyowm


# In[4]:


owm=pyowm.OWM('cfad055fca0296c5371e2877c24f7284')


# In[19]:


city='Chennai,India'
temp=owm.weather_at_place(city)


# In[20]:


temp.get_weather().get_temperature()


# In[21]:


temp.get_weather().get_temperature('celsius')['temp']


# In[22]:


temp.get_weather().get_sunrise_time(timeformat='iso')


# In[23]:


forecast=owm.three_hours_forecast(city)


# In[24]:


forecast.will_have_rain()


# In[25]:


forecast.will_have_clouds()


# In[26]:


forecast.will_have_fog()


# In[27]:


from geopy.geocoders import Nominatim


# In[28]:


location=Nominatim().geocode(city)


# In[29]:


location.latitude


# In[31]:


location.longitude
import datetime


# In[33]:


uvi=owm.uvindex_history_around_coords(location.latitude,location.longitude,start=datetime.datetime(2019,12,1,0,0,0),
                                          end=datetime.datetime(2019,12,5,0,0,0))


# In[34]:


uvi


# In[ ]:




