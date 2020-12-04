import sys
sys.path.append('../')

from list import *

# an entry from the data formatted as:
#   - date (string) - YYYY-MM-DD
#   - time (string)
#   - guard (int) - guard ID
#   - fellAsleep (bool) - whether the guard in question fell asleep on this turn
#   - min (int) - derived from the last two digits of time string
class Entry:
    def __init__(self, d, t, g, f):
        self.date = d
        self.time = t
        self.guard = int(g)
        self.fellAsleep = f
        self.min = int(self.time[3:])
    def __str__(self):
        return str((self.date, self.time, self.guard, self.fellAsleep))

class EntryList(List):
    def __init__(self, file):
        super().__init__(file)
        self.guards = set()

    # load data from the file, sorted alphabetically, into the list as entries.
    def load(self):
        # load data into data field
        super().load()
        self.data.sort()
        # convert each item in data field into an entry object based on its text
        # and put it into list
        i = 0
        guard = ''
        while i < len(self.data):
            string = self.data[i]
            string = string.split()
            # print(string)
            date = string[0][1:]
            # print(f'Date: {date}')
            time = string[1][0:-1]
            # print(f'Time: {time}')
            # if this is a guard entry, don't create an entry, just update the
            # guard variable for next time
            if string[2][0] == 'G':
                guard = string[3][1:]
                i+= 1
                continue
            elif string[2] == 'falls':
                fellAsleep = 1
            elif string[2] == 'wakes':
                fellAsleep = 0
            thisGuard = guard
            # print(f'guard for this entry: {thisGuard}')
            self.list.append(Entry(date, time, guard, fellAsleep))
            print(Entry(date, time, guard, fellAsleep))
            i+=1

        # make a set of guards in the data within the object
        g = set()
        for i in self.list:
            g.add(i.guard)
        self.guards = g

    # gets entries relevant to a given guard
    def getGuardEntries(self, guard):
        activityList = []
        for entry in self.list:
            if entry.guard == guard:
                activityList.append(entry)
        return activityList

    # takes guard number (int) and returns how many minutes that guard slept
    def calculateGuardSleep(self, guard):
        # load guard-relevant data into list
        activityList = self.getGuardEntries(guard)
        # for item in activityList:
        #     print(item)
        minutesSlept = 0
        for i, entry in enumerate(activityList):
            if entry.fellAsleep == 0:
                timeAlseep = entry.min - activityList[i-1].min
                minutesSlept += timeAlseep
        print(f'Guard {guard} slept {minutesSlept} minutes!')
        return minutesSlept

    def findSleepiestGuard(self):
        # print(f'Guards: {guards}')
        # for each guard
        sleepiest = 0
        max = 0
        for guard in self.guards:
            #print(f'inspecting guard: {guard}, max: {max}')
            currentSleep = self.calculateGuardSleep(guard)
            if currentSleep > max:
                #print(f"new sleepiest!:{guard}")
                sleepiest = guard
                max = currentSleep
        return sleepiest

    # returns the minute that a given guard was sleeping the most
    def findSleepyMinute(self, guard):
        return self.minsAsleep(guard).index(max(self.minsAsleep(guard)))

    # finds, for all guards, the most slept most slept minute.
    def findMostSleptMinute(self):
        maxGuard = 0
        maxMin = 0
        for guard in self.guards:
            print(f"--checking guard {guard}")
            m = self.minsAsleep(guard)
            if max(m) > maxMin:
                # print(f"Current guard {guard} has new sleepiest minute: {max(m)}")
                maxMin = max(m)
                maxGuard = guard
                # print(f'max(m) in if: {max(m)}')
                # print(f'maxGuard in if: {maxGuard}')
        return maxGuard, self.minsAsleep(maxGuard).index(maxMin)

    def minsAsleep(self, guard):
        minsAsleep = [0 for i in range(60)]
        guardActivity = self.getGuardEntries(guard)
        for i, entry in enumerate(guardActivity):
            if entry.fellAsleep == 0:
                for min in range(guardActivity[i-1].min, entry.min):
                    minsAsleep[min] += 1
        return minsAsleep

    # returns the solutions to the first and second sections of the puzzle as tuple
    def solve(self):
        g = self.findSleepiestGuard()
        print(g)
        print(self.findSleepyMinute(g))
        return self.findSleepyMinute(g) * g, self.findMostSleptMinute()[0] * self.findMostSleptMinute()[1]

if __name__ == '__main__':
    a = EntryList("input.txt")
    a.load()
    print(a.solve())
