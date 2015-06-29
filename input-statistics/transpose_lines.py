with open('ncvoter_clusters_aggregated.txt', 'r') as input:
    with open('out', 'w') as output:
        for line in input:
            
            output.write(line.replace(', ', '\n'))
        
