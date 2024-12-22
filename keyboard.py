import time
from pynput import keyboard

# 配置击键速率 (按键次数/秒)
KPressRate = 10
delay_time = 1 / KPressRate  # 按键间隔时间 (秒)

# 记录上一次按键的时间和键值
last_time = 0
last_key = None

# 按键回调函数
def on_press(key):
    global last_time, last_key

    current_time = time.time()
    key_value = None

    try:
        # 获取按键的值（正常键）
        key_value = key.char
    except AttributeError:
        # 处理特殊按键（例如 Ctrl、Shift 等）
        key_value = str(key)

    # 判断是否是重复按键
    if key_value == last_key and (current_time - last_time) < delay_time:
        print(f"重复按键 {key_value} 被屏蔽")
        return  # 屏蔽按键

    # 记录按键信息
    last_time = current_time
    last_key = key_value

    print(f"按键 {key_value} 被按下")

# 启动键盘监听器
def main():
    print(f"屏蔽时间间隔小于 {delay_time * 1000:.2f} 毫秒的重复按键")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
