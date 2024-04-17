#include <iostream>
#include <string>
#include <cmath>


#ifndef __MEMORY__H__
#define __MEMORY__H__
#endif
class PublicMem{
    public:
    class MassMem;
};



class FreeMem : public MassMem {

    public:
    signed int memor_buff;
    signed int memor_alloc;
    signed int total_mem;

};

void *ref_mem(signed int mem_st, signed int mem_alloc, signed int total_mem){

signed int m_st = mem_st;
signed int m_alloc = mem_alloc;
signed int m_total = total_mem;
    
auto mem_test;

};



int main(int argc, char **agrv){



   return 0; 
}