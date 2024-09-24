import datetime
import asyncio
EventSchedule = {
    "Monday" : "DeathMatch (Mountain Struggle)-21:00-23:00",
    "Tuesday": "Territory Wars-21:00-22:00",
    "Wednesday": "Free Battles (Field)-21:00-23:00",
    "Thursday": "DeathMatch (Navy Shipyard)-21:00-23:00",
    "Friday": "Ranked Battles-19:00-23:00",
    "Saturday": "Territory Wars-21:00-22:00",
    "Sunday": "Free Battles (Siege)-21:00-23:00"
}

#"Saturday": "Ranked Battles-13:00-21:00 | Territory Wars-21:00-22:00",
#"Sunday": "Ranked Battles-13:00-21:00 | Free Battles (Siege)-21:00-23:00"


def getDay():
    
    
    today = datetime.datetime.today().strftime("%A")
    return today

def getTime():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    
    return time


def splitter(entryBase):
    entry = EventSchedule[entryBase]
    if ( entry.find ("|")== -1):
        splitted= entry.split("-")
        startTime = splitted[1]
        endTime= splitted[2]
        
        return startTime,endTime
    else:
        DoubleEvents = entry.split("|")
        First=DoubleEvents[0]
        Second=DoubleEvents[1]
        splittedOne= First.split("-")
        startTimeOne = splittedOne[1]
        endTimeOne= splittedOne[2]

        splittedTwo= Second.split("-")
        startTimeTwo = splittedTwo[1]
        endTimeTwo= splittedTwo[2]
        return startTimeOne,endTimeOne,startTimeTwo,endTimeTwo

def getNextEvent():
    day=getDay()
    #day=getDayDebug(6)
    
    times =splitter(day)
    time=getTime()
    #time = "22:00"
    EtA=compareTime(times[0],time)
    
    #Check if already started
    
    if (int(EtA.split(":")[0])<0):
        EtA = compareTime(times[1],time)
        if(int(EtA.split(":")[0])<0):
            output = "No more events today"
            print(output)
            return output
            
        eventName=EventSchedule[day].split("-")[0]

        output = eventName+" ends in "+EtA.split(":")[0]+ " hours and "+ EtA.split(":")[1]+" minutes"
        print(output)
        return output
    ####################


    #Formatting
    
    eventName=EventSchedule[day].split("-")[0]
    output = eventName+" in "+EtA.split(":")[0]+" hours and "+ EtA.split(":")[1]+" minutes"
    print(output)
    ###############
    return output

def compareTime(t1,t2):
    h=int(t1.split(":")[0])-int(t2.split(":")[0])

    if(int(t1.split(":")[1])-int(t2.split(":")[1])<0):
        h=h-1
        m = 60-int(t2.split(":")[1])
    else:
        m = int(t1.split(":")[1])-int(t2.split(":")[1])
    return str(h)+":"+str(m)


def getDayDebug(i):
    Debug = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return Debug[i]

def getRanked():
    if(getDay()=="Friday"):
        print("Ranked today at 19:00-23:00")
        return "Ranked today at 19:00-23:00"
    if(getDay()=="Saturday" or getDay()=="Sunday"):
        print("Ranked today at 13:00-21:00")
        return "Ranked today at 13:00-21:00"
    print("Ranked Battles take place Fridays to Sundays")
    return "Ranked Battles take place Fridays to Sundays"


def getSpecificEvent(eventInp):
    event = eventInp.split("$")[1]
    if (event == "free"):
        return "Free Battle (Field): Wednesday at 21:00-23:00"+"\n"+"Free Battle (Siege): Sunday at 21:00-23:00"
    if (event == "dm"):
        return "DeathMatch (Mountain Struggle): Monday at 21:00-23:00 \nDeathMatch (Navy Shipyard) at 21:00-23:00"
    if (event == 'tw'):
        return "Territory Wars: Tuesday and Saturday at 21:00-22:00"
    else:
        return "My stupid bot doesn't know that command"

def getHelp():
    helper= "Available commands: \ne: Sends current's day event, how long to wait for it and how long until its finished\nr: Sends info for Ranked Battles\n$free: Sends info about Free Battles\n$dm: Sends info about DeathMatches\n$tw: Sends info about Territory Wars\n$help: Lists out the commands available"

    return helper





