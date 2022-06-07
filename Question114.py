#Question9 section1

class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit
    def convertFahrenheit(self):
        f=((9.0/5.0)*self.celsius)+32
        return f
    def convertCelsius(self):
        c=(self.fahrenheit-32)*(5.0/9.0)
        return c

inst=Temperature(45,92)
print(inst.convertCelsius())
print(inst.convertFahrenheit())