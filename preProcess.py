import json
import ast
import re

dataset_string = "[{\"attributes\": {\"x\": \"oriolpva:eceb82\", \"y\": \"oriolpva:389241\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"color\": \"#17BECF\"}, \"opacity\": 0.8}}, {\"attributes\": {\"x\": \"oriolpva:eceb82\", \"y\": \"oriolpva:11bf2e\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"color\": \"#7F7F7F\"}, \"opacity\": 0.8}}, {\"attributes\": {\"x\": \"Malc01:e43e72\", \"y\": \"Malc01:dfcfc5\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"marker\": {\"color\": \"rgb(234, 153, 153)\"}}}, {\"attributes\": {\"x\": \"crujones5:66cc6b\", \"y\": \"crujones5:ad63fc\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"crujones5:66cc6b\", \"y\": \"crujones5:277b05\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"teliaklient:474f26\", \"y\": \"teliaklient:ed8385\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"teliaklient:474f26\", \"y\": \"teliaklient:dbec5c\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"teliaklient:474f26\", \"y\": \"teliaklient:e35ee4\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"vpatel74:a4159f\", \"y\": \"vpatel74:437090\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(50,205,50)\"}}}, {\"attributes\": {\"x\": \"vpatel74:a4159f\", \"y\": \"vpatel74:d35832\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(255,69,0)\"}}}, {\"attributes\": {\"x\": \"maragones:4bfaf8\", \"y\": \"maragones:100bf9\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"opacity\": 0.6, \"marker\": {\"line\": {\"color\": \"rgb(8,48,107)\", \"width\": 1.5}, \"color\": \"rgb(158,202,225)\"}}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:e5fa73\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(166,206,227)\"}}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:1c66f7\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(251,154,153)\"}}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:a3d224\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(202,178,214)\"}, \"textsrc\": \"maragones:399:9e750d\"}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:293212\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(253,191,111)\"}}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:774840\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(227,26,28)\"}}}, {\"attributes\": {\"x\": \"maragones:e66500\", \"y\": \"maragones:9c8ea4\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"color\": \"rgb(178,223,138)\"}}}, {\"attributes\": {\"x\": \"erasmocf.ufrgs:c47ad7\", \"y\": \"erasmocf.ufrgs:50dfc7\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 1.3, \"color\": \"rgba(255, 153, 51, 1.0)\", \"dash\": \"solid\"}, \"text\": \"\"}}, {\"attributes\": {\"x\": \"erasmocf.ufrgs:c47ad7\", \"y\": \"erasmocf.ufrgs:b4129c\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 1.3, \"color\": \"rgba(55, 128, 191, 1.0)\", \"dash\": \"solid\"}, \"text\": \"\"}}, {\"attributes\": {\"x\": \"erasmocf.ufrgs:c47ad7\", \"y\": \"erasmocf.ufrgs:85f505\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 1.3, \"color\": \"rgba(50, 171, 96, 1.0)\", \"dash\": \"solid\"}, \"text\": \"\"}}, {\"attributes\": {\"x\": \"erasmocf.ufrgs:c47ad7\", \"y\": \"erasmocf.ufrgs:3a822d\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 1.3, \"color\": \"rgba(128, 0, 128, 1.0)\", \"dash\": \"solid\"}, \"text\": \"\"}}, {\"attributes\": {\"x\": \"erasmocf.ufrgs:c47ad7\", \"y\": \"erasmocf.ufrgs:5f72e9\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 1.3, \"color\": \"rgba(219, 64, 82, 1.0)\", \"dash\": \"solid\"}, \"text\": \"\"}}, {\"attributes\": {\"x\": \"maragones:491ae4\", \"y\": \"maragones:dfc6b2\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"colorsrc\": \"maragones:734:63a603\"}}}, {\"attributes\": {\"x\": \"maragones:2baffc\", \"y\": \"maragones:812fad\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"colorsrc\": \"maragones:732:3f5d8e\"}}}, {\"attributes\": {\"x\": \"manaioussema:e686b8\", \"y\": \"manaioussema:dabae6\"}, \"config\": {\"type\": \"line\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"uid\": \"101b1f\", \"autobiny\": true, \"autobinx\": true}}, {\"attributes\": {\"x\": \"manaioussema:e686b8\", \"y\": \"manaioussema:860206\"}, \"config\": {\"type\": \"line\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"uid\": \"5453da\", \"autobiny\": true, \"autobinx\": true}}, {\"attributes\": {\"x\": \"manaioussema:e686b8\", \"y\": \"manaioussema:180ca6\"}, \"config\": {\"type\": \"line\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"uid\": \"072e93\", \"autobiny\": true, \"autobinx\": true}}, {\"attributes\": {\"x\": \"manaioussema:e686b8\", \"y\": \"manaioussema:58cc9c\"}, \"config\": {\"type\": \"line\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"uid\": \"fe5f05\", \"autobiny\": true, \"autobinx\": true}}, {\"attributes\": {\"x\": \"nestorcgk:1e8c1d\", \"y\": \"nestorcgk:3e83b4\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"colorsrc\": \"nestorcgk:90:51de4a\"}}}, {\"attributes\": {\"x\": \"nestorcgk:1e8c1d\", \"y\": \"nestorcgk:b73740\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"categorical\", \"y-type\": \"quantitative\", \"marker\": {\"colorsrc\": \"nestorcgk:90:e37bd5\"}}}, {\"attributes\": {\"x\": \"itsthejb:178c9f\", \"y\": \"itsthejb:23287e\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"shape\": \"spline\"}, \"connectgaps\": true}}, {\"attributes\": {\"x\": \"itsthejb:178c9f\", \"y\": \"itsthejb:8d0269\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"shape\": \"spline\"}, \"connectgaps\": true}}, {\"attributes\": {\"x\": \"itsthejb:178c9f\", \"y\": \"itsthejb:ce3342\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"shape\": \"spline\"}, \"connectgaps\": true}}, {\"attributes\": {\"x\": \"itsthejb:178c9f\", \"y\": \"itsthejb:fe3748\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"shape\": \"spline\"}, \"connectgaps\": true}}, {\"attributes\": {\"x\": \"nirajd:56dafa\", \"y\": \"nirajd:e842f8\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\"}}, {\"attributes\": {\"x\": \"bharat5005:563563\", \"y\": \"bharat5005:eca0c5\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"bharat5005:563563\", \"y\": \"bharat5005:baf914\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"bharat5005:563563\", \"y\": \"bharat5005:bc109d\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\"}}, {\"attributes\": {\"x\": \"magndahl:b64c45\", \"y\": \"magndahl:90ca3d\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 2.0, \"color\": \"rgba (255, 0, 0, 1)\", \"dash\": \"solid\"}}}, {\"attributes\": {\"x\": \"magndahl:b64c45\", \"y\": \"magndahl:d69c9f\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 2.0, \"color\": \"rgba (0, 0, 0, 1)\", \"dash\": \"solid\"}}}, {\"attributes\": {\"x\": \"magndahl:9f7436\", \"y\": \"magndahl:7b8457\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 2.0, \"color\": \"rgba (0, 0, 0, 1)\", \"dash\": \"solid\"}}}, {\"attributes\": {\"x\": \"magndahl:9f7436\", \"y\": \"magndahl:bf6f61\"}, \"config\": {\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"mode\": \"lines\", \"line\": {\"width\": 2.0, \"color\": \"rgba (255, 0, 0, 1)\", \"dash\": \"solid\"}}}, {\"attributes\": {\"x\": \"penestia:daa77b\", \"y\": \"penestia:0b4c04\"}, \"config\": {\"type\": \"bar\", \"x-type\": \"quantitative\", \"y-type\": \"quantitative\"}}]"
dataset = json.loads(dataset_string)
## if I only have each line as String:
# entry="{\"type\": \"line\", \"x-type\": \"temporal\", \"y-type\": \"quantitative\", \"line\": {\"color\": \"#17BECF\"}, \"opacity\": 0.8}"
# print(type(dataset[0]['config']))
# conv_e=ast.literal_eval(entry)
# print(conv_e,type(conv_e))

txt_data = []


def fillDecimal(sentence, s, index):
    s= str(s).split(".")
    sentence[index]=re.sub('[^0-9]','',str(s[0]))
    sentence[index+1]='.'
    if len(s)>1:
        sentence[index+2]=re.sub('[^0-9]','',str(s[1]))
    else:
        sentence[index+2]=0


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def fillColor(sentence, s, index):
    if s[0] == '#':
        s_conv = hex_to_rgb(s)
    else:
        s_conv=s.split(",")
    sentence[index] = re.sub('[^0-9]','',str(s_conv[0]))
    sentence[index + 1] = re.sub('[^0-9]','',str(s_conv[1]))
    sentence[index + 2] = re.sub('[^0-9]','',str(s_conv[2]))
    if len(s_conv)>3:
        fillDecimal(sentence,s_conv[3],index+3)
    else:
        sentence[index + 3] = 1
        sentence[index + 4] = '.'
        sentence[index + 5] =0


def fillLine(sentence, s, index):
    for key in s:
        idx = -1
        match key:
            case 'width':
                fillDecimal(sentence, s[key], index)
            case 'color':
                fillColor(sentence, s[key], index + 3)
            case 'dash':
                idx = 9
            case 'shape':
                idx = 10
        if idx != -1:
            if s[key] != '':
                sentence[idx + index] = s[key]


def fillMarker(sentence, s):
    for key in s:
        match key:
            case 'line':
                fillLine(sentence, s[key], 18)
            case 'color':
                fillColor(sentence, s[key], 29)
            case 'colorsrc':
                fillSrc(sentence, s[key], 35)


def fillSrc(sentence, s, index):
    s_list = s.split(":")
    sentence[index] = s_list[0]
    sentence[index + 1] = s_list[1]
    sentence[index + 2] = s_list[2]


def convert_to_txt(s):
    sentence = ["/"] * 42
    for key in s:
        idx = -1
        match key:
            case 'type':
                idx = 0
            case 'x-type':
                idx = 1
            case 'y-type':
                idx = 2
            case 'mode':
                idx = 3
            case 'line':
                fillLine(sentence, s[key], 4)
            case 'opacity':
                fillDecimal(sentence,s[key],15)
            case 'marker':
                fillMarker(sentence, s[key])
            case 'txt':
                idx = 38
            case 'textsrc':
                fillSrc(sentence, s[key], 39)
            case _:
                idx = -1

        if idx != -1:
            if s[key] != '':
                sentence[idx] = s[key]
    txt_data.append(' '.join(str(x) for x in sentence))

## for the whole dataset
for i in dataset:
    config = i["config"]
    convert_to_txt(config)

with open(f'./text_dataset.txt', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(txt_data))
