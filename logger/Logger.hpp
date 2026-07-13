#ifndef LOGGER_HPP
#define LOGGER_HPP

#include <string>
#include <fstream>

enum class LogStatus
{
    SUCCESS,
    WARNING,
    ERROR
};

class Logger
{
public:
    Logger(const std::string& filename);

    ~Logger();

    void log(LogStatus status,
             const std::string& module,
             const std::string& message,
             const std::string& errorCode = "NONE");

private:
    std::ofstream logFile;

    std::string getCurrentTime() const;

    std::string statusToString(LogStatus status) const;
};

#endif