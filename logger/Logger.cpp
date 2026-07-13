#include "Logger.hpp"

#include <iostream>
#include <chrono>
#include <iomanip>
#include <sstream>

Logger::Logger(const std::string& filename)
{
    logFile.open(filename, std::ios::app);
}

Logger::~Logger()
{
    if (logFile.is_open())
    {
        logFile.close();
    }
}

std::string Logger::getCurrentTime() const
{
    auto now = std::chrono::system_clock::now();

    auto time = std::chrono::system_clock::to_time_t(now);

    std::tm* localTime = std::localtime(&time);

    std::ostringstream stream;

    stream << std::put_time(localTime, "%Y-%m-%d %H:%M:%S");

    return stream.str();
}

std::string Logger::statusToString(LogStatus status) const
{
    switch(status)
    {
        case LogStatus::SUCCESS:
            return "SUCCESS";

        case LogStatus::WARNING:
            return "WARNING";

        case LogStatus::ERROR:
            return "ERROR";
    }

    return "UNKNOWN";
}

void Logger::log(
    LogStatus status,
    const std::string& module,
    const std::string& message,
    const std::string& errorCode)
{
    if(!logFile.is_open())
        return;

    logFile
        << "[" << getCurrentTime() << "]\n"
        << "MODULE : " << module << "\n"
        << "STATUS : " << statusToString(status) << "\n"
        << "MESSAGE : " << message << "\n"
        << "ERROR : " << errorCode << "\n"
        << "---------------------------------\n";

    logFile.flush();

    std::cout
        << "[" << getCurrentTime() << "] "
        << module << " : "
        << message << std::endl;
}