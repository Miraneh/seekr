from seekr.kmer_counts import BasicCounter
import pandas as pd
from seekr.pearson import pearson

counter = BasicCounter(infasta='seekr/tests/data/example.fa',
                       outfile='example_2mers.npy',
                       k=2,
                       binary=False)
counts = counter.make_count_file()
dist = pearson(counts1=counts,
               counts2=counts)
pd.DataFrame(dist).to_csv('example_vs_example_2mers.csv')
