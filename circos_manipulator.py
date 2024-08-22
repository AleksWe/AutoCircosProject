import logging
import sys
from subprocess import Popen, PIPE
import plotting as p
import configparser
import os


# Selecting info about file names in config.ini
META_DATA = "metadata.ini"
# Path
PATH = "circos.conf"


def create_logger():
    # Create a handler
    log = logging.getLogger('test')
    handler = logging.StreamHandler(sys.stdout)
    log.addHandler(handler)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def meta_data(META_DATA):
    configParser = configparser.RawConfigParser()
    configParser.read(META_DATA)
    return configParser


def plot_finder(circos_conf):
    new_string = circos_conf[circos_conf.find('<plot>'):circos_conf.find('<plot>')].strip()
    return new_string


def plot_generator(config):
    try:
        new_circos_conf = ''
        karyotype = config.get('MetaData', 'karyotype')
        # try:
        #     plot_info = int(config.get('OverallPlotInfo', 'number_of_plots'))
        # except ValueError as e:
        #     logging.error(f"   INFO: {e} - Not a valid value. Enter a number.")
        #     sys.exit(0)
        new_circos_conf += p.Plotter.karyotype_adder(karyotype)
        new_circos_conf += p.Plotter.ideogram_adder()
        new_circos_conf += p.Plotter.plot_starter()
        if 'gene_name' in config:
            plotter_one = p.Plotter(file=config.get('MetaData', 'gene_name'))
            new_circos_conf += plotter_one.name_plotter()
        if 'file_ind' in config:
            plotter = p.Plotter(file=config.get('MetaData', 'file_ind'))
            new_circos_conf += plotter.line_plotting()
            new_circos_conf += plotter.scatter_plotting()
            new_circos_conf += plotter.bar_plotting()
        if 'file_p_div' in config:
            plotter = p.Plotter(file=config.get('MetaData', 'file_p_div'))
            new_circos_conf += plotter.line_plotting()
        new_circos_conf += p.Plotter.plot_ender()
        new_circos_conf += p.Plotter.image_adder()
        return new_circos_conf
    except configparser.NoSectionError as e:
        logging.error(f"   INFO: {e} - Not a valid value. Validate meta_data.ini data.")


def position_modifier(circos_conf):
    logging.info("   INFO: starting position modifications \n")
    new_string = plot_finder(circos_conf)
    return circos_conf


def config_writer(new_config, name):
    with open(name, "w", newline="") as file:
        file.write(new_config)


def main():
    # Calling function to log every step of the way
    # create_logger()
    # logging.info("   INFO: starting data reading")

    # Creating config variable that holds all names from META_DATA
    config = meta_data(META_DATA)

    # Write a newly generated circos.conf to file
    config_writer(plot_generator(config), PATH)


if __name__ == '__main__':
    main()
