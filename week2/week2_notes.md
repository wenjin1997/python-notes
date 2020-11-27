# 第二周 Python基本图形绘制
## 前课复习
### Python基本语法元素
* 缩进、注释、命名、变量、保留字
* 数据类型、字符串、整数、浮点数、列表
* 赋值语句、分支语句、函数
* input()、print()、eval()、print()格式化
### 保留字
and elif import raise global  
as else in return nonlocal   
assert except is try True  
break finally lambda while False  
class for not with None  
continue from or yield async  
def if pass del await 
## 2.1 深入理解Python语言
* 计算机系统结构时代到人工智能时代的演进路线
* 五种编程语言的初心和历史使命
* Python语言的通用性、简洁性和生态性
* Python是以计算生态为标志的“超级语言”
## 2.2 实例2 Python蟒蛇绘制
## 2.3 turtle库的使用
### turtle库概述
* **turtle(海龟)库是turtle绘图体系的Python实现**
* turtle绘图体系：1969年诞生，主要用于程序设计入门
* Python语言的**标准库**之一
* 入门级的图形绘制函数库
### 标准库
* **Python计算生态=标准库+第三方库**
### turtle的绘图窗体
`turtle.setup(width, height, startx, starty)`
* setup()设置窗体大小及位置
* 4个参数中后两个可选
* setup()不是必须的