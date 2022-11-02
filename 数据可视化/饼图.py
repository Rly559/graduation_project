# _*_ coding :utf-8 _*_
# @Time :2022/4/4 17:11
# @Author :河北地质大学 李林逸
# @File : 饼图
# @Project :爬虫


#工作经验与岗位的关系
from pyecharts.charts import Pie
import pyecharts.options as opts


num = [21792,11771,3991,1068,800,719,175]
lab = ['本科','大专','硕士','中专','博士','高中','初中及以下']

pie = (
    Pie(init_opts=opts.InitOpts(width='720px',height='320px'))
    .add(series_name='',data_pair=[(j,i)for i,j in zip(num,lab)])
)

pie.render('工作经验饼图.html')
