import os
import random 
import logging
if not os.path.exists('logs'):
    os.mkdir('logs')
logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/weather.log"),
            logging.StreamHandler()
                 ]
                       )


def get_weather(city):
    """模拟获取天气（带异常处理和日志）"""
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
        city=input("请输入城市名(输入q退出):").strip()
        if city.lower()=='q':
            logging.info("用户退出程序")
            break
        if not city:
            logging.warning("用户输出为空,请重新输入")
            continue
        result=get_weather(city)
        if result:
            print(f"天气信息:{result}")
        else:
            print("查询失败，请查看日志")
if __name__=='__main__':
    main()

