from glob import glob
import configparser
import d6tstack.combine_csv


def file_list(folder, station) -> object:
    uri = '{}*/*{}*'.format(folder, station)
    return list(glob(uri))


def combine_csv(files, filename):
    d6tstack.combine_csv.CombinerCSV(
            files,
            sep=';',
            columns_select=['sensor_id', 'sensor_type', 'location', 'lat', 'lon', 'timestamp', 'P1', 'P2',
                            'temperature', 'humidity'],
            add_filename=False
    ).to_csv_combine(filename)


if __name__ == '__main__':
    # load config
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')

    combine_csv(file_list(cfg["archive"]["folder"], cfg["station"]["id"]), cfg["output"]["filename"])
