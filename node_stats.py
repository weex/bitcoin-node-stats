#!/usr/bin/env python

import optparse
import urllib, json

parser = optparse.OptionParser(usage="%prog [options]")
parser.add_option("--live", dest="live", default=True,
		help="Get data from server")
parser.add_option("--provider", dest="provider", default="bitnodes",
		help="Choose from 'bitnodes' only.")
(options, args) = parser.parse_args()

# obtain data to process
if options.live:
	raw = ''
	if options.provider == 'bitnodes':
		url = "https://getaddr.bitnodes.io/api/v1/snapshots/latest/"
			
		response = urllib.urlopen(url);
		raw = response.read()
		#print raw[0:500]
		parsed = json.loads(raw)
				
		data = {}
		data = parsed  
				
		f = open("lastraw.json", "w")
		f.write(json.dumps(raw))
		f.close()
else:
	if options.provider == 'bitnodes':
		the_file = 'index.html'

	with open(the_file) as data_file:
		data = json.load(data_file)

total_nodes = 0
max_height = 0
nodes = data[u'nodes']
f = open("list_nodes.csv", "w")
for ip in nodes:	
	a = ip + "," + nodes[ip][1] + "," + str(int(nodes[ip][4]))
	f.write(a + "\n")
	if int(nodes[ip][4]) > max_height and int(nodes[ip][4]) < 500000:
		max_height = int(nodes[ip][4])
f.close()

count_updated_nodes = 0
count_updated_xt = 0
for ip in nodes:
	if int(nodes[ip][4]) == max_height or int(nodes[ip][4]) == max_height - 1:
		if 'XT' in nodes[ip][1]:
			count_updated_xt += 1
		count_updated_nodes += 1

print "Max block height: " + str(max_height)
print "Total syncd nodes: " + str(count_updated_nodes)
print "Total syncd XT nodes: " + str(count_updated_xt)
