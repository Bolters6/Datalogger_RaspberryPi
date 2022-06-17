from config_letture import toolkit
from flask import Flask, render_template, request
from datetime import datetime
import time
from os import listdir, remove
from os.path import isfile, isdir
import requests
import ftplib


app = Flask(__name__)


tk = toolkit()
tk.Config()
tk.Direction()
datestring = ""
timestring = ""
#tk.Intonoff(0b00000000)
tk.LetturaGPIOPORT()
time.sleep(0.5)

@app.route("/")
def index():

    
    TENSIONIBANK1 = tk.LetturaMapGPIOBK1()
    TENSIONIBANK2 = tk.LetturaMapGPIOBK2()

    now = datetime.now()
    datestring = now.strftime("%d-%m-%Y")
    timestring = now.strftime("%H:%M:%S")
    
    TemplateData = {
            
        'timestr' : timestring,
            'datestr' : datestring,
            'P5V_A1' : TENSIONIBANK1[0],
            'P12V_A1' : TENSIONIBANK1[1],
            'P5V_B1' : TENSIONIBANK1[2],
            'P12V_B1' : TENSIONIBANK1[3],
            'P5V_C1' : TENSIONIBANK1[4],
            'P12V_C1' : TENSIONIBANK1[5],
            'P5V_D1' : TENSIONIBANK1[6],
            'P12V_D1' : TENSIONIBANK1[7],
            'P24V_M1': TENSIONIBANK1[8],
            'P24V_AUS1': TENSIONIBANK1[9],
            'P5V_A2' : TENSIONIBANK1[10],
            'P12V_A2' : TENSIONIBANK1[11],
            'P5V_B2' : TENSIONIBANK1[12],
            'P12V_B2' : TENSIONIBANK1[13],
            'P5V_C2' : TENSIONIBANK1[14],
            'P12V_C2' : TENSIONIBANK1[15],
            'P5V_D2' : TENSIONIBANK1[16],
            'P12V_D2' : TENSIONIBANK1[17],
        'P24V_M2': TENSIONIBANK1[18],
        'P24V_AUS2': TENSIONIBANK1[19],
        'P5V_A3' : TENSIONIBANK1[20],
            'P12V_A3' : TENSIONIBANK1[21],
            'P5V_B3' : TENSIONIBANK1[22],
            'P12V_B3' : TENSIONIBANK1[23],
            'P5V_C3' : TENSIONIBANK1[24],
            'P12V_C3' : TENSIONIBANK1[25],
            'P5V_D3' : TENSIONIBANK1[26],
            'P12V_D3' : TENSIONIBANK1[27],
        'P24V_M3': TENSIONIBANK1[28],
            'P24V_AUS3': TENSIONIBANK1[29],
            'P5V_A4' : TENSIONIBANK1[30],
            'P12V_A4' : TENSIONIBANK1[31],
            'P5V_B4' : TENSIONIBANK1[32],
            'P12V_B4' : TENSIONIBANK1[33],
            'P5V_C4' : TENSIONIBANK1[34],
            'P12V_C4' : TENSIONIBANK1[35],
            'P5V_D4' : TENSIONIBANK1[36],
            'P12V_D4' : TENSIONIBANK1[37],
        'P24V_M4': TENSIONIBANK1[38],
            'P24V_AUS4': TENSIONIBANK1[39],
            'P5V_A5' : TENSIONIBANK1[40],
            'P12V_A5' : TENSIONIBANK1[41],
            'P5V_B5' : TENSIONIBANK1[42],
            'P12V_B5' : TENSIONIBANK1[43],
            'P5V_C5' : TENSIONIBANK1[44],
            'P12V_C5' : TENSIONIBANK1[45],
            'P5V_D5' : TENSIONIBANK1[46],
            'P12V_D5' : TENSIONIBANK1[47],
        'P24V_M5': TENSIONIBANK1[48],
        'P24V_AUS5': TENSIONIBANK1[49],
            'P5V_A6' : TENSIONIBANK1[50],
            'P12V_A6' : TENSIONIBANK1[51],
            'P5V_B6' : TENSIONIBANK1[52],
            'P12V_B6' : TENSIONIBANK1[53],
            'P5V_C6' : TENSIONIBANK1[54],
            'P12V_C6' : TENSIONIBANK1[55],
            'P5V_D6' : TENSIONIBANK1[56],
            'P12V_D6' : TENSIONIBANK1[57],
        'P24V_M6': TENSIONIBANK1[58],
            'P24V_AUS6': TENSIONIBANK1[59],
        'P5V_A11' : TENSIONIBANK2[0],
            'P12V_A11' : TENSIONIBANK2[1],
            'P5V_B11' : TENSIONIBANK2[2],
            'P12V_B11' : TENSIONIBANK2[3],
            'P5V_C11' : TENSIONIBANK2[4],
            'P12V_C11' : TENSIONIBANK2[5],
            'P5V_D11' : TENSIONIBANK2[6],
            'P12V_D11' : TENSIONIBANK2[7],
            'P24V_M11': TENSIONIBANK2[8],
            'P24V_AUS11': TENSIONIBANK2[9],
            'P5V_A12' : TENSIONIBANK2[10],
            'P12V_A12' : TENSIONIBANK2[11],
            'P5V_B12' : TENSIONIBANK2[12],
            'P12V_B12' : TENSIONIBANK2[13],
            'P5V_C12' : TENSIONIBANK2[14],
            'P12V_C12' : TENSIONIBANK2[15],
            'P5V_D12' : TENSIONIBANK2[16],
            'P12V_D12' : TENSIONIBANK2[17],
        'P24V_M12': TENSIONIBANK2[18],
        'P24V_AUS12': TENSIONIBANK2[19],
        'P5V_A10' : TENSIONIBANK2[20],
            'P12V_A10' : TENSIONIBANK2[21],
            'P5V_B10' : TENSIONIBANK2[22],
            'P12V_B10' : TENSIONIBANK2[23],
            'P5V_C10' : TENSIONIBANK2[24],
            'P12V_C10' : TENSIONIBANK2[25],
            'P5V_D10' : TENSIONIBANK2[26],
            'P12V_D10' : TENSIONIBANK2[27],
        'P24V_M10': TENSIONIBANK2[28],
            'P24V_AUS10': TENSIONIBANK2[29],
            'P5V_A9' : TENSIONIBANK2[30],
            'P12V_A9' : TENSIONIBANK2[31],
            'P5V_B9' : TENSIONIBANK2[32],
            'P12V_B9' : TENSIONIBANK2[33],
            'P5V_C9' : TENSIONIBANK2[34],
            'P12V_C9' : TENSIONIBANK2[35],
            'P5V_D9' : TENSIONIBANK2[36],
            'P12V_D9' : TENSIONIBANK2[37],
        'P24V_M9': TENSIONIBANK2[38],
            'P24V_AUS9': TENSIONIBANK2[39],
            'P5V_A8' : TENSIONIBANK2[40],
            'P12V_A8' : TENSIONIBANK2[41],
            'P5V_B8' : TENSIONIBANK2[42],
            'P12V_B8' : TENSIONIBANK2[43],
            'P5V_C8' : TENSIONIBANK2[44],
            'P12V_C8' : TENSIONIBANK2[45],
            'P5V_D8' : TENSIONIBANK2[46],
            'P12V_D8' : TENSIONIBANK2[47],
        'P24V_M8': TENSIONIBANK2[48],
        'P24V_AUS8': TENSIONIBANK2[49],
            'P5V_A7' : TENSIONIBANK2[50],
            'P12V_A7' : TENSIONIBANK2[51],
            'P5V_B7' : TENSIONIBANK2[52],
            'P12V_B7' : TENSIONIBANK2[53],
            'P5V_C7' : TENSIONIBANK2[54],
            'P12V_C7' : TENSIONIBANK2[55],
            'P5V_D7' : TENSIONIBANK2[56],
            'P12V_D7' : TENSIONIBANK2[57],
        'P24V_M7': TENSIONIBANK2[58],
            'P24V_AUS7': TENSIONIBANK2[59],
            
         }  
    
     
    return render_template('index.html', **TemplateData)

@app.route("/fault")
def fault():

    pos = 0
    faultlog = open("/home/pi/Desktop/proyectoempresaconestadoprevio/fault.txt", "r")
    faultlatch = list(faultlog.read())
    for element in faultlatch[:]:
        if element == '0' or element == '1':
            faultlatch[pos] = int(element)
            pos = pos + 1
    faultlog.close()
    now = datetime.now()
    datestring = now.strftime("%d-%m-%Y")
    timestring = now.strftime("%H:%M:%S")

    
    TemplateData = {
            
        'timestr' : timestring,
            'datestr' : datestring,
            'P5V_A1' : faultlatch[0],
            'P12V_A1' : faultlatch[1],
            'P5V_B1' : faultlatch[2],
            'P12V_B1' : faultlatch[3],
            'P5V_C1' : faultlatch[4],
            'P12V_C1' : faultlatch[5],
            'P5V_D1' : faultlatch[6],
            'P12V_D1' : faultlatch[7],
            'P24V_M1': faultlatch[8],
            'P24V_AUS1': faultlatch[9],
            'P5V_A2' : faultlatch[10],
            'P12V_A2' : faultlatch[11],
            'P5V_B2' : faultlatch[12],
            'P12V_B2' : faultlatch[13],
            'P5V_C2' : faultlatch[14],
            'P12V_C2' : faultlatch[15],
            'P5V_D2' : faultlatch[16],
            'P12V_D2' : faultlatch[17],
        'P24V_M2': faultlatch[18],
        'P24V_AUS2': faultlatch[19],
        'P5V_A3' : faultlatch[20],
            'P12V_A3' : faultlatch[21],
            'P5V_B3' : faultlatch[22],
            'P12V_B3' : faultlatch[23],
            'P5V_C3' : faultlatch[24],
            'P12V_C3' : faultlatch[25],
            'P5V_D3' : faultlatch[26],
            'P12V_D3' : faultlatch[27],
        'P24V_M3': faultlatch[28],
            'P24V_AUS3': faultlatch[29],
            'P5V_A4' : faultlatch[30],
            'P12V_A4' : faultlatch[31],
            'P5V_B4' : faultlatch[32],
            'P12V_B4' : faultlatch[33],
            'P5V_C4' : faultlatch[34],
            'P12V_C4' : faultlatch[35],
            'P5V_D4' : faultlatch[36],
            'P12V_D4' : faultlatch[37],
        'P24V_M4': faultlatch[38],
            'P24V_AUS4': faultlatch[39],
            'P5V_A5' : faultlatch[40],
            'P12V_A5' : faultlatch[41],
            'P5V_B5' : faultlatch[42],
            'P12V_B5' : faultlatch[43],
            'P5V_C5' : faultlatch[44],
            'P12V_C5' : faultlatch[45],
            'P5V_D5' : faultlatch[46],
            'P12V_D5' : faultlatch[47],
        'P24V_M5': faultlatch[48],
        'P24V_AUS5': faultlatch[49],
            'P5V_A6' : faultlatch[50],
            'P12V_A6' : faultlatch[51],
            'P5V_B6' : faultlatch[52],
            'P12V_B6' : faultlatch[53],
            'P5V_C6' : faultlatch[54],
            'P12V_C6' : faultlatch[55],
            'P5V_D6' : faultlatch[56],
            'P12V_D6' : faultlatch[57],
        'P24V_M6': faultlatch[58],
            'P24V_AUS6': faultlatch[59],
        'P5V_A11' : faultlatch[60],
            'P12V_A11' : faultlatch[61],
            'P5V_B11' : faultlatch[62],
            'P12V_B11' : faultlatch[63],
            'P5V_C11' : faultlatch[64],
            'P12V_C11' : faultlatch[65],
            'P5V_D11' : faultlatch[66],
            'P12V_D11' : faultlatch[67],
            'P24V_M11': faultlatch[68],
            'P24V_AUS11': faultlatch[69],
            'P5V_A12' : faultlatch[70],
            'P12V_A12' : faultlatch[71],
            'P5V_B12' : faultlatch[72],
            'P12V_B12' : faultlatch[73],
            'P5V_C12' : faultlatch[74],
            'P12V_C12' : faultlatch[75],
            'P5V_D12' : faultlatch[76],
            'P12V_D12' : faultlatch[77],
        'P24V_M12': faultlatch[78],
        'P24V_AUS12': faultlatch[79],
        'P5V_A10' : faultlatch[80],
            'P12V_A10' : faultlatch[81],
            'P5V_B10' : faultlatch[82],
            'P12V_B10' : faultlatch[83],
            'P5V_C10' : faultlatch[84],
            'P12V_C10' : faultlatch[85],
            'P5V_D10' : faultlatch[86],
            'P12V_D10' : faultlatch[87],
        'P24V_M10': faultlatch[88],
            'P24V_AUS10': faultlatch[89],
            'P5V_A9' : faultlatch[90],
            'P12V_A9' : faultlatch[91],
            'P5V_B9' : faultlatch[92],
            'P12V_B9' : faultlatch[93],
            'P5V_C9' : faultlatch[94],
            'P12V_C9' : faultlatch[95],
            'P5V_D9' : faultlatch[96],
            'P12V_D9' : faultlatch[97],
        'P24V_M9': faultlatch[98],
            'P24V_AUS9': faultlatch[99],
            'P5V_A8' : faultlatch[100],
            'P12V_A8' : faultlatch[101],
            'P5V_B8' : faultlatch[102],
            'P12V_B8' : faultlatch[103],
            'P5V_C8' : faultlatch[104],
            'P12V_C8' : faultlatch[105],
            'P5V_D8' : faultlatch[106],
            'P12V_D8' : faultlatch[107],
        'P24V_M8': faultlatch[108],
        'P24V_AUS8': faultlatch[109],
            'P5V_A7' : faultlatch[110],
            'P12V_A7' : faultlatch[111],
            'P5V_B7' : faultlatch[112],
            'P12V_B7' : faultlatch[113],
            'P5V_C7' : faultlatch[114],
            'P12V_C7' : faultlatch[115],
            'P5V_D7' : faultlatch[116],
            'P12V_D7' : faultlatch[117],
        'P24V_M7': faultlatch[118],
            'P24V_AUS7': faultlatch[119],
            
         }
         
    return render_template('Faultlatch.html', **TemplateData) 

@app.route("/impostazioni")
def impostazioni():
    serial1 = ""
    serial2 = ""
    serial3 = ""
    serial4 = ""
    serial5 = ""
    serial6 = ""
    serial7 = ""
    serial8 = ""
    serial9 = ""
    serial10 = ""
    serial11 = ""
    serial12 = ""
    status = []
    operatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/operatore.txt', 'r')
    operaio = operatore.read()
    operatore.close()
    status1 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore1.txt', 'r')
    status.append(status1.read())
    status1.close()
    status2 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore2.txt', 'r')
    status.append(status2.read())
    status2.close()
    status3 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore3.txt', 'r')
    status.append(status3.read())
    status3.close()
    status4 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore4.txt', 'r')
    status.append(status4.read())
    status4.close()
    status5 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore5.txt', 'r')
    status.append(status5.read())
    status5.close()
    status6 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore6.txt', 'r')
    status.append(status6.read())
    status6.close()
    status7 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore7.txt', 'r')
    status.append(status7.read())
    status7.close()
    status8 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore8.txt', 'r')
    status.append(status8.read())
    status8.close()
    status9 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore9.txt', 'r')
    status.append(status9.read())
    status9.close()
    status10 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore10.txt', 'r')
    status.append(status10.read())
    status10.close()
    status11 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore11.txt', 'r')
    status.append(status11.read())
    status11.close()
    status12 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore12.txt', 'r')
    status.append(status12.read())
    status12.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab1.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab2.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab3.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab4.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab5.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab6.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab7.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab8.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab9.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab10.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab11.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab12.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show.txt', 'r')
    status.append(showelement.read())
    showelement.close()
    
    for letter in status[0]:
        if letter == " ":
            break
        serial1 = serial1 + letter
    for letter in status[1]:
        if letter == " ":
            break
        serial2 = serial2 + letter
    for letter in status[2]:
        if letter == " ":
            break
        serial3 = serial3 + letter
    for letter in status[3]:
        if letter == " ":
            break
        serial4 = serial4 + letter
    for letter in status[4]:
        if letter == " ":
            break
        serial5 = serial5 + letter
    for letter in status[5]:
        if letter == " ":
            break
        serial6 = serial6 + letter
    for letter in status[6]:
        if letter == " ":
            break
        serial7 = serial7 + letter
    for letter in status[7]:
        if letter == " ":
            break
        serial8 = serial8 + letter
    for letter in status[8]:
        if letter == " ":
            break
        serial9 = serial9 + letter
    for letter in status[9]:
        if letter == " ":
            break
        serial10 = serial10 + letter
    for letter in status[10]:
        if letter == " ":
            break
        serial11 = serial11 + letter
    for letter in status[11]:
        if letter == " ":
            break
        serial12 = serial12 + letter
        
    TemplateData = {
    
        'operatore': operaio,
        'alimentatore1': status[0],
        'alimentatore2': status[1],
        'alimentatore3': status[2],
        'alimentatore4': status[3],
        'alimentatore5': status[4],
        'alimentatore6': status[5],
        'alimentatore7': status[6],
        'alimentatore8': status[7],
        'alimentatore9': status[8],
        'alimentatore10': status[9],
        'alimentatore11': status[10],
        'alimentatore12': status[11],
        'playone': status[12],
        'playtwo': status[13],
        'playthree': status[14],
        'playfour': status[15],
        'playfive': status[16],
        'playsix': status[17],
        'playseven': status[18],
        'playeight': status[19],
        'playnine': status[20],
        'playten': status[21],
        'playeleven': status[22],
        'playtwelve': status[23],
        'show': status[24],
        'serial1': serial1,
        'serial2': serial2,
        'serial3': serial3,
        'serial4': serial4,
        'serial5': serial5,
        'serial6': serial6,
        'serial7': serial7,
        'serial8': serial8,
        'serial9': serial9,
        'serial10': serial10,
        'serial11': serial11,
        'serial12': serial12,
        
        }
      
    return render_template('impostazioni.html', **TemplateData)

@app.route("/finalreport")
def finalreport():
    
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw1.txt', 'r')
    resultato1 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw2.txt', 'r')
    resultato2 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw3.txt', 'r')
    resultato3 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw4.txt', 'r')
    resultato4 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw5.txt', 'r')
    resultato5 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw6.txt', 'r')
    resultato6 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw7.txt', 'r')
    resultato7 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw8.txt', 'r')
    resultato8 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw9.txt', 'r')
    resultato9 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw10.txt', 'r')
    resultato10 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw11.txt', 'r')
    resultato11 = report.read()
    report.close()
    report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw12.txt', 'r')
    resultato12 = report.read()
    report.close()
    
    TemplateData = {
    'report1' : resultato1,
    'report2' : resultato2,
    'report3' : resultato3,
    'report4' : resultato4,
    'report5' : resultato5,
    'report6' : resultato6,
    'report7' : resultato7,
    'report8' : resultato8,
    'report9' : resultato9,
    'report10' : resultato10,
    'report11' : resultato11,
    'report12' : resultato12,
            }
    return render_template('report.html', **TemplateData)    
      
@app.route("/datalogger")
def datalogger():

    return render_template('datalogger.html')
    
@app.route("/<logfile>/<tipo>")
def Logfile(logfile, tipo):
    linelog = []   
    delete = ""
    serialfile = ""
    for letter in logfile:
        if letter == "_":
            break
        serialfile = serialfile + letter
    if tipo == 'l':
        data = logfile
        datalog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/logs/'+data+".txt", "r")
        with datalog as reader:
            for line in reader:
                linelog.append(line)
        
            datalog.close()
     
        delete = 'logs/'+logfile+'/c'
    
    if tipo == 's':
        data = logfile
        datalog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/SerialLogs/'+data+".txt", "r")
        with datalog as reader:
            for line in reader:
                linelog.append(line)
        
            datalog.close()
    
        delete = 'SerialLogs/'+logfile+'/c'
            
    return render_template('log.html', linelog = linelog, delete = delete, logfile = serialfile)
           
#@app.route("/list")
#def listfiles():
#      i = 0
#      listfile = []
#      listfilewf = []
#      files = [obj for obj in listdir('/home/pi/Desktop/proyectoempresaconestadoprevio/logs/') if isfile('/home/pi/Desktop/proyectoempresaconestadoprevio/logs/' + obj)]
#     for file in files:
#       listfile.append(file)
#       filewf = ""
#       for letter in file:
#         if letter == '.' or letter == 't' or letter == 'x':
#           continue
#         filewf = filewf+letter
#       listfilewf.append(filewf)
#      return  render_template('datalogger.html', listfile = listfile, listfilewf = listfilewf)
      
@app.route("/list/<fileslist>/<tipo>")
def listfiles(fileslist, tipo):
      i = 0
      listfile = []
      listfilewf = []
      files = [obj for obj in listdir('/home/pi/Desktop/proyectoempresaconestadoprevio/'+fileslist+'/') if isfile('/home/pi/Desktop/proyectoempresaconestadoprevio/'+fileslist+'/' + obj)]
      for file in files:
        listfile.append(file)
        filewf = ""
        for letter in file:
          if letter == '.':
            break
          filewf = filewf+letter
        listfilewf.append(filewf)
      return  render_template('datalogger.html', listfile = listfile, listfilewf = listfilewf, fileslist = fileslist, tipo = tipo)
      
@app.route("/<fileslist>/<logfile>/c")
def DeleteFile(fileslist, logfile):
      remove("/home/pi/Desktop/proyectoempresaconestadoprevio/"+fileslist+"/"+logfile+'.txt')
      TemplateData = {
      'delete':"File Cancellato con successo"
      }
      return render_template('datalogger.html', **TemplateData)
      
@app.route("/domanda/<folder>")
def Domanda(folder):
    return render_template('domanda.html', folder = folder)
    
@app.route("/deleteall/<fileslist>")
def DeleteAll(fileslist):
      i = 0
      listfile = []
      files = [obj for obj in listdir('/home/pi/Desktop/proyectoempresaconestadoprevio/'+fileslist+'/') if isfile('/home/pi/Desktop/proyectoempresaconestadoprevio/'+fileslist+'/' + obj)]
      for file in files:
          remove("/home/pi/Desktop/proyectoempresaconestadoprevio/"+fileslist+"/"+file)
      
      TemplateData = {
      'delete':"Files Cancellati con successo"
      }
      return render_template('datalogger.html', **TemplateData)
        
@app.route("/operatore/<name>/<status>")
def operatore(name, status):

    if status == "1":
        operatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/operatore.txt', 'w')
        operatore.write(name)
        operatore.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show.txt', 'w')
        showelement.write('1')
        showelement.close()
    if status == "0":
        operatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/operatore.txt', 'w')
        operatore.write(name)
        operatore.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show.txt', 'w')
        showelement.write('0')
        showelement.close()
    
    return render_template('operatore.html', name=name)
      
@app.route("/play/<serial>/<alimentatore>")
def playrunin(serial, alimentatore):

    status = []
    now = datetime.now()
    datestring = now.strftime("%d-%m-%Y")
    timestring = now.strftime("%H:%M:%S")
    operatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/operatore.txt', 'r')
    operaio = operatore.read()
    operatore.close()
    logalimentatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/SerialLogs/'+serial+"_"+datestring+timestring+".txt", 'a+')
    logalimentatore.write("prodotto FDB360 \n"+
                          "\n"+
                          "Test: Run-in \n"+
                          "Operatore: "+operaio+"\n"+
                          "S/N: "+serial+"\n"+
                          "\n"+
                          "START TEST: Data: "+datestring+" Ora: "+timestring+"\n")
    logalimentatore.close()

    if alimentatore == '1':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status1 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore1.txt', 'w')
        status1.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status1.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab1.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show1.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show2.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw1.txt', 'w')
        report.write(serial+': OK')
        report.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 2) | 0b11110000, 2)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 2) | 0b00111111, 2)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '2':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status2 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore2.txt', 'w')
        status2.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status2.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw2.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab2.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show2.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show3.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 2) | 0b11000000, 2)
        tk.WriteRegistro(0x04, 0b11111111, 3)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '3':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status3 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore3.txt', 'w')
        status3.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status3.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw3.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab3.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show3.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show4.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 1) | 0b11111100, 1)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 2) | 0b00001111, 2)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '4':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status4 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore4.txt', 'w')
        status4.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status4.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw4.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab4.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show4.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show5.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,0b11111111, 3)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 4) | 0b00000011, 4)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '5':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status5 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore5.txt', 'w')
        status5.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status5.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw5.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab5.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show5.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show6.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x04, 0b11111111, 1)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 1) | 0b00000011, 1)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '6':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status6 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore6.txt', 'w')
        status6.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status6.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw6.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab6.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show6.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show7.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 4) | 0b11111100, 4)
        tk.WriteRegistro(0x05, 0b00001111, 4)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '7':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status7 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore7.txt', 'w')
        status7.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status7.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw7.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab7.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show7.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show8.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 6) | 0b11110000, 6)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 6) | 0b00111111, 6)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '8':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status8 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore8.txt', 'w')
        status8.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status8.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw8.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab8.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show8.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show9.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 6) | 0b11000000, 6)
        tk.WriteRegistro(0x04, 0b11111111, 7)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '9':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status9 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore9.txt', 'w')
        status9.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status9.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw9.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab9.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show9.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show10.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 5) | 0b11111100, 5)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 6) | 0b00001111, 6)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '10':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status10 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore10.txt', 'w')
        status10.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status10.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw10.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab10.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show10.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show11.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x05,0b11111111, 7)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 8) | 0b00000011, 8)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '11':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status11 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore11.txt', 'w')
        status11.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status11.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw11.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab11.txt', 'w')
        showelement.write('0')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show11.txt', 'w')
        #showelement.write('0')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show12.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        tk.WriteRegistro(0x04, 0b11111111, 5)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 5) | 0b00000011, 5)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
    if alimentatore == '12':
		tk.LetturaGPIOPORT()
		time.sleep(0.1)
        status12 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore12.txt', 'w')
        status12.write(serial+"_"+datestring+timestring+" "+"RUN IN")
        status12.close()
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw12.txt', 'w')
        report.write(serial+': OK')
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab12.txt', 'w')
        showelement.write('0')
        showelement.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 8) | 0b11111100, 8)
        tk.WriteRegistro(0x05, 0b00001111, 8)
        tk.INTCONChange(0b11111111)
        #time.sleep(0.1)
        tk.INTCONChange(0b00000000)
        time.sleep(0.1)
        
    return render_template("playstop.html", play = "Alimentatore in Run in")
    
@app.route('/stop/<alimentatore>/<serial>')
def stoprunin(alimentatore, serial):
    
    if alimentatore == "alimentatore1":
        status1 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore1.txt', 'w')
        status1.write("RUN IN STOP")
        status1.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 2) & 0b00001111, 2)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 2) & 0b11000000, 2)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw1.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab1.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore2":
        status2 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore2.txt', 'w')
        status2.write("RUN IN STOP")
        status2.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 2) & 0b00111111, 2)
        tk.WriteRegistro(0x04, 0b00000000, 3)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw2.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab2.txt', 'w')
        showelement.write('1')
        showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show1.txt', 'w')
        #showelement.write('1')
        #showelement.close()
        #showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/show2.txt', 'w')
        #showelement.write('0')
        #showelement.close()
    if alimentatore == "alimentatore3":
        status3 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore3.txt', 'w')
        status3.write("RUN IN STOP")
        status3.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 1) & 0b00000011, 1)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 2) & 0b11110000, 2)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw3.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab3.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore4":
        status4 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore4.txt', 'w')
        status4.write("RUN IN STOP")
        status4.close()
        tk.WriteRegistro(0x05, 0b00000000, 3)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 4) & 0b11111100, 4) 
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw4.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab4.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore5":
        status5 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore5.txt', 'w')
        status5.write("RUN IN STOP")
        status5.close()
        tk.WriteRegistro(0x04,0b00000000, 1)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 1) & 0b11111100, 1) 
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw5.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab5.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore6":
        status6 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore6.txt', 'w')
        status6.write("RUN IN STOP")
        status6.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 4) & 0b00000011, 4)
        tk.WriteRegistro(0x05, 0b00000000, 4)  
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw6.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab6.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore7":
        status7 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore7.txt', 'w')
        status7.write("RUN IN STOP")
        status7.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 6) & 0b00001111, 6)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 6) & 0b11000000, 6)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw7.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab7.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore8":
        status8 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore8.txt', 'w')
        status8.write("RUN IN STOP")
        status8.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 6) & 0b00111111, 6)
        tk.WriteRegistro(0x04, 0b00000000, 7)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw8.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab8.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore9":
        status9 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore9.txt', 'w')
        status9.write("RUN IN STOP")
        status9.close()
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 5) & 0b00000011, 5)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 6) & 0b11110000, 6)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw9.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab9.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore10":
        status10 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore10.txt', 'w')
        status10.write("RUN IN STOP")
        status10.close()
        tk.WriteRegistro(0x05, 0b00000000, 7)
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 8) & 0b11111100, 8)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw10.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab10.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore11":
        status11 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore11.txt', 'w')
        status11.write("RUN IN STOP")
        status11.close()
        tk.WriteRegistro(0x04,0b00000000, 5)
        tk.WriteRegistro(0x05,tk.ReadRegistro(0x05, 5) & 0b11111100, 5)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw11.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab11.txt', 'w')
        showelement.write('1')
        showelement.close()
    if alimentatore == "alimentatore12":
        status12 = open('/home/pi/Desktop/proyectoempresaconestadoprevio/alimentatore12.txt', 'w')
        status12.write("RUN IN STOP")
        status12.close()
        tk.WriteRegistro(0x04,tk.ReadRegistro(0x04, 8) & 0b00000011, 8)
        tk.WriteRegistro(0x05, 0b00000000, 8)
        report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw12.txt', 'r')
        resultato = report.read()
        report.close()
        showelement = open('/home/pi/Desktop/proyectoempresaconestadoprevio/abilitazioni/ab12.txt', 'w')
        showelement.write('1')
        showelement.close()
        
    now = datetime.now()
    datestring = now.strftime("%d-%m-%Y")
    timestring = now.strftime("%H:%M:%S")
    logalimentatore = open('/home/pi/Desktop/proyectoempresaconestadoprevio/SerialLogs/'+serial+".txt", 'a+')
    logalimentatore.write("END TEST: "+"Data: "+datestring+" Ora: "+timestring+"\n"+
                          "\n"+ 
                          "Esito: "+resultato+"\n")
    logalimentatore.close()
    
    return render_template("playstop.html", play = "Alimentatore in Stop")
        
if __name__=='__main__':
    app.run(debug = True, port = 8000, host = '0.0.0.0')   



