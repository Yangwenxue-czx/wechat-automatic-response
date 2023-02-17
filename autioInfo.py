from pywinauto.application import Application
import  keyboard
import time
import re
import uiautomation as auto
import psutil
import io

def autoReplat(ToName):
    wx_chat_in = wx_xin.child_window(title=ToName, control_type="ListItem")
    wx_msg_input = wx_xin.child_window(title="输入", control_type="Edit")

    unRead = False
    try:
        if wx_chat_in.child_window(title="1", control_type="Text").Exists:
            unRead = True
    except:
        unRead = False

    if unRead:
        wx_chat_in.click_input()
        wx_msg_input.click_input()

        chat = wx_xin.child_window(title="消息", control_type="List")
        wechatWindow = auto.WindowControl(searchDepth=1, Name="微信", ClassName='WeChatMainWndForPC')
        messages = wechatWindow.ListControl(Name='消息')
        chat = []
        for message in messages.GetChildren():
            content = message.Name
            if re.match("[0-9]+:[0-9]+", str(content)) is None:
                if content.find("撤回了一条消息") == -1:
                    chat.append(content)

        keyboard.write(chat[-1] + "这是机器人回复（正在测试自动回复机器人")
        keyboard.send('enter')

        wx_chat_in = wx_xin.child_window(title="文件传输助手", control_type="ListItem")
        wx_chat_in.click_input()

if __name__ == '__main__':

    # wx_path = r'D:\Program Files (x86)\Tencent\WeChat\WeChat.exe'
    wx_path = r'D:\WeChat\WeChat.exe'
    print("请输入微信的安装路径：如 D:\WeChat\WeChat.exe")
    keys = input()

    wx_app = Application(backend='uia').start(keys)
    process = psutil.process_iter()
    processId = 0
    for pro in process:
        if pro.name() == "WeChat.exe":
            process = pro.pid
    if processId == 0:
        print("未找到微信")
        exit()

    wx_app = Application(backend='uia').connect(process=760)

    list = ['需要回复的微信名']
    while 1 :
        wx_xin = wx_app.window(class_name='WeChatMainWndForPC')
        haveMessage = False
        try:
            if wx_xin.child_window(title="1", control_type="Text").Exists:
                haveMessage = True
        except:
            haveMessage = False

        if haveMessage:
            for i in list:
                autoReplat(i)
