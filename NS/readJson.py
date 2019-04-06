import pandas as pd

def readJson(name):
    try:
        path='./{}.json'.format(name)
        df = pd.read_json(path)
        return df
    except Exception as e:
        print('json파일을 읽을 수 없음',e)


def writeExcel(df,name):
    try:
        path = './{}.xlsx'.format(name)
        writer=pd.ExcelWriter(path)
        df.to_excel(writer,'sheet1')
        writer.save()
    except Exception as e:
        print('엑셀을 쓸수 없음',e)
