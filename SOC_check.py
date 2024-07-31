# SOC
def LOW_SOC_BREACH(soc):
    if soc < 20:
        LOW_SOC_BREACH_message()
        return False
    return False
        
def LOW_SOC_WARNING(soc):
    if(20 < soc < 25):
        LOW_SOC_WARNING_message()
        return True
    return False

def NORMAL_SOC(soc):
    if(25 <= soc < 76):
        NORMAL_SOC_message()
        return True
    return False
        
def  HIGH_SOC_WARNING(soc):
    if(76 <= soc < 81):
        HIGH_SOC_WARNING_message()
        return True
    return False      
    
def HIGH_SOC_BREACH(soc):
    if soc > 81:
        HIGH_SOC_BREACH_message()
        return False
    return False
        
def LOW_SOC_BREACH_message():
    print ("LOW SOC BREACH")
        
def HIGH_SOC_BREACH_message():
    print ("HIGH SOC BREACH")

def LOW_SOC_WARNING_message():
    print ("LOW SOC WARNING") 

def NORMAL_SOC_message():
    print ("NORMAL SOC")        
    
def HIGH_SOC_WARNING_message():
    print ("HIGH SOC WARNING")


def low_soc_is_ok(soc):
    return(LOW_SOC_WARNING(soc) or
    LOW_SOC_BREACH(soc))

def high_soc_is_ok(soc):
    return(HIGH_SOC_WARNING(soc) or 
           HIGH_SOC_BREACH(soc))

def soc_is_ok(soc):
    return (NORMAL_SOC(soc) or low_soc_is_ok(soc) or high_soc_is_ok(soc) )
    
