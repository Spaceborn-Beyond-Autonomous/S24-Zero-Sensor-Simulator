#include <iostream>
#include "battery/BatterySimulator.hpp"

int main()
{
    BatterySimulator battery;

    if (!battery.initialize())
    {
        std::cout << "Battery initialization failed!\n";
        return 1;
    }

    std::cout << "Battery initialized successfully.\n";
    std::cout << "Voltage: " << battery.getVoltage() << " V\n";
    std::cout << "State of Charge: " << battery.getStateOfCharge() << " %\n";
    std::cout << "Temperature: " << battery.getTemperature() << " C\n";

    return 0;
}