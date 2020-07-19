Week04学习笔记
 Pandas 类似python 的Excel 。

数据分析时习惯用工具进行数据清洗，数据切分等。替代数据转为CSV+正则表达式；
 
三个重要的库 import pandas  as  pd、import numpy as  np、import matplotlib as plt;;

Pandas 会智能看到文档的全貌、默认会增加标题；同时其筛选功能是必备技能；
通过pandas 的map函数

Pandas 的基本数据结构：
Series 数据结构     单行单列 两个基本属性: index 和 value  创建可以通过字典创建、另外可以通过列表 关键字+列表创建；
DataFrame 数据结构 多行多列  创建可以通过列表，或者通过嵌套列表创建；
自己创建的比较少。

数据的获取和预处理
数据的导入和新建，导入较多
数据预处理：缺失、重复、异常值的处理方法
索引设置
高阶函数 map reduce filter

Pandas 使用read_*() 进行大量格式的数据导入；例如read_excel、read_csv、read_sql
常用的连接mysq 数据库为：
Import pymysql
Sql = ‘select * from mytable’
Conn = pymysql.connect(‘ip’,’name’, ‘dbname’, ‘charset = utf8’)
Df = pd.read_sql(sql,conn) 

Pandas 数据预处理
	缺失值处理: 使用平均值填充（x.fillna）、前向填充(df.ffill)、缺失值删除（df.isnull 查看缺失值，df.dropna 缺失值删除）；
	重复值处理：删除(drop_duplicates)

数据的操作调整
	数据的排序操作（by）、行列删除（df.drop）、查找操作、行列互换（.T功能） 数据透视。

使用jieba机型自动分词，
	Jieba分词与提取关键词、jieba 调整词典 jieba 词性标注

使用SnowNLP 进行语义情感标注
通过掌握Pandas 可以更快的针对爬虫数据进行数据清洗，并快速提取想要的数据。
