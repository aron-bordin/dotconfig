" ======= Loading Vundle
" Use Vim settings, rather than Vi settings
set pyxversion=3
set nocompatible

filetype off

" Set the runtime path to include Vundle and initialize
call plug#begin('~/.vim/plugged-nvim')
"
Plug '/usr/bin/fzf'
" ####### Plugins #########
Plug 'airblade/vim-gitgutter'
Plug 'brooth/far.vim'
Plug 'carlitux/deoplete-ternjs'
"Plug 'chriskempson/base16-vim'
Plug 'danielwe/base16-vim'
Plug 'davidhalter/jedi-vim'
Plug 'dense-analysis/ale'
Plug 'chrisbra/Recover.vim'
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'easymotion/vim-easymotion'
Plug 'ekalinin/dockerfile.vim'
Plug 'ervandew/supertab'
Plug 'francoiscabrol/ranger.vim'
Plug 'rbgrouleff/bclose.vim'  " ranger dep
Plug 'inside/vim-search-pulse'
Plug 'hashivim/vim-terraform'
Plug 'janko/vim-test'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'kshenoy/vim-signature'
Plug 'Konfekt/FastFold'
Plug 'machakann/vim-highlightedyank'
Plug 'majutsushi/tagbar'
Plug 'matze/vim-move'
Plug 'mbbill/undotree'
Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
" Plug 'nvie/vim-flake8'
Plug 'posva/vim-vue'
Plug 'roman/golden-ratio'
Plug 'ryanoasis/vim-devicons'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'takac/vim-hardtime'
Plug 'terryma/vim-multiple-cursors'
Plug 'tmhedberg/SimpylFold'
Plug 'thaerkh/vim-workspace'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-eunuch'
Plug 't9md/vim-choosewin'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-scripts/indentpython.vim'
Plug 'xolox/vim-misc'
Plug 'Yggdroot/indentLine'
Plug 'ycmjason/html5.vim'

" ####### End-Plugins ####

call plug#end()

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
set shell=/usr/bin/fish

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

let g:airline_powerline_fonts = 1
let g:airline_theme='bubblegum'

set incsearch
set hlsearch
set inccommand=split
nnoremap <Leader><space> :noh<cr>

let &colorcolumn="80,".join(range(121,999),",")

set formatoptions-=t
set updatetime=250

let g:goldenview__enable_default_mapping = 0

nnoremap <F5> :UndotreeToggle<cr>
nmap <F8> :TagbarToggle<CR>

nnoremap tn :tabnew<Space>
nnoremap tc :tabclose<CR>
nnoremap tk :tabnext<CR>
nnoremap tj :tabprev<CR>
nnoremap th :tabfirst<CR>
nnoremap tl :tablast<CR>

inoremap <C-o> <Esc>O<Esc>jA
nmap <silent> <C-i> <Plug>(pydocstring)

set pastetoggle=<F3>

let g:airline#extensions#ale#enabled = 1
let g:ale_completion_enabled = 0

let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
nmap <silent> <C-q> <Plug>(ale_previous_wrap)
nmap <silent> <C-w> <Plug>(ale_next_wrap)
let g:ale_sign_error = '💥'
let g:ale_sign_warning = '⚠'

"let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_start_level = 2
let g:indent_guides_guide_size = 1

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

autocmd! FileType fzf
autocmd  FileType fzf set laststatus=0 noshowmode noruler
  \| autocmd BufLeave <buffer> set laststatus=2 showmode ruler

let g:fzf_command_prefix = 'Fzf'

nnoremap ,f :FzfFiles<CR>
nnoremap ,F :FzfGFiles<CR>
nnoremap ,b :FzfBuffers<CR>
nnoremap ,s :FzfAg<CR>
nnoremap ,S :FzfRg<CR>

nmap <leader>f <Plug>(ale_fix)
nmap <leader>F <Plug>(ALEFixSuggest)

let g:fzf_layout = { 'down': '~40%' }
let g:fzf_buffers_jump = 1
let g:hardtime_maxcount = 2

let g:multi_cursor_use_default_mapping=0

" Default mapping
let g:multi_cursor_start_word_key      = '<C-n>'
let g:multi_cursor_select_all_word_key = 'a<C-N>'
let g:multi_cursor_start_key           = 'g<C-n>'
let g:multi_cursor_select_all_key      = 'ag<C-n>'
let g:multi_cursor_next_key            = '<C-n>'
let g:multi_cursor_prev_key            = '<C-p>'
let g:multi_cursor_skip_key            = '<C-x>'
let g:multi_cursor_quit_key            = '<Esc>'

let g:ale_fixers = {
\   '*': ['remove_trailing_lines', 'trim_whitespace'],
\   'javascript': ['eslint', 'prettier'],
\   'python': ['autopep8']
\}

let g:ale_linters = {
\   'python': ['autopep8', 'flake8', 'yapf'],
\   'javascript': ['prettier']
\}

let g:EasyMotion_startofline = 0 " keep cursor column when JK motion
let g:EasyMotion_smartcase = 1

nnoremap <F2> :call ToogleFold()<CR>

function! ToogleFold()
     if &foldlevel >= 20
         set foldlevel=1
     else
         set foldlevel=99
     endif
 endfunction

let g:ranger_map_keys = 0
map <leader>m :Ranger<CR>
map <leader>M :RangerWorkingDirectory<CR>

nnoremap <leader>w :ToggleWorkspace<CR>
let g:workspace_session_directory = $HOME . '/.vim/sessions/'
let g:workspace_session_disable_on_args = 1

set cursorline
let g:workspace_autosave = 0
set lazyredraw
set showmatch
set smartcase
set visualbell
set title
set columns=120
set textwidth=120

let g:move_key_modifier = 'S'

function! WinLabel()
endfunction

nmap <Leader>l <Plug>(choosewin)

let g:choosewin_label='ABCDEFGHIJKLMNOPQRTUVWYZ'
let g:choosewin_statusline_replace='0'

function! WinLabel(...)
    let builder = a:1
    let context = a:2

    call builder.add_section('airline_b', '%{"[ " . g:choosewin_label[winnr() - 1] . " ]"}')
    return 0
endfunction

call airline#add_statusline_func('WinLabel')
call airline#add_inactive_statusline_func('WinLabel')

if has('wildmenu')
	set wildmenu
	set wildmode=list:longest,full
	set wildoptions=tagfile
	set wildignorecase
	set wildignore+=.hg,.git,.svn
	set wildignore+=*.aux,*.out
	set wildignore+=*.jpg,*.bmp,*.gif,*.png,*.jpeg
	set wildignore+=*.o,*.obj,*.exe,*.dll,*.manifest
	set wildignore+=*.spl
	set wildignore+=*.sw?
	set wildignore+=.DS_Store
	set wildignore+=*.luac
	set wildignore+=*.pyc
endif

let g:highlightedyank_highlight_duration = 1000
let g:deoplete#enable_at_startup = 1
let g:deoplete#sources#jedi#show_docstring = 1
let g:deoplete#max_info_width = 0
let g:jedi#completions_enabled = 0

if has('autocmd') && v:version > 701
    augroup todo
        autocmd!
        autocmd Syntax * call matchadd(
                    \ 'Debug',
                    \ '\v\W\zs<(NOTE|INFO|IDEA|TODO|FIXME|CHANGED|REMOVE|XXX|BUG|HACK|TRICKY)>'
                    \ )
    augroup END
endif

let g:deoplete#sources#ternjs#filetypes = ['vue']

highlight ALEError ctermbg=none cterm=underline
highlight ALEWarning ctermbg=none cterm=underline

nmap t<C-n> :TestNearest<CR>
nmap t<C-f> :TestFile<CR>
nmap t<C-s> :TestSuite<CR>
nmap t<C-l> :TestLast<CR>
nmap t<C-g> :TestVisit<CR>

let test#strategy = "neovim"
let g:test#preserve_screen = 1
let test#neovim#term_position = "belowright"
let test#python#runner = 'pytest'
let test#enabled_runners = ["python#pytest"]

let test#python#pytest#options = {
  \ 'all':   '--cov-report term-missing'
\}
if has('nvim')
  tmap <C-o> <C-\><C-n>
endif

autocmd! FileType fzf
autocmd  FileType fzf set laststatus=0 noshowmode noruler
  \| autocmd BufLeave <buffer> set laststatus=2 showmode ruler


set secure " END OF CONFIG
