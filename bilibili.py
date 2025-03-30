import time

def beep(freq=1000, duration=200):
    """通过 /dev/input/by-path 控制蜂鸣器"""
    try:
        with open('/dev/input/by-path/platform-pcspkr-event-spkr', 'wb') as f:
            # 生成蜂鸣信号 (需计算频率和时长)
            # 此处为简化示例，实际需构造 input_event 结构体
            f.write(b'\x01' * 10)  # 触发蜂鸣
            time.sleep(duration / 1000)
            f.write(b'\x00' * 10)  # 停止蜂鸣
    except PermissionError:
        print("权限不足！请用 sudo 运行。")
    except FileNotFoundError:
        print("蜂鸣器设备未找到，请检查 pcspkr 模块是否加载。")

# 调用示例
beep(freq=2000, duration=500)