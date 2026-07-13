#include <iostream>

#include "battery/BatterySimulator.hpp"
#include "logger/Logger.hpp"

int main()
{
    // Create logger
    Logger logger("logs/battery.log");

    BatterySimulator battery;

    if (!battery.initialize())
    {
        logger.log(
            LogStatus::ERROR,
            "Battery",
            "Battery initialization failed.",
            "BATTERY_INIT_FAILED"
        );

        std::cout << "Battery initialization failed!\n";
        return 1;
    }

    logger.log(
        LogStatus::SUCCESS,
        "Battery",
        "Battery initialized successfully."
    );

    std::cout << "Battery initialized successfully.\n";
    std::cout << "Voltage: " << battery.getVoltage() << " V\n";
    std::cout << "State of Charge: " << battery.getStateOfCharge() << " %\n";
    std::cout << "Temperature: " << battery.getTemperature() << " C\n";

    return 0;
}