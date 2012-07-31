#include "stdio.h"

typedef void ( * instruction_type ) ( ) ;

int g_instructions = 0 ;
int g_arg [ 1 ] ;
int g_counter [ 1 ] ;
instruction_type g_instruction = 0 ;

void instruction1 ( ) ;
void instruction2 ( ) ;
void instruction3 ( ) ;
void instruction4 ( ) ;
void instruction5 ( ) ;

void instruction1 ( )
{
    printf ( "    cycle start\n" ) ;
    * g_counter = 0 ;
    g_instruction = instruction2 ;
    g_instructions += 1 ;
}

void instruction2 ( )
{
    printf ( "    cycle check\n" ) ;
    if ( * g_counter < * g_arg )
        g_instruction = instruction3 ;
    else
        g_instruction = instruction5 ;
    g_instructions += 2 ;
}

void instruction3 ( )
{
    printf ( "    cycle tick: %i\n" , * g_counter ) ;
    g_instruction = instruction4 ;
    g_instructions += 2 ;
}

void instruction4 ( )
{
    printf ( "    cycle loop\n" ) ;
    ++ * g_counter ;
    g_instruction = instruction2 ;
    g_instructions += 2 ;
}

void instruction5 ( )
{
    printf ( "    cycle finish\n" ) ;
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

int continuate ( int instructions )
{
    int desired = g_instructions + instructions ;
    while ( g_instruction && g_instructions < desired )
        ( * g_instruction ) ( ) ;
    return g_instruction != 0 ;
}

int main ( int argc , char * * argv )
{
    int iteration = 0 ;

    printf ( "first call\n" ) ;

    iteration = 0 ;
    envoke ( 11 ) ;
    do
    {
        printf ( "iteration: %i\n" , iteration ++ ) ;
    }
    while ( continuate ( 1 ) ) ;

    printf ( "\n" );
    printf ( "\n" );
    printf ( "second call\n" ) ;

    iteration = 0 ;
    envoke ( 22 ) ;
    do
    {
        printf ( "iteration: %i\n" , iteration ++ ) ;
    }
    while ( continuate ( 3 ) ) ;

    printf ( "hello world\n" ) ;
    return 0 ;
}
