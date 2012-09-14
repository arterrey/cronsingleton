#!/usr/bin/env python2.7

import logging
import subprocess
import sys
import time

from apscheduler.scheduler import Scheduler



def parse_cron_spec (cron_spec):
    s = {}
    s["minute"], s["hour"], s["day"], s["month"], s["day_of_week"] = cron_spec.split(" ")
    return s


def run_scheduler(cron_spec, argv):

    # Convert cron style spec inot apscheduler spec
    spec = parse_cron_spec(cron_spec)

    # Set up scheduler
    sched = Scheduler()
    @sched.cron_schedule(**spec)
    def run():
        subprocess.call(argv)

    # Run scheduler
    sched.start()

    # Infinatly sleep
    while (True):
        time.sleep(15.0)



def main():

    logging.basicConfig()

    if not len(sys.argv) >= 3:
        print "cronsingleton: cronsingleton cron_spec command [args ...]"
        return -1

    cron_spec = sys.argv[1]
    argv = sys.argv[2:]
    run_scheduler(cron_spec, argv)

    return 0


