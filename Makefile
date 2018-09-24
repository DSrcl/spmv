CXXFLAGS  = -I${TACO_INCLUDE} -std=c++11 -O3
LDFLAGS = -ltaco -L${TACO_LIB}

all: build_idxs spmv

spmv: spmv.o fast.o
	$(CXX) -o $@ $^ $(LDFLAGS)

build_idxs: build_idxs.cc
