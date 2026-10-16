# fix state update warning in components

Fixes an issue where we had setState in a useMemo - which caused a console error

fixes https://github.com/tokens-studio/figma-plugin/issues/2943
