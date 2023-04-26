import requests
import matplotlib.pyplot as plt


def get_response(date):
    responses = requests.get("https://data.police.uk/api/stops-force?force=north-wales&date=" + date).json()
    return responses


def analyse_responses(responses, age_ranges):

    results = [0, 0, 0, 0, 0, 0, 0, 0]

    for response in responses:
        if response['legislation'] == "Misuse of Drugs Act 1971 (section 23)":

            outcome = response['outcome']
            age_range = response['age_range']

            i = 0

            for range in age_ranges:
                if age_range == range:
                    if outcome == '':
                        results[i] += 1
                    else:
                        results[i+1] += 1
                else:
                    i += 2

    return results


def generate_graph(data, ranges, date):
    no_outcome = [data[0], data[2], data[4], data[6]]
    other_outcome = [data[1], data[3], data[5], data[7]]

    plt.bar(ranges, no_outcome, color='r')
    plt.bar(ranges, other_outcome, bottom=no_outcome, color='b')

    plt.title(label="NWP Stop and Search outcomes by age " + date)
    plt.xlabel("Age Ranges")
    plt.ylabel("Number of Stop and Searches")


    #for legend only
    colors = {'No Outcome':'red', 'Further Action Taken':'blue'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)


    plt.show()



def main():
    
    print("Police records for stop and search")
    date = input("Enter date in format 'YYYY-MM' >>")

    age_ranges = ['10-17', '18-24', '25-34', 'over 34']

    responses = get_response(date)

    analysed_data = analyse_responses(responses, age_ranges)

    print(analysed_data)

    generate_graph(analysed_data, age_ranges, date)
    

if __name__ == '__main__':
    main()