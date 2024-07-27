# dictionaries
MonthConversation = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(MonthConversation["Mar"])
print(MonthConversation.get("Jan"))
print(MonthConversation.get("Hello", "Not a valid input"))
