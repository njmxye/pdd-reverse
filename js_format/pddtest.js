const axios = require('axios');
const {antigain} = require('./pdd');
const url = 'https://pifa.pinduoduo.com/pifa/search/searchOptGoods';
const antianti = antigain();
const headers = {
  "accept": "*/*",
  "accept-language": "zh-CN,zh;q=0.9",
  "anti-content": antianti,
  "cache-control": "no-cache",
  "content-type": "application/json",
  "origin": "https://pifa.pinduoduo.com",
  "pragma": "no-cache",
  "priority": "u=1, i",
  "referer": "https://pifa.pinduoduo.com/search?cate=10232&level=2&sn=64658.3322086.0.10232&refer_page_id=64658_1723661851771_e24a1df2b",
  "sec-ch-ua-mobile": "?0",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
};

const data = {
    "page": 1,
    "size": 20,
    "sort": 0,
    "optId": 22224,
    "level": 2,
    "url": "",
    "propertyItems": []
};
let res = axios.post(url, data, headers);
console.log(res);