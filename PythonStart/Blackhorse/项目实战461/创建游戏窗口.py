import time

import pygame

pygame.init()
# set_mode(resolution= (0,0),flags= 0,depth=0) ->Surface
# resolution 指定屏幕的宽和高，默认创建的窗口和屏幕大小一致
# flags参数指定屏幕的附加选项，例如是否全屏等，默认不需要传递
# depth 参数表示颜色的位数，默认自动匹配

# 注意：必须使用变量记录 set_mode 方法的返回结果！因为后续所有的图像绘制都基于这个返回结果


# 创建游戏的窗口 480*700

screen = pygame.display.set_mode((480, 700))

while True:
    time.sleep(10)
    pygame.quit()

