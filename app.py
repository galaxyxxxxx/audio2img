from flask import Flask, render_template, request, jsonify,redirect, url_for
from werkzeug.utils import secure_filename
import requests
import random
import json
import os
import time
import xlrd
from requests_toolbelt import MultipartEncoder

app = Flask(__name__)

# 语音识别api
ASR_URL = 'https://voice.lenovomm.com/lasf/asr'

def send(ixid, pidx, over, session, voice):
    files = {'voice-data': voice}
    data = {
        'param-data': 'cpf=windows&dtp=iO2S&ver=1.1.9&did=270931c188c281ca&uid=6922073&'
                      'dev=lenovo.ecs.vt&app=com.lenovo.menu_assistant&stm=1494237601458&'
                      'ssm=true&vdm=all&rvr=&sce=long&ntt=wifi&aue=speex-wb;7&'
                      'auf=audio%2FL16%3Brate%3D16000&ixid=' + str(ixid) + '&pidx=' + str(pidx) + '&over=' + str(over)
    }
    header = {
        'lenovokey': 'LENOVO-VOICE-4a817ca65xb7fa574yf252',
        'secretkey': 'BBDAB59701C1CEA201968DFB7E3DAAD7',
        'channel': 'cloudasr'
    }

    response = session.post(ASR_URL, headers=header, data=data, files=files, verify=False, timeout=30)
    print(response.text)
    return response

# 根据语音识别内容 选择图片 
def filter(text):
    word_list=["天空","阳光","云","海","草","花","山","楼","车","路"]
    result=[1 if i in text else 0 for i in word_list]
    keyWords = result
    book = xlrd.open_workbook("./static/image/test.xlsx")
    sheet1 = book.sheet_by_index(0) # 打开索引号为0的表
    scores = {}
    lists = []
    # 读取图片权重分值
    for i in range(sheet1.nrows):
        row = sheet1.row_values(i) # 逐行读取
        scores[row[0]] = [row[1:11]]            
        # 计算加权平均数
    for name in scores:
        total = 0 
        for x in scores[name]:
            for i in range(len(x)):
                total += x[i]*keyWords[i]
                lists.append([name,total])                        
        # 排序
    def takeSecond(elem):
        return elem[1]
    lists.sort(key = takeSecond, reverse = True)    
    tem = lists[0]
    name = tem[0]
    name_num = name[-2:]
    name_num_int = int(name_num)
    nameNum = name_num_int*10 + random.randint(0,3)
    fileName = './static/image/'+'image' + str (nameNum) + '.jpg'
    return fileName


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/receiveAudio', methods=['POST'])
def receiveAudio():
    session = requests.session()
    ixid = int(round(time.time() * 1000))
    pidx = 1
    over = 0
    file = request.files['file'].read()
    
    txt = send(ixid, pidx, 1, session, file).json().get("rawText","") #识别的语音内容
    imgUrl = filter(txt) #对应的图片
    return imgUrl
    

if __name__ == '__main__':
    app.run(debug=True)
