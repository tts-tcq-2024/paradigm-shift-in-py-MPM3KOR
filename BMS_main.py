#Battery Management System

from Temperature_check import temperature_is_ok
from SOC_check import soc_is_ok
from Charge_rate_check import charge_rate_is_ok


def battery_is_ok(temperature, soc, charge_rate):
    Temperature_status = temperature_is_ok(temperature)
    SOC_status = soc_is_ok (soc)
    Charge_rate_status = charge_rate_is_ok (charge_rate)
    return (Temperature_status and SOC_status and Charge_rate_status)


if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True) 
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(-1,70,0.7) is False)
    assert(battery_is_ok(25,100,0.9) is False)
    assert(battery_is_ok(25,22,0) is True)
  

