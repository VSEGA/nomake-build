#pragma once

namespace NomakeApi {
    enum class ErrorsCodes {
        Win32GetConsoleScreenBuffer = 1,
        OutOfRange,
        NotFoundItem,
        IncorrectArg
    };
}