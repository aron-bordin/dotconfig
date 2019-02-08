function su
    /bin/su --shell=/usr/bin/fish $argv
end

function vimf
    vim -O (fzf)
end

function fish_user_key_bindings
  fzf_key_bindings
end

function ranger
    if set -q RANGER_LEVEL
        exit
    else
        /usr/bin/ranger $argv
    end
end

function ranger-cd
    set -x tempfile (mktemp -t tmp.XXXXXX)
    ranger --choosedir="$tempfile" "$HOME"
    cd (cat "$tempfile")
    rm -f "$tempfile"
end


function ccat
    pygmentize -g $argv
end

function update_pip
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip install -U
    pip2 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip2 install -U
end


set -gx SSH_AUTH_SOCK /run/user/1000/keyring/ssh
set -gx EDITOR vim
set -gx ARON_GEM_PATH ~/.gem/ruby/2.6.0/bin
set -gx ARON_PYTHON_PATH /home/aron/.local/bin
set -gx SPARK_HOME /home/aron/Tools/spark
set -gx PYSPARK_SUBMIT_ARGS '--master local[8]'
set -gx JAVA_OPTS -Xmx2g
set -gx JAVA_HOME /usr/lib/jvm/java-8-openjdk/
set -gx MONGO_HOST mongodb://127.0.0.1:27017
 
set -gx CUDA_BIN_PATH /opt/cuda/bin
set -gx CONDA_PATH /home/aron/Tools/miniconda3/bin


set -gx PATH $ARON_GEM_PATH $PATH
set -gx PATH $CUDA_BIN_PATH $PATH
set -gx PATH $ARON_PYTHON_PATH $PATH
set -gx PATH $ANDROID_HOME/tools $PATH
set -gx PATH $ANDROID_HOME/tools/bin $PATH
set -gx PATH $ANDROID_HOME/platform-tools $PATH
set -gx NODE_PATH /usr/lib/node_modules/
set -gx XDG_CURRENT_DESKTOP GNOME
set -gx FZF_DEFAULT_OPTS "--no-mouse --ansi --tabstop=4 --exit-0 --layout=reverse -m --height 50% --border"
set -gx FZF_DEFAULT_COMMAND 'fd --type f --exclude .git'
set -gx FZF_CTRL_T_COMMAND "command find -L \$dir -type f 2> /dev/null | sed '1d; s#^\./##'"


setenv SSH_ENV $HOME/.ssh/environment


function loadTheme
    set -gx BASE16_THEME (~/.config/fish/loadThemes.py)
    eval sh ~/.config/base16-shell/scripts/base16-$BASE16_THEME.sh
end

function selectTheme
    ~/.config/fish/loadThemes.py set
    loadTheme
end

loadTheme

function use_gcc5
    set -gx CC gcc-5
    set -gx CXX g++-5
end

function gnome-keyring-daemon
  if test -n "$DESKTOP_SESSION"
    set -gx SSH_AUTH_SOCK (gnome-keyring-daemon --start | awk -F= '{print  $2}')
  end
end

function activate_pyspark
    set -gx PATH $SPARK_HOME/bin $PATH
end

function activate_conda
    set -gx PATH $CONDA_PATH $PATH
end

function activate_resty
    set -gx PATH /opt/openresty/bin/ $PATH
    set -gx PATH /opt/openresty/nginx/sbin/ $PATH
end

function activate_term
    set -x TERM xterm-color
end


abbr setclip "xclip -selection c"
abbr getclip "xclip -selection c -o"

if set -q RANGERCD
    cd $RANGERCD
    set -e RANGERCD
end

if set -q VIMRUNTIME
    set -gx FZF_DEFAULT_OPTS "--preview '~/.config/ranger/scope.sh {} 0 0 /tmp/ False'" $FZF_DEFAULT_OPTS
end
