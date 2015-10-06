#!/usr/bin/python

#Header Info
__author__ = 'Kirk Hammond'
__email__ = 'kirkdhammond@gmail.com'
__license__ = 'GPLv3'


#import modules
import psutil
import sys
from optparse import OptionParser, OptionGroup


#parse argumements
def parse_args():
    parser = OptionParser()
    parser.description = "Check Linux Host Memory Usage"
    parser.add_option("-W", "--warn", dest="warn", default = float('85'), help="Warning level for memory % use, default is 85%")
    parser.add_option("-C", "--crit", dest="crit", default = float('95'), help="Critical level for memory % use, default is 95%")
    (options, args) = parser.parse_args()
    return options


#convert KB to MB using this quick function
def k_to_mb(num):
    num /= 1024.0
    num /= 1024.0
    return "%.1f" % (num)


#get memory usage data
def get_data():
    mem_info = psutil.virtual_memory()
    total = mem_info.total
    available = mem_info.available
    percent = mem_info.percent
    used = mem_info.used
    active = mem_info.active
    inactive = mem_info.inactive
    buffers = mem_info.buffers
    cached = mem_info.cached
    #convert KB to MB using above created function
    total = k_to_mb(total)
    available = k_to_mb(available)
    used = k_to_mb(used)
    active = k_to_mb(active)
    inactive = k_to_mb(inactive)
    buffers = k_to_mb(buffers)
    cached = k_to_mb(cached)
    return total,available,percent,used,active,inactive,buffers,cached


#process the memory data returned
def nagios(total,available,percent,used,active,inactive,buffers,cached,options):
    #nagios return codes
    UNKNOWN = -1
    OK = 0
    WARNING = 1
    CRITICAL = 2
    #set values to floats for less than / greater than comparisons
    warn = float(options.warn)
    crit = float(options.crit)
    percent = float(percent)
    #performance data for pnp4nagios graphing
    pnp4 = ' | Percent=' + str(percent) + '%;' + str(warn) + str(';') + str(crit) + str(';0;100;') +\
           'Buffered=' + str(buffers) + 'MB;' +\
           'Cached=' + str(cached) + 'MB;' +\
           'Used=' + str(used) + 'MB;'
    #perform nagios checks with perper exit codes
    if percent > crit:
        print("CRITICAL - Memory use is: " + str(percent) + '%' + pnp4)
        sys.exit(CRITICAL)
    elif percent > warn:
        print("WARNING - Memory use is: " + str(percent) + '%' + pnp4)
        sys.exit(WARNING)
    else:
        print("OK - Memory use is: " + str(percent) + '%' + pnp4)
        sys.exit(OK)


#main function, controls script flow
def main():
    #get options needed to execute script
    options = parse_args()
    #collect memory information
    total,available,percent,used,active,inactive,buffers,cached = get_data()
    #Nagios_processing
    nagios(total,available,percent,used,active,inactive,buffers,cached,options)


#call main function
if __name__ == '__main__':
    main()
