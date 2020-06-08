import sys
from urllib import parse
from urllib.request import urlopen
import simplejson
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

from pytorch_pretrained_bert import BertForTokenClassification

"""
import urllib
 import simplejson

 id = 'KQEOBZLx-Z8'
 url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id

 json = simplejson.load(urllib.urlopen(url))

 title = json['entry']['title']['$t']
 author = json['entry']['author'][0]['name']

 print "id:%s\nauthor:%s\ntitle:%s" % (id, author, title)
 
"""




def subtitle_to_text(subtitle):
    for i in subtitl

if __name__=="__main__":
    # link to video id
    url = sys.argv[1] 
    url = parse.urlparse(url)
    query = parse.parse_qs(url.query)
    video_id = query["v"][0]

    # extract subtitle
    try:
        subtitle = YouTubeTranscriptApi.get_transcript('pXCHYq6PXto', languages = ['en'])
    except:
        try: 
            subtitle = YouTubeTranscriptApi.get_transcript('pXCHYq6PXto', languages = ['ko'])
        except:
            assert False: "영어, 한국어 자막이 없습니다."


    
