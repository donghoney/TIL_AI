import pandas as pd

def readJson(name):
    try:
        fileName='{}_products.json'.format(name)
        df = pd.read_json(fileName)
        return df
    except:
        print('이름에 맞는 json파일이 없습니다.')


def writeExcel(df,name):
    try:
        fileName = '{}_products.xlsx'.format(name)
        writer=pd.ExcelWriter(fileName)
        df.to_excel(writer,'sheet1')
        writer.save()
    except:
        print('엑셀파일을 저장할 수 없습니다.')

name = '설화수'
df=readJson(name)
writeExcel(df,name)