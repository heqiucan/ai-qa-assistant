import random
import logging

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