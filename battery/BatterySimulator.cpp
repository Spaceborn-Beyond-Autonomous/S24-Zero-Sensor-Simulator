#include "BatterySimulator.hpp"

BatterySimulator::BatterySimulator()
{
    voltage_ = 12.6f;
    soc_ = 100.0f;
    temperature_ = 25.0f;
}

bool BatterySimulator::initialize()
{
    return true;
}

float BatterySimulator::getVoltage() const
{
    return voltage_;
}

float BatterySimulator::getStateOfCharge() const
{
    return soc_;
}

float BatterySimulator::getTemperature() const
{
    return temperature_;
}

void BatterySimulator::update()
{
    // Dummy simulator:
    // Values stay constant.
}