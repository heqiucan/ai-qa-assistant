import os
import sys
import random
import logging

# 获取项目根目录（假设本脚本在 scripts/ 下，根目录是其父目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = os.path.join(LOG_DIR, "weather.log")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def get_weather(city):
    """模拟获取天气（带日志）"""
    logging.info(f"开始查询 {city} 的天气")
    try:
        weather_types = ["晴", "多云", "阴", "小雨", "中雨", "雷阵雨"]
        weather = random.choice(weather_types)
        temperature = random.randint(5, 35)
        logging.info(f"成功获取 {city} 天气：{weather}，温度：{temperature}℃")
        return {"city": city, "weather": weather, "temp": temperature}
    except Exception as e:
        logging.error(f"模拟天气出错：{e}")
        return None

def main():
    logging.info("天气查询程序启动")
    while True:
        city = input("请输入城市名（输入 q 退出）：").strip()
        if city.lower() == 'q':
            logging.info("用户退出程序")
            break
        if not city:
            logging.warning("用户输入为空，请重新输入")
            continue
        result = get_weather(city)
        if result:
            print(f"天气信息：{result}")
        else:
            print("查询失败，请查看日志")

if __name__ == '__main__':
    main()