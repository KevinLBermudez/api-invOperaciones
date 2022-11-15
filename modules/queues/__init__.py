from . import functions_queues as queues
from sympy import *

def get_teory(data):
    try:

        if(data.averageArrivals > data.averageServices):
            
            return {
                "error": "The average arrivals must be less than the average services"
            }

        operations = queues.VariousService(data)
        
        if data.numberServices == 1 :
            #operations for M/M/1 queue
            p0 = operations.p0()
            lq = operations.lq()
            pw = operations.pw()
        else : 
            #operations for M/M/K queue
            p0 = operations.p0VariousService()
            lq = operations.lqVariousService(p0)
            pw = operations.pwVariousService(p0)

        #operations for every queue
        wq = operations.wq(lq)
        w = operations.w(wq)
        l = operations.l(lq)

        return{
            "p0" : p0,
            "lq": lq,
            "wq": wq,
            "w":w,
            "l":l,
            "pw":pw
        }
    except Exception as e:
        return Exception(e)

def get_teory_analysis_economic(data): 

    try:

        if (data.averageArrivals > data.averageServices):
            return {
                "error": "The average arrivals must be less than the average services"
            }

        economic = queues.EconomicAnalysis(data)

        if data.numberServices == 1 :

            dailyCost = economic.costDailyOneService()
            costTotal = economic.costTotalOneService();

        else:
            dailyCost = economic.costDailyVariousService()
            costTotal = economic.costTotalVariousService()
        return{
            
            "dailyCost": dailyCost,
            "costTotal": costTotal
        }
    except Exception as e:
        return Exception(e)


def calculateProbabilities(data):
    try:

        if(data.averageArrivals > data.averageServices):
            return {
                "error": "The average arrivals must be less than the average services"
            }

        operations = queues.VariousService(data)

        if data.numberServices == 1 :
            pn = operations.pn(data.n)
        else:
            pn = operations.pnVariousService(data.n)

        return {
            "pn": pn
        }
    except Exception as e:
        return Exception(e)
