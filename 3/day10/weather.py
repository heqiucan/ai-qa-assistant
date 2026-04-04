# day10/weather.py
import random

def get_weather(city):
    weather_types = ["晴", "多云", "阴", "小雨", "中雨", "雷阵雨"]
    weather = random.choice(weather_types)
    temperature = random.randint(5,35)
    print(f"{city}天气：{weather}，温度：{temperature}℃")
    return {"city": city, "weather": weather, "temp": temperature}

if __name__ == "__main__":
    city = input("请输入城市名：")
    get_weather(city)