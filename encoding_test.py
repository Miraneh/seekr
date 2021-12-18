from seekr.kmer_counts import BasicCounter
import pandas as pd
from seekr.pearson import pearson
from seekr.graph import Maker

counter = BasicCounter(infasta='seekr/tests/data/v39-01.fa',
                       outfile='test_encoding/k7/v39-01_kmers.npy',
                       k=7,
                       binary=False)
counts = counter.make_count_file()
dist = pearson(counts1=counts,
               counts2=counts,
               outfile='test_encoding/k7/v39_vs_v39_7mers.npy')
print("creating graph...")
maker = Maker(adj='test_encoding/k7/v39_vs_v39_7mers.npy',
              gml_path='test_encoding/k7/v39_v39_graph.gml',
              csv_path='test_encoding/k7/v39_v39_connected.csv')
maker.make_gml_csv_files()
