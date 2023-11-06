# Marvish Chandra
# NFL Football Algorithm for finding fast ball carriers



class fastestCarriers():
    def weeklyStatistics(weekAvg,givenStat,wkcarrierAvg,rusher,passer,receiver):
        totalPerformance = (weekAvg * givenStat) + wkcarrierAvg + rusher + passer + receiver
        if wkcarrierAvg > 22:
            print("The weekly performance of the given ball carrier is above average.")
        if wkcarrierAvg < 22:
            print("The weekly performance of the given ball carrier is below average.")
        else: print("The carrier may not be available to perform.")
        if rusher > 0:
            print("The rusher's range is between zero and a hundred yards")
        else: print("The rusher may not be available to perform.")
        if passer > 20:
            print("The passer's range must be above twenty yards.")
        if receiver > 20:
            print("The receiver's reception must be above twenty yards.")
        else: print("The receiver may not be available to perform.")
        return totalPerformance


