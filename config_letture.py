from RPiMCP23S17.MCP23S17 import MCP23S17
import time
import spidev

class toolkit(object):

    def __init__(self):
        spi = spidev.SpiDev()
        spi.open(0, 0)
        spi.max_speed_hz = 500000
        self.mcp1 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x00)
        self.mcp2 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x01)
        self.mcp3 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x02)
        self.mcp4 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x03)
        self.mcp5 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x04)
        self.mcp6 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x05)
        self.mcp7 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x06)
        self.mcp8 = MCP23S17(bus=0x00, pin_cs=0x00, device_id=0x07)
        
        self.mcp1.open()
        self.mcp2.open()
        self.mcp3.open()
        self.mcp4.open()
        self.mcp5.open()        
        self.mcp6.open()
        self.mcp7.open()
        self.mcp8.open()
       
                
    def Config(self):
        
        
        self.mcp1._writeRegister(0x0A, 0b00001100)
        self.mcp2._writeRegister(0x0A, 0b00001100)
        self.mcp3._writeRegister(0x0A, 0b00001100)
        self.mcp4._writeRegister(0x0A, 0b00001100)
        self.mcp5._writeRegister(0x0A, 0b00001100)
        self.mcp6._writeRegister(0x0A, 0b00001100)
        self.mcp7._writeRegister(0x0A, 0b00001100)
        self.mcp8._writeRegister(0x0A, 0b00001100)
        self.mcp1._writeRegister(0x0B, 0b00001100)
        self.mcp2._writeRegister(0x0B, 0b00001100)
        self.mcp3._writeRegister(0x0B, 0b00001100)
        self.mcp4._writeRegister(0x0B, 0b00001100)
        self.mcp5._writeRegister(0x0B, 0b00001100)
        self.mcp6._writeRegister(0x0B, 0b00001100)
        self.mcp7._writeRegister(0x0B, 0b00001100)
        self.mcp8._writeRegister(0x0B, 0b00001100)

        self.mcp1._writeRegister(0x04, 0b00000000)
        self.mcp2._writeRegister(0x04, 0b00000000)
        self.mcp3._writeRegister(0x04, 0b00000000)
        self.mcp4._writeRegister(0x04, 0b00000000)
        self.mcp5._writeRegister(0x04, 0b00000000)
        self.mcp6._writeRegister(0x04, 0b00000000)
        self.mcp7._writeRegister(0x04, 0b00000000)
        self.mcp8._writeRegister(0x04, 0b00000000)
        self.mcp1._writeRegister(0x05, 0b00000000)
        self.mcp2._writeRegister(0x05, 0b00000000)
        self.mcp3._writeRegister(0x05, 0b00000000)
        self.mcp4._writeRegister(0x05, 0b00000000)
        self.mcp5._writeRegister(0x05, 0b00000000)
        self.mcp6._writeRegister(0x05, 0b00000000)
        self.mcp7._writeRegister(0x05, 0b00000000)
        self.mcp8._writeRegister(0x05, 0b00000000)
        
        self.mcp1._writeRegister(0x08, 0b00000000)
        self.mcp2._writeRegister(0x08, 0b00000000)
        self.mcp3._writeRegister(0x08, 0b00000000)
        self.mcp4._writeRegister(0x08, 0b00000000)
        self.mcp5._writeRegister(0x08, 0b00000000)
        self.mcp6._writeRegister(0x08, 0b00000000)
        self.mcp7._writeRegister(0x08, 0b00000000)
        self.mcp8._writeRegister(0x08, 0b00000000)
        self.mcp1._writeRegister(0x09, 0b00000000)
        self.mcp2._writeRegister(0x09, 0b00000000)
        self.mcp3._writeRegister(0x09, 0b00000000)
        self.mcp4._writeRegister(0x09, 0b00000000)
        self.mcp5._writeRegister(0x09, 0b00000000)
        self.mcp6._writeRegister(0x09, 0b00000000)
        self.mcp7._writeRegister(0x09, 0b00000000)
        self.mcp8._writeRegister(0x09, 0b00000000)
        
                
        self.mcp1._writeRegister(0x06, 0b00000000)
        self.mcp2._writeRegister(0x06, 0b00000000)
        self.mcp3._writeRegister(0x06, 0b00000000)
        self.mcp4._writeRegister(0x06, 0b00000000)
        self.mcp5._writeRegister(0x06, 0b00000000)
        self.mcp6._writeRegister(0x06, 0b00000000)
        self.mcp7._writeRegister(0x06, 0b00000000)
        self.mcp8._writeRegister(0x06, 0b00000000)
        self.mcp1._writeRegister(0x07, 0b00000000)
        self.mcp2._writeRegister(0x07, 0b00000000)
        self.mcp3._writeRegister(0x07, 0b00000000)
        self.mcp4._writeRegister(0x07, 0b00000000)
        self.mcp5._writeRegister(0x07, 0b00000000)
        self.mcp6._writeRegister(0x07, 0b00000000)
        self.mcp7._writeRegister(0x07, 0b00000000)
        self.mcp8._writeRegister(0x07, 0b00000000)
        
    def INTCONChange(self, val):

        self.mcp1._writeRegister(0x08, val)
        self.mcp2._writeRegister(0x08, val)
        self.mcp3._writeRegister(0x08, val)
        self.mcp4._writeRegister(0x08, val)
        self.mcp5._writeRegister(0x08, val)
        self.mcp6._writeRegister(0x08, val)
        self.mcp7._writeRegister(0x08, val)
        self.mcp8._writeRegister(0x08, val)
        self.mcp1._writeRegister(0x09, val)
        self.mcp2._writeRegister(0x09, val)
        self.mcp3._writeRegister(0x09, val)
        self.mcp4._writeRegister(0x09, val)
        self.mcp5._writeRegister(0x09, val)
        self.mcp6._writeRegister(0x09, val)
        self.mcp7._writeRegister(0x09, val)
        self.mcp8._writeRegister(0x09, val)

    def Direction(self):
                
        for x in range(0, 16):
            self.mcp1.setDirection(x, self.mcp1.DIR_INPUT)
            self.mcp2.setDirection(x, self.mcp2.DIR_INPUT)
            self.mcp3.setDirection(x, self.mcp3.DIR_INPUT)
            self.mcp4.setDirection(x, self.mcp4.DIR_INPUT)
            self.mcp5.setDirection(x, self.mcp5.DIR_INPUT)
            self.mcp6.setDirection(x, self.mcp6.DIR_INPUT)
            self.mcp7.setDirection(x, self.mcp7.DIR_INPUT)
            self.mcp8.setDirection(x, self.mcp8.DIR_INPUT)


    def LetturaGPIOPORT(self):
        GPIOPORTAB1 = self.mcp1.readGPIO()
        GPIOPORTAB2 = self.mcp2.readGPIO()
        GPIOPORTAB3 = self.mcp3.readGPIO()
        GPIOPORTAB4 = self.mcp4.readGPIO()
        GPIOPORTAB5 = self.mcp5.readGPIO()
        GPIOPORTAB6 = self.mcp6.readGPIO()
        GPIOPORTAB7 = self.mcp7.readGPIO()
        GPIOPORTAB8 = self.mcp8.readGPIO()
 #       print(GPIOPORTAB1)
  #      print('1')
   #     print(GPIOPORTAB2)
    #    print('2')
     #   print(GPIOPORTAB3)
      #  print('3')
       # print(GPIOPORTAB4)
        #print('4')
        #print(GPIOPORTAB5)
        #print('5')
        #print(GPIOPORTAB6)
        #print('6')
        #print(GPIOPORTAB7)
        #print('7')
        #print(GPIOPORTAB8)
        #print('8')
#        print(self.mcp1._readRegister(0x0A), self.mcp2._readRegister(0x0A), self.mcp3._readRegister(0x0A) ,self.mcp4._readRegister(0x0A), self.mcp5._readRegister(0x0A), self.mcp6._readRegister(0x0A), self.mcp7._readRegister(0x0A), self.mcp8._readRegister(0x0A))
 #       print('A')
  #      print(self.mcp1._readRegister(0x0B), self.mcp2._readRegister(0x0B), self.mcp3._readRegister(0x0B) ,self.mcp4._readRegister(0x0B), self.mcp5._readRegister(0x0B), self.mcp6._readRegister(0x0B), self.mcp7._readRegister(0x0B), self.mcp8._readRegister(0x0B))
        
        return( GPIOPORTAB1, GPIOPORTAB2, GPIOPORTAB3, GPIOPORTAB4, GPIOPORTAB5, GPIOPORTAB6, GPIOPORTAB7, GPIOPORTAB8)



    def LetturaRegistroINTCAPAB(self):
        INTCAPA1 = self.mcp1._readRegister(0x10)
        INTCAPA2 = self.mcp2._readRegister(0x10)
        INTCAPA3 = self.mcp3._readRegister(0x10)
        INTCAPA4 = self.mcp4._readRegister(0x10)
        INTCAPA5 = self.mcp5._readRegister(0x10)
        INTCAPA6 = self.mcp6._readRegister(0x10)
        INTCAPA7 = self.mcp7._readRegister(0x10)
        INTCAPA8 = self.mcp8._readRegister(0x10)
        INTCAPB1 = self.mcp1._readRegister(0x11)
        INTCAPB2 = self.mcp2._readRegister(0x11)
        INTCAPB3 = self.mcp3._readRegister(0x11)
        INTCAPB4 = self.mcp4._readRegister(0x11)
        INTCAPB5 = self.mcp5._readRegister(0x11)
        INTCAPB6 = self.mcp6._readRegister(0x11)
        INTCAPB7 = self.mcp7._readRegister(0x11)
        INTCAPB8 = self.mcp8._readRegister(0x11)
        return(INTCAPA1,INTCAPB1,INTCAPA2,INTCAPB2,INTCAPA3,INTCAPB3,INTCAPA4,INTCAPB4,INTCAPA5,INTCAPB5,INTCAPA6,INTCAPB6,INTCAPA7,INTCAPB7,INTCAPA8,INTCAPB8)

    def LetturaRegistroINTFAB(self):
        INTFA1 = self.mcp1._readRegister(0x0E)
        INTFA2 = self.mcp2._readRegister(0x0E)
        INTFA3 = self.mcp3._readRegister(0x0E)
        INTFA4 = self.mcp4._readRegister(0x0E)
        INTFA5 = self.mcp5._readRegister(0x0E)
        INTFA6 = self.mcp6._readRegister(0x0E)
        INTFA7 = self.mcp7._readRegister(0x0E)
        INTFA8 = self.mcp8._readRegister(0x0E)
        INTFB1 = self.mcp1._readRegister(0x0F)
        INTFB2 = self.mcp2._readRegister(0x0F)
        INTFB3 = self.mcp3._readRegister(0x0F)
        INTFB4 = self.mcp4._readRegister(0x0F)
        INTFB5 = self.mcp5._readRegister(0x0F)
        INTFB6 = self.mcp6._readRegister(0x0F)
        INTFB7 = self.mcp7._readRegister(0x0F)
        INTFB8 = self.mcp8._readRegister(0x0F)
        return(INTFA1,INTFB1,INTFA2,INTFB2,INTFA3,INTFB3,INTFA4,INTFB4,INTFA5,INTFB5,INTFA6,INTFB6,INTFA7,INTFB7,INTFA8,INTFB8)   

    def LetturaMapGPIOBK1(self):
                
                GPIOPORTVAL = []
                MCP1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                pos = 0

                
                GPIOPORTVAL = self.LetturaGPIOPORT()
               
                for bitelement in list(bin(GPIOPORTVAL[0])[2:].zfill(16)):
                        MCP1[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[1])[2:].zfill(16)):
                        MCP2[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[2])[2:].zfill(16)):
                        MCP3[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[3])[2:].zfill(16)):
                        MCP4[15-pos] = int(bitelement)^1
                        pos = pos + 1

                P5V_A5 = MCP1[0]
                P12V_A5 = MCP1[1]
                P5V_B5 = MCP1[2]
                P12V_B5 = MCP1[3]
                P5V_C5 = MCP1[4]
                P12V_C5 = MCP1[5]
                P5V_D5 = MCP1[6]
                P12V_D5 = MCP1[7]
                P24V_M5 = MCP1[8]
                P24V_AUS5 = MCP1[9]
                P5V_A3 = MCP1[10]
                P12V_A3 = MCP1[11]
                P5V_B3 = MCP1[12]
                P12V_B3 = MCP1[13]
                P5V_C3 = MCP1[14]
                P12V_C3 = MCP1[15]
                P5V_D3 = MCP2[0]
                P12V_D3 = MCP2[1]
                P24V_M3 = MCP2[2]
                P24V_AUS3 = MCP2[3]
                P5V_A1 = MCP2[4]
                P12V_A1 = MCP2[5]
                P5V_B1 = MCP2[6]
                P12V_B1 = MCP2[7]
                P5V_C1 = MCP2[8]
                P12V_C1 = MCP2[9]
                P5V_D1 = MCP2[10]
                P12V_D1 = MCP2[11]
                P24V_M1 = MCP2[12]
                P24V_AUS1 = MCP2[13]
                P5V_A2 = MCP2[14]
                P12V_A2 = MCP2[15]
                P5V_B2 = MCP3[0]
                P12V_B2 = MCP3[1]
                P5V_C2 = MCP3[2]
                P12V_C2 = MCP3[3]
                P5V_D2 = MCP3[4]
                P12V_D2 = MCP3[5]
                P24V_M2 = MCP3[6]
                P24V_AUS2 = MCP3[7]
                P5V_A4 = MCP3[8]
                P12V_A4 = MCP3[9]
                P5V_B4 = MCP3[10]
                P12V_B4 = MCP3[11]
                P5V_C4 = MCP3[12]
                P12V_C4 = MCP3[13]
                P5V_D4 = MCP3[14]
                P12V_D4 = MCP3[15]
                P24V_M4 = MCP4[0]
                P24V_AUS4 = MCP4[1]
                P5V_A6 = MCP4[2]
                P12V_A6 = MCP4[3]
                P5V_B6 = MCP4[4]
                P12V_B6 = MCP4[5]
                P5V_C6 = MCP4[6]
                P12V_C6 = MCP4[7]
                P5V_D6 = MCP4[8]
                P12V_D6 = MCP4[9]
                P24V_M6 = MCP4[10]
                P24V_AUS6 = MCP4[11]
                return(P5V_A1, P12V_A1, P5V_B1, P12V_B1, P5V_C1, P12V_C1, P5V_D1, P12V_D1, P24V_M1, P24V_AUS1, P5V_A2, P12V_A2, P5V_B2, P12V_B2, P5V_C2, P12V_C2, P5V_D2, P12V_D2, P24V_M2, P24V_AUS2, P5V_A3, P12V_A3, P5V_B3, P12V_B3, P5V_C3, P12V_C3, P5V_D3, P12V_D3, P24V_M3, P24V_AUS3, P5V_A4, P12V_A4, P5V_B4, P12V_B4, P5V_C4, P12V_C4, P5V_D4, P12V_D4, P24V_M4, P24V_AUS4, P5V_A5, P12V_A5, P5V_B5, P12V_B5, P5V_C5, P12V_C5, P5V_D5, P12V_D5, P24V_M5, P24V_AUS5, P5V_A6, P12V_A6, P5V_B6, P12V_B6, P5V_C6, P12V_C6, P5V_D6, P12V_D6, P24V_M6, P24V_AUS6)
                                        

    def LetturaMapGPIOBK2(self):
                
                GPIOPORTVAL = []
                MCP5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                MCP8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                pos = 0

                
                GPIOPORTVAL = self.LetturaGPIOPORT()
                
                for bitelement in list(bin(GPIOPORTVAL[4])[2:].zfill(16)):
                        MCP5[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[5])[2:].zfill(16)):
                        MCP6[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[6])[2:].zfill(16)):
                        MCP7[15-pos] = int(bitelement)^1
                        pos = pos + 1
                pos = 0
                for bitelement in list(bin(GPIOPORTVAL[7])[2:].zfill(16)):
                        MCP8[15-pos] = int(bitelement)^1
                        pos = pos + 1



                P5V_A11 = MCP5[0]
                P12V_A11 = MCP5[1]
                P5V_B11 = MCP5[2]
                P12V_B11 = MCP5[3]
                P5V_C11 = MCP5[4]
                P12V_C11 = MCP5[5]
                P5V_D11 = MCP5[6]
                P12V_D11 = MCP5[7]
                P24V_M11 = MCP5[8]
                P24V_AUS11 = MCP5[9]
                P5V_A9 = MCP5[10]
                P12V_A9 = MCP5[11]
                P5V_B9 = MCP5[12]
                P12V_B9 = MCP5[13]
                P5V_C9 = MCP5[14]
                P12V_C9 = MCP5[15]
                P5V_D9 = MCP6[0]
                P12V_D9 = MCP6[1]
                P24V_M9 = MCP6[2]
                P24V_AUS9 = MCP6[3]
                P5V_A7 = MCP6[4]
                P12V_A7 = MCP6[5]
                P5V_B7 = MCP6[6]
                P12V_B7 = MCP6[7]
                P5V_C7 = MCP6[8]
                P12V_C7 = MCP6[9]
                P5V_D7 = MCP6[10]
                P12V_D7 = MCP6[11]
                P24V_M7 = MCP6[12]
                P24V_AUS7 = MCP6[13]
                P5V_A8 = MCP6[14]
                P12V_A8 = MCP6[15]
                P5V_B8 = MCP7[0]
                P12V_B8 = MCP7[1]
                P5V_C8 = MCP7[2]
                P12V_C8 = MCP7[3]
                P5V_D8 = MCP7[4]
                P12V_D8 = MCP7[5]
                P24V_M8 = MCP7[6]
                P24V_AUS8 = MCP7[7]
                P5V_A10 = MCP7[8]
                P12V_A10 = MCP7[9]
                P5V_B10 = MCP7[10]
                P12V_B10 = MCP7[11]
                P5V_C10 = MCP7[12]
                P12V_C10 = MCP7[13]
                P5V_D10 = MCP7[14]
                P12V_D10 = MCP7[15]
                P24V_M10 = MCP8[0]
                P24V_AUS10 = MCP8[1]
                P5V_A12 = MCP8[2]
                P12V_A12 = MCP8[3]
                P5V_B12 = MCP8[4]
                P12V_B12 = MCP8[5]
                P5V_C12 = MCP8[6]
                P12V_C12 = MCP8[7]
                P5V_D12 = MCP8[8]
                P12V_D12 = MCP8[9]
                P24V_M12 = MCP8[10]
                P24V_AUS12 = MCP8[11]
                return(P5V_A7, P12V_A7, P5V_B7, P12V_B7, P5V_C7, P12V_C7, P5V_D7, P12V_D7, P24V_M7, P24V_AUS7, P5V_A8, P12V_A8, P5V_B8, P12V_B8, P5V_C8, P12V_C8, P5V_D8, P12V_D8, P24V_M8, P24V_AUS8, P5V_A9, P12V_A9, P5V_B9, P12V_B9, P5V_C9, P12V_C9, P5V_D9, P12V_D9, P24V_M9, P24V_AUS9, P5V_A10, P12V_A10, P5V_B10, P12V_B10, P5V_C10, P12V_C10, P5V_D10, P12V_D10, P24V_M10, P24V_AUS10, P5V_A11, P12V_A11, P5V_B11, P12V_B11, P5V_C11, P12V_C11, P5V_D11, P12V_D11, P24V_M11, P24V_AUS11, P5V_A12, P12V_A12, P5V_B12, P12V_B12, P5V_C12, P12V_C12, P5V_D12, P12V_D12, P24V_M12, P24V_AUS12)

    
    def Intonoff(self, val):

        self.mcp1._writeRegister(0x04, val)
        self.mcp2._writeRegister(0x04, val)
        self.mcp3._writeRegister(0x04, val)
        self.mcp4._writeRegister(0x04, val)
        self.mcp5._writeRegister(0x04, val)
        self.mcp6._writeRegister(0x04, val)
        self.mcp7._writeRegister(0x04, val)
        self.mcp8._writeRegister(0x04, val)
        self.mcp1._writeRegister(0x05, val)
        self.mcp2._writeRegister(0x05, val)
        self.mcp3._writeRegister(0x05, val)
        self.mcp4._writeRegister(0x05, val)
        self.mcp5._writeRegister(0x05, val)
        self.mcp6._writeRegister(0x05, val)
        self.mcp7._writeRegister(0x05, val)
        self.mcp8._writeRegister(0x05, val)
        
    def WriteRegistro(self, reg, val, chip):

        if chip == 1:
            self.mcp1._writeRegister(reg, val)
        elif chip == 2:
            self.mcp2._writeRegister(reg, val)
        elif chip == 3:
            self.mcp3._writeRegister(reg, val)
        elif chip == 4:
            self.mcp4._writeRegister(reg, val)
        elif chip == 5:
            self.mcp5._writeRegister(reg, val)
        elif chip == 6:
            self.mcp6._writeRegister(reg, val)
        elif chip == 7:
            self.mcp7._writeRegister(reg, val)
        elif chip == 8:
            self.mcp8._writeRegister(reg, val)
            
    def ReadRegistro(self, reg, chip):

        if chip == 1:
            val = self.mcp1._readRegister(reg)
        elif chip == 2:
            val = self.mcp2._readRegister(reg)
        elif chip == 3:
            val = self.mcp3._readRegister(reg)
        elif chip == 4:
            val = self.mcp4._readRegister(reg)
        elif chip == 5:
            val = self.mcp5._readRegister(reg)
        elif chip == 6:
            val = self.mcp6._readRegister(reg)
        elif chip == 7:
            val = self.mcp7._readRegister(reg)
        elif chip == 8:
            val = self.mcp8._readRegister(reg)

        return(val)
    
    def LetturaMapInterruptINTF(self):

        MCP1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        MCP5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pos = 0

        REGISTROINTF = self.LetturaRegistroINTFAB()
        
        for bitelement in list(bin(REGISTROINTF[0])[2:].zfill(8)):
            MCP1[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[1])[2:].zfill(8)):
            MCP1[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[2])[2:].zfill(8)):
            MCP2[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[3])[2:].zfill(8)):
            MCP2[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[4])[2:].zfill(8)):
            MCP3[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[5])[2:].zfill(8)):
            MCP3[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[6])[2:].zfill(8)):
            MCP4[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[7])[2:].zfill(8)):
            MCP4[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[8])[2:].zfill(8)):
            MCP5[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[9])[2:].zfill(8)):
            MCP5[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[10])[2:].zfill(8)):
            MCP6[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[11])[2:].zfill(8)):
            MCP6[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[12])[2:].zfill(8)):
            MCP7[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[13])[2:].zfill(8)):
            MCP7[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[14])[2:].zfill(8)):
            MCP8[7-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTF[15])[2:].zfill(8)):
            MCP8[15-pos] = int(bitelement)
            pos = pos + 1
        pos = 0
            
        P5V_A5 = MCP1[0]
        P12V_A5 = MCP1[1]
        P5V_B5 = MCP1[2]
        P12V_B5 = MCP1[3]
        P5V_C5 = MCP1[4]
        P12V_C5 = MCP1[5]
        P5V_D5 = MCP1[6]
        P12V_D5 = MCP1[7]
        P24V_M5 = MCP1[8]
        P24V_AUS5 = MCP1[9]
        P5V_A3 = MCP1[10]
        P12V_A3 = MCP1[11]
        P5V_B3 = MCP1[12]
        P12V_B3 = MCP1[13]
        P5V_C3 = MCP1[14]
        P12V_C3 = MCP1[15]
        P5V_D3 = MCP2[0]
        P12V_D3 = MCP2[1]
        P24V_M3 = MCP2[2]
        P24V_AUS3 = MCP2[3]
        P5V_A1 = MCP2[4]
        P12V_A1 = MCP2[5]
        P5V_B1 = MCP2[6]
        P12V_B1 = MCP2[7]
        P5V_C1 = MCP2[8]
        P12V_C1 = MCP2[9]
        P5V_D1 = MCP2[10]
        P12V_D1 = MCP2[11]
        P24V_M1 = MCP2[12]
        P24V_AUS1 = MCP2[13]
        P5V_A2 = MCP2[14]
        P12V_A2 = MCP2[15]
        P5V_B2 = MCP3[0]
        P12V_B2 = MCP3[1]
        P5V_C2 = MCP3[2]
        P12V_C2 = MCP3[3]
        P5V_D2 = MCP3[4]
        P12V_D2 = MCP3[5]
        P24V_M2 = MCP3[6]
        P24V_AUS2 = MCP3[7]
        P5V_A4 = MCP3[8]
        P12V_A4 = MCP3[9]
        P5V_B4 = MCP3[10]
        P12V_B4 = MCP3[11]
        P5V_C4 = MCP3[12]
        P12V_C4 = MCP3[13]
        P5V_D4 = MCP3[14]
        P12V_D4 = MCP3[15]
        P24V_M4 = MCP4[0]
        P24V_AUS4 = MCP4[1]
        P5V_A6 = MCP4[2]
        P12V_A6 = MCP4[3]
        P5V_B6 = MCP4[4]
        P12V_B6 = MCP4[5]
        P5V_C6 = MCP4[6]
        P12V_C6 = MCP4[7]
        P5V_D6 = MCP4[8]
        P12V_D6 = MCP4[9]
        P24V_M6 = MCP4[10]
        P24V_AUS6 = MCP4[11]
        P5V_A11 = MCP5[0]
        P12V_A11 = MCP5[1]
        P5V_B11 = MCP5[2]
        P12V_B11 = MCP5[3]
        P5V_C11 = MCP5[4]
        P12V_C11 = MCP5[5]
        P5V_D11 = MCP5[6]
        P12V_D11 = MCP5[7]
        P24V_M11 = MCP5[8]
        P24V_AUS11 = MCP5[9]
        P5V_A9 = MCP5[10]
        P12V_A9 = MCP5[11]
        P5V_B9 = MCP5[12]
        P12V_B9 = MCP5[13]
        P5V_C9 = MCP5[14]
        P12V_C9 = MCP5[15]
        P5V_D9 = MCP6[0]
        P12V_D9 = MCP6[1]
        P24V_M9 = MCP6[2]
        P24V_AUS9 = MCP6[3]
        P5V_A7 = MCP6[4]
        P12V_A7 = MCP6[5]
        P5V_B7 = MCP6[6]
        P12V_B7 = MCP6[7]
        P5V_C7 = MCP6[8]
        P12V_C7 = MCP6[9]
        P5V_D7 = MCP6[10]
        P12V_D7 = MCP6[11]
        P24V_M7 = MCP6[12]
        P24V_AUS7 = MCP6[13]
        P5V_A8 = MCP6[14]
        P12V_A8 = MCP6[15]
        P5V_B8 = MCP7[0]
        P12V_B8 = MCP7[1]
        P5V_C8 = MCP7[2]
        P12V_C8 = MCP7[3]
        P5V_D8 = MCP7[4]
        P12V_D8 = MCP7[5]
        P24V_M8 = MCP7[6]
        P24V_AUS8 = MCP7[7]
        P5V_A10 = MCP7[8]
        P12V_A10 = MCP7[9]
        P5V_B10 = MCP7[10]
        P12V_B10 = MCP7[11]
        P5V_C10 = MCP7[12]
        P12V_C10 = MCP7[13]
        P5V_D10 = MCP7[14]
        P12V_D10 = MCP7[15]
        P24V_M10 = MCP8[0]
        P24V_AUS10 = MCP8[1]
        P5V_A12 = MCP8[2]
        P12V_A12 = MCP8[3]
        P5V_B12 = MCP8[4]
        P12V_B12 = MCP8[5]
        P5V_C12 = MCP8[6]
        P12V_C12 = MCP8[7]
        P5V_D12 = MCP8[8]
        P12V_D12 = MCP8[9]
        P24V_M12 = MCP8[10]
        P24V_AUS12 = MCP8[11]
        return(P5V_A1, P12V_A1, P5V_B1, P12V_B1, P5V_C1, P12V_C1, P5V_D1, P12V_D1, P24V_M1, P24V_AUS1, P5V_A2, P12V_A2, P5V_B2, P12V_B2, P5V_C2, P12V_C2, P5V_D2, P12V_D2, P24V_M2, P24V_AUS2, P5V_A3, P12V_A3, P5V_B3, P12V_B3, P5V_C3, P12V_C3, P5V_D3, P12V_D3, P24V_M3, P24V_AUS3, P5V_A4, P12V_A4, P5V_B4, P12V_B4, P5V_C4, P12V_C4, P5V_D4, P12V_D4, P24V_M4, P24V_AUS4, P5V_A5, P12V_A5, P5V_B5, P12V_B5, P5V_C5, P12V_C5, P5V_D5, P12V_D5, P24V_M5, P24V_AUS5, P5V_A6, P12V_A6, P5V_B6, P12V_B6, P5V_C6, P12V_C6, P5V_D6, P12V_D6, P24V_M6, P24V_AUS6, P5V_A7, P12V_A7, P5V_B7, P12V_B7, P5V_C7, P12V_C7, P5V_D7, P12V_D7, P24V_M7, P24V_AUS7, P5V_A8, P12V_A8, P5V_B8, P12V_B8, P5V_C8, P12V_C8, P5V_D8, P12V_D8, P24V_M8, P24V_AUS8, P5V_A9, P12V_A9, P5V_B9, P12V_B9, P5V_C9, P12V_C9, P5V_D9, P12V_D9, P24V_M9, P24V_AUS9, P5V_A10, P12V_A10, P5V_B10, P12V_B10, P5V_C10, P12V_C10, P5V_D10, P12V_D10, P24V_M10, P24V_AUS10, P5V_A11, P12V_A11, P5V_B11, P12V_B11, P5V_C11, P12V_C11, P5V_D11, P12V_D11, P24V_M11, P24V_AUS11, P5V_A12, P12V_A12, P5V_B12, P12V_B12, P5V_C12, P12V_C12, P5V_D12, P12V_D12, P24V_M12, P24V_AUS12)

    def LetturaMapInterruptINTCAP(self):
        
        MCP1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        MCP5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        MCP8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pos = 0

        REGISTROINTCAP = self.LetturaRegistroINTCAPAB()

        for bitelement in list(bin(REGISTROINTCAP[0])[2:].zfill(8)):
            MCP1[7-pos] = int(bitelement)^1
            pos = pos + 1 
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[1])[2:].zfill(8)):
            MCP1[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[2])[2:].zfill(8)):
            MCP2[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[3])[2:].zfill(8)):
            MCP2[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[4])[2:].zfill(8)):
            MCP3[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[5])[2:].zfill(8)):
            MCP3[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[6])[2:].zfill(8)):
            MCP4[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[7])[2:].zfill(8)):
            MCP4[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[8])[2:].zfill(8)):
            MCP5[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[9])[2:].zfill(8)):
            MCP5[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[10])[2:].zfill(8)):
            MCP6[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[11])[2:].zfill(8)):
            MCP6[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[12])[2:].zfill(8)):
            MCP7[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[13])[2:].zfill(8)):
            MCP7[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[14])[2:].zfill(8)):
            MCP8[7-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        for bitelement in list(bin(REGISTROINTCAP[15])[2:].zfill(8)):
            MCP8[15-pos] = int(bitelement)^1
            pos = pos + 1
        pos = 0
        
        P5V_A5 = MCP1[0]
        P12V_A5 = MCP1[1]
        P5V_B5 = MCP1[2]
        P12V_B5 = MCP1[3]
        P5V_C5 = MCP1[4]
        P12V_C5 = MCP1[5]
        P5V_D5 = MCP1[6]
        P12V_D5 = MCP1[7]
        P24V_M5 = MCP1[8]
        P24V_AUS5 = MCP1[9]
        P5V_A3 = MCP1[10]
        P12V_A3 = MCP1[11]
        P5V_B3 = MCP1[12]
        P12V_B3 = MCP1[13]
        P5V_C3 = MCP1[14]
        P12V_C3 = MCP1[15]
        P5V_D3 = MCP2[0]
        P12V_D3 = MCP2[1]
        P24V_M3 = MCP2[2]
        P24V_AUS3 = MCP2[3]
        P5V_A1 = MCP2[4]
        P12V_A1 = MCP2[5]
        P5V_B1 = MCP2[6]
        P12V_B1 = MCP2[7]
        P5V_C1 = MCP2[8]
        P12V_C1 = MCP2[9]
        P5V_D1 = MCP2[10]
        P12V_D1 = MCP2[11]
        P24V_M1 = MCP2[12]
        P24V_AUS1 = MCP2[13]
        P5V_A2 = MCP2[14]
        P12V_A2 = MCP2[15]
        P5V_B2 = MCP3[0]
        P12V_B2 = MCP3[1]
        P5V_C2 = MCP3[2]
        P12V_C2 = MCP3[3]
        P5V_D2 = MCP3[4]
        P12V_D2 = MCP3[5]
        P24V_M2 = MCP3[6]
        P24V_AUS2 = MCP3[7]
        P5V_A4 = MCP3[8]
        P12V_A4 = MCP3[9]
        P5V_B4 = MCP3[10]
        P12V_B4 = MCP3[11]
        P5V_C4 = MCP3[12]
        P12V_C4 = MCP3[13]
        P5V_D4 = MCP3[14]
        P12V_D4 = MCP3[15]
        P24V_M4 = MCP4[0]
        P24V_AUS4 = MCP4[1]
        P5V_A6 = MCP4[2]
        P12V_A6 = MCP4[3]
        P5V_B6 = MCP4[4]
        P12V_B6 = MCP4[5]
        P5V_C6 = MCP4[6]
        P12V_C6 = MCP4[7]
        P5V_D6 = MCP4[8]
        P12V_D6 = MCP4[9]
        P24V_M6 = MCP4[10]
        P24V_AUS6 = MCP4[11]
        P5V_A11 = MCP5[0]
        P12V_A11 = MCP5[1]
        P5V_B11 = MCP5[2]
        P12V_B11 = MCP5[3]
        P5V_C11 = MCP5[4]
        P12V_C11 = MCP5[5]
        P5V_D11 = MCP5[6]
        P12V_D11 = MCP5[7]
        P24V_M11 = MCP5[8]
        P24V_AUS11 = MCP5[9]
        P5V_A9 = MCP5[10]
        P12V_A9 = MCP5[11]
        P5V_B9 = MCP5[12]
        P12V_B9 = MCP5[13]
        P5V_C9 = MCP5[14]
        P12V_C9 = MCP5[15]
        P5V_D9 = MCP6[0]
        P12V_D9 = MCP6[1]
        P24V_M9 = MCP6[2]
        P24V_AUS9 = MCP6[3]
        P5V_A7 = MCP6[4]
        P12V_A7 = MCP6[5]
        P5V_B7 = MCP6[6]
        P12V_B7 = MCP6[7]
        P5V_C7 = MCP6[8]
        P12V_C7 = MCP6[9]
        P5V_D7 = MCP6[10]
        P12V_D7 = MCP6[11]
        P24V_M7 = MCP6[12]
        P24V_AUS7 = MCP6[13]
        P5V_A8 = MCP6[14]
        P12V_A8 = MCP6[15]
        P5V_B8 = MCP7[0]
        P12V_B8 = MCP7[1]
        P5V_C8 = MCP7[2]
        P12V_C8 = MCP7[3]
        P5V_D8 = MCP7[4]
        P12V_D8 = MCP7[5]
        P24V_M8 = MCP7[6]
        P24V_AUS8 = MCP7[7]
        P5V_A10 = MCP7[8]
        P12V_A10 = MCP7[9]
        P5V_B10 = MCP7[10]
        P12V_B10 = MCP7[11]
        P5V_C10 = MCP7[12]
        P12V_C10 = MCP7[13]
        P5V_D10 = MCP7[14]
        P12V_D10 = MCP7[15]
        P24V_M10 = MCP8[0]
        P24V_AUS10 = MCP8[1]
        P5V_A12 = MCP8[2]
        P12V_A12 = MCP8[3]
        P5V_B12 = MCP8[4]
        P12V_B12 = MCP8[5]
        P5V_C12 = MCP8[6]
        P12V_C12 = MCP8[7]
        P5V_D12 = MCP8[8]
        P12V_D12 = MCP8[9]
        P24V_M12 = MCP8[10]
        P24V_AUS12 = MCP8[11]
        return(P5V_A1, P12V_A1, P5V_B1, P12V_B1, P5V_C1, P12V_C1, P5V_D1, P12V_D1, P24V_M1, P24V_AUS1, P5V_A2, P12V_A2, P5V_B2, P12V_B2, P5V_C2, P12V_C2, P5V_D2, P12V_D2, P24V_M2, P24V_AUS2, P5V_A3, P12V_A3, P5V_B3, P12V_B3, P5V_C3, P12V_C3, P5V_D3, P12V_D3, P24V_M3, P24V_AUS3, P5V_A4, P12V_A4, P5V_B4, P12V_B4, P5V_C4, P12V_C4, P5V_D4, P12V_D4, P24V_M4, P24V_AUS4, P5V_A5, P12V_A5, P5V_B5, P12V_B5, P5V_C5, P12V_C5, P5V_D5, P12V_D5, P24V_M5, P24V_AUS5, P5V_A6, P12V_A6, P5V_B6, P12V_B6, P5V_C6, P12V_C6, P5V_D6, P12V_D6, P24V_M6, P24V_AUS6, P5V_A7, P12V_A7, P5V_B7, P12V_B7, P5V_C7, P12V_C7, P5V_D7, P12V_D7, P24V_M7, P24V_AUS7, P5V_A8, P12V_A8, P5V_B8, P12V_B8, P5V_C8, P12V_C8, P5V_D8, P12V_D8, P24V_M8, P24V_AUS8, P5V_A9, P12V_A9, P5V_B9, P12V_B9, P5V_C9, P12V_C9, P5V_D9, P12V_D9, P24V_M9, P24V_AUS9, P5V_A10, P12V_A10, P5V_B10, P12V_B10, P5V_C10, P12V_C10, P5V_D10, P12V_D10, P24V_M10, P24V_AUS10, P5V_A11, P12V_A11, P5V_B11, P12V_B11, P5V_C11, P12V_C11, P5V_D11, P12V_D11, P24V_M11, P24V_AUS11, P5V_A12, P12V_A12, P5V_B12, P12V_B12, P5V_C12, P12V_C12, P5V_D12, P12V_D12, P24V_M12, P24V_AUS12)



"""
tk = toolkit()
tk.Config()
tk.Direction()
while True:
    print(tk.LetturaGPIOPORT())
    time.sleep(1)
"""
"""     
def LetturaMapBankone():
        
        mcp1 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x00)
        mcp2 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x01)
        mcp3 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x02)
        mcp4 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x03)

        
        mcp1.open()
        mcp2.open()
        mcp3.open()
        mcp4.open()

        
        for x in range(0, 16):
                mcp1.setDirection(x, mcp1.DIR_INPUT)
                mcp2.setDirection(x, mcp2.DIR_INPUT)
                mcp3.setDirection(x, mcp3.DIR_INPUT)
                mcp4.setDirection(x, mcp4.DIR_INPUT)

        
                
        MCP1 = []
        MCP2 = []
        MCP3 = []
        MCP4 = []

                                
        for x in range(0 , 16):
                        
                MCP1.append(mcp1.digitalRead(x)) 
                MCP2.append(mcp2.digitalRead(x))
                MCP3.append(mcp3.digitalRead(x))
                MCP4.append(mcp4.digitalRead(x))                

                
        P5V_A5 = MCP1[0]
        P12V_A5 = MCP1[1]
        P5V_B5 = MCP1[2]
        P12V_B5 = MCP1[3]
        P5V_C5 = MCP1[4]
        P12V_C5 = MCP1[5]
        P5V_D5 = MCP1[6]
        P12V_D5 = MCP1[7]
        P24V_M5 = MCP1[8]
        P24V_AUS5 = MCP1[9]
        P5V_A3 = MCP1[10]
        P12V_A3 = MCP1[11]
        P5V_B3 = MCP1[12]
        P12V_B3 = MCP1[13]
        P5V_C3 = MCP1[14]
        P12V_C3 = MCP1[15]
        P5V_D3 = MCP2[0]
        P12V_D3 = MCP2[1]
        P24V_M3 = MCP2[2]
        P24V_AUS3 = MCP2[3]
        P5V_A1 = MCP2[4]
        P12V_A1 = MCP2[5]
        P5V_B1 = MCP2[6]
        P12V_B1 = MCP2[7]
        P5V_C1 = MCP2[8]
        P12V_C1 = MCP2[9]
        P5V_D1 = MCP2[10]
        P12V_D1 = MCP2[11]
        P24V_M1 = MCP2[12]
        P24V_AUS1 = MCP2[13]
        P5V_A2 = MCP2[14]
        P12V_A2 = MCP2[15]
        P5V_B2 = MCP3[0]
        P12V_B2 = MCP3[1]
        P5V_C2 = MCP3[2]
        P12V_C2 = MCP3[3]
        P5V_D2 = MCP3[4]
        P12V_D2 = MCP3[5]
        P24V_M2 = MCP3[6]
        P24V_AUS2 = MCP3[7]
        P5V_A4 = MCP3[8]
        P12V_A4 = MCP3[9]
        P5V_B4 = MCP3[10]
        P12V_B4 = MCP3[11]
        P5V_C4 = MCP3[12]
        P12V_C4 = MCP3[13]
        P5V_D4 = MCP3[14]
        P12V_D4 = MCP3[15]
        P24V_M4 = MCP4[0]
        P24V_AUS4 = MCP4[1]
        P5V_A6 = MCP4[2]
        P12V_A6 = MCP4[3]
        P5V_B6 = MCP4[4]
        P12V_B6 = MCP4[5]
        P5V_C6 = MCP4[6]
        P12V_C6 = MCP4[7]
        P5V_D6 = MCP4[8]
        P12V_D6 = MCP4[9]
        P24V_M6 = MCP4[10]
        P24V_AUS6 = MCP4[11]
        return(P5V_A1, P12V_A1, P5V_B1, P12V_B1, P5V_C1, P12V_C1, P5V_D1, P12V_D1, P24V_M1, P24V_AUS1, P5V_A2, P12V_A2, P5V_B2, P12V_B2, P5V_C2, P12V_C2, P5V_D2, P12V_D2, P24V_M2, P24V_AUS2, P5V_A3, P12V_A3, P5V_B3, P12V_B3, P5V_C3, P12V_C3, P5V_D3, P12V_D3, P24V_M3, P24V_AUS3, P5V_A4, P12V_A4, P5V_B4, P12V_B4, P5V_C4, P12V_C4, P5V_D4, P12V_D4, P24V_M4, P24V_AUS4, P5V_A5, P12V_A5, P5V_B5, P12V_B5, P5V_C5, P12V_C5, P5V_D5, P12V_D5, P24V_M5, P24V_AUS5, P5V_A6, P12V_A6, P5V_B6, P12V_B6, P5V_C6, P12V_C6, P5V_D6, P12V_D6, P24V_M6, P24V_AUS6)
                                        
                
                
                
def LetturaMapBanktwo():
        
        mcp5 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x04)
        mcp6 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x05)
        mcp7 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x06)
        mcp8 = MCP23S17(bus=0x00, pin_cs=0x01, device_id=0x07)
        
        mcp5.open()     
        mcp6.open()
        mcp7.open()
        mcp8.open()
        
        for x in range(0, 16):
                
                mcp5.setDirection(x, mcp5.DIR_INPUT)
                mcp6.setDirection(x, mcp6.DIR_INPUT)
                mcp7.setDirection(x, mcp7.DIR_INPUT)
                mcp8.setDirection(x, mcp8.DIR_INPUT)

                
        MCP5 = []
        MCP6 = []
        MCP7 = []
        MCP8 = []
        
        for x in range(0 , 16):
                                        
                MCP5.append(mcp5.digitalRead(x))
                MCP6.append(mcp6.digitalRead(x))                
                MCP7.append(mcp7.digitalRead(x))
                MCP8.append(mcp8.digitalRead(x))
                
        
        P5V_A11 = MCP5[0]
        P12V_A11 = MCP5[1]
        P5V_B11 = MCP5[2]
        P12V_B11 = MCP5[3]
        P5V_C11 = MCP5[4]
        P12V_C11 = MCP5[5]
        P5V_D11 = MCP5[6]
        P12V_D11 = MCP5[7]
        P24V_M11 = MCP5[8]
        P24V_AUS11 = MCP5[9]
        P5V_A9 = MCP5[10]
        P12V_A9 = MCP5[11]
        P5V_B9 = MCP5[12]
        P12V_B9 = MCP5[13]
        P5V_C9 = MCP5[14]
        P12V_C9 = MCP5[15]
        P5V_D9 = MCP6[0]
        P12V_D9 = MCP6[1]
        P24V_M9 = MCP6[2]
        P24V_AUS9 = MCP6[3]
        P5V_A7 = MCP6[4]
        P12V_A7 = MCP6[5]
        P5V_B7 = MCP6[6]
        P12V_B7 = MCP6[7]
        P5V_C7 = MCP6[8]
        P12V_C7 = MCP6[9]
        P5V_D7 = MCP6[10]
        P12V_D7 = MCP6[11]
        P24V_M7 = MCP6[12]
        P24V_AUS7 = MCP6[13]
        P5V_A8 = MCP6[14]
        P12V_A8 = MCP6[15]
        P5V_B8 = MCP7[0]
        P12V_B8 = MCP7[1]
        P5V_C8 = MCP7[2]
        P12V_C8 = MCP7[3]
        P5V_D8 = MCP7[4]
        P12V_D8 = MCP7[5]
        P24V_M8 = MCP7[6]
        P24V_AUS8 = MCP7[7]
        P5V_A10 = MCP7[8]
        P12V_A10 = MCP7[9]
        P5V_B10 = MCP7[10]
        P12V_B10 = MCP7[11]
        P5V_C10 = MCP7[12]
        P12V_C10 = MCP7[13]
        P5V_D10 = MCP7[14]
        P12V_D10 = MCP7[15]
        P24V_M10 = MCP8[0]
        P24V_AUS10 = MCP8[1]
        P5V_A12 = MCP8[2]
        P12V_A12 = MCP8[3]
        P5V_B12 = MCP8[4]
        P12V_B12 = MCP8[5]
        P5V_C12 = MCP8[6]
        P12V_C12 = MCP8[7]
        P5V_D12 = MCP8[8]
        P12V_D12 = MCP8[9]
        P24V_M12 = MCP8[10]
        P24V_AUS12 = MCP8[11]
        return(P5V_A7, P12V_A7, P5V_B7, P12V_B7, P5V_C7, P12V_C7, P5V_D7, P12V_D7, P24V_M7, P24V_AUS7, P5V_A8, P12V_A8, P5V_B8, P12V_B8, P5V_C8, P12V_C8, P5V_D8, P12V_D8, P24V_M8, P24V_AUS8, P5V_A9, P12V_A9, P5V_B9, P12V_B9, P5V_C9, P12V_C9, P5V_D9, P12V_D9, P24V_M9, P24V_AUS9, P5V_A10, P12V_A10, P5V_B10, P12V_B10, P5V_C10, P12V_C10, P5V_D10, P12V_D10, P24V_M10, P24V_AUS10, P5V_A11, P12V_A11, P5V_B11, P12V_B11, P5V_C11, P12V_C11, P5V_D11, P12V_D11, P24V_M11, P24V_AUS11, P5V_A12, P12V_A12, P5V_B12, P12V_B12, P5V_C12, P12V_C12, P5V_D12, P12V_D12, P24V_M12, P24V_AUS12)
"""             
