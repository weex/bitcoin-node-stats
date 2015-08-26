# bitcoin-node-stats
Pulls API data and summarizes sync'd node counts

This script pulls json data from the bitnodes.com API and does some simple stats on it. This was created to get a better view on the XT vs Core nodes count and bases stats on nodes being synchronized (i.e. being on the latest or previous block) rather than just being present.

Sample output:

    Max block height: 371549
    Total syncd nodes: 5773
    Total syncd XT nodes: 932

The script also saves the downloaded json as lastraw.json and a comma separated values list of nodes with IP, Useragent, and block height as list_nodes.csv.
