class Electric_calculation:
    def __init__(self, datacase, resistance):
        try:
            self.datacase = datacase
            self.resistance = resistance
            self.datacaseinit = datacase
        except:
            self.datacase = int(input("테스트 케이스의 갯수를 입력하세요> "))
            self.resistance = int(input("저항의 값을 입력하세요> "))

    def intensity(self):
        self.amperelist = []
        self.r_list = []
        for voltage in range(self.datacase):
            self.r_list.append(voltage)
            ampere = voltage / self.resistance
            self.amperelist.append(ampere)
        return self.amperelist

    def voltage(self):
        self.voltagelist = []
        for i in range(self.datacase):
            voltage = self.amperelist[i] * self.r_list[i]
            self.voltagelist.append(voltage)
        return self.voltagelist


