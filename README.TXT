This script performs a memory check using the python psutil library. As this script is called via NRPE there are a few things that must be done in Nagios for it work work right and to use the right template for graphing.

##################
##custom command##
##################
Since you cannot use the same graph for all check_nrpe commands, you have to create a custom command for each NRPE check that will use a unique graph.

 define command{
          command_name check_nrpe_mem
          command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
	  }

#################
#define service##
#################
With the command now created, you can build the service check

#mem_check      
define service{
        use                     linux-service,srv-pnp
        service_description     Memory
        hosts                   hq-nagios
        servicegroups           MEMORY
        max_check_attempts      5   
        check_command           check_nrpe_mem!mem_check
        }

Note that the service is using the command created above, the check_nrpe_mem!mem_check. We are using the same check_nrpe command, however it must have a unique name to use a custome template

############
##Template##
############
Place the provided template into the /usr/local/pnp4nagios/share/template directory. Provided the names of services and checks are correct, and your pnp4nagios install is working the graph should start using the new template.

#################
##check_command##
#################
Create a check_command file for this check in /usr/local/pnp4nagios/etc/check_command/. Just copy another template that uses a custom template to a file named check_nrpe_mem.cfg


