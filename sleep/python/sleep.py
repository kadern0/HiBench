#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys, time

from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: sleep <parallel> <seconds>"
        exit(-1)
    sc = SparkContext(appName="PythonSleep")
    parallel = int(sys.argv[1])
    seconds  = int(sys.argv[2])
    workload = sc.parallelize(range(parallel))
    workload.map(lambda x: time.sleep(seconds)).collect()
    sc.stop()