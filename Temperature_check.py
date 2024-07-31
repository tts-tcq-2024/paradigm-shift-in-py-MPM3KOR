#Temperature 

def LOW_TEMPERATURE_BREACH(temperature):
    if temperature < 0:
        LOW_TEMPERATURE_BREACH_message()
        return False
    return False
    
        
def LOW_TEMPERATURE_WARNING(temperature):
    if(0 <=temperature < 2.25):
        LOW_TEMPERATURE_WARNING_message()
        return True
    return False
    

def NORMAL_TEMPERATURE(temperature):
    if(2.25 <= temperature < 42.75):
        NORMAL_TEMPERATURE_message()
        return True
    return False
        
def  HIGH_TEMPERATURE_WARNING(temperature):
    if(42.75 <= temperature < 45):
        HIGH_TEMPERATURE_WARNING_message()
        return True 
    return False       
    
def HIGH_TEMPERATURE_BREACH(temperature):
    if temperature > 45:
        HIGH_TEMPERATURE_BREACH_message()
        return False
    return False

def LOW_TEMPERATURE_BREACH_message():
    print ("LOW TEMPERATURE BREACH")
        
def HIGH_TEMPERATURE_BREACH_message():
    print ("HIGH TEMPERATURE BREACH")

def LOW_TEMPERATURE_WARNING_message():
    print ("LOW TEMPERATURE WARNING") 

def NORMAL_TEMPERATURE_message():
    print ("NORMAL TEMPERATURE")        
    
def HIGH_TEMPERATURE_WARNING_message():
    print ("HIGH TEMPERATURE WARNING")


def low_temperature_is_ok(temperature):
    return(LOW_TEMPERATURE_WARNING(temperature) or
    LOW_TEMPERATURE_BREACH(temperature))

def high_temperature_is_ok(temperature):
    return(HIGH_TEMPERATURE_WARNING(temperature) or 
           HIGH_TEMPERATURE_BREACH(temperature))


def temperature_is_ok(temperature):
    
    return (NORMAL_TEMPERATURE(temperature) or 
            low_temperature_is_ok(temperature) or 
            high_temperature_is_ok(temperature))
