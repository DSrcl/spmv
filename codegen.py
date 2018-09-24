print '''
void spmv2(int A1_size, int *A2_pos, int *A2_idx, double *A, double *y, double *x) {
  '''

BEGIN = 6000 
END = 15000
with open('idxs') as idxs:
  curi = 0
  locAndJ = []
  for row in idxs:
    i, j, aloc, _ = map(int, row.strip().split(','))
    if i == curi:
      locAndJ.append((aloc, j))
    else:
      if i >= BEGIN and i < END:
        print '{'
        print 'double t = ', ' + '.join('A[%d]*x[%d]'%idx for idx in locAndJ), ';'
        print 'y[%d] = t;'% curi
        print '}'
      curi = i
      locAndJ = [(aloc, j)]
  if i >= BEGIN and i < END:
    print '{'
    print 'double t = ', ' + '.join('A[%d]*x[%d]'%idx for idx in locAndJ), ';'
    print 'y[%d] = t;'% curi
    print '}'
    curi = i
    locAndJ = [(j,aloc)]

print '}'
