import math

class Service:

    def __init__(self,data) -> None:
        self.medLambda = data.averageArrivals
        self.undServiceTime = data.averageServices


    def p0(self):

        result  = (1-self.medLambda)/self.undServiceTime
        
        return result

    # Para K = 1 or K > 1
    def lq(self):

        result = ((self.medLambda**2)/(self.undServiceTime*(self.undServiceTime - self.medLambda)))

        return result
    
    def wq(self,lq):
        result = lq/self.medLambda

        return result
        
    def w(self,wq):
        result = wq + (1/self.undServiceTime)

        return result

    def l(self,lq):

        result = lq + (self.medLambda/self.undServiceTime)

        return result

    def pw(self):
        result = (self.medLambda/self.undServiceTime)

        return result

    def pn(self,n):

        p0 = self.p0()
        result = 0

        probabilityPn = ((self.medLambda/self.undServiceTime)**n)*p0

        for i in range(0,n):
            result += ((self.medLambda/self.undServiceTime)**i)*p0    

        #for n = n
        probabilityNorLess = result
        #for n >= n
        probabilityNorMore = 1 - probabilityNorLess

        return {"nNorLess": probabilityNorLess,
                "nNorMor": probabilityNorMore,
                "n": probabilityPn}


class VariousService(Service):
    
    def __init__(self, data) -> None:
        
        self.medLambda = data.averageArrivals
        self.undServiceTime = data.averageServices
        self.numberServices = data.numberServices
        Service.__init__(self, data)

    def p0VariousService(self):

        summation = 0

        for i in range(self.numberServices):
            summation += (self.medLambda/self.undServiceTime)**i/math.factorial(i)

        result = 1/(summation + ((self.medLambda/self.undServiceTime)**self.numberServices/math.factorial(self.numberServices))*(1/(1-(self.medLambda/(self.numberServices*self.undServiceTime)))))
        
        return result
    
    def lqVariousService(self, p0):

        result = ((((self.medLambda/self.undServiceTime)**self.numberServices) * self.medLambda * self.undServiceTime) /((math.factorial(self.numberServices - 1) * (self.numberServices * self.undServiceTime - self.medLambda)**2 )))*p0

        return result

    def pwVariousService(self, p0):

        result = (1/math.factorial(self.numberServices)) * ((self.medLambda/self.undServiceTime)**self.numberServices) * ((self.undServiceTime*self.numberServices)/((self.undServiceTime*self.numberServices)-self.medLambda)) * p0

        return result

    def pnVariousService(self,n):

        p0 = self.p0VariousService()
        result = 0

        probabilityPn = (((self.medLambda/self.undServiceTime)**n)/math.factorial(n)) * p0

        for i in range(0,n):
            if i >= self.numberServices:
                result += (((self.medLambda/self.undServiceTime)**i)/(math.factorial(self.numberServices) * self.numberServices**(i-self.numberServices)))*p0
            else:
                result += (((self.medLambda/self.undServiceTime) ** i)/ math.factorial(i) )* p0
                
        probabilityNorLess =  result
        probabilityNorMore = 1 - probabilityNorLess

        return {"nNorLess": probabilityNorLess,
                "nNorMor": probabilityNorMore,
                "n": probabilityPn}


#for economic analysis

class EconomicAnalysis():
    
    def __init__(self,data) -> None:
        self.costAverageByService = data.costAverageByService
        self.hoursServiceByDay = data.hoursServiceByDay
        self.numberServices = data.numberServices
        self.medLambda = data.averageArrivals
        self.undServiceTime = data.averageServices

    def costDailyOneService(self):
        
        result = self.costAverageByService * self.hoursServiceByDay * self.medLambda

        return result

    def costDailyVariousService(self):
        
        result = self.costAverageByService * self.hoursServiceByDay * self.medLambda * self.numberServices

        return result
    