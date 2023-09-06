import requests
import csv


def download():
    list_id = requests.get(" https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    jsondata = []
    for id in range(100):
        current_id = list_id.json()[id]
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{current_id}.json?print=pretty")
        if response.status_code == 200:
            jsondata.append(response.json())
    # for id in list_id.json():
    #     response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
    #     if response.status_code == 200:
    #         jsondata.append(response.json())

    data_file = open('jsonoutput.csv', 'w', newline='')
    convert_json_to_csv(jsondata=jsondata, data_file=data_file)


def convert_json_to_csv(jsondata, data_file):
    csv_writer = csv.writer(data_file)
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()


if __name__ == '__main__':
    download()
