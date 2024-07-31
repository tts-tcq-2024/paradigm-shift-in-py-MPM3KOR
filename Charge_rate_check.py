#Charge Rate

def LOW_CHARGE_RATE_BREACH(charge_rate):
    if charge_rate < 0:
        LOW_CHARGE_RATE_BREACH_message()
        return False
    return False
        
def LOW_CHARGE_RATE_WARNING(charge_rate):
    if(0 <= charge_rate < 0.04):
        LOW_CHARGE_RATE_WARNING_message()
        return True
    return False

def NORMAL_CHARGE_RATE(charge_rate):
    if(0.04 <= charge_rate < 0.76):
        NORMAL_CHARGE_RATE_message()
        return True
    return False
        
def  HIGH_CHARGE_RATE_WARNING(charge_rate):
    if(0.76 <= charge_rate <= 0.8):
        HIGH_CHARGE_RATE_WARNING_message()
        return True 
    return False       
    
def HIGH_CHARGE_RATE_BREACH(charge_rate):
    if charge_rate > 0.8:
        HIGH_CHARGE_RATE_BREACH_message()
        return False
    return False
        
def LOW_CHARGE_RATE_BREACH_message():
    print ("LOW CHARGE_RATE BREACH")
        
def HIGH_CHARGE_RATE_BREACH_message():
    print ("HIGH CHARGE_RATE BREACH")

def LOW_CHARGE_RATE_WARNING_message():
    print ("LOW CHARGE_RATE WARNING") 

def NORMAL_CHARGE_RATE_message():
    print ("NORMAL CHARGE_RATE")        
    
def HIGH_CHARGE_RATE_WARNING_message():
    print ("HIGH CHARGE_RATE WARNING")


def charge_rate_is_ok(charge_rate):
    return(NORMAL_CHARGE_RATE(charge_rate) or
    LOW_CHARGE_RATE_WARNING(charge_rate) or
    HIGH_CHARGE_RATE_WARNING(charge_rate) or
    LOW_CHARGE_RATE_BREACH(charge_rate) or
    HIGH_CHARGE_RATE_BREACH(charge_rate))
