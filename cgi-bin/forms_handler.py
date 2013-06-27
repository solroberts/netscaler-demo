#!/usr/bin/env python
import os
import cgi
import time
import timeit
from src import pxsint
import subprocess
from multiprocessing import Process, Lock

#first, we grab our variables
form = cgi.FieldStorage()
network_ip = form.getvalue('network_ip', 'empty')
machine_start = form.getvalue('machine_start', 'empty')
machine_end = form.getvalue('machine_end', 'empty')
script_id = form.getvalue('script_id', 'empty')
password = form.getvalue('password', 'empty')
# then, we avoid script injection escaping the user input
network_ip = cgi.escape(network_ip)
machine_start = cgi.escape(machine_start)
machine_end = cgi.escape(machine_end)
script_id = cgi.escape(script_id)
password = cgi.escape(password)
#next, we add our html wrapper (better way to do this?)
#skip to around line 100 for actual code to run
print """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap, from Twitter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="../assets/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="../assets/css/bootstrap-responsive.css" rel="stylesheet">
      <!-- Le styles -->
    <link href="assets/css/docs.css" rel="stylesheet">
    <link href="assets/js/google-code-prettify/prettify.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="../assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="../assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="../assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="../assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="../assets/ico/favicon.png">
       </script>
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="../index.html">Home</a></li>
              <li class="active"><a href="../../pages.html">Scripts</a></li>
              <li><a href="../pages/labsnap.html">Lab Snapshots</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">
    <fieldset>
          <legend>Legend for boxes below</legend>
      <p>The submited network ip, machine start, machine end, and script were "%s, %s and %s"</p>
 """ % (machine_start, machine_end, script_id)
#legacy stuff below:
#

print """
scripts_dir = "/home/storage/scripts/attac-scripts/"
refresh_nfs = "%srefresh_nfs.sh"
cleanup_blades = "%scleanup_blades.sh" %(scripts_dir)
cleanup_netapp = "%scleanup_netapp.sh" %(scripts_dir)
desktop_cleanup = "%sdesktop_cleanup.sh" %(scripts_dir)
print cleanup_blades
print scripts_dir
print desktop_cleanup
username = "root"
password = password
command = script_id
base_ip = "6.7.42."
machine_start_int = int(machine_start)
machine_end_int = int(machine_end)
myrange = ([machine_start_int, machine_end_int])
start = timeit.default_timer()
for num in range(myrange[0], (myrange[1] +1)):
      if num.len() < 2
      hostname = "%s%s" %(base_ip, num) 
      pxsint.pxssh_mod(hostname, username, password, command)
stop = timeit.default_timer()
time = stop - start
"""
print """\
  <br>
  <br>"""
print "<h4>elapsed time: %s seconds</h4>" %(time)

print "<h2>all scripts have run</h2>"

#python to bash scripts

#subprocess.check_call(["../scripts/blade_run.sh", "-f %s -l %s -s %s"]) %(machine_start, machine_end, script_id)

#os.system("../scripts/blade_run.sh -f %s -l %s -s %s" %(machine_start,machine_end,script_id))


print"""     
    </fieldset>
    </div> <!-- container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../assets/js/jquery-1.9.1.min.js"></script>
    <script src="../assets/js/bootstrap-transition.js"></script>
    <script src="../assets/js/bootstrap-alert.js"></script>
    <script src="../assets/js/bootstrap-modal.js"></script>
    <script src="../assets/js/bootstrap-dropdown.js"></script>
    <script src="../assets/js/bootstrap-scrollspy.js"></script>
    <script src="../assets/js/bootstrap-tab.js"></script>
    <script src="../assets/js/bootstrap-tooltip.js"></script>
    <script src="../assets/js/bootstrap-popover.js"></script>
    <script src="../assets/js/bootstrap-button.js"></script>
    <script src="../assets/js/bootstrap-collapse.js"></script>
    <script src="../assets/js/bootstrap-carousel.js"></script>
    <script src="../assets/js/bootstrap-typeahead.js"></script>
""" 


