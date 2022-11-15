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

        try:

            summation = 0

            for i in range(self.numberServices):
                summation += (self.medLambda/self.undServiceTime)**i/math.factorial(i)

            result = 1/(summation + ((self.medLambda/self.undServiceTime)**self.numberServices/math.factorial(self.numberServices))*(1/(1-(self.medLambda/(self.numberServices*self.undServiceTime)))))
            
            return result
        except Exception as e:
            return Exception(e)
    
    def lqVariousService(self, p0):

        try:
            result = ((((self.medLambda/self.undServiceTime)**self.numberServices) * self.medLambda * self.undServiceTime) /((math.factorial(self.numberServices - 1) * (self.numberServices * self.undServiceTime - self.medLambda)**2 )))*p0

            return result
        except Exception as e:
            return Exception(e)


    def pwVariousService(self, p0):

        try:
            result = (1/math.factorial(self.numberServices)) * ((self.medLambda/self.undServiceTime)**self.numberServices) * ((self.undServiceTime*self.numberServices)/((self.undServiceTime*self.numberServices)-self.medLambda)) * p0

            return result

        except Exception as e:
            return Exception(e)

    def pnVariousService(self,n):
        try:
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

        except Exception as e:
            return Exception(e)

#for economic analysis

class EconomicAnalysis(VariousService,Service):
    
    def __init__(self,data) -> None:
        self.costAverageByService = data.costAverageByService
        self.hoursServiceByDay = data.hoursServiceByDay
        self.numberServices = data.numberServices
        self.medLambda = data.averageArrivals
        self.undServiceTime = data.averageServices
        self.costAverageByPerson = data.costAverageByPerson
        Service.__init__(self, data)
        VariousService.__init__(self, data)

    def costDailyOneService(self):
        try:

            result = self.costAverageByService * self.hoursServiceByDay * self.medLambda

            return result

        except Exception as e:
            return Exception(e)

    def costDailyVariousService(self):
        try:

            result = self.costAverageByService * self.hoursServiceByDay * self.medLambda * self.numberServices
            
            return result

        except Exception as e:
            return Exception(e)

    def costTotalOneService(self):
        try:

            lq = self.lq()
            l = self.l(lq)
            result = self.costAverageByPerson * l  +  self.costAverageByService * self.numberServices
            return result
        except Exception as e:
            return Exception(e)


    def costTotalVariousService(self):
        
        try:

            p0 = self.p0VariousService()
            lq = self.lqVariousService(p0)
            l = self.l(lq)
            result = self.costAverageByPerson * l + self.costAverageByService * self.numberServices
            
            print(result)

            return result

        except Exception as e:
            return Exception(e)
    
    