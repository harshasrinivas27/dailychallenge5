n = int(input("enter number of requests: "))
requests = []
for i in range(n):
    value = int(input("enter request " + str(i+1) + ": "))
    requests.append(value)

low = []
moderate = []
high= []
invalid = []

valid_count = 0

for value in requests:
    if value < 0:
        invalid.append(value)
    elif value == 0:
        pass
    elif value >= 1 and value <= 20:
        low.append(value)
        valid_count = valid_count + 1
    elif value >= 21 and value <= 49:
        moderate.append(value)
        valid_count = valid_count + 1
    elif value >= 50:
        high.append(value)
        valid_count = valid_count + 1

name = "Harsha Srinivas"
L = 0

for ch in name:
    if ch != " ":
        L = L + 1

PLI = L % 3

removed_count = 0

if PLI == 0:
    removed_count = len(low)
    low= []

elif PLI == 1:
    removed_count = len(high)
    high = []

elif PLI == 2:
    removed_count = len(low) + len(high)
    low = []
    high = []

print("name length (L):", L)
print("PLI value:", PLI)

print("low demand:", low)
print("moderate demand:", moderate)
print("high demand:", high)
print("invalid requests:", invalid)

print("total valid requests:", valid_count)
print("requests removed due to PLI:", removed_count)
