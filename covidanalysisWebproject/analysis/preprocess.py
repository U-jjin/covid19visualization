import csv

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt;

from config.settings import DATA_DIRS
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/gulim.ttc"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font) ## 그래프를 알아보기위해 폰트 설정

df = pd.read_excel(DATA_DIRS[0]+'\\data1.xlsx',engine='openpyxl');
areacode = pd.read_excel(DATA_DIRS[0]+'\\areacode.xlsx',engine='openpyxl');
df2 = pd.read_excel(DATA_DIRS[0]+'\\gamgi.xlsx',engine='openpyxl');
df3 = pd.read_excel(DATA_DIRS[0]+'\\chunsik.xlsx',engine='openpyxl');
df7 = pd.read_excel(DATA_DIRS[0]+'\\smartwork_exp1.xlsx',engine='openpyxl');
df8 = pd.read_excel(DATA_DIRS[0]+'\\smartwork_exp2.xlsx',engine='openpyxl');
df10 = pd.read_excel(DATA_DIRS[0]+'\\hospitaldata.xlsx',engine='openpyxl');

class preprocess:
    def gamgi(self):
        df2.columns =['날짜','지역코드','발생건수'];
        # print(df);
        areacode.columns=['지역코드','지역명'];
        # print(areacode);
        mg = pd.merge(df2,areacode); # 지역코드-지역명 파일과 연결
        # result = mg.set_index(mg['날짜']);
        new_result = mg[mg['지역코드']==99]; # 99(전국) 데이터만 추출
        del new_result['지역코드'];
        new_result.reset_index(drop=True,inplace=True); ## 인덱스 재설정
        new_result = new_result.iloc[2069:];  # 필요한 날짜만 잘라내기 20190901~20200930(index:2464)
        # print(new_result);
        # ------ 월별로 잘라야할곳 -----

        new_result = new_result.sort_values(by='날짜', ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);

        new_result['날짜'] = pd.to_datetime(new_result['날짜'], format='%Y%m%d', errors='ignore');
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        new_result['월'] = new_result['날짜'].dt.to_period(freq='M');
        # print(new_result)
        # new_result = new_result.set_index(new_result['월']);
        new_data = new_result.groupby(by='월',axis=0).sum()
        # print(type(new_data.index.tolist()[0]))
        # print(new_data);
        # ---------------------
        catg = list(map(str,new_data.index.tolist()));
        # print(catg);
        d1 = new_data['발생건수'].tolist();
        fresult = {};
        fresult['catg'] = catg;
        fresult['d1'] = d1;
        # print(fresult);
        # print(name)
        return fresult;
    def gamgi_new(self):
        df2.columns =['날짜','지역코드','발생건수'];
        # print(df);
        areacode.columns=['지역코드','지역명'];
        # print(areacode);
        mg = pd.merge(df2,areacode); # 지역코드-지역명 파일과 연결
        # result = mg.set_index(mg['날짜']);
        new_result = mg[mg['지역코드']==99]; # 99(전국) 데이터만 추출
        del new_result['지역코드'];
        new_result.reset_index(drop=True,inplace=True); ## 인덱스 재설정
        # print(new_result);
        # ------ 월별로 잘라야할곳 -----

        new_result = new_result.sort_values(by='날짜', ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);

        new_result['날짜'] = pd.to_datetime(new_result['날짜'], format='%Y%m%d', errors='ignore');
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        new_result['월'] = new_result['날짜'].dt.to_period(freq='M');
        # print(new_result)
        # new_result = new_result.set_index(new_result['월']);
        new_data = new_result.groupby(by='월',axis=0).sum()
        # print(type(new_data.index.tolist()[0]))
        # print(new_data);
        new_data14 = new_data.loc['2014'];
        new_data15 = new_data.loc['2015'];
        new_data16 = new_data.loc['2016'];
        new_data17 = new_data.loc['2017'];
        new_data18 = new_data.loc['2018'];
        new_data19 = new_data.loc['2019'];
        new_data20 = new_data.loc['2020'];
        # print(new_data14)
        d14 = new_data14['발생건수'].tolist();
        d15 = new_data15['발생건수'].tolist();
        d16 = new_data16['발생건수'].tolist();
        d17 = new_data17['발생건수'].tolist();
        d18 = new_data18['발생건수'].tolist();
        d19 = new_data19['발생건수'].tolist();
        d20 = new_data20['발생건수'].tolist();
        fresult = {};
        fresult['d14'] = d14;
        fresult['d15'] = d15;
        fresult['d16'] = d16;
        fresult['d17'] = d17;
        fresult['d18'] = d18;
        fresult['d19'] = d19;
        fresult['d20'] = d20;
        # print(fresult);
        return fresult;
    def chunsik(self):
        df3.columns = ['날짜', '지역코드', '발생건수'];
        # print(df);
        areacode.columns = ['지역코드', '지역명'];
        # print(areacode);
        mg = pd.merge(df3, areacode);
        result = mg.set_index(mg['날짜']);
        new_result = result[result['지역코드'] == 99]
        del new_result['지역코드'];
        new_result.reset_index(drop=True, inplace=True);  ## 인덱스 재설정
        new_result = new_result.iloc[2069:];  # 필요한 날짜만 잘라내기 20190901~20200930(index:2464)
        # print(new_result);
        # ------ 월별로 잘라야할곳 -----

        new_result = new_result.sort_values(by='날짜', ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);

        new_result['날짜'] = pd.to_datetime(new_result['날짜'], format='%Y%m%d', errors='ignore');
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        new_result['월'] = new_result['날짜'].dt.to_period(freq='M');
        # print(new_result)
        # new_result = new_result.set_index(new_result['월']);
        new_data = new_result.groupby(by='월', axis=0).sum()
        # print(type(new_data.index.tolist()[0]))
        # print(new_data);
        # ---------------------
        catg = list(map(str, new_data.index.tolist()));
        # print(catg);
        d1 = new_data['발생건수'].tolist();
        fresult = {};
        fresult['catg'] = catg;
        fresult['d1'] = d1;
        print(fresult);
        return fresult;
    def smartwork(self):
        df7.columns = ['년도','재택근무','영상회의'];
        exp1 = df7.set_index(df7['년도']);
        df8.columns = ['년도','재택근무','영상회의'];
        exp2 = df8.set_index(df7['년도']);
        # print(exp1,exp2);
        e1 = exp1['재택근무'].tolist();
        e2 = exp1['영상회의'].tolist();
        e3 = exp2['재택근무'].tolist();
        e4 = exp2['영상회의'].tolist();
        result = {};
        result['e1'] = e1;
        result['e2'] = e2;
        result['e3'] = e3;
        result['e4'] = e4;
        print(result);
        return result;
    def hospital(self):
        df10.columns = ['인허가일자','영업상태','휴업시작일','폐업일자','주소'];
        # print(df10.info());
        df10['영업상태'].fillna('영업중', inplace=True);
        # df10['휴업시작일'].fillna('x',inplace=True);
        # df10['폐업일자'].fillna('x', inplace=True);

        # hu_data = df10.copy();
        # hup = [];
        # h_data = hu_data['휴업시작일'].tolist();
        # for i in range(0,len(h_data)):
        #     if h_data[i] != 'x':
        #         h = h_data[i];
        #         hup.append(h);
        # print(hup);
        # print(len(hup));
        # hup2 = [];
        # for j in range(0,len(hup)):
        #     if hup[j] >= 20200000:
        #         l= hup[j]
        #         hup2.append(l)
        # print(hup2);
        # print(len(hup2));
        # # ----------------------------------
        # pe_data = df10.copy();
        # ped = [];
        # p_data = pe_data['폐업일자'].tolist();
        # for i in range(0, len(p_data)):
        #     if p_data[i] != 'x':
        #         p = p_data[i];
        #         ped.append(p);
        # print(ped);
        # print(len(ped));
        # ped2 = [];
        # for j in range(0, len(ped)):
        #     if ped[j] >= 20200000:
        #         l = ped[j]
        #         ped2.append(l)
        # print(ped2);
        # print(len(ped2));
        # ----------전체주소,도로명주소 합체시도-----------
        # a_data = df10[['전화번호','주소','도로명주소']];
        # print(a_data.info()); # 6462 , 5461 , 6326

        # a = df10['주소'].str.split(expand=True)[0];
        # b = df10['도로명주소'].str.split(expand=True)[0];
        # c = [];
        # print(type(a[0]),type(b[0]))
        # if np.isnan(b[0]):
        #     print('p')
        # for i in range(0,len(b)):
        #     if np.isnan(b[i]):
        #         c[i] = a[i]
        #     else:
        #         c[i] = b[i]
        # print(c.info())
        # ---------------------------------
        ad = df10['주소'].str.split(expand=True)[0]
        new_data = pd.concat([df10[['인허가일자','휴업시작일','폐업일자']],ad],axis=1)
        new_data.columns = ['인허가일자','휴업시작일','폐업일자', '주소']
        # print(new_data)
        for i in range(0,len(new_data['인허가일자'])):
            if new_data['인허가일자'][i] == 19000101:
                new_data = new_data.drop(i,axis=0);

        new_data = new_data.sort_values(by='인허가일자',ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);
        new_data['인허가일자'] = pd.to_datetime(new_data['인허가일자'],format='%Y%m%d', errors='ignore');
        # print(new_data);
        # pr_day = new_data['인허가일자'].dt.to_period(freq='D');
        # print(pr_day);
        # pr_month = new_data['인허가일자'].dt.to_period(freq='M');
        # print(pr_month);
        # pr_year = new_data['인허가일자'].dt.to_period(freq='A');
        # print(pr_year);
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        # new_data['월'] = new_data['인허가일자'].dt.to_period(freq='M');
        new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);
        # n_data = new_data.groupby(by='주소',axis=0).count();
        # print(n_data);
        new_data_y21 = new_data['2021'];  ## 여기 year 변수로 바꾸면 특정년도 데이터추출가능
        new_data_y20 = new_data['2020'];
        new_data_y19 = new_data['2019'];
        new_data_y18 = new_data['2018'];
        new_data_y17 = new_data['2017'];
        new_data_y16 = new_data['2016'];
        # print(new_data_y);
        # new_data_ym = new_data.loc['2021-01'];
        # print(new_data_ym);
        data_2021 = new_data_y21.groupby(by='주소', axis=0).count();
        data_2020 = new_data_y20.groupby(by='주소', axis=0).count();
        data_2019 = new_data_y19.groupby(by='주소', axis=0).count();
        data_2018 = new_data_y18.groupby(by='주소', axis=0).count();
        data_2017 = new_data_y17.groupby(by='주소', axis=0).count(); # 제주도 누락
        data_2016 = new_data_y16.groupby(by='주소', axis=0).count(); # 세종 누락
        print(data_2017);
        print(data_2016);
        # print(data_2021['인허가일자'].sum());

        # print(data_2021.index)
        # print(data_2021.loc['강원도'].tolist());
        catg = data_2020.index.tolist();
        d21 = data_2021['인허가일자'].tolist();
        d20 = data_2020['인허가일자'].tolist();
        d19 = data_2019['인허가일자'].tolist();
        d18 = data_2018['인허가일자'].tolist();
        d17 = data_2017['인허가일자'].tolist();
        d16 = data_2016['인허가일자'].tolist();
        # d21.append(int(data_2021['인허가일자'].sum()));
        # d20.append(int(data_2020['인허가일자'].sum()));
        # d19.append(int(data_2019['인허가일자'].sum()));
        # d18.append(int(data_2018['인허가일자'].sum()));
        # d17.append(int(data_2017['인허가일자'].sum()));
        # d16.append(int(data_2016['인허가일자'].sum()));
        # catg.append('전국');
        # print(catg);
        result = {};
        result['catg'] = catg;
        result['d21'] = d21;
        result['d20'] = d20;
        result['d19'] = d19;
        result['d18'] = d18;
        result['d17'] = d17;
        result['d16'] = d16;

        # print(result);
        return result;

    def hospital_h(self):
        df10.columns = ['인허가일자', '영업상태', '휴업시작일', '폐업일자', '주소'];
        df10['영업상태'].fillna('영업중', inplace=True);

        ad = df10['주소'].str.split(expand=True)[0]
        new_data = pd.concat([df10[['인허가일자', '휴업시작일', '폐업일자']], ad], axis=1)
        new_data.columns = ['인허가일자', '휴업시작일', '폐업일자', '주소']
        # print(new_data)
        for i in range(0, len(new_data['인허가일자'])): ## 19000101로 설정된 데이터 삭제
            if new_data['인허가일자'][i] == 19000101:
                new_data = new_data.drop(i, axis=0);

        new_data = new_data.dropna(axis=0, subset=['휴업시작일']); # na값 제거
        new_data = new_data.sort_values(by='휴업시작일', ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);

        new_data['휴업시작일'] = pd.to_datetime(new_data['휴업시작일'], format='%Y%m%d', errors='ignore');
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        # new_data['월'] = new_data['인허가일자'].dt.to_period(freq='M');
        new_data = new_data.set_index(new_data['휴업시작일']);
        print(new_data);
        # n_data = new_data.groupby(by='주소',axis=0).count();
        # print(n_data);
        new_data_y21 = new_data['2021'];  ## 여기 year 변수로 바꾸면 특정년도 데이터추출가능
        new_data_y20 = new_data['2020'];
        new_data_y19 = new_data['2019'];
        new_data_y18 = new_data['2018'];
        new_data_y17 = new_data['2017'];
        new_data_y16 = new_data['2016'];
        # print(new_data_y);
        # new_data_ym = new_data.loc['2021-01'];
        # print(new_data_ym);
        data_2021 = new_data_y21.groupby(by='주소', axis=0).count();
        data_2020 = new_data_y20.groupby(by='주소', axis=0).count();
        data_2019 = new_data_y19.groupby(by='주소', axis=0).count();
        data_2018 = new_data_y18.groupby(by='주소', axis=0).count();
        data_2017 = new_data_y17.groupby(by='주소', axis=0).count();
        data_2016 = new_data_y16.groupby(by='주소', axis=0).count();
        print(data_2020);
        # print(data_2021.index)
        # print(data_2021.loc['강원도'].tolist());
        catg = data_2020.index.tolist();
        d21 = data_2021['휴업시작일'].tolist();
        d20 = data_2020['휴업시작일'].tolist();
        d19 = data_2019['휴업시작일'].tolist();
        d18 = data_2018['휴업시작일'].tolist();
        d17 = data_2017['휴업시작일'].tolist();
        d16 = data_2016['휴업시작일'].tolist();
        result = {};
        result['catg'] = catg;
        result['d21'] = d21;
        result['d20'] = d20;
        result['d19'] = d19;
        result['d18'] = d18;
        result['d17'] = d17;
        result['d16'] = d16;
        # print(result);
        return result;
    def hospital_p(self):
        df10.columns = ['인허가일자', '영업상태', '휴업시작일', '폐업일자', '주소'];
        df10['영업상태'].fillna('영업중', inplace=True);

        ad = df10['주소'].str.split(expand=True)[0]
        new_data = pd.concat([df10[['인허가일자', '휴업시작일', '폐업일자']], ad], axis=1)
        new_data.columns = ['인허가일자', '휴업시작일', '폐업일자', '주소']
        # print(new_data)
        for i in range(0, len(new_data['인허가일자'])): ## 19000101로 설정된 데이터 삭제
            if new_data['인허가일자'][i] == 19000101:
                new_data = new_data.drop(i, axis=0);

        new_data = new_data.dropna(axis=0, subset=['폐업일자']); # na값 제거
        new_data = new_data.sort_values(by='폐업일자', ascending=False)
        # new_data = new_data.set_index(new_data['인허가일자']);
        # print(new_data);

        new_data['폐업일자'] = pd.to_datetime(new_data['폐업일자'], format='%Y%m%d', errors='ignore');
        # new_data['년'] = new_data['인허가일자'].dt.to_period(freq='A');
        # new_data['월'] = new_data['인허가일자'].dt.to_period(freq='M');
        new_data = new_data.set_index(new_data['폐업일자']);
        print(new_data);
        # n_data = new_data.groupby(by='주소',axis=0).count();
        # print(n_data);
        new_data_y21 = new_data['2021'];  ## 여기 year 변수로 바꾸면 특정년도 데이터추출가능
        new_data_y20 = new_data['2020'];
        new_data_y19 = new_data['2019'];
        new_data_y18 = new_data['2018'];
        new_data_y17 = new_data['2017'];
        new_data_y16 = new_data['2016'];
        # print(new_data_y);
        # new_data_ym = new_data.loc['2021-01'];
        # print(new_data_ym);
        data_2021 = new_data_y21.groupby(by='주소', axis=0).count();
        data_2020 = new_data_y20.groupby(by='주소', axis=0).count();
        data_2019 = new_data_y19.groupby(by='주소', axis=0).count();
        data_2018 = new_data_y18.groupby(by='주소', axis=0).count();
        data_2017 = new_data_y17.groupby(by='주소', axis=0).count();
        data_2016 = new_data_y16.groupby(by='주소', axis=0).count();
        print(data_2020);
        # print(data_2021.index)
        # print(data_2021.loc['강원도'].tolist());
        catg = data_2020.index.tolist();
        d21 = data_2021['폐업일자'].tolist();
        d20 = data_2020['폐업일자'].tolist();
        d19 = data_2019['폐업일자'].tolist();
        d18 = data_2018['폐업일자'].tolist();
        d17 = data_2017['폐업일자'].tolist();
        d16 = data_2016['폐업일자'].tolist();
        result = {};
        result['catg'] = catg;
        result['d21'] = d21;
        result['d20'] = d20;
        result['d19'] = d19;
        result['d18'] = d18;
        result['d17'] = d17;
        result['d16'] = d16;
        # print(result);
        return result;

if __name__ == '__main__':
    preprocess().gamgi_new();