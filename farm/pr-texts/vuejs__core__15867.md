# fix(runtime-vapor): remove block node from its actual parentNode on unmount

When a component's root node has been relocated in the DOM (e.g. via a portal or moved under another container in `onMounted`), unmounting it previously threw:
```
NotFoundError: Failed to execute 'removeChild' on 'Node': The node to be removed is not a child of this node
```
because `removeNode` attempted to remove the node from the parent container it was initially inserted into.

This PR aligns `removeNode` with VDOM's `nodeOps.remove` by removing the node from its actual `block.parentNode` when `parent` is provided, and safely ignoring already detached nodes.

Fixes #15861

🤖 Generated with [Claude Code](https://claude.com/claude-code)
