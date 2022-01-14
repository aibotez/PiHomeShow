
from flask import Flask
#从app模块中导入app应用
from app import app

# app = Flask(import_name=__name__,
#             static_url_path='/s', # 配置静态文件的访问 url 前缀
#             static_folder='static',    # 配置静态文件的文件夹
#             template_folder='templates') # 配置模板文件的文件夹

#防止被引用后执行，只有在当前模块中才可以使用
if __name__=='__main__':
    app.run('0.0.0.0')