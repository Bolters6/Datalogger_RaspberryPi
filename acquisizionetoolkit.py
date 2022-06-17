from config_letture import toolkit
import RPi.GPIO as GPIO
from datetime import datetime
import time

#comprobazionemodificataultimalatchcambiato
time.sleep(1)
tool = toolkit()
tool.Config()
tool.Direction()
tool.LetturaGPIOPORT()
time.sleep(0.2)
#tool.Intonoff(0b00000000)
time.sleep(1)
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
PIN_INT = 15
PIN_LED = 13
PIN_RESET = 11
PIN_LOG = 31
PIN_LEDGREEN = 29
GPIO.setup(PIN_INT, GPIO.IN)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_LEDGREEN, GPIO.OUT)
GPIO.setup(PIN_RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_LOG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
primalettura = tool.LetturaMapInterruptINTF()
time.sleep(0.1)
faultlog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/fault.txt', 'w')
faultlog.write(str(primalettura))
faultlog.close()

time.sleep(1)
save = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#tool.Intonoff(0b00000000)
#time.sleep(0.1)

def seriallog(alimentatore, datafault):
    
      now = datetime.now()
      datestring = now.strftime("%Y-%m-%d")
      timestring = now.strftime("%H:%M:%S")
      serialalimentatore = ""
      alimentatori = open('/home/pi/Desktop/proyectoempresaconestadoprevio/'+alimentatore+'.txt', 'r')
      serial = alimentatori.read()
      alimentatori.close()
      for letter in serial:
          if letter == " ":
              break
          serialalimentatore = serialalimentatore + letter
      logalimentatore = open("/home/pi/Desktop/proyectoempresaconestadoprevio/SerialLogs/"+serialalimentatore+".txt", 'a+')
      logalimentatore.write('---------------------------------------------------------------------------------------------------------'+'\n'+
                          'DATE:'+datestring+'\n'+
                          'TIME:'+timestring+'\n'+
                          datafault+'\n'+
                          '---------------------------------------------------------------------------------------------------------'+'\n')
      logalimentatore.close()
      if alimentatore == 'alimentatore1':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw1.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore2':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw2.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore3':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw3.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore4':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw4.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore5':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw5.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore6':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw6.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore7':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw7.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore8':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw8.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore9':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw9.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore10':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw10.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore11':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw11.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
      if alimentatore == 'alimentatore12':
          report = open('/home/pi/Desktop/proyectoempresaconestadoprevio/reportfinale/pw12.txt', 'w')
          report.write(serialalimentatore+': FAIL')
          report.close()
          
while True:
    
    pos = 0
    
    if GPIO.input(PIN_RESET) == 0:
        pos = 0
        tool.LetturaRegistroINTCAPAB()
        letturareset = tool.LetturaMapInterruptINTF()
        time.sleep(0.1)
        faultlog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/fault.txt', 'w')
        faultlog.write(str(letturareset))
        faultlog.close()
        GPIO.output(PIN_LED, GPIO.LOW)
        for posreset in range(0, 120):
            save[posreset] = 0

  
        
    GPIO.output(PIN_LEDGREEN, GPIO.HIGH)
        
   
        
   
   
    if GPIO.input(PIN_INT) == 0:
        REGISTROINTF = tool.LetturaMapInterruptINTF()
        tool.LetturaRegistroINTCAPAB()
        now = datetime.now()
        datestring = now.strftime("%Y-%m-%d")
        timestring = now.strftime("%H:%M:%S")
        
        GPIO.output(PIN_LED, GPIO.HIGH)
        
        #faultlatch = tool.LetturaMapInterruptINTCAP()
        for element in REGISTROINTF[:]:
            save[pos] = save[pos] | element
            pos = pos + 1
        if REGISTROINTF[0] == 1:
            datafault = "FAULT:"+" P5V_A1"
            #tool.WriteRegistro(0x04, 0b11101111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[1] == 1:
            datafault = "FAULT:"+" P12V_A1"
            #tool.WriteRegistro(0x04, 0b11011111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[2] == 1:
            datafault = "FAULT:"+" P5V_B1"
            #tool.WriteRegistro(0x04, 0b10111111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[3] == 1:
            datafault = "FAULT:"+" P12V_B1"
            #tool.WriteRegistro(0x04, 0b01111111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[4] == 1:
            datafault = "FAULT:"+" P5V_C1"
            #tool.WriteRegistro(0x05, 0b11111110, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[5] == 1:
            datafault = "FAULT:"+" P12V_C1"
            #tool.WriteRegistro(0x05, 0b11111101, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[6] == 1:
            datafault = "FAULT:"+" P5V_D1"
            #tool.WriteRegistro(0x05, 0b11111011, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[7] == 1:
            datafault = "FAULT:"+" P12V_D1"
            #tool.WriteRegistro(0x05, 0b11110111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[8] == 1:
            datafault = "FAULT:"+" P24V_M1"
            #tool.WriteRegistro(0x05, 0b11101111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[9] == 1:
            datafault = "FAULT:"+" P24V_AUS1"
            #tool.WriteRegistro(0x05, 0b11011111, 2)
            seriallog('alimentatore1', datafault)
        if REGISTROINTF[10] == 1:
            datafault = "FAULT:"+" P5V_A2"
            #tool.WriteRegistro(0x05, 0b10111111, 2)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[11] == 1:
            datafault = "FAULT:"+" P12V_A2"
            #tool.WriteRegistro(0x05, 0b01111111, 2)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[12] == 1:
            datafault = "FAULT:"+" P5V_B2"
            #tool.WriteRegistro(0x04, 0b11111110, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[13] == 1:
            datafault = "FAULT:"+" P12V_B2"
            #tool.WriteRegistro(0x04, 0b11111101, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[14] == 1:
            datafault = "FAULT:"+" P5V_C2"
            #tool.WriteRegistro(0x04, 0b11111011, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[15] == 1:
            datafault = "FAULT:"+" P12V_C2"
            #tool.WriteRegistro(0x04, 0b11110111, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[16] == 1:
            datafault = "FAULT:"+" P5V_D2"
            #tool.WriteRegistro(0x04, 0b11101111, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[17] == 1:
            datafault = "FAULT:"+" P12V_D2"
            #tool.WriteRegistro(0x04, 0b11011111, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[18] == 1:
            datafault = "FAULT:"+" P24V_M2"
            #tool.WriteRegistro(0x04, 0b10111111, 3)
            seriallog('alimentatore2', datafault)
        if REGISTROINTF[19] == 1:
            datafault = "FAULT:"+" P24V_AUS2"
            #tool.WriteRegistro(0x04, 0b01111111, 3)
            seriallog('alimentatore2', datafault)
        if  REGISTROINTF[20] == 1:
            datafault = "FAULT:"+" P5V_A3"
            #tool.WriteRegistro(0x05, 0b11111011, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[21] == 1:
            datafault = "FAULT:"+" P12V_A3"
            #tool.WriteRegistro(0x05, 0b11110111, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[22] == 1:
            datafault = "FAULT:"+" P5V_B3"
            #tool.WriteRegistro(0x05, 0b11101111, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[23] == 1:
            datafault = "FAULT:"+" P12V_B3"
            #tool.WriteRegistro(0x05, 0b11011111, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[24] == 1:
            datafault = "FAULT:"+" P5V_C3"
            #tool.WriteRegistro(0x05, 0b10111111, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[25] == 1:
            datafault = "FAULT:"+" P12V_C3"
            #tool.WriteRegistro(0x05, 0b01111111, 1)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[26] == 1:
            datafault = "FAULT:"+" P5V_D3"
            #tool.WriteRegistro(0x04, 0b11111110, 2)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[27] == 1:
            datafault = "FAULT:"+" P12V_D3"
            #tool.WriteRegistro(0x04, 0b11111101, 2)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[28] == 1:
            datafault = "FAULT:"+" P24V_M3"
            #tool.WriteRegistro(0x04, 0b11111011, 2)
            seriallog('alimentatore3', datafault)
        if REGISTROINTF[29] == 1:
            datafault = "FAULT:"+" P24V_AUS3"
            #tool.WriteRegistro(0x04, 0b11110111, 2)
            seriallog('alimentatore3', datafault)
        if  REGISTROINTF[30] == 1:
            datafault = "FAULT:"+" P5V_A4"
            #tool.WriteRegistro(0x05, 0b11111110, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[31] == 1:
            datafault = "FAULT:"+" P12V_A4"
            #tool.WriteRegistro(0x05, 0b11111101, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[32] == 1:
            datafault = "FAULT:"+" P5V_B4"
            #tool.WriteRegistro(0x05, 0b11111011, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[33] == 1:
            datafault = "FAULT:"+" P12V_B4"
            #tool.WriteRegistro(0x05, 0b11110111, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[34] == 1:
            datafault = "FAULT:"+" P5V_C4"
            #tool.WriteRegistro(0x05, 0b11101111, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[35] == 1:
            datafault = "FAULT:"+" P12V_C4"
            #tool.WriteRegistro(0x05, 0b11011111, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[36] == 1:
            datafault = "FAULT:"+" P5V_D4"
            #tool.WriteRegistro(0x05, 0b10111111, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[37] == 1:
            datafault = "FAULT:"+" P12V_D4"
            #tool.WriteRegistro(0x05, 0b01111111, 3)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[38] == 1:
            datafault = "FAULT:"+" P24V_M4"
            #tool.WriteRegistro(0x04, 0b11111110, 4)
            seriallog('alimentatore4', datafault)
        if REGISTROINTF[39] == 1:
            datafault = "FAULT:"+" P24V_AUS4"
            #tool.WriteRegistro(0x05, 0b11111101, 4)
            seriallog('alimentatore4', datafault)
        if  REGISTROINTF[40] == 1:
            datafault = "FAULT:"+" P5V_A5"
            #tool.WriteRegistro(0x04, 0b11111110, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[41] == 1:
            datafault = "FAULT:"+" P12V_A5"
            #tool.WriteRegistro(0x04, 0b11111101, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[42] == 1:
            datafault = "FAULT:"+" P5V_B5"
            #tool.WriteRegistro(0x04, 0b11111011, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[43] == 1:
            datafault = "FAULT:"+" P12V_B5"
            #tool.WriteRegistro(0x04, 0b11110111, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[44] == 1:
            datafault = "FAULT:"+" P5V_C5"
            #tool.WriteRegistro(0x04, 0b11101111, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[45] == 1:
            datafault = "FAULT:"+" P12V_C5"
            #tool.WriteRegistro(0x04, 0b11011111, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[46] == 1:
            datafault = "FAULT:"+" P5V_D5"
            #tool.WriteRegistro(0x04, 0b10111111, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[47] == 1:
            datafault = "FAULT:"+" P12V_D5"
            #tool.WriteRegistro(0x04, 0b01111101, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[48] == 1:
            datafault = "FAULT:"+" P24V_M5"
            #tool.WriteRegistro(0x05, 0b11111110, 1)
            seriallog('alimentatore5', datafault)
        if REGISTROINTF[49] == 1:
            datafault = "FAULT:"+" P24V_AUS5"
            #tool.WriteRegistro(0x05, 0b11111101, 1)
            seriallog('alimentatore5', datafault)
        if  REGISTROINTF[50] == 1:
            datafault = "FAULT:"+" P5V_A6"
            #tool.WriteRegistro(0x04, 0b11111011, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[51] == 1:
            datafault = "FAULT:"+" P12V_A6"
            #tool.WriteRegistro(0x04, 0b11110111, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[52] == 1:
            datafault = "FAULT:"+" P5V_B6"
            #tool.WriteRegistro(0x04, 0b11101111, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[53] == 1:
            datafault = "FAULT:"+" P12V_B6"
            #tool.WriteRegistro(0x04, 0b11011111, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[54] == 1:
            datafault = "FAULT:"+" P5V_C6"
            #tool.WriteRegistro(0x04, 0b10111111, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[55] == 1:
            datafault = "FAULT:"+" P12V_C6"
            #tool.WriteRegistro(0x04, 0b01111111, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[56] == 1:
            datafault = "FAULT:"+" P5V_D6"
            #tool.WriteRegistro(0x05, 0b11111110, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[57] == 1:
            datafault = "FAULT:"+" P12V_D6"
            #tool.WriteRegistro(0x05, 0b11111101, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[58] == 1:
            datafault = "FAULT:"+" P24V_M6"
            #tool.WriteRegistro(0x05, 0b11111011, 4)
            seriallog('alimentatore6', datafault)
        if REGISTROINTF[59] == 1:
            datafault = "FAULT:"+" P24V_AUS6"
            #tool.WriteRegistro(0x05, 0b11110111, 4)
            seriallog('alimentatore6', datafault)
        if  REGISTROINTF[60] == 1:
            datafault = "FAULT:"+" P5V_A11"
            #tool.WriteRegistro(0x04, 0b11101111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[61] == 1:
            datafault = "FAULT:"+" P12V_A11"
            #tool.WriteRegistro(0x04, 0b11011111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[62] == 1:
            datafault = "FAULT:"+" P5V_B11"
            #tool.WriteRegistro(0x04, 0b10111111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[63] == 1:
            datafault = "FAULT:"+" P12V_B11"
            #tool.WriteRegistro(0x04, 0b01111111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[64] == 1:
            datafault = "FAULT:"+" P5V_C11"
            #tool.WriteRegistro(0x05, 0b11111110, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[65] == 1:
            datafault = "FAULT:"+" P12V_C11"
            #tool.WriteRegistro(0x05, 0b11111101, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[66] == 1:
            datafault = "FAULT:"+" P5V_D11"
            #tool.WriteRegistro(0x05, 0b11111011, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[67] == 1:
            datafault = "FAULT:"+" P12V_D11"
            #tool.WriteRegistro(0x05, 0b11110111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[68] == 1:
            datafault = "FAULT:"+" P24V_M11"
            #tool.WriteRegistro(0x05, 0b11101111, 6)
            seriallog('alimentatore11', datafault)
        if REGISTROINTF[69] == 1:
            datafault = "FAULT:"+" P24V_AUS11"
            #tool.WriteRegistro(0x05, 0b11011111, 6)
            seriallog('alimentatore11', datafault)
        if  REGISTROINTF[70] == 1:
            datafault = "FAULT:"+" P5V_A12"
            #tool.WriteRegistro(0x05, 0b10111111, 6)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[71] == 1:
            datafault = "FAULT:"+" P12V_A12"
            #tool.WriteRegistro(0x05, 0b01111111, 6)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[72] == 1:
            datafault = "FAULT:"+" P5V_B12"
            #tool.WriteRegistro(0x04, 0b11111110, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[73] == 1:
            datafault = "FAULT:"+" P12V_B12"
            #tool.WriteRegistro(0x04, 0b11111101, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[74] == 1:
            datafault = "FAULT:"+" P5V_C12"
            #tool.WriteRegistro(0x04, 0b11111011, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[75] == 1:
            datafault = "FAULT:"+" P12V_C12"
            #tool.WriteRegistro(0x04, 0b11110111, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[76] == 1:
            datafault = "FAULT:"+" P5V_D12"
            #tool.WriteRegistro(0x04, 0b11101111, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[77] == 1:
            datafault = "FAULT:"+" P12V_D12"
            #tool.WriteRegistro(0x04, 0b11011111, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[78] == 1:
            datafault = "FAULT:"+" P24V_M12"
            #tool.WriteRegistro(0x04, 0b10111111, 7)
            seriallog('alimentatore12', datafault)
        if REGISTROINTF[79] == 1:
            datafault = "FAULT:"+" P24V_AUS12"
            #tool.WriteRegistro(0x04, 0b01111111, 7)
            seriallog('alimentatore12', datafault)
        if  REGISTROINTF[80] == 1:
            datafault = "FAULT:"+" P5V_A10"
            #tool.WriteRegistro(0x05, 0b11111011, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[81] == 1:
            datafault = "FAULT:"+" P12V_A10"
            #tool.WriteRegistro(0x05, 0b11110111, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[82] == 1:
            datafault = "FAULT:"+" P5V_B10"
            #tool.WriteRegistro(0x05, 0b11101111, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[83] == 1:
            datafault = "FAULT:"+" P12V_B10"
            #tool.WriteRegistro(0x05, 0b11011111, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[84] == 1:
            datafault = "FAULT:"+" P5V_C10"
            #tool.WriteRegistro(0x05, 0b10111111, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[85] == 1:
            datafault = "FAULT:"+" P12V_C10"
            #tool.WriteRegistro(0x05, 0b01111111, 5)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[86] == 1:
            datafault = "FAULT:"+" P5V_D10"
            #tool.WriteRegistro(0x04, 0b11111110, 6)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[87] == 1:
            datafault = "FAULT:"+" P12V_D10"
            #tool.WriteRegistro(0x04, 0b11111101, 6)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[88] == 1:
            datafault = "FAULT:"+" P24V_M10"
            #tool.WriteRegistro(0x04, 0b11111011, 6)
            seriallog('alimentatore10', datafault)
        if REGISTROINTF[89] == 1:
            datafault = "FAULT:"+" P24V_AUS10"
            #tool.WriteRegistro(0x04, 0b11110111, 6)
            seriallog('alimentatore10', datafault)
        if  REGISTROINTF[90] == 1:
            datafault = "FAULT:"+" P5V_A9"
            #tool.WriteRegistro(0x05, 0b11111110, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[91] == 1:
            datafault = "FAULT:"+" P12V_A9"
            #tool.WriteRegistro(0x05, 0b11111101, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[92] == 1:
            datafault = "FAULT:"+" P5V_B9"
            #tool.WriteRegistro(0x05, 0b11111011, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[93] == 1:
            datafault = "FAULT:"+" P12V_B9"
            #tool.WriteRegistro(0x05, 0b11110111, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[94] == 1:
            datafault = "FAULT:"+" P5V_C9"
            #tool.WriteRegistro(0x05, 0b11101111, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[95] == 1:
            datafault = "FAULT:"+" P12V_C9"
            #tool.WriteRegistro(0x05, 0b11011111, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[96] == 1:
            datafault = "FAULT:"+" P5V_D9"
            #tool.WriteRegistro(0x05, 0b10111111, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[97] == 1:
            datafault = "FAULT:"+" P12V_D9"
            #tool.WriteRegistro(0x05, 0b01111111, 7)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[98] == 1:
            datafault = "FAULT:"+" P24V_M9"
            #tool.WriteRegistro(0x04, 0b11111110, 8)
            seriallog('alimentatore9', datafault)
        if REGISTROINTF[99] == 1:
            datafault = "FAULT:"+" P24V_AUS9"
            #tool.WriteRegistro(0x04, 0b11111101, 8)
            seriallog('alimentatore9', datafault)
        if  REGISTROINTF[100] == 1:
            datafault = "FAULT:"+" P5V_A8"
            #tool.WriteRegistro(0x04, 0b11111110, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[101] == 1:
            datafault = "FAULT:"+" P12V_A8"
            #tool.WriteRegistro(0x04, 0b11111101, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[102] == 1:
            datafault = "FAULT:"+" P5V_B8"
            #tool.WriteRegistro(0x04, 0b11111011, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[103] == 1:
            datafault = "FAULT:"+" P12V_B8"
            #tool.WriteRegistro(0x04, 0b11110111, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[104] == 1:
            datafault = "FAULT:"+" P5V_C8"
            #tool.WriteRegistro(0x04, 0b11101111, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[105] == 1:
            datafault = "FAULT:"+" P12V_C8"
            #tool.WriteRegistro(0x04, 0b11011111, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[106] == 1:
            datafault = "FAULT:"+" P5V_D8"
            #tool.WriteRegistro(0x04, 0b10111111, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[107] == 1:
            datafault = "FAULT:"+" P12V_D8"
            #tool.WriteRegistro(0x04, 0b01111111, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[108] == 1:
            datafault = "FAULT:"+" P24V_M8"
            #tool.WriteRegistro(0x05, 0b11111110, 5)
            seriallog('alimentatore8', datafault)
        if REGISTROINTF[109] == 1:
            datafault = "FAULT:"+" P24V_AUS8"
            #tool.WriteRegistro(0x05, 0b11111101, 5)
            seriallog('alimentatore8', datafault)
        if  REGISTROINTF[110] == 1:
            datafault = "FAULT:"+" P5V_A7"
            #tool.WriteRegistro(0x04, 0b11111011, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[111] == 1:
            datafault = "FAULT:"+" P12V_A7"
            #tool.WriteRegistro(0x04, 0b11110111, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[112] == 1:
            datafault = "FAULT:"+" P5V_B7"
            #tool.WriteRegistro(0x04, 0b11101111, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[113] == 1:
            datafault = "FAULT:"+" P12V_B7"
            #tool.WriteRegistro(0x04, 0b11011111, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[114] == 1:
            datafault = "FAULT:"+" P5V_C7"
            #tool.WriteRegistro(0x04, 0b10111111, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[115] == 1:
            datafault = "FAULT:"+" P12V_C7"
            #tool.WriteRegistro(0x04, 0b01111111, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[116] == 1:
            datafault = "FAULT:"+" P5V_D7"
            #tool.WriteRegistro(0x05, 0b11111110, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[117] == 1:
            datafault = "FAULT:"+" P12V_D7"
            #tool.WriteRegistro(0x05, 0b11111101, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[118] == 1:
            datafault = "FAULT:"+" P24V_M7"
            #tool.WriteRegistro(0x05, 0b11111011, 8)
            seriallog('alimentatore7', datafault)
        if REGISTROINTF[119] == 1:
            datafault = "FAULT:"+" P24V_AUS7"
            #tool.WriteRegistro(0x05, 0b11110111, 8)
            seriallog('alimentatore7', datafault)
            
        faultlog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/fault.txt', 'w')
        faultlog.write(str(save))
        faultlog.close()

    
        datalog = open('/home/pi/Desktop/proyectoempresaconestadoprevio/logs/'+datestring+".txt", 'a+')
        datalog.write('---------------------------------------------------------------------------------------------------------'+'\n'+
                        'DATE:'+datestring+'\n'+
                        'TIME:'+timestring+'\n'+
                        datafault+'\n'+
                        '---------------------------------------------------------------------------------------------------------'+'\n')
        datalog.close()
            
        
       
