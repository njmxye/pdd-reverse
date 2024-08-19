import requests
import json
import execjs
js_code = open('pdd.js',encoding='utf-8').read()
ctx = execjs.compile(js_code)
result = ctx.call('antigain')
url = 'https://pifa.pinduoduo.com/pifa/search/searchOptGoods'
headers = {
  "accept": "*/*",
  "accept-language": "zh-CN,zh;q=0.9",
  "anti-content": result,
  "cache-control": "max-age=0",
  "content-type": "application/json",
  "origin": "https://pifa.pinduoduo.com",
  "priority": "u=1, i",
  "referer": "https://pifa.pinduoduo.com/search?cate=23366&level=2&sn=64658.3322086.1.23366&refer_page_id=64658_1724034821798_a9dcf9297",
  "sec-ch-ua-mobile": "?0",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

cookies={
  "_nano_fp": "XpmxXqEYX0UYX5TJnC_rZLhRsP1l6ZhUYmmi_0cD",
  "webp": "true",
  "api_uid": "CiSla2a+hFBUFgBSMOs5Ag",
  "rckk": "0gk8zcU3Z3ZGrbhCL4wAUCmS8VoiQ9XN",
  "_bee": "0gk8zcU3Z3ZGrbhCL4wAUCmS8VoiQ9XN",
  "ru1k": "3466e8fb-3cc1-4c37-8ca5-85cd270a0b27",
  "_f77": "3466e8fb-3cc1-4c37-8ca5-85cd270a0b27",
  "ru2k": "8aa92f09-afad-4bcd-8c11-a4ed9e48bb32",
  "_a42": "8aa92f09-afad-4bcd-8c11-a4ed9e48bb32",
  "terminalFinger": "sYxt1auV2AiELLncy3NyvfvPrELZprXz",
  "VISITOR_PASS_ID": "sCioRoH9OlxKLgrqvo_ECUQ-PLAsMEWCtN3_Snhy23lKC7zU1iJFz8_CodlzlkcZb2LNfn0JArAvZlzb36Xw_A5QnqAqq47rI_ssJMiJkrY_fc52a9123a"
}

data={
  "page": 2,
  "size": 20,
  "sort": 0,
  "optId": 23366,
  "level": 2,
  "url": "",
  "propertyItems": [],
  "rn": "5149bf86400eb4378f727185408b9f90"
}
data = json.dumps(data, separators=(',', ':'))

# 发送GET请求
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)