if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
let &cpo=s:cpo_save
unlet s:cpo_save
set backspace=2
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=ja
set modelines=0
set shiftwidth=2
set tabstop=2
set window=0
" vim: set ft=vim :
