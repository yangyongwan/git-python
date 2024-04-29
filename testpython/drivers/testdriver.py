# 1️⃣ 编辑相关:
# 🔍 缩进代码: Tab / Shift + Tab
# ✍️ 注释代码: Ctrl + / (单行注释) / Ctrl + Shift + / (多行注释)
# 💥 复制行/选定代码块: Ctrl + D
# 🗑️ 删除行/选定代码块: Ctrl + Y
# ⬆️⬇️ 上移/下移行/选定代码块: Ctrl + Shift + Up / Ctrl + Shift + Down
# 🎨 格式化代码: Ctrl + Alt + L
# 🔍 查找定义: Ctrl + 左键点击变量名或方法名
# 📚 查找引用: Alt + F7
# 🆕 自动导入丢失的模块: Alt + Enter
# 🛠️ 快速修复错误或警告: Alt + Enter
# 2️⃣ 文件与项目:
# 📂 新建文件: Ctrl + N
# 📂 打开文件: Ctrl + O
# 💾 保存文件: Ctrl + S
# ❌ 关闭当前标签页: Ctrl + F4
# ⏭️ 跳转到下一个标签页: Alt + Right
# ⏮️ 跳转到上一个标签页: Alt + Left
# 🔍 查找文件: Ctrl + Shift + N
# 🔎 查找类、文件、符号等: Ctrl + Shift + F
# 3️⃣ 运行和调试:
# ▶️ 运行程序: Shift + F10
# 🐞 调试程序: Shift + F9
# ⏹️ 停止运行: Ctrl + F2
# ⏩ 单步执行: F8
# ⏪ 进入方法内部: F7
# 🏃 跳出方法内部: Shift + F8
# 4️⃣ 导航和窗口:
# 🔛 跳转到指定行: Ctrl + G
# 🔍 查找: Ctrl + F
# 🔄 替换: Ctrl + R
# 📁 显示/隐藏项目工具窗口: Alt + 1
# 🖥️ 显示/隐藏终端窗口: Alt + F12
# 🔀 切换代码/工程视图: Alt + 1 / Alt + 4


from selenium import webdriver

import time

from selenium.webdriver.common.by import By


class Login:

    def __init__(self,url1='http://xh-test.zhidu30.xinhuimed.net/v3/#/login'):

        self.url1 = url1

    def login(self,username='admin',password='Xh@2022!@#',captcha_code='6666'):
        driver = webdriver.Chrome()
        driver.get(self.url1)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[1]/div/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[2]/div/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[3]/div/input').send_keys(captcha_code)
        driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[4]/button').click()
        time.sleep(8)
        text = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/header/div/h1').text
        driver.quit()
        # if text == False:
        #     print('没有值')
        # else:
        #     print(text)

        return text




if __name__ == '__main__':
    dri = Login()
    dri.login()

