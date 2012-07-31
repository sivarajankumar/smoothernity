#include <iostream>

typedef void ( * instruction_type ) ( ) ;

int g_instructions = 0 ;
int g_arg [ 1 ] = { 0 } ;
int g_counter = 0 ;
instruction_type g_instruction = 0 ;

void instruction1 ( ) ;
void instruction2 ( ) ;
void instruction3 ( ) ;
void instruction4 ( ) ;
void instruction5 ( ) ;

void instruction1 ( )
{
    std :: cerr << "    cycle start" << std :: endl ;
    g_counter = 0 ;
    g_instruction = instruction2 ;
    g_instructions += 1 ;
}

void instruction2 ( )
{
    std :: cerr << "    cycle check" << std :: endl ;
    if ( g_counter < * g_arg )
        g_instruction = instruction3 ;
    else
        g_instruction = instruction5 ;
    g_instructions += 2 ;
}

void instruction3 ( )
{
    std :: cerr << "    cycle tick: " << g_counter << std :: endl ;
    g_instruction = instruction4 ;
    g_instructions += 2 ;
}

void instruction4 ( )
{
    std :: cerr << "    cycle loop" << std :: endl ;
    ++ g_counter ;
    g_instruction = instruction2 ;
    g_instructions += 2 ;
}

void instruction5 ( )
{
    std :: cerr << "    cycle finish" << std :: endl ;
    g_instruction = 0 ;
    g_instructions += 1 ;
}

void envoke ( int arg )
{
    if ( ! g_instruction )
    {
        * g_arg = arg ;
        g_instructions = 0 ;
        g_instruction = instruction1 ;
    }
}

bool continuate ( int instructions )
{
    int desired = g_instructions + instructions ;
    while ( g_instruction && g_instructions < desired )
        ( * g_instruction ) ( ) ;
    return g_instruction ;
}

int main ( int , char * * )
{
    int iteration = 0 ;

    std :: cerr << "first call" << std :: endl ;

    iteration = 0 ;
    envoke ( 11 ) ;
    do
    {
        std :: cerr << "iteration: " << iteration ++ << std :: endl ;
    }
    while ( continuate ( 1 ) ) ;

    std :: cerr << std :: endl ;
    std :: cerr << std :: endl ;
    std :: cerr << "second call" << std :: endl ;

    iteration = 0 ;
    envoke ( 22 ) ;
    do
    {
        std :: cerr << "iteration: " << iteration ++ << std :: endl ;
    }
    while ( continuate ( 3 ) ) ;

    std :: cerr << "hello world" << std :: endl ;
    return 0 ;
}
