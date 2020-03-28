import modules
from modules.mymodule import say_hi, __version__
# from mymodule import *
# 这将导入诸如 say_hi 等所有公共名称，但不会导入 __version__ 名称，因为后者以双下划线开头。
say_hi()
print('Version', __version__)
# 包是指一个包含模块与一个特殊的 __init__.py 文件的文件夹
# 后者向 Python 表明这一文件夹是特别的，因为其包含了 Python 模块。
# 包是一种能够方便地分层组织模块的方式。
