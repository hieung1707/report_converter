import pandas


# basic info
no = []
tels = []
names = []
genders = []
products = []
amounts = []
due_dates = []
contract_nums = []

# Welcome call info
call_starts_welcome = []
pickup = []
pickup_times = []
hangup_times = []
hangup_steps = []


def calculate_hangup_steps(data):
    answers = data.split('/')
    print len(answers)


path = ('Master.csv')
df = pandas.read_csv(path, header=None)
df.fillna("", inplace=True)
for i in range(len(df)):
    data = df.loc[i]
    for col in data:
        no.append(i)
        tels.append(data[0])
        names.append(data[1])
        genders.append(data[2])
        products.append(data[3])
        amounts.append(data[4])
        due_dates.append(data[5])
        contract_nums.append(data[6])
        call_starts_welcome.append(data[7])
        pickup.append(data[8])
        pickup_times.append(data[9])
        hangup_times.append(data[10])
        hangup_steps.append(calculate_hangup_steps(data[11]))
