# Convert to pandas datetime
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"])
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])

# Normalize to midnight, subtract, and extract total days
df["WaitingDays"] = (
    df["AppointmentDay"].dt.normalize() - 
    df["ScheduledDay"].dt.normalize()
).dt.days
 df["Weekday"] = df["AppointmentDay"].dt.day_name() 
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0,18,35,50,65,120],
    labels=["Child","Young Adult","Adult","Middle Age","Senior"]
)
