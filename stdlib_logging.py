# os 模块用以和操作系统交互
# platform 模块用以获取平台——操作系统——的信息
# logging 模块用来记录（Log）信息
import os
import platform
import logging

# platform.platform() 返回的字符串来确认我们正在使用的操作系统
# 如果它是 Windows，
# 我们将找出其主驱动器（Home Drive），主文件夹（Home Folder）以及我们希望存储信息的文件名
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
# 对于其它平台而言，我们需要知道的只是用户的主文件夹位置，这样我们就可获得文件的全部位置信息
else:
    # 使用 os.path.join() 函数来将这三部分位置信息聚合到一起
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

# 调试，提醒，警告
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")