#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2023/9/24 15:22
Desc: 百度地图慧眼-迁徙城市代码映射
"""

province_dict = {
    "820000": "澳门",
    "810000": "香港",
    "710000": "台湾省",
    "650000": "新疆维吾尔自治区",
    "640000": "宁夏回族自治区",
    "630000": "青海省",
    "620000": "甘肃省",
    "610000": "陕西省",
    "540000": "西藏自治区",
    "530000": "云南省",
    "520000": "贵州省",
    "510000": "四川省",
    "500000": "重庆市",
    "460000": "海南省",
    "450000": "广西壮族自治区",
    "440000": "广东省",
    "430000": "湖南省",
    "420000": "湖北省",
    "410000": "河南省",
    "370000": "山东省",
    "360000": "江西省",
    "350000": "福建省",
    "340000": "安徽省",
    "330000": "浙江省",
    "320000": "江苏省",
    "310000": "上海市",
    "230000": "黑龙江省",
    "220000": "吉林省",
    "210000": "辽宁省",
    "150000": "内蒙古自治区",
    "140000": "山西省",
    "130000": "河北省",
    "120000": "天津市",
    "110000": "北京市",
}

city_dict = {
    "520300": "遵义市",
    "510300": "自贡市",
    "370300": "淄博市",
    "512000": "资阳市",
    "411700": "驻马店市",
    "430200": "株洲市",
    "440400": "珠海市",
    "411600": "周口市",
    "330900": "舟山市",
    "500100": "重庆市",
    "500200": "重庆市",
    "640500": "中卫市",
    "442000": "中山市",
    "410100": "郑州市",
    "321100": "镇江市",
    "441200": "肇庆市",
    "530600": "昭通市",
    "140400": "长治市",
    "430100": "长沙市",
    "220100": "长春市",
    "350600": "漳州市",
    "719007": "彰化县",
    "620700": "张掖市",
    "130700": "张家口市",
    "430800": "张家界市",
    "440800": "湛江市",
    "370400": "枣庄市",
    "140800": "运城市",
    "719008": "云林县",
    "445300": "云浮市",
    "430600": "岳阳市",
    "530400": "玉溪市",
    "632700": "玉树藏族自治州",
    "450900": "玉林市",
    "610800": "榆林市",
    "431100": "永州市",
    "210800": "营口市",
    "360600": "鹰潭市",
    "640100": "银川市",
    "430900": "益阳市",
    "719005": "宜兰县",
    "360900": "宜春市",
    "420500": "宜昌市",
    "511500": "宜宾市",
    "654000": "伊犁哈萨克自治州",
    "230700": "伊春市",
    "140300": "阳泉市",
    "441700": "阳江市",
    "321000": "扬州市",
    "320900": "盐城市",
    "222400": "延边朝鲜族自治州",
    "610600": "延安市",
    "370600": "烟台市",
    "511800": "雅安市",
    "341800": "宣城市",
    "411000": "许昌市",
    "320300": "徐州市",
    "341300": "宿州市",
    "321300": "宿迁市",
    "152200": "兴安盟",
    "130500": "邢台市",
    "411500": "信阳市",
    "719004": "新竹县",
    "719002": "新竹市",
    "360500": "新余市",
    "410700": "新乡市",
    "710300": "新北市",
    "140900": "忻州市",
    "420900": "孝感市",
    "420600": "襄阳市",
    "433100": "湘西土家族苗族自治州",
    "430300": "湘潭市",
    "810000": "香港",
    "610400": "咸阳市",
    "421200": "咸宁市",
    "429004": "仙桃市",
    "152500": "锡林郭勒盟",
    "532800": "西双版纳傣族自治州",
    "630100": "西宁市",
    "610100": "西安市",
    "620600": "武威市",
    "420100": "武汉市",
    "469001": "五指山市",
    "659004": "五家渠市",
    "450400": "梧州市",
    "640300": "吴忠市",
    "340200": "芜湖市",
    "320200": "无锡市",
    "650100": "乌鲁木齐市",
    "150900": "乌兰察布市",
    "150300": "乌海市",
    "532600": "文山壮族苗族自治州",
    "469005": "文昌市",
    "330300": "温州市",
    "610500": "渭南市",
    "370700": "潍坊市",
    "371000": "威海市",
    "469006": "万宁市",
    "469022": "屯昌县",
    "650400": "吐鲁番市",
    "659003": "图木舒克市",
    "520600": "铜仁市",
    "340700": "铜陵市",
    "610200": "铜川市",
    "150500": "通辽市",
    "220500": "通化市",
    "659006": "铁门关市",
    "211200": "铁岭市",
    "620500": "天水市",
    "429006": "天门市",
    "120100": "天津市",
    "710600": "桃园市",
    "130200": "唐山市",
    "321200": "泰州市",
    "370900": "泰安市",
    "140100": "太原市",
    "331000": "台州市",
    "710400": "台中市",
    "710500": "台南市",
    "719012": "台东县",
    "710100": "台北市",
    "654200": "塔城地区",
    "510900": "遂宁市",
    "421300": "随州市",
    "231200": "绥化市",
    "320500": "苏州市",
    "220700": "松原市",
    "220300": "四平市",
    "140600": "朔州市",
    "230500": "双鸭山市",
    "659007": "双河市",
    "640200": "石嘴山市",
    "130100": "石家庄市",
    "659001": "石河子市",
    "420300": "十堰市",
    "210100": "沈阳市",
    "429021": "神农架林区",
    "440300": "深圳市",
    "330600": "绍兴市",
    "430500": "邵阳市",
    "440200": "韶关市",
    "361100": "上饶市",
    "310100": "上海市",
    "411400": "商丘市",
    "611000": "商洛市",
    "441500": "汕尾市",
    "440500": "汕头市",
    "540500": "山南市",
    "350200": "厦门市",
    "460200": "三亚市",
    "460300": "三沙市",
    "350400": "三明市",
    "411200": "三门峡市",
    "371100": "日照市",
    "540200": "日喀则市",
    "350500": "泉州市",
    "530300": "曲靖市",
    "330800": "衢州市",
    "469030": "琼中黎族苗族自治县",
    "469002": "琼海市",
    "621000": "庆阳市",
    "441800": "清远市",
    "370200": "青岛市",
    "130300": "秦皇岛市",
    "450700": "钦州市",
    "522300": "黔西南布依族苗族自治州",
    "522700": "黔南布依族苗族自治州",
    "522600": "黔东南苗族侗族自治州",
    "429005": "潜江市",
    "230200": "齐齐哈尔市",
    "230900": "七台河市",
    "530800": "普洱市",
    "410900": "濮阳市",
    "350300": "莆田市",
    "360300": "萍乡市",
    "719011": "屏东县",
    "620800": "平凉市",
    "410400": "平顶山市",
    "719014": "澎湖县",
    "211100": "盘锦市",
    "510400": "攀枝花市",
    "533300": "怒江傈僳族自治州",
    "350900": "宁德市",
    "330200": "宁波市",
    "511000": "内江市",
    "411300": "南阳市",
    "719009": "南投县",
    "320600": "南通市",
    "350700": "南平市",
    "450100": "南宁市",
    "320100": "南京市",
    "511300": "南充市",
    "360100": "南昌市",
    "540600": "那曲市",
    "231000": "牡丹江市",
    "719006": "苗栗县",
    "510700": "绵阳市",
    "441400": "梅州市",
    "511400": "眉山市",
    "440900": "茂名市",
    "340500": "马鞍山市",
    "141100": "吕梁市",
    "411100": "漯河市",
    "410300": "洛阳市",
    "510500": "泸州市",
    "431300": "娄底市",
    "621200": "陇南市",
    "350800": "龙岩市",
    "520200": "六盘水市",
    "341500": "六安市",
    "450200": "柳州市",
    "469028": "陵水黎族自治县",
    "371300": "临沂市",
    "622900": "临夏回族自治州",
    "469024": "临高县",
    "141000": "临汾市",
    "530900": "临沧市",
    "540400": "林芝市",
    "371500": "聊城市",
    "220400": "辽源市",
    "211000": "辽阳市",
    "513400": "凉山彝族自治州",
    "320700": "连云港市",
    "331100": "丽水市",
    "530700": "丽江市",
    "511100": "乐山市",
    "469027": "乐东黎族自治县",
    "131000": "廊坊市",
    "620100": "兰州市",
    "451300": "来宾市",
    "540100": "拉萨市",
    "659009": "昆玉市",
    "530100": "昆明市",
    "653000": "克孜勒苏柯尔克孜自治州",
    "650200": "克拉玛依市",
    "659008": "可克达拉市",
    "410200": "开封市",
    "653100": "喀什地区",
    "620900": "酒泉市",
    "360400": "九江市",
    "360200": "景德镇市",
    "421000": "荆州市",
    "420800": "荆门市",
    "140700": "晋中市",
    "140500": "晋城市",
    "210700": "锦州市",
    "330700": "金华市",
    "620300": "金昌市",
    "445200": "揭阳市",
    "410800": "焦作市",
    "440700": "江门市",
    "620200": "嘉峪关市",
    "719010": "嘉义县",
    "719003": "嘉义市",
    "330400": "嘉兴市",
    "230800": "佳木斯市",
    "419001": "济源市",
    "370800": "济宁市",
    "370100": "济南市",
    "220200": "吉林市",
    "360800": "吉安市",
    "719001": "基隆市",
    "230300": "鸡西市",
    "441300": "惠州市",
    "420200": "黄石市",
    "341000": "黄山市",
    "632300": "黄南藏族自治州",
    "421100": "黄冈市",
    "340400": "淮南市",
    "340600": "淮北市",
    "320800": "淮安市",
    "431200": "怀化市",
    "719013": "花莲县",
    "330500": "湖州市",
    "211400": "葫芦岛市",
    "150700": "呼伦贝尔市",
    "150100": "呼和浩特市",
    "532500": "红河哈尼族彝族自治州",
    "430400": "衡阳市",
    "131100": "衡水市",
    "231100": "黑河市",
    "230400": "鹤岗市",
    "410600": "鹤壁市",
    "451100": "贺州市",
    "371700": "菏泽市",
    "441600": "河源市",
    "451200": "河池市",
    "653200": "和田地区",
    "340100": "合肥市",
    "330100": "杭州市",
    "610700": "汉中市",
    "130400": "邯郸市",
    "632800": "海西蒙古族藏族自治州",
    "632500": "海南藏族自治州",
    "460100": "海口市",
    "630200": "海东市",
    "632200": "海北藏族自治州",
    "650500": "哈密市",
    "230100": "哈尔滨市",
    "632600": "果洛藏族自治州",
    "450300": "桂林市",
    "520100": "贵阳市",
    "450800": "贵港市",
    "440100": "广州市",
    "510800": "广元市",
    "511600": "广安市",
    "640400": "固原市",
    "710200": "高雄市",
    "360700": "赣州市",
    "513300": "甘孜藏族自治州",
    "623000": "甘南藏族自治州",
    "341200": "阜阳市",
    "210900": "阜新市",
    "361000": "抚州市",
    "210400": "抚顺市",
    "350100": "福州市",
    "440600": "佛山市",
    "450600": "防城港市",
    "422800": "恩施土家族苗族自治州",
    "420700": "鄂州市",
    "150600": "鄂尔多斯市",
    "370500": "东营市",
    "441900": "东莞市",
    "469007": "东方市",
    "621100": "定西市",
    "469021": "定安县",
    "533400": "迪庆藏族自治州",
    "371400": "德州市",
    "510600": "德阳市",
    "533100": "德宏傣族景颇族自治州",
    "460400": "儋州市",
    "210600": "丹东市",
    "232700": "大兴安岭地区",
    "140200": "大同市",
    "230600": "大庆市",
    "210200": "大连市",
    "532900": "大理白族自治州",
    "511700": "达州市",
    "532300": "楚雄彝族自治州",
    "341100": "滁州市",
    "451400": "崇左市",
    "150400": "赤峰市",
    "341700": "池州市",
    "469023": "澄迈县",
    "130800": "承德市",
    "510100": "成都市",
    "431000": "郴州市",
    "445100": "潮州市",
    "211300": "朝阳市",
    "320400": "常州市",
    "430700": "常德市",
    "469026": "昌江黎族自治县",
    "652300": "昌吉回族自治州",
    "540300": "昌都市",
    "130900": "沧州市",
    "652700": "博尔塔拉蒙古自治州",
    "341600": "亳州市",
    "371600": "滨州市",
    "520500": "毕节市",
    "210500": "本溪市",
    "659005": "北屯市",
    "110100": "北京市",
    "450500": "北海市",
    "469029": "保亭黎族苗族自治县",
    "530500": "保山市",
    "130600": "保定市",
    "610300": "宝鸡市",
    "150200": "包头市",
    "340300": "蚌埠市",
    "451000": "百色市",
    "620400": "白银市",
    "220600": "白山市",
    "469025": "白沙黎族自治县",
    "220800": "白城市",
    "511900": "巴中市",
    "652800": "巴音郭楞蒙古自治州",
    "150800": "巴彦淖尔市",
    "820000": "澳门",
    "210300": "鞍山市",
    "410500": "安阳市",
    "520400": "安顺市",
    "340800": "安庆市",
    "610900": "安康市",
    "542500": "阿里地区",
    "654300": "阿勒泰地区",
    "152900": "阿拉善盟",
    "659002": "阿拉尔市",
    "652900": "阿克苏地区",
    "513200": "阿坝藏族羌族自治州",
}
