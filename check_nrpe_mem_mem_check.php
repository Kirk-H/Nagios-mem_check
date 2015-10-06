<?php

#graph 1 (shows percentage of memory used)
$ds_name[1] = 'Percent Used';
$opt[1] = "--vertical-label % --title \"Mem Use for $hostname / $servicedesc\" ";
$def[1] = rrd::def("var1", $RRDFILE[1], $DS[1], "AVERAGE");

if ($WARN[1] != "") {
    $def[1] .= "HRULE:$WARN[1]#FFFF00 ";
}
if ($CRIT[1] != "") {
    $def[1] .= "HRULE:$CRIT[1]#FF0000 ";    
}

$def[1] .= rrd::area("var1", "#077DB0", "Percent") ;
$def[1] .= rrd::gprint("var1", array("LAST", "AVERAGE", "MAX"), "%6.2lf $UNIT[1]");


#graph 2 (shows total MB used, buffered, and cached memory line graphs)
$ds_name[2] = 'Memory Statistics';
$opt[2] = "--vertical-label $UNIT[2] --title \"Memory Statistics for $hostname / $servicedesc\" ";
$def[2] = rrd::def("var2", $RRDFILE[1], $DS[2], "AVERAGE");
$def[2] .= rrd::def("var3", $RRDFILE[1], $DS[3], "AVERAGE");
$def[2] .= rrd::def("var4", $RRDFILE[1], $DS[4], "AVERAGE");

if ($WARN[1] != "") {
    $def[1] .= "HRULE:$WARN[1]#FFFF00 ";
}
if ($CRIT[1] != "") {
    $def[1] .= "HRULE:$CRIT[1]#FF0000 ";    
}

$def[2] .= rrd::line1('var2', '#71C300', 'Buffered');
$def[2] .= rrd::gprint("var2", array("LAST", "AVERAGE", "MAX"), "%6.2lf $UNIT[2]");
$def[2] .= rrd::line1('var3', '#D57800', 'Cached');
$def[2] .= rrd::gprint("var3", array("LAST", "AVERAGE", "MAX"), "%6.2lf $UNIT[2]");
$def[2] .= rrd::line1('var4', '#0924CA', 'Used');
$def[2] .= rrd::gprint("var4", array("LAST", "AVERAGE", "MAX"), "%6.2lf $UNIT[2]");

?>
