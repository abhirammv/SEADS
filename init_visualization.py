import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import datetime as dt


if __name__ == "__main__":
    energy_data = { "data": [{ "time": "2017-04-28 00:00:00", "energy": "0.01620527777777777778" },{ "time": "2017-04-27 00:00:00", "energy": "0.01819916666666666667" },{ "time": "2017-04-26 00:00:00", "energy": "0.03094111111111111111" },{ "time": "2017-04-25 00:00:00", "energy": "0.02504527777777777778" },{ "time": "2017-04-24 00:00:00", "energy": "0.04676444444444444444" },{ "time": "2017-04-23 00:00:00", "energy": "0.02356111111111111111" },{ "time": "2017-04-22 00:00:00", "energy": "0.01240555555555555556" },{ "time": "2017-04-21 00:00:00", "energy": "0.02247166666666666667" },{ "time": "2017-04-20 00:00:00", "energy": "0.03190916666666666667" },{ "time": "2017-04-19 00:00:00", "energy": "0.01657222222222222222" },{ "time": "2017-04-18 00:00:00", "energy": "0.27470194444444444444" },{ "time": "2017-04-17 00:00:00", "energy": "0.04904305555555555556" },{ "time": "2017-04-16 00:00:00", "energy": "0.04503111111111111111" },{ "time": "2017-04-15 00:00:00", "energy": "0.03348722222222222222" },{ "time": "2017-04-14 00:00:00", "energy": "0.04503250000000000000" },{ "time": "2017-04-13 00:00:00", "energy": "0.04610555555555555556" },{ "time": "2017-04-12 00:00:00", "energy": "0.05072777777777777778" },{ "time": "2017-04-11 00:00:00", "energy": "0.03824111111111111111" },{ "time": "2017-04-10 00:00:00", "energy": "0.02862944444444444444" },{ "time": "2017-04-09 00:00:00", "energy": "0.04002222222222222222" },{ "time": "2017-04-08 00:00:00", "energy": "0.05428638888888888889" },{ "time": "2017-04-07 00:00:00", "energy": "0.05387000000000000000" },{ "time": "2017-04-06 00:00:00", "energy": "0.03153666666666666667" },{ "time": "2017-04-05 00:00:00", "energy": "0.00167388888888888889" },{ "time": "2017-04-04 00:00:00", "energy": "0.00642000000000000000" },{ "time": "2017-04-03 00:00:00", "energy": "0.00231972222222222222" },{ "time": "2017-04-02 00:00:00", "energy": "0.00329694444444444444" },{ "time": "2017-04-01 00:00:00", "energy": "0.00726000000000000000" },{ "time": "2017-03-31 00:00:00" ,"energy": "0.01512944444444444444" }]}
    X = []
    y = []
    for i in range(0, len(energy_data["data"]) - 1):
        X.append(energy_data["data"][i]["time"])
        y.append(energy_data["data"][i]["energy"])

    X_datetime = np.array([datetime.datetime(2017, 4, i, 0, 0) for i in range(1, 29)])
    y = y[::-1]
    y_en = np.asarray(y)

    plt.plot(X_datetime, y_en)
    plt.title("Energy Data")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.show()

    #Channel Harmonics data
    list_data = [["time", "P"], ["2017-08-03 23:07:58.002579", "0"], ["2017-08-03 23:07:58.002526", "0"],
                 ["2017-08-03 23:07:58.002474", "0"], ["2017-08-03 23:07:58.002421", "0"],
                 ["2017-08-03 23:07:58.002368", "0"], ["2017-08-03 23:07:58.002316", "0"],
                 ["2017-08-03 23:07:58.002263", "0"], ["2017-08-03 23:07:58.002211", "0"],
                 ["2017-08-03 23:07:58.002158", "0"], ["2017-08-03 23:07:58.002105", "0"],
                 ["2017-08-03 23:07:58.002053", "0"], ["2017-08-03 23:07:58.002000", "0"],
                 ["2017-08-03 23:07:58.001947", "0"], ["2017-08-03 23:07:58.001895", "0"],
                 ["2017-08-03 23:07:58.001842", "0"], ["2017-08-03 23:07:58.001789", "0"],
                 ["2017-08-03 23:07:58.001737", "0"], ["2017-08-03 23:07:58.001684", "0"],
                 ["2017-08-03 23:07:58.001632", "0"], ["2017-08-03 23:07:58.001579", "0"],
                 ["2017-08-03 23:07:58.001526", "0"], ["2017-08-03 23:07:58.001474", "0"],
                 ["2017-08-03 23:07:58.001421", "0"], ["2017-08-03 23:07:58.001368", "0"],
                 ["2017-08-03 23:07:58.001316", "0"], ["2017-08-03 23:07:58.001263", "0"],
                 ["2017-08-03 23:07:58.001211", "0"], ["2017-08-03 23:07:58.001158", "0"],
                 ["2017-08-03 23:07:58.001105", "0"], ["2017-08-03 23:07:58.001053", "0"],
                 ["2017-08-03 23:07:58.001000", "0"], ["2017-08-03 23:07:58.000947", "0"],
                 ["2017-08-03 23:07:58.000895", "0"], ["2017-08-03 23:07:58.000842", "0"],
                 ["2017-08-03 23:07:58.000789", "0"], ["2017-08-03 23:07:58.000737", "0"],
                 ["2017-08-03 23:07:58.000684", "0"], ["2017-08-03 23:07:58.000632", "0"],
                 ["2017-08-03 23:07:58.000579", "0"], ["2017-08-03 23:07:58.000526", "0"],
                 ["2017-08-03 23:07:58.000474", "0"], ["2017-08-03 23:07:58.000421", "0"],
                 ["2017-08-03 23:07:58.000368", "0"], ["2017-08-03 23:07:58.000316", "0"],
                 ["2017-08-03 23:07:58.000263", "0"], ["2017-08-03 23:07:58.000211", "0"],
                 ["2017-08-03 23:07:58.000158", "0"], ["2017-08-03 23:07:58.000105", "0"],
                 ["2017-08-03 23:07:58.000053", "2"], ["2017-08-03 23:07:58", "23"],
                 ["2017-08-03 23:07:56.002579", "0"], ["2017-08-03 23:07:56.002526", "0"],
                 ["2017-08-03 23:07:56.002474", "0"], ["2017-08-03 23:07:56.002421", "0"],
                 ["2017-08-03 23:07:56.002368", "0"], ["2017-08-03 23:07:56.002316", "0"],
                 ["2017-08-03 23:07:56.002263", "0"], ["2017-08-03 23:07:56.002211", "0"],
                 ["2017-08-03 23:07:56.002158", "0"], ["2017-08-03 23:07:56.002105", "0"],
                 ["2017-08-03 23:07:56.002053", "0"], ["2017-08-03 23:07:56.002000", "0"],
                 ["2017-08-03 23:07:56.001947", "0"], ["2017-08-03 23:07:56.001895", "0"],
                 ["2017-08-03 23:07:56.001842", "0"], ["2017-08-03 23:07:56.001789", "0"],
                 ["2017-08-03 23:07:56.001737", "0"], ["2017-08-03 23:07:56.001684", "0"],
                 ["2017-08-03 23:07:56.001632", "0"], ["2017-08-03 23:07:56.001579", "0"],
                 ["2017-08-03 23:07:56.001526", "0"], ["2017-08-03 23:07:56.001474", "0"],
                 ["2017-08-03 23:07:56.001421", "0"], ["2017-08-03 23:07:56.001368", "0"],
                 ["2017-08-03 23:07:56.001316", "0"], ["2017-08-03 23:07:56.001263", "0"],
                 ["2017-08-03 23:07:56.001211", "0"], ["2017-08-03 23:07:56.001158", "0"],
                 ["2017-08-03 23:07:56.001105", "0"], ["2017-08-03 23:07:56.001053", "0"],
                 ["2017-08-03 23:07:56.001000", "0"], ["2017-08-03 23:07:56.000947", "0"],
                 ["2017-08-03 23:07:56.000895", "0"], ["2017-08-03 23:07:56.000842", "0"],
                 ["2017-08-03 23:07:56.000789", "0"], ["2017-08-03 23:07:56.000737", "0"],
                 ["2017-08-03 23:07:56.000684", "0"], ["2017-08-03 23:07:56.000632", "0"],
                 ["2017-08-03 23:07:56.000579", "0"], ["2017-08-03 23:07:56.000526", "0"],
                 ["2017-08-03 23:07:56.000474", "0"], ["2017-08-03 23:07:56.000421", "0"],
                 ["2017-08-03 23:07:56.000368", "0"], ["2017-08-03 23:07:56.000316", "1"],
                 ["2017-08-03 23:07:56.000263", "1"], ["2017-08-03 23:07:56.000211", "1"],
                 ["2017-08-03 23:07:56.000158", "1"], ["2017-08-03 23:07:56.000105", "1"],
                 ["2017-08-03 23:07:56.000053", "1"], ["2017-08-03 23:07:56", "12"]]

    X_1 = []
    y_1 = []
    for i in range(1, len(list_data)):
        X_1.append(list_data[i][0])
        y_1.append(list_data[i][1])

    X_1[49] = '2017-08-03 23:07:58.000001'
    X_1[99] = '2017-08-03 23:07:56.000001'

    X_time = []
    X_time.append([dt.strptime(X_1[i], "%Y-%m-%d %H:%M:%S.%f") for i in range(0, len(X_1))])
    X_time = X_time[0]
    X_datetime_harmonics = np.array(X_time)
    y_p = np.asarray(y_1)

    plt.plot(X_datetime_harmonics, y_p)
    plt.title("Harmonics Data of Channel 1")
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.show()








