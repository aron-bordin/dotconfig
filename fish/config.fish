function su
        /bin/su --shell=/usr/bin/fish $argv
end

function restart_inotify
	sudo sysctl fs.inotify.max_user_watches=1000000
end

function update_pip
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip install -U
    pip2 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip2 install -U
end


alias vim="nvim"
set -gx EDITOR vim
set -gx ANT_ROOT /usr/bin
set -gx NDK_ROOT /opt/android-ndk
set -gx ANDROID_SDK_ROOT /opt/android-sdk
set -gx ARON_GEM_PATH ~/.gem/ruby/2.3.0/bin
set -gx CARGO_PATH /home/aron/.cargo/bin
set -gx RUST_SRC_PATH /usr/local/src/rustc-1.7.0/src
set -gx ARON_PYTHON_PATH /home/aron/.local/bin

set -gx LUA_PATH '/home/aron/.luarocks/share/lua/5.1/?.lua;/home/aron/.luarocks/share/lua/5.1/?/init.lua;/home/aron/Programming/GitHub/torch/install/share/lua/5.1/?.lua;/home/aron/Programming/GitHub/torch/install/share/lua/5.1/?/init.lua;./?.lua;/home/aron/Programming/GitHub/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
set -gx LUA_CPATH '/home/aron/.luarocks/lib/lua/5.1/?.so;/home/aron/Programming/GitHub/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
set -gx PATH /home/aron/Programming/GitHub/torch/install/bin $PATH
set -gx LD_LIBRARY_PATH /home/aron/Programming/GitHub/torch/install/lib $LD_LIBRARY_PATH
set -gx DYLD_LIBRARY_PATH /home/aron/Programming/GitHub/torch/install/lib $DYLD_LIBRARY_PATH
set -gx LUA_CPATH '/home/aron/Programming/GitHub/torch/install/lib/?.so;' $LUA_CPATH


set -gx PATH $ARON_GEM_PATH $PATH
set -gx PATH $CARGO_PATH $PATH
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

function start_agent                                                                                                                                                                    
    echo "Initializing new SSH agent ..."
    ssh-agent -c | sed 's/^echo/#echo/' > $SSH_ENV
    echo "succeeded"
    chmod 600 $SSH_ENV 
    . $SSH_ENV > /dev/null
    ssh-add
end
