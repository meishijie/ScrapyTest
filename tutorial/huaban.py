#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author :insun
#http://yxmhero1989.blog.163.com/blog/static/112157956201311994027168/
import urllib, urllib2, re, sys, os
reload(sys)


#url = 'http://huaban.com/favorite/'
if(os.path.exists('beauty') == False):
    os.mkdir('beauty')

def get_huaban_beauty():
    pin_id = 48145457
    limit = 20 #他默认允许的limit为100
    while pin_id != None:
        # url = 'http://huaban.com/boards/31435061/?max=' + str(pin_id) + '&limit=' + str(limit) + '&wfl=1'
        url = 'http://huaban.com/boards/31435061/?limit=' + str(limit) + '&wfl=1'
        try:
            i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                         "Connection":"keep-alive",
                         "Referer":"http://huaban.com/boards/31435061/",
                         "Host":"huaban.com",
                         "Connection":"keep-alive",
                         "Accept":"application/json"
                         }
            req = urllib2.Request(url, headers=i_headers)
            html = urllib2.urlopen(req).read()
            # print html
            # reg = re.compile('"pin_id":(.*?),.+?"file":{"farm":"farm1", "bucket":"hbimg",.+?"key":"(.*?)",.+?"type":"image/(.*?)"', re.S)
            reg = re.compile('"pin_id":(.*?),.+?"file":\{"id":.+?"key":(.*?),.+?"type":"image\/(.*?)"', re.S)
            groups = re.findall(reg, html)
            for att in groups:
                pin_id = att[0]
                att_url = att[1][1:-1]
                print att_url
                img_type = att[2]
                img_url = 'http://img.hb.aicdn.com/' + att_url
                print(img_url)
                if(urllib.urlretrieve(img_url, 'beauty/'+att_url+'.'+img_type)):
                    print img_url + '.' + img_type + ' download success!'
                else:
                    print img_url + '.' + img_type + ' save failed'
            return
#print pin_id
        except:
            print 'error occurs'


get_huaban_beauty()