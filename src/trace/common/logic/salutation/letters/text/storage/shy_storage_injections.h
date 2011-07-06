#ifndef _shy_trace_common_logic_salutation_letters_text_storage_injections_included
#define _shy_trace_common_logic_salutation_letters_text_storage_injections_included

#ifdef shy_build_with_trace
    #include "./worker/shy_worker_injections.h"
    typedef so_called_trace_common_logic_salutation_letters_text_storage_worker so_called_trace_common_logic_salutation_letters_text_storage ;
#endif

#ifdef shy_build_without_trace
    #include "./fribble/shy_fribble_injections.h"
    typedef so_called_trace_common_logic_salutation_letters_text_storage_fribble so_called_trace_common_logic_salutation_letters_text_storage ;
#endif

#endif
