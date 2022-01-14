#从app模块中即从__init__.py中导入创建的app应用
from app import app
from flask import render_template
import os

def GetImg():
    curDir = os.getcwd()
    file = curDir.replace('\\','/')+'/app/static/picture/'
    imgs = os.listdir(file)

    imgInfo = []
    for i in imgs:
        imgInfo.append({
            'imgFeid': 'Fe'+i,
            'imgid':i,
            'imgro': '/static/picture/'+i,
        })
    return imgInfo

#建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
def index():
    imgInfo = GetImg()
    return render_template('pic2.html',imgInfos=imgInfo)
