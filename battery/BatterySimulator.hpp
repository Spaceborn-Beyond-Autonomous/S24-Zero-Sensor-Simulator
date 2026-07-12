#ifndef BATTERY_SIMULATOR_HPP
#define BATTERY_SIMULATOR_HPP

class BatterySimulator
{
public:
    BatterySimulator();

    // Initialize the dummy battery
    bool initialize();

    // Read dummy values
    float getVoltage() const;
    float getStateOfCharge() const;
    float getTemperature() const;

    // Update battery values (dummy)
    void update();

private:
    float voltage_;
    float soc_;
    float temperature_;
};

#endif