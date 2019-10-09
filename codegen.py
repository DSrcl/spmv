from scipy.io import mmread
from collections import defaultdict
import sys


coo = mmread(sys.argv[1])
csr = coo.tocsr()

m, n = csr.shape 

with open('spmv2.c', 'w') as out:
  out.write('double vals[%d] = {%s};\n' % (len(csr.data), ','.join(map(str, csr.data))))
  out.write('void spmv2(double  *restrict a, double *restrict x, double *restrict y) {\n')
  for i in range(m):
    col_idxs = csr.indices[csr.indptr[i]:csr.indptr[i+1]]
    pos = range(csr.indptr[i], csr.indptr[i+1])
    out.write('{\n')
    out.write('double t = %s;\n' % '+'.join('a[%d]*x[%d]'%pj for pj in zip(pos, col_idxs)))
    out.write('y[%d] = t;\n' % i)
    out.write('}\n')
  out.write('}\n')

#block_size = 64
#
# (ii,jj) -> [(i,j,v)]
#blocks = defaultdict(list)
#
#for i, j, v in zip(coo.row, coo.col, coo.data):
#  ii = int(i / block_size)
#  jj = int(j / block_size)
#  blocks[ii,jj].append((i,j,v))
#
#data = []
#
#
#with open('spmv2.c', 'w') as out:
#
#  print >>out, 'extern double a[];'
#  print >>out, 'void spmv2(double *restrict x, double *restrict y) {'
#
#  for block in blocks.values():
#    x_vals = set()
#    y_results = defaultdict(list)
#    print >>out, '{'
#
#    for i, j, v in block:
#      x_var = 'x_%d' % j
#      if j not in x_vals:
#        x_vals.add(j)
#        print >>out, 'int %s = x[%d];' % (x_var, j)
#
#      y_results[i].append('a[%d]*%s' % (len(data), x_var))
#      data.append(v)
#
#    for i, y_result in y_results.iteritems():
#      print >>out, 'y[%d] += %s;' % (i, ' + '.join(y_result))
#
#    print >>out, '}'
#
#  print >>out, '}'
#  print >>out, 'double a[%d] = {%s};' % (len(coo.data), ','.join(map(str, coo.data)))
