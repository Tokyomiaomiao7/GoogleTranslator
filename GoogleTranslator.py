#coding=UTF-8
import urllib.request
import urllib.parse
import json
import argparse
import traceback

 
languages = ['zh-CN', 'en', 'de', 'ja', 'ru', 'fr']
 
class GoogleTranslator(object) :
         
        def __init__(self) :
                self.userAgent = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'}
                self.requestUrl = 'http://translate.google.cn'
                self.requestMethod = 'POST'
         
        def requestForTranslate(self, typeDestination, textSource) :
                userAgent = self.userAgent
                #print(userAgent)
                requestUrl = self.requestUrl
                #print(requestUrl)
                requestMethod = self.requestMethod
                #print(requestMethod)
                values = {'client' : 'a', 'sl' : 'auto', 'tl' : typeDestination, 'hl' : 'zh-CN', 'ie' : 'UTF-8', 'oe' : 'UTF-8', 'q' : textSource}
                #print(values)
                data = urllib.parse.urlencode(values).encode('UTF-8')
                #print(data)
                request = urllib.request.Request(url = requestUrl, data = data, headers = userAgent, method = requestMethod)
                #print(request)
                try :                        
                        Recievedtext = urllib.request.urlopen(request).read().decode('utf-8')
                        indx1 = Recievedtext.find('TRANSLATED_TEXT=')
                        indx2 = Recievedtext.find(';INPUT_TOOL_PATH=')
                        trans = Recievedtext[indx1+17:indx2-1]
                        print(trans)
                except :
                        print('翻译失败')
                        #traceback.print_exc()
                        exit()
 
        def main(self) :
                parser = argparse.ArgumentParser(description = 'This is a description of %(prog)s', formatter_class = argparse.ArgumentDefaultsHelpFormatter)
                parser.add_argument('-l', '--lang', dest = 'typeDestination', help = '译文语种', default = 'en')
                parser.add_argument('-t', '--text', dest = 'textSource', help = '待译原文', required = True, nargs = '+')
                args = parser.parse_args()
                #print(args)
                if args.typeDestination not in languages :
                        print('尚不支持该语种')
                        exit()
                typeDestination = args.typeDestination
                textSource = ''
                for text in args.textSource :
                        textSource += text
                        textSource += ' '
                #print(typeDestination)
                #print(textSource)
                self.requestForTranslate(typeDestination, textSource)
 
if __name__ == '__main__' :
        translator = GoogleTranslator()
        translator.main()
