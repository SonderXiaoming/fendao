import json
import os

stage_dict = {"A":1,"B":2,"C":3,"D":4,"E":5}

def lap2stage(lap_num):
    if lap_num in range(4):
        stage = 'A'
    elif lap_num in range(4,11):
        stage = 'B'
    elif lap_num in range(11,35):
        stage = 'C'
    elif lap_num in range(35,45):
        stage = 'D'
    else:
        stage = 'E'
    return stage

async def load_config(path):
    try:
        with open(path, encoding='utf8') as f:
            config = json.load(f)
            return config
    except:
        return []

async def create_path(path):
    folder = os.path.exists(path)
    if not folder:                 
        os.makedirs(path)