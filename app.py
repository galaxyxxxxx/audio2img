from flask import Flask, render_template, request, jsonify
import requests
import random
import json
from requests_toolbelt import MultipartEncoder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/receiveAudio', methods=['POST'])
def receiveAudio():

    data = request.get_data()
    print(data)

    # blobUrl = json.dumps(request.get_json())
    # print(blobUrl['arr'])
    # return blobUrl

    # apiUrl = "https://voice.lenovomm.com/lasf/asr"
    # print(blobUrl)
    # params = {
    #     "cpf": "windows",
    #     "dtp": "lenovo",
    #     "ver": "1.0.0",
    #     "did": "90:a4:de:ba:41:a5",
    #     "uid": 123456789,
    #     "dev": "com.lenovo.rt.urc",
    #     "app": "com.lenovo.menu_assistant",
    #     "stm": "1356663021692",
    #     "ssm": "false",
    #     "vdm": "all",
    #     "rvr": "",
    #     "sce": "cmd",
    #     "ntt": "none",
    #     "aue": "speex-wb",
    #     "auf": "audio/L16:rate=16000",
    #     "ixid": random.randint(0, 99999999),
    #     "pidx": 1,
    #     "over": 1,
    #     "key": 123456
    # }
    # pd = ""
    # for k in params:
    #     pd += k + "=" + str(params[k]) + "&"
    # ByteArrayBody byteBody = new ByteArrayBody(byte_array, file.getName());
    # m = MultipartEncoder(fields={"param-data": pd.encode('utf8'), "voice-data": byteBody})
    # headers = {
    #     "content-type": m.content_type,
    #     "User-Agent": "{platform=[android 4.2.0], name=[app.py], version=[1.0]}"
    # }
    # return requests.post(apiUrl, headers=headers, data=m)


if __name__ == '__main__':
    app.run(debug=True)
