function fish_prompt
  if test -z $WINDOW
   printf '{%s%s%s at %s%s%s%s%s%s%s}$ ' (set_color "#FFFF00") (echo "Aron") (set_color "#00FF00") (set_color "#FFFF00") (hostname|cut -d . -f 1) (set_color $fish_color_cwd) (prompt_pwd)(set_color "#FFFF00") (__fish_git_prompt) (set_color normal)
 else 
	printf '{%s%s%s at %s%s%s(%s)%s%s%s%s}$ ' (set_color "#FFFF00") (echo "Aron") (set_color "#00FF00") (set_color "#FFFF00") (hostname|cut -d . -f 1) (set_color $fish_color_cwd) (echo $WINDOW) (prompt_pwd)(set_color "#FFFF00") (__fish_git_prompt) (set_color normal)
   #printf '%s%s at %s%s%s(%s)%s%s%s$ ' (set_color white) (whoami) (set_color purple) (hostname|cut -d . -f 1) (set_color white) (echo $WINDOW) (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
 end
end

function fish_greeting
	echo ""
	set_color "#FFFF00"
	echo ""
	echo "Welcome to the Cyberspace"
	echo "A consensual hallucination experienced daily by billions of legitimate operators, in every nation. We are all connected."
	echo ""
	echo "Powered by Hosaka ®"
	echo ""	
end

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


set -gx EDITOR nano
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
