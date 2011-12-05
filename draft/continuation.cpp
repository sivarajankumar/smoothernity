#include <iostream>

int g_instructions = 0 ;
int g_arg = 0 ;

void envoke ( int arg )
{
    g_arg = arg ;
    // start continuation
}

bool continuate ( int instructions )
{
    // continue continuation
    return false ;
}

int main ( int , char * * )
{
    int iteration = 0 ;

    iteration = 0 ;
    envoke ( 111 ) ;
    do
    {
        std :: cerr << "iteration: " << iteration ++ << std :: endl ;
    }
    while ( continuate ( 1 ) ) ;

    iteration = 0 ;
    envoke ( 222 ) ;
    do
    {
        std :: cerr << "iteration: " << iteration ++ << std :: endl ;
    }
    while ( continuate ( 3 ) ) ;

    std :: cerr << "hello world" << std :: endl ;
    return 0 ;
}
