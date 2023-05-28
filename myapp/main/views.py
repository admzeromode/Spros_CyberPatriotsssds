from django.shortcuts import render
from . import rasp
from . import var

# Create your views here.

def index(request):
     reis = ['Выберите направление', ]
     date = ['Выберите рейс',]
     class_br = ['Выберите дату',]
     bron_for_user = ['Выберите класс',]
     bron_men_new = []
     period = []
     reis2 = ['Выберите направление', ]
     class_br2 = ['Выберите дату',]
     bron_for_user2 = ['Выберите класс',]
     bron_men_new2 = []
     period2 = []
     x = []
     y = []
     vozv = []
     date_input = '12.01.2018'
     if request.POST.get('bron') == 'Выбрать дату' or request.POST.get('bron1') == 'Найти1':
          if request.POST:
               gor_ot = request.POST.get('gor_ot')
               gor_do = request.POST.get('gor_do')
               reis_input = request.POST.get('reis')
               day = request.POST.get('day')
               mon = request.POST.get('mon')
               year = request.POST.get('year')
               class_br_input = request.POST.get('class_br')
               bron_for_user_start = request.POST.get('bron_for_user_start')
               bron_for_user_end = request.POST.get('bron_for_user_end')
               slov = {'Москва' : 'SVO','Сочи':'AER', 'Астрахань' : 'ASF' }
               month = {'Январь' : '01','Февраль':'02', 'Март' : '03', 'Апрель' : '04', 'Май' : '05', 'Июнь' : '06', 'Июль' : '07', 'Август' : '08', 'Сентябрь' : '09', 'Октябрь' : '10', 'Ноябрь' : '11', 'Декабрь' : '12'}
               int_bron = []
               if gor_ot in slov.keys():
                    aer_ot = slov[gor_ot]
               if gor_do in slov.keys():
                    aer_do = slov[gor_do]
               if mon in month.keys():
                    mon_new = month[mon]
               true_dat = day + '.' + mon_new + '.' + year

               data = rasp.databron(mon_new,year,aer_ot, aer_do,reis_input,true_dat,class_br_input,bron_for_user_start,bron_for_user_end)
               reis = data[2] 
               date = data[3] 
               class_br = data[4]
               bron_for_user = data[5]
               bron_men_new = data[6]
               period = data[7]

     if  request.POST.get('bron2') == 'Найти2':
          if request.POST:
               gor_ot = request.POST.get('gor_ot2')
               gor_do = request.POST.get('gor_do2')
               reis_input = request.POST.get('reis2')
               class_br_input = request.POST.get('class_br2')
               bron_for_user_start = request.POST.get('bron_for_user_start2')
               bron_for_user_end = request.POST.get('bron_for_user_end2')
               slov = {'Москва' : 'SVO','Сочи':'AER', 'Астрахань' : 'ASF' }
               month = {'Январь' : '01','Февраль':'02', 'Март' : '03', 'Апрель' : '04', 'Май' : '05', 'Июнь' : '06', 'Июль' : '07', 'Август' : '08', 'Сентябрь' : '09', 'Октябрь' : '10', 'Ноябрь' : '11', 'Декабрь' : '12'}
               if gor_ot in slov.keys():
                    aer_ot = slov[gor_ot]
               if gor_do in slov.keys():
                    aer_do = slov[gor_do]
               data = rasp.databron2(aer_ot, aer_do,reis_input,class_br_input,bron_for_user_start,bron_for_user_end)
               reis2 = data[2] 
               class_br2 = data[3]
               bron_for_user2 = data[4]
               bron_men_new2 = data[5]
               period2 = data[6]
               int_bron = []
               if period2 != [] and bron_men_new != []:
                    for i in bron_men_new2:
                         new = int(i)
                         int_bron.append(new)
                    data2,data3,data4 = var.poisk_sezonov([period2, int_bron], 10, 10)
                    x = []
                    y = []
                    vozv = []
                    for i in data2:
                         for j in i:
                              print('x:',j[0][0])
                              print('y:',j[0][1])
                              print('Возвышение:',j[1][1])
                              x.append(j[0][0])
                              y.append(j[0][1])
                              vozv.append(j[1][1])
     context = {
     'reis': reis,'reis2': reis2, 'date': date , 'class_br' : class_br, 'class_br2' : class_br2, 'bron_for_user' : bron_for_user,'bron_for_user2' : bron_for_user2,
       'bron_men_new' : bron_men_new, 'bron_men_new2' : bron_men_new2,'date_input' : date_input, 'period' : period, 'period2' : period2, 'x' : x, 'y' : y, 'vozv' : vozv,
     }       
     return render(request, 'main/index.html', context)

