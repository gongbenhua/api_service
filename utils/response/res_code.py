class Code:
    OK = "0"
    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    DATAERR = "4004"
    METHERR = "4005"
    SMSERROR = "4006"
    SMSFAIL = "4007"

    SESSIONERR = "4101"
    LOGINERR = "4102"
    PARAMERR = "4103"
    USERERR = "4104"
    ROLEERR = "4105"
    PWDERR = "4106"

    SERVERERR = "4500"
    UNKOWNERR = "4501"


error_map = {
    Code.OK: "success",
    Code.DBERR: "Database query error",
    Code.NODATA: "no date",
    Code.DATAEXIST: "Data already exists",
    Code.DATAERR: "Data error",
    Code.METHERR: "Method error",

    Code.SESSIONERR: "User is not logged in",
    Code.LOGINERR: "User login failed",
    Code.PARAMERR: "Parameter error",
    Code.USERERR: "The user does not exist or is not activated",
    Code.ROLEERR: "User identity error",
    Code.PWDERR: "Password error",

    Code.SERVERERR: "internal error",
    Code.UNKOWNERR: "unknown error",
}