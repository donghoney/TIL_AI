import pandas as pd

def readJson(path):
    try:
        df = pd.read_json(path+'.json')
        return df
    except Exception as e:
        print('{} json파일을 읽을 수 없음'.format(path+'.json'))


def writeExcel(df,path):
    try:
        writer=pd.ExcelWriter(path+'.xlsx')
        df.to_excel(writer,'sheet1')
        writer.save()
        writer.close()
    except Exception as e:
        print('{} 엑셀을 쓸수 없음'.format(path+'.xlsx'))
