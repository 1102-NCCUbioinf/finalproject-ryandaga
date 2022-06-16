
# Expression Divergence of Chemosensory Genes between *Drosophila sechellia* and Its Sibling Species and Its Implications for Host Shift 
### Members
* Ryan Rey M Daga, 110761501
* Mequanent Argaw Muluneh, 110761504
* Assefa Chekole Addis, 110162865

### Demo 
You can run the python script to generate the dendrogram for the different species of *Drosophila* for a specific gene group.
```R
python code/dendrogram.py --gene genetype
```
The values for the parameter gene are Or, Ir, and Obp. Sample code is shown below.
```R
python code/dendrogram.py --gene Ir
```
## Folder organization and its related information

### docs
* reading4_group1_paper1.pptx

### data
* *D. sechelia* and *D. simulans*
  * Source: NCBI GEO under accession numbers GSE67587, GSE67861, and GSE67862
  * Tab-delimited file
  * 1.5 MB for each file
* *D. melanogaster*
  * Supplementary data from Shiao, M. S., Fan, W. L., Fang, S., Lu, M. Y. J., Kondo, R., & Li, W. H. (2013). Transcriptional profiling of adult *Drosophila* antennae by high-throughput sequencing. _Zoological Studies_, _52_(1), 1-10.
  * .xlsx file
  * 1.4 MB
* Orthologous genes form the three species of *Drosophila*
  * .csv file
  * 430 KB

### code
* `dendrogram.py`
  * The main scrip that performs the operation to generate a dendrogram for a specific gene group of *Drosophila*
  * Requires Python installed in computer and uses the `pandas` and `seaborn` library

### results
* Dendrogram of Olfactory receptor (*Or*), Ionotropic receptor (*Ir*), and Odor-binding protien (*Obp*) genes 

## References
* Shiao, M. S., Chang, J. M., Fan, W. L., Lu, M. Y. J., Notredame, C., Fang, S., ... & Li, W. H. (2015). Expression divergence of chemosensory genes between *Drosophila sechellia* and its sibling species and its implications for host shift. _Genome biology and evolution_, _7_(10), 2843-2858.
* Shiao, M. S., Fan, W. L., Fang, S., Lu, M. Y. J., Kondo, R., & Li, W. H. (2013). Transcriptional profiling of adult *Drosophila* antennae by high-throughput sequencing. _Zoological Studies_, _52_(1), 1-10.
