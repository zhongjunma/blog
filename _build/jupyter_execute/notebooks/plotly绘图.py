#!/usr/bin/env python
# coding: utf-8

# # plotly 绘图
# 
# `plotly` 是我最喜欢的绘制地图的包，能绘制出各种好看的地图，并且能够保存成可交互的 html 或者图片（png、eps）。这个 notebook 将会持续更新相关的代码。

# In[1]:


import pandas as pd

import plotly
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


mapbox_token = 'pk.eyJ1IjoiemhvbmdqdW5tYSIsImEiOiJja2pwbzA3c2YwNjd3MnJxaDFrcHh5NmNyIn0.6mzTX-clHuP5h9lUO17TCw'


# # Mapbox 设置
# 
# 

# # 绘制 scatter plot
# 
# 将 point 绘制在地图上。这个 point 可以是 AIS data 的一个 observation，也可以是 stay points。总之，必须提供 point 的经纬度坐标。

# ## 基础
# 
# 不分组，也没有 heading，只是单纯的将 point 绘制在地图上。

# In[3]:


def plot_points(df):
    fig = px.scatter_mapbox(
        df,
        lat=df['latitude'],
        lon=df['longitude'],
        hover_data=['imo', 'timestamp', 'speed', 'heading'],
        zoom=10,
    )
    fig.update_layout(
        mapbox={
            'accesstoken': mapbox_token,
            'style': 'satellite-streets',
        },
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    )
    return fig


# In[4]:


ais_df = pd.read_csv('./data/ais_Dalian_201801.csv', sep='|', header=0)


# In[5]:


ais_df.head()


# In[6]:


plot_points(ais_df)


# ## 分组
# 
# 按照 point 的 label 分组，每一组有不同的颜色。

# In[7]:


def plot_points_by_label(df):
    fig = px.scatter_mapbox(
        df,
        lat=df['lat'],
        lon=df['lng'],
        hover_data=['imo', 'timestamp_start', 'timestamp_end', 'time_delta'],
        color=df['cluster_label'].astype(str),
        zoom=10,
    )
    fig.update_layout(
        mapbox={
            'accesstoken': mapbox_token,
            'style': 'satellite-streets',
        },
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    )
    return fig


# In[8]:


stay_points_df = pd.read_csv('./data/Ras Tanura.csv', sep='|', header=0)


# In[9]:


stay_points_df.head()


# In[10]:


plot_points_by_label(stay_points_df)


# ## Heading
# 
# AIS data 中其实也包含了 heading，在绘制 point 的时候，加上 heading 可以更加直观。

# In[11]:


def plot_points_heading(df):
    fig = go.Figure(go.Scattermapbox(
        lon=df['longitude'], 
        lat=df['latitude'],
        text=(
            df['timestamp'].astype(str) + ' | ' + 
            df['imo'].astype(str) + ' | ' + 
            df['heading'].astype(str)
        ),
        marker= {
            'symbol': 'monument',
            'angle': df['heading'],
            'allowoverlap': True,
        },
    ))

    fig.update_layout(
        mapbox={
            'accesstoken': mapbox_token,
            'style': "satellite-streets", 
            'zoom': 10,
            'center': {
                'lat': df['latitude'].mean(),
                'lon': df['longitude'].mean(),
            },
        },
        showlegend=False,
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    )
    return fig


# In[12]:


plot_points_heading(ais_df)

