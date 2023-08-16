import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
RESULT_DIR = '../res'
CSV_FILES_DIR = os.path.abspath('../resources/csv_files')
CAT_PACKET_LENGTH = 'Packet_Length'
CAT_CCDF = 'CCDF'
CAT_PDF = 'PDF'


def make_plots_dir():
    # Create the 'Plots' directory
    plots_path = os.path.abspath(RESULT_DIR)
    if os.path.isdir(plots_path):
        shutil.rmtree(plots_path)
    os.mkdir(plots_path)

    # Create subdirectories for different plot categories
    categories = [CAT_PACKET_LENGTH, CAT_CCDF, CAT_PDF]
    for category in categories:
        os.mkdir(get_plot_dir_path(category))


def get_plot_dir_path(category):
    return os.path.abspath(f"{RESULT_DIR}/{category}")


def get_plot_file_path(category, filename):
    return os.path.abspath(f"{RESULT_DIR}/{category}/{filename}")

def calculate_fit_exponential_distribution(lambda_fit, max_delay, scale):
    x = np.linspace(0, max_delay, 1000)
    y = lambda_fit * np.exp(-lambda_fit * x) * scale

    return x, y


def plot_packet_length_time(df):
    """
    Plot the packet length as a function of time.

    Parameters:
    df (pd.DataFrame): Input dataframe containing 'Time' and 'Length' columns.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(df['Time'], df['Length'], width=0.8)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Length')
    plt.title('Packet Length as a Function of Time')
    plt.grid(True)

    return plt


def plot_delay_pdf(df):
    """
    Plot the probability density function of inter-packet delays.

    Parameters:
    df (pd.DataFrame): Input dataframe containing 'Time' column.
    """
    delay = np.diff(df['Time'])
    delay = np.append(delay, 0)
    lambda_fit = 1 / np.mean(delay)
    max_delay = delay.max()
    bin_step = np.arange(0, int(np.ceil(max_delay)))
    pdf_, pdf_bins = np.histogram(delay, bins=bin_step, density=True)
    pdf = np.append(pdf_, 0)

    scale = max(pdf) / lambda_fit * np.exp(-lambda_fit * pdf_bins[np.argmax(pdf)])
    x, y = calculate_fit_exponential_distribution(lambda_fit, max_delay, scale)

    fig, subplot = plt.subplots(figsize=(10, 4))

    # Plot the PDF and the fitted exponential distribution
    subplot.step(pdf_bins, pdf, label='PDF')
    subplot.plot(x, y, label='exponential distribution', alpha=0.4, color='red')

    subplot.set_title('Probability Density Function of Inter-Packet Delays')
    subplot.set_xlabel('Inter Message Delays (Seconds)')
    subplot.set_ylabel('Probability Density')
    subplot.legend()
    subplot.grid(True)

    plt.tight_layout()  # Ensuring proper spacing

    # plt.xticks(np.arange(0, np.max(delay) + 1, 1))

    return plt



def make_ccdf(filter, threshold=0.7):
    """
    Calculate the Complementary Cumulative Distribution Function (CCDF) for given data.

    Parameters:
    filter (np.array): Input data for which CCDF is calculated.
    threshold (float, optional): Threshold for CCDF calculation.

    Returns:
    np.array: Normalized data array, CCDF values.
    """
    sort_array = np.sort(filter)
    normalized_array = sort_array / max(sort_array)
    ccdf = 1 - (np.arange(1, len(sort_array) + 1) / len(sort_array))

    return normalized_array, ccdf


def plot_ccdf(data):
    """
    Plot the CCDF of packets size distribution for different datasets.

    Parameters:
    dframes (list of pd.DataFrame): List of dataframes containing 'Length' column.
    classification (list of str): Labels for different datasets.
    """

    plt.figure(figsize=(10, 6))

    for ccdf_key in data:
        label = data[ccdf_key]['label']
        df = data[ccdf_key]['df']

        normalized_array, ccdf = make_ccdf(df['Length'])
        plt.plot(normalized_array, ccdf, label=label)

    # plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Normalized Message Sizes')
    plt.ylabel('CCDF')
    plt.title('CCDF of Packets Size Distribution')
    plt.legend(loc="lower left")
    plt.savefig(get_plot_file_path(CAT_CCDF, 'Plots.png'))
    plt.clf()


def get_csv_files_paths_with_name():
    files = os.listdir(CSV_FILES_DIR)
    csv_files = []
    for file in files:
        file_path = os.path.join(CSV_FILES_DIR, file)
        file_name_without_extension = os.path.splitext(file)[0]
        csv_files.append((file_path, file_name_without_extension))
    return csv_files



def plot_all_packet_length(dfs):

    for name in dfs:
        plt_to_save_path = plot_packet_length_time(dfs[name])
        plt_to_save_path.savefig(get_plot_file_path(CAT_PACKET_LENGTH, name))
        plt_to_save_path.clf()



def plot_all_delay_pdf(dfs):

    for name in dfs:
        plt_to_save_path = plot_delay_pdf(dfs[name])
        plt_to_save_path.savefig(get_plot_file_path(CAT_PDF, name))
        plt_to_save_path.clf()


def main():
    plt.rcParams['figure.max_open_warning'] = 50  # Set the desired maximum number of open figures
    make_plots_dir()

    # Get paths and data types of CSV files
    csv_files = get_csv_files_paths_with_name()

    # Labels for different datasets
    ccdf_data = {
        'WhatsApp_text': {
            'label': 'Text Group',
            'df': None
        },
        'WhatsApp_photos': {
            'label': 'Photos Group',
            'df': None
        },
        'WhatsApp_audio': {
            'label': 'Audio Group',
            'df': None
        },
        'WhatsApp_videos': {
            'label': 'Video Group',
            'df': None
        }
    }

    # Read CSV files into dataframes
    dfs = {}

    for file_path, data_type in csv_files:
        df = pd.read_csv(file_path, encoding='windows-1255')
        dfs[data_type] = df
        for ccdf_key in ccdf_data:
            if data_type.startswith(ccdf_key):
                ccdf_data[ccdf_key]['df'] = df

    # Generate and save packet length plots
    plot_all_packet_length(dfs)

    # Generate and save delay PDF plots
    plot_all_delay_pdf(dfs)

    # Generate and save CCDF plot
    plot_ccdf(ccdf_data)

    print('Files generated successfully')


if __name__ == "__main__":
    main()
