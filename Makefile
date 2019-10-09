CXXFLAGS  = -O3 -mfma -mavx -mavx2 -mtune=native

all: mat.c spmv

spmv: spmv.o spmv2.o
	$(CXX) -o $@ $^ $(LDFLAGS)

spmv2.s: spmv2.c
	$(CC) $(CXXFLAGS) $^ -o $@ -c -S

spmv2.o: spmv2.s

clean:
	rm -f fast.o spmv.o fast.o fast.s smpv2.o
