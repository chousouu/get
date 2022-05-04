import matplotlib.pyplot as plt
import numpy as np


def cvt_to_volt(data):
    for i in range(0, len(data)):
        data[i] = 3.3 * data[i] / 255 

    return data

def read_data(path_to_data: str):
    with open(path_to_data, "r") as file_:
        data_str = file_.read().split()
        data = np.array(list(map(float, data_str)))

    return data

def count_time(data: np.ndarray, freq: float, total_time: float):
    charging_time = data.argmax() * freq
    discharging_time = total_time - charging_time

    return charging_time, discharging_time


def plot_data(path_to_data: str, path_to_stat: str, figsize=(18, 12), markerevery=250, markerstyle="o", color="red",
              save_graph = False, save_name = None):
    
    raw_data = read_data(path_to_data)
    data = cvt_to_volt(raw_data)
    stat = read_data(path_to_stat)
    total_time = stat[3]
    freqs      = stat[0]

    Y_values = data
    X_values = np.arange(start=freqs, stop=total_time, step=freqs)
    charg_time, discharg_time = count_time (data, freqs, total_time)
    fig, ax = plt.subplots(figsize=figsize, dpi=140)
    ax.minorticks_on()
    ax.set(xlim=(0, 90), ylim=(0, 3.3))
    plt.plot(X_values, Y_values, marker=markerstyle, markevery=markerevery, label="V(t)", color=color, )
    plt.text(0.82 * X_values.max(), 0.8 * Y_values.max(), 
            f"Total time is: {total_time:.2f} secs\n"
            f"Charging time is: {charg_time:.2f}\n"
            f"Discharging time is: {discharg_time:.2f}\n")

    plt.xlabel("Time, s")
    plt.ylabel("Voltage, V")
    plt.title("Proccess of capacitor's charging in RC-circut")
    plt.grid(which="major", linestyle="-", linewidth=1)
    plt.grid(which="minor", linestyle="--", linewidth=0.5)
    plt.legend()

    if save_graph and save_name is not None:
        plt.savefig(save_name)

    plt.show()


path_to_data = "./data.txt"
path_to_stat = "./settings.txt"

plot_data(path_to_data, path_to_stat, save_graph=True, color="blue", save_name="./plot.svg")


