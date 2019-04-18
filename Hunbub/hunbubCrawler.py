import requests
from bs4 import BeautifulSoup
import re
import urllib

def crawl(eventNo):
    url = 'http://search.ccourt.go.kr/ths/pr/ths_pr0103_P1.do'
    params = {
        'seq':'0',
        'cname':'결정문',
        'eventNum':'57535',
        'eventNo':eventNo,
        'pubFlag':'2',
        'cId':'010500',
        'qrylist':'|',
        'page':'',
        'selectFont':'',
    }
    query=urllib.parse.urlencode(params, encoding='UTF-8', doseq=True)
    result_url = '{}?{}'.format(url,query)
    data=requests.get(result_url)
    print(data.status_code,result_url)

    return data.content

def parse(htmlDoc):
    result = BeautifulSoup(htmlDoc,'html.parser')
    #print(result)
    paras = result.findAll('div',{'class':'para'})
    resultDict={}
    for i in range(0,len(paras)):
        paraSplited=paras[i].text.strip().split()
        print(paraSplited)
        if paraSplited:
            firstWord = paraSplited[0]
            if firstWord=='헌':
                resultDict['hunjae'] = ''.join(paraSplited) #1 헌법재판소
            elif firstWord[-3:]=='재판부':
                resultDict['juche'] = paraSplited[0] #2 주체
            elif firstWord=='결':
                if not paraSplited[-1]=='정':
                    resultDict['gyuljung_y'] = paraSplited[-3].replace('.','')  # 6 결정일(년)
                    resultDict['gyuljung_m'] = paraSplited[-2].replace('.','')  # 7 결정일(월)
                    resultDict['gyuljung_d'] = paraSplited[-1].replace('.','')  # 8 결정일(일)
            elif firstWord=='선' and paraSplited[1]=='고':
                resultDict['sungo_y'] = paraSplited[-3].replace('.', '')  # 6 선고일(년)
                resultDict['sungo_m'] = paraSplited[-2].replace('.', '')  # 7 선고일(월)
                resultDict['sungo_d'] = paraSplited[-1].replace('.', '')  # 8 선고일(일)

            elif firstWord=='사':
                resultDict['sagunnum'] = paraSplited[2]  # 3 사건번호
                resultDict['sagunname'] = ' '.join(paraSplited[3:])  # 4 사건명
            elif firstWord=='청':
                resultDict['chungguin'] = ' '.join(paraSplited[3:]) # 5 청구인
            elif firstWord=='주':
                resultDict['jumoon']= paras[i+1].text.strip() # 9 주문
            elif firstWord=='이' and paraSplited[1]=='유':
                yiyuEndPoint=0
                for j in range(len(paras)):
                    splited=paras[j].text.strip().split()
                    if splited:
                        if splited[0]=='재판장':
                            yiyuEndPoint=j
                            break
                yiyus=paras[i+1:yiyuEndPoint]
                yiyuText = ''
                for yiyu in yiyus:
                    yiyuText += yiyu.text.strip() + '\n'
                resultDict['yiyu']=yiyuText # 10 이유
            elif firstWord=='재판장':
                jepanGwansList=[]
                for i in range(0,len(paraSplited)):
                    t=paraSplited[i]
                    if t=='재판관' and i<len(paraSplited)-1:
                        jepanGwansList.append(paraSplited[i+1])
                    resultDict['jepangwan']=jepanGwansList  # 11 재판관
            elif firstWord=='피':
                resultDict['pichungguin']=' '.join(paraSplited[4:])  # 12 피청구인
            elif firstWord=='당':
                resultDict['danghaesagun']=' '.join(paraSplited[4:])  # 13 당해선고
            elif firstWord=='국선대리인':
                resultDict['kuksundaeriin']=' '.join(paraSplited[1:])   # 14 국선대리
            elif firstWord=='청구인들의':
                resultDict['chunggudaeriin']=' '.join(paraSplited[2:]) # 15 청구인들의 대리인
            elif '(병합)' in firstWord:
                resultDict['byunghabnum']=paraSplited[0]  # 16 병합사건번호
                resultDict['byunghabname']=' '.join(paraSplited[1:]) # 17 병합사건명
            elif firstWord=='대리인':
                resultDict['daeriin']=' '.join(paraSplited[1:]) # 18 대리인
            elif firstWord=='담당변호사':
                resultDict['damdanglayer']=''.join(paraSplited[1:]).split(',') # 19 담당변호사
            #elif re.findall('[(]+([2])+([0])', firstWord):
                #여기는 사건 아래에 (2019헌마341 불기소처분취소) 등으로 적힌 부분을 크롤링하는 부분입니다.
            elif firstWord=='재심대상결정':
                resultDict['jaesimdaesanggyuljung']=' '.join(paraSplited[1:])
                print(paraSplited)
    return resultDict

def main():
    sagunCrawling=True
    gyuljungCrawling=True
    #if sagunCrawling:
    # 사건번호 크롤링 코드 작성해야함. 테이블에서 사건번호 리스트 크롤링하기
    # http://search.ccourt.go.kr/ths/pr/selectThsPr0101List.do 들어가서 post headers 확인하여 작성

    htmlDoc=crawl('2019헌사66')
    resultDict=parse(htmlDoc)
    for key,value in resultDict.items():
        print('key : {} , value : {}'.format(key,value))
    # if gyuljungCrawling:
    #     nvMids = list(df['nvMid'])
    #     global current_nvMid
    #
    #     for nvMid in nvMids:
    #         total_reviews = []
    #         path2 = os.path.join(base_path, '{}_reviews'.format(nvMid))
    #         print(path2)
    #         current_nvMid = nvMid
    #         reviewIndex = int(getReviewIndex(current_nvMid))
    #         review_index_list = [i for i in range(1, reviewIndex + 1)]
    #         with Pool(processes=workers) as pool:
    #             reviewInfos = pool.map(multiprocessing_review_crawl, review_index_list)
    #             for reviewInfo in reviewInfos:
    #                 total_reviews += reviewInfo
    #
    #         print(total_reviews)
    #         file = open(path2 + '.json', 'w+')
    #         file.write(json.dumps(total_reviews))
    #         file.close()
    #     # df=readJson(path2)
    #     # writeExcel(df,path2)


if __name__ =='__main__':
    main()