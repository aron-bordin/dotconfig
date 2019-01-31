" ======= Loading Vundle

" Use Vim settings, rather than Vi settings
set nocompatible

filetype off

" Set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
"set rtp+=~/.fzf
call vundle#begin()

"let Vundle manage Vundle

" ####### Plugins #########
Plugin 'airblade/vim-gitgutter'
Plugin 'chriskempson/base16-vim'
Plugin 'davidhalter/jedi-vim'
"Plugin 'derekwyatt/vim-scala'
"Plugin 'ensime/ensime-vim'
Plugin 'euclio/gitignore.vim'
Plugin 'ervandew/supertab'
Plugin 'gmarik/Vundle.vim'
Plugin 'hashivim/vim-terraform'
Plugin 'heavenshell/vim-pydocstring'
"Plugin 'leafgarland/typescript-vim'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'juliosueiras/vim-terraform-completion'
Plugin 'junegunn/fzf'
Plugin 'Konfekt/FastFold'
Plugin 'majutsushi/tagbar'
Plugin 'mbbill/undotree'
Plugin 'nvie/vim-flake8'
Plugin 'posva/vim-vue'
Plugin 'ryanoasis/vim-devicons'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/nerdtree'
Plugin 'w0rp/ale'
Plugin 'takac/vim-hardtime'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'tmhedberg/SimpylFold'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-surround'
"Plugin 'Valloric/YouCompleteMe'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'xolox/vim-lua-ftplugin'
Plugin 'xolox/vim-misc'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'zhaocai/GoldenView.Vim'
"Plugin 'wincent/command-t'

" ####### End-Plugins ####

call vundle#end()

filetype plugin indent on
set exrc

" End Vundle @@

" Enable theme
let base16colorspace=256  " Access colors present in 256 colorspace
colorscheme base16-$BASE16_THEME
set background=dark


" Allow backspacing over everything in insert mode.
set backspace=indent,eol,start

set history=200		" keep 200 lines of command line history
set ruler		" show the cursor position all the time
set showcmd		" display incomplete commands
set wildmenu		" display completion matches in status line

set ttimeout		" time out for key codes
set ttimeoutlen=100	" wait up to 100

" Show @@@ in the last line if it is truncated
set display=truncate

" Show a few lines of context around the cursor
set scrolloff=5

" Do incremental searching when it's possitble to timeout
if has('reltime')
	set incsearch
endif

" Do not recognize octal number for Ctrl-A and Ctrl-X
set nrformats-=octal

" Don't use Ex mode, use Q for formatting.
" " Revert with ":unmap Q".
map Q gq
"
" CTRL-U in insert mode deletes a lot.  Use CTRL-G u to first break undo,
" so that you can undo CTRL-U after inserting a line break.
" Revert with ":iunmap <C-U>".
inoremap <C-U> <C-G>u<C-U>

" In many terminal emulators the mouse works just fine.  By enabling it you
" can position the cursor, Visually select and scroll with the mouse.
if has('mouse')
"   set mouse=a
endif

" Switch syntax highlighting on when the terminal has colors or when using the
" GUI (which always has colors).
if &t_Co > 2 || has("gui_running")
  " Revert with ":syntax off".
  syntax on

  " I like highlighting strings inside C comments.
  " Revert with ":unlet c_comment_strings".
  let c_comment_strings=1
endif

" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Enable file type detection.
  " Use the default filetype settings, so that mail gets 'tw' set to 72,
  " 'cindent' is on in C files, etc.
  " Also load indent files, to automatically do language-dependent indenting.
  " Revert with ":filetype off".
  filetype plugin indent on

  " Put these in an autocmd group, so that you can revert them with:
  " ":augroup vimStartup | au! | augroup END"
  augroup vimStartup
    au!

    " When editing a file, always jump to the last known cursor position.
    " Don't do it when the position is invalid or when inside an event handler
    " (happens when dropping a file on gvim).
    autocmd BufReadPost *
      \ if line("'\"") >= 1 && line("'\"") <= line("$") |
      \   exe "normal! g`\"" |
      \ endif

  augroup END

endif " has("autocmd")

" Convenient command to see the difference between the current buffer and the
" file it was loaded from, thus the changes you made.
" Only define it when not defined already.
" Revert with: ":delcommand DiffOrig".
if !exists(":DiffOrig")
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis
		  \ | wincmd p | diffthis
endif

if has('langmap') && exists('+langremap')
  " Prevent that the langmap option applies to characters that result from a
  " mapping.  If set (default), this may break plugins (but it's backward
  " compatible).
  set nolangremap
endif

set splitbelow
set splitright

" split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" folding
nnoremap <space> za

" Code indent settings
set tabstop=4
set softtabstop=4
set shiftwidth=4
set textwidth=79
set expandtab
set autoindent
set fileformat=unix
set encoding=utf-8
set relativenumber
set number


" Use bash
set shell=/bin/bash

" Autocompletion
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoTo<CR>
map <leader>e  :YcmCompleter GoToDefinition<CR>
map <leader>d  :YcmCompleter GoToDeclaration<CR>

"python with virtualenv support

python << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  project_base_dir in sys.path or sys.path.insert(0, project_base_dir)

  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF
" Enable folding
" set foldmethod=indent
set foldlevel=99

" SimpylFold issue #27
"autocmd BufWinEnter *.py setlocal foldexpr=SimpylFold(v:lnum) foldmethod=expr
"autocmd BufWinLeave *.py setlocal foldexpr< foldmethod<
let python_highlight_all=1

" syntastic settings

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let NERDTreeIgnore=['\.git$', '\.pyc$', '\~$', '\.egg*', '\.tox$', '__pycache__$', 'venv$', '^env$'] "ignore files in NERDTree

" NERDTree settings
" show NERDTree automatically if is a dir
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif

nnoremap nf :NERDTreeFocus<CR>
nnoremap nr :NERDTreeRefreshRoot<CR>
nnoremap np :NERDTreeFind<CR>
" file name hightlight
let g:NERDTreeFileExtensionHighlightFullName = 1
let g:NERDTreeExactMatchHighlightFullName = 1
let g:NERDTreePatternMatchHighlightFullName = 1
let g:NERDTreeHighlightFolders = 1 " enables folder icon highlighting using exact match
let g:NERDTreeHighlightFoldersFullName = 1 " highlights the folder name

let g:airline_powerline_fonts = 1
let g:airline_theme='luna'

set incsearch
set hlsearch
nnoremap <Leader><space> :noh<cr>
let NERDTreeMapActivateNode='<space>'

let &colorcolumn="80,".join(range(121,999),",")
let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']

set formatoptions-=t
set updatetime=250

let g:goldenview__enable_default_mapping = 0
nmap <silent> <C-S>  <Plug>GoldenViewSplit
nmap <silent> <F8>   <Plug>GoldenViewSwitchMain
nmap <silent> <S-F8> <Plug>GoldenViewSwitchToggle

nnoremap <F5> :UndotreeToggle<cr>
nmap <F8> :TagbarToggle<CR>

nnoremap tn :tabnew<Space>
nnoremap tc :tabclose<CR>
nnoremap tk :tabnext<CR>
nnoremap tj :tabprev<CR>
nnoremap th :tabfirst<CR>
nnoremap tl :tablast<CR>

:nmap <ScrollWheelUp> <nop>
:nmap <S-ScrollWheelUp> <nop>
:nmap <C-ScrollWheelUp> <nop>
:nmap <ScrollWheelDown> <nop>
:nmap <S-ScrollWheelDown> <nop>
:nmap <C-ScrollWheelDown> <nop>
:nmap <ScrollWheelLeft> <nop>
:nmap <S-ScrollWheelLeft> <nop>
:nmap <C-ScrollWheelLeft> <nop>
:nmap <ScrollWheelRight> <nop>
:nmap <S-ScrollWheelRight> <nop>
:nmap <C-ScrollWheelRight> <nop>

nnoremap <leader>rv :source $MYVIMRC<CR>
inoremap <C-o> <Esc>O<Esc>jA

let g:ycm_goto_buffer_command = 'vertical-split'

map <C-p> :CommandT<CR>

if &term =~ "xterm" || &term =~ "screen"
    let g:CommandTCancelMap = ['<ESC>', '<C-c>']
endif

nmap <silent> <C-i> <Plug>(pydocstring)
set pastetoggle=<F3>
let g:ycm_server_python_interpreter = '/usr/bin/python3'
let g:ycm_python_binary_path = '/usr/bin/python3'

autocmd Filetype scala setlocal ts=4 sw=4 expandtab

let g:CommandTWildIgnore=&wildignore . ",*/bower_components,*/data,*/venv,*/.git,*/dataset,*/.tox"

let g:airline#extensions#ale#enabled = 1

let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'

"let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_start_level = 2
let g:indent_guides_guide_size = 1

let NERDTreeShowHidden=1
let NERDTreeShowLineNumbers=1
let NERDTreeMinimalUI=1
map <C-m> :NERDTreeToggle<CR>
let g:gitgutter_max_signs=700
let g:SimpylFold_docstring_preview = 1

nmap zuz <Plug>(FastFoldUpdate)
let g:fastfold_savehook = 1
let g:fastfold_fold_command_suffixes =  ['x','X','a','A','o','O','c','C']
let g:fastfold_fold_movement_commands = [']z', '[z', 'zj', 'zk']
let g:markdown_folding = 1
let g:tex_fold_enabled = 1
let g:vimsyn_folding = 'af'
let g:xml_syntax_folding = 1
let g:javaScript_fold = 1
let g:sh_fold_enabled= 7
let g:ruby_fold = 1
let g:perl_fold = 1
let g:perl_fold_blocks = 1
let g:r_syntax_folding = 1
let g:rust_fold = 1
let g:php_folding = 1
let g:SuperTabDefaultCompletionType = "<c-n>"
let g:jedi#use_splits_not_buffers = "right"


set secure " END OF CONFIG
