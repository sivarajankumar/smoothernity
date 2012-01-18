syntax enable
set hls is
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set ruler
set history=100
set backspace=indent,eol,start
set laststatus=2
set backupdir=~/tmp/vim/
set directory=~/tmp/vim/
mapclear

nnoremap j gj
nnoremap k gk
nnoremap <down> gj
nnoremap <up> gk

vnoremap j gj
vnoremap k gk
vnoremap <down> gj
vnoremap <up> gk

inoremap <up> <c-o>gk
inoremap <down> <c-o>gj
