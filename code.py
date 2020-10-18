import requests
    while  True:
        string = input("请输入一段要翻译的文字:")
        data = {'doctpye':'json','tpye':'AUTO','i':string}
        url = 'http://fangyi.youdao.com/translate'
        r = requests.get(url,params= date)
        result = r.json()
        print(result['translateResult'][0][0]['tgt'])