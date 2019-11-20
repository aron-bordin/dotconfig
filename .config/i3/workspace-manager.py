#!/bin/env python3
import itertools
import sys
import re
from i3ipc import Connection

i3 = Connection()


def extend_workspace():
    focused = i3.get_tree().find_focused()
    workspace = focused.workspace()
    name = workspace.name

    is_extended = any(re.findall(r'^[\d]+:[\d]+\>', name))

    if not is_extended:
        name = f'{workspace.num}:0>{name}'

        i3.command(f'rename workspace to "{name}"')
    else:
        active_windows = list(filter(lambda x: x.window, workspace))

        if active_windows:
            workspaces = _get_workspaces_by_num(workspace.num)
            target = _add_workspace(workspaces[-1].name)
            if not name.endswith('_'):
                i3.command(f'rename workspace to "{name}_"')
            i3.command(f'workspace "{target}"')


def _get_workspaces_by_num(num, *, priorize=False):
    workspaces = i3.get_workspaces()

    items = filter(lambda x: x.name.startswith(f'{num}:'), workspaces)

    if priorize:
        return list(sorted(items, key=lambda x: (x.name.endswith('_'), int(re.findall(r'(?<=[\d]:)(\d+)', x.name)[0]))))
    else:
        return list(sorted(items, key=lambda x: int(re.findall(r'(?<=[\d]:)(\d+)', x.name)[0])))


def _add_workspace(name):
    current_id = int(re.findall(r'(?<=[\d]:)(\d+)', name)[0])
    new_id = str(current_id + 1)

    new_name = re.sub(r'(?<=[\d]:)(\d+)', new_id, name)
    if new_name.endswith('_'):
        new_name = new_name[:-1]

    return re.sub(r'\:[\d]+\|', '|', new_name)


def _next_workspace(workspaces, current_name):
    items = itertools.cycle(workspaces)

    for item in items:
        if item.name == current_name:
            break

    return next(items).name


def switch_workspace(target):
    focused = i3.get_tree().find_focused()
    workspace = focused.workspace()
    name = workspace.name

    is_extended = any(re.findall(r'^[\d]+:[\d]+\>', name))

    target_num = re.findall(r'^[\d]+', target)

    if not target_num:
        raise ValueError('Invalid workspace target: ', target)

    target_num = int(target_num.pop())

    workspaces = _get_workspaces_by_num(target_num, priorize=True)
    if is_extended and target_num == workspace.num:
        workspaces = _get_workspaces_by_num(target_num, priorize=False)
        target = _next_workspace(workspaces, name)
        if target != name:
            i3.command(f'rename workspace to "{name}_"')
    elif workspaces:
        target = workspaces[0].name

    i3.command(f'workspace "{target}"')

    if target.endswith('_'):
        target = target[:-1]
        i3.command(f'rename workspace to "{target}"')


def move(target):
    focused = i3.get_tree().find_focused()
    workspace = focused.workspace()

    target_num = re.findall(r'^[\d]+', target)

    if not target_num:
        raise ValueError('Invalid workspace target: ', target)

    target_num = int(target_num.pop())

    workspaces = _get_workspaces_by_num(target_num)
    if workspaces:
        if target_num == workspace.num:
            target = _next_workspace(workspaces, workspace.name)
        else:
            target = workspaces[0].name
    else:
        target = target

    i3.command(f'move container to workspace "{target}"')


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'extend':
        extend_workspace()
    elif cmd == 'switch':
        switch_workspace(sys.argv[2])
    elif cmd == 'move':
        move(sys.argv[2])
    else:
        raise Exception('Invalid command: ', cmd)
