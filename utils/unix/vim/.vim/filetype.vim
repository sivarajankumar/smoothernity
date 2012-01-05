if exists("did_load_filetypes")
    finish
endif
augroup filetypedetect
    au! BufRead,BufNewFile *.shy setfiletype smoothernity
    au! BufRead,BufNewFile *.g setfiletype antlr3
augroup END

