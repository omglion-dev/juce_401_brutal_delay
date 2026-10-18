import numpy as np
from brutal_delay import BrutalDelay

def main():
    # 实例化，延迟长度=5
    delay_effect = BrutalDelay(delay_length=5)

    # 构造测试输入
    x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], dtype=np.float64)
    y = np.zeros_like(x)

    # 执行延迟处理
    delay_effect.process(x, y)
    print("output y =", y)

    # 如需重新处理新音频，调用reset清空历史状态
    # delay_effect.reset()
    
if __name__ == "__main__":
    main()
