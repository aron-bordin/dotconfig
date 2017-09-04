function su
        /bin/su --shell=/usr/bin/bash $argv
end

function update_pip
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip install -U
    pip2 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip2 install -U
end


set -gx SSH_AUTH_SOCK /run/user/1000/keyring/ssh
set -gx EDITOR vim
set -gx ARON_GEM_PATH ~/.gem/ruby/2.4.0/bin
set -gx ARON_PYTHON_PATH /home/aron/.local/bin
set -gx SPARK_HOME /home/aron/Tools/spark
set -gx PYSPARK_SUBMIT_ARGS '--master local[8]'
 
set -gx CUDA_BIN_PATH /opt/cuda/bin
set -gx CONDA_PATH /home/aron/Tools/miniconda3/bin


set -gx PATH $ARON_GEM_PATH $PATH
set -gx PATH $ARON_PYTHON_PATH $PATH
set -gx NODE_PATH /usr/lib/node_modules/

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

abbr setclip "xclip -selection c"
abbr getclip "xclip -selection c -o"
