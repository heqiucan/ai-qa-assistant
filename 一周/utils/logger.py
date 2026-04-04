import os
import logging

def setup_logger():
    """配置日志：输出到控制台和 logs/weather.log"""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/weather.log"),
            logging.StreamHandler()
        ]
    )