set TEXT_COLOR "#FFFF00"
set INFO_COLOR "#00FF00"

function fish_prompt
    printf '{%s%s%s at %s%s%s%s%s%s%s}$ ' \
        (set_color $TEXT_COLOR) (echo "Aron") \
        (set_color $INFO_COLOR) \
        (set_color $TEXT_COLOR) (hostname|cut -d . -f 1) \
        (set_color $fish_color_cwd) (prompt_pwd) \
        (set_color $TEXT_COLOR) (__fish_git_prompt) \
        (set_color normal)
end

# Fish git prompt
set __fish_git_prompt_showdirtystate 'yes'
set __fish_git_prompt_showstashstate 'yes'
set __fish_git_prompt_showuntrackedfiles 'yes'
set __fish_git_prompt_showupstream 'yes'
set __fish_git_prompt_color_branch yellow
set __fish_git_prompt_color_upstream_ahead green
set __fish_git_prompt_color_upstream_behind red

# Status Chars
set __fish_git_prompt_char_dirtystate '~'
set __fish_git_prompt_char_stagedstate '→'
set __fish_git_prompt_char_untrackedfiles '§'
set __fish_git_prompt_char_stashstate '↩'
set __fish_git_prompt_char_upstream_ahead '+'
set __fish_git_prompt_char_upstream_behind '-'
