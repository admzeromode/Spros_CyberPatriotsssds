import csv
import datetime 
from datetime import timedelta
import numpy as np 
import os

def databron(mon_new,year,aer_ot, aer_do,reis_input,true_dat,class_br_input,bron_for_user_start,bron_for_user_end): 
    ff = os.getcwd()
    file = ff+'dd'
    file = f'./dataset/CLASS_{mon_new}{year}.csv' # тут необходимо указатьрасположение датасета
    with open(file, encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ";"
        file_reader = csv.DictReader(r_file, delimiter = ";")
        # Считывание данных из CSV файла
        reis = []
        date = []
        d_do_v = []
        class_br = []
        bron = []
        bron_for_user = []
        bron_men = []
        for row in file_reader:
            # Вывод строк
            if (aer_ot == row["SORG"]) and (aer_do == row["SDST"]):
                #print(f' {row["LEG_ORIG"]},{row["LEG_DEST"]}', end='')
                #print(row["FLT_NUMSH"])
                reis.append(row["FLT_NUM"])
            
            else: 
                list_res = 0
            try:
                if (reis_input == row["FLT_NUM"]) and (aer_ot == row["SORG"]) and (aer_do == row["SDST"]):
                    #print('Дата полета-',row["DD"],':',"Кол-во дней до вылета-",row["DTD"]) 
                    date.append(row['DD'])
                    d_do_v.append(row['DTD'])
            except:
                reis_input = 0
            
            
            
            try:
                if (true_dat == row["DD"]) and (aer_ot == row["SORG"]) and (aer_do == row["SDST"]) and (reis_input == row["FLT_NUM"]) and (row["PASS_BK"] != '0'):
                    class_br.append(row["SEG_CLASS_CODE"])
            except:
                true_dat = 0
            
            
            
            try:
                if (class_br_input == row["SEG_CLASS_CODE"]) and(true_dat == row["DD"]) and (aer_ot == row["SORG"]) and (aer_do == row["SDST"]) and (reis_input == row["FLT_NUM"]) and (row["PASS_BK"] != '0'):
                    bron_for_user.append(row["SDAT_S"])
                    bron_men.append(row['PASS_BK'])
                    bron.append(datetime.datetime.strptime(row["SDAT_S"], "%d.%m.%Y"))
                
            except:
                class_br_input = 0
        period = [] 
        try:
                start_date = (datetime.datetime.strptime(bron_for_user_start, "%d.%m.%Y"))
                end_date = (datetime.datetime.strptime(bron_for_user_end, "%d.%m.%Y"))    
                delta = end_date - start_date   
                for i in range(delta.days + 1):
                    day = start_date + timedelta(days=i)
                    date_new = day.strftime('%d.%m.%Y')
                    period.append(date_new)  
        except:
            bron_for_user_start = 0
            bron_for_user_end = 0
        bron_men_new = []
        slov = dict(zip(bron_for_user,bron_men))
        for i in period:
            if i in slov.keys():
                us_men = slov[i]
                bron_men_new.append(us_men)
        set_reis = set(reis)
        list_res = list(set_reis)

        set_date = set(date)
        list_date = list(set_date)
        
        set_class = set(class_br) 
        list_class = list(set_class)
        
        
    return(aer_ot, aer_do,list_res, list_date, list_class,bron_for_user,bron_men_new,period)


def databron2(aer_ot, aer_do,reis_input,class_br_input,bron_for_user_start,bron_for_user_end): 
    list_class_global = []
    bron_for_user__global = []
    bron_men_new__global = []
    period_global = []
    list_res_global = []
    mon_new = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in mon_new:
        file = f'main/dataset/CLASS_{i}2018.csv'
        with open(file, encoding='utf-8') as r_file:
            # Создаем объект DictReader, указываем символ-разделитель ";"
            file_reader = csv.DictReader(r_file, delimiter = ";")
            # Считывание данных из CSV файла
            reis = []
            class_br = []
            bron = []
            bron_for_user = []
            bron_men = []
            for row in file_reader:
                # Вывод строк
                if (aer_ot == row["SORG"]) and (aer_do == row["SDST"]):
                    #print(f' {row["LEG_ORIG"]},{row["LEG_DEST"]}', end='')
                    #print(row["FLT_NUMSH"])
                    reis.append(row["FLT_NUM"])
                
                else: 
                    list_res = 0
                
                
                try:
                    if  (aer_ot == row["SORG"]) and (aer_do == row["SDST"]) and (reis_input == row["FLT_NUM"]):
                        class_br.append(row["SEG_CLASS_CODE"])
                except:
                    true_dat = 0
                
                
                
                try:
                    if (class_br_input == row["SEG_CLASS_CODE"])  and (aer_ot == row["SORG"]) and (aer_do == row["SDST"]) and (reis_input == row["FLT_NUM"]):
                        bron_for_user.append(row["SDAT_S"])
                        bron_men.append(row['PASS_BK'])
                        bron.append(datetime.datetime.strptime(row["SDAT_S"], "%d.%m.%Y"))
                    
                except:
                    class_br_input = 0
            period = [] 
            try:
                    start_date = (datetime.datetime.strptime(bron_for_user_start, "%d.%m.%Y"))
                    end_date = (datetime.datetime.strptime(bron_for_user_end, "%d.%m.%Y"))    
                    delta = end_date - start_date   
                    for i in range(delta.days + 1):
                        day = start_date + timedelta(days=i)
                        date_new = day.strftime('%d.%m.%Y')
                        period.append(date_new)  
            except:
                bron_for_user_start = 0
                bron_for_user_end = 0
            bron_men_new = []
            slov = dict(zip(bron_for_user,bron_men))
            for i in period:
                if i in slov.keys():
                    us_men = slov[i]
                    bron_men_new.append(us_men)
            set_reis = set(reis)
            list_res = list(set_reis)

            set_class = set(class_br) 
            list_class = list(set_class)
            list_class_global.append(list_class)
            bron_for_user__global.append(bron_for_user)
            bron_men_new__global.append(bron_men_new)
            period_global.append(period)
            list_res_global.append(list_res)
    class_glob = [item for sublist in list_class_global for item in sublist]
    reis_glob = [item for sublist in list_res_global for item in sublist]
    bron_for_user__glob = [item for sublist in bron_for_user__global for item in sublist]
    bron_men_new__glob = [item for sublist in bron_men_new__global for item in sublist]
    period_glob = [item for sublist in period_global for item in sublist]
    set_rs_gl = set(reis_glob) 
    list_rs_gl = list(set_rs_gl)
    set_cl_gl = set(class_glob) 
    list_cl_gl = list(set_cl_gl)
    set_for_gl = set(bron_for_user__glob) 
    list_for_gl = list(set_for_gl)
    period2 = [] 
    try:
            start_date = (datetime.datetime.strptime(bron_for_user_start, "%d.%m.%Y"))
            end_date = (datetime.datetime.strptime(bron_for_user_end, "%d.%m.%Y"))    
            delta = end_date - start_date   
            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i)
                date_new = day.strftime('%d.%m.%Y')
                period2.append(date_new)  
    except:
        bron_for_user_start = 0
        bron_for_user_end = 0
    bron_men_new2= []
    slov = dict(zip(bron_for_user__glob,bron_men_new__glob))
    for i in period2:
        if i in slov.keys():
            us_men = slov[i]
            bron_men_new2.append(us_men)

    

    return(aer_ot, aer_do,list_rs_gl, list_cl_gl,list_for_gl,bron_men_new2,period2)