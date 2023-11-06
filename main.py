# Marvish Chandra
# NFL Football Algorithm for finding fast ball carriers



class fastestCarriers():
    def weeklyStatistics(weekAvg,givenStat): #performance weekly, of overall
        weeklyPerformance = (weekAvg * givenStat)
        if weeklyPerformance > 20:
            print("The weekly performance of the given ball carrier is above average.")
        if weeklyPerformance < 18:
            print("The weekly performance of the given ball carrier is below average.")
        else: print("Weekly performance of the ball carrier must be between the boundaries of 18 and 25 miles per hour.")
    def Carriers(weeklyAvg,givenStat):
        carriersPerformance = (weeklyAvg * givenStat) > 22

    def playerPosition(rusher,passer,receiver):
        if rusher > 0:
            rusherRange = 100 > rusher > 0
            print("The rusher's range is between zero and a hundred yards")
        else: print("The rusher did not achieve any yards to qualify.")
        if passer > 20:
            passedRange = 100 > passer > 0
            print("The passer's range must be above twenty yards.")
        else: print("The passer did not achieve any yards to qualify.")
        if receiver > 20:
            receivedRange = 100 > receiver > 0
            print("The reciever's reception must be above twenty yards")
        else: print("The reciever did not achieve any yards to qualify.")



