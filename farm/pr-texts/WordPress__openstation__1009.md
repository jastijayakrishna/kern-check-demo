# Station Home: Add a tribute to Eric Binnion

## Proposed Changes

Adds a small "Thank you, Eric" line with a heart at the bottom of the Station Home sidebar. It links to [The Big Legacy of Eric Binnion](https://friendsofericbinnion.wordpress.com/) in a new tab. When the window is narrow and the sidebar turns into a top bar, the line moves to the end of the page instead.

The line is muted and only reaches full contrast on hover or keyboard focus. It uses neutral colors, not the accent, since the accent marks state.

<img width="1249" height="765" alt="Screenshot 2026-10-14 at 11 46 46" src="https://github.com/user-attachments/assets/8b5e1ace-86d3-44df-918b-ccd5531a9de1" />


## Why are these changes being made?

A small tribute from the team to Eric Binnion, pointing to the site friends and colleagues put together for Eric.

## Testing Instructions

1. Go to OpenStation Preferences > Features and turn on **Use Station Home as your Dashboard** under Beta features.
2. Open the Dashboard from the dock, so Station Home opens.
3. Make sure a heart and "Thank you, Eric" show at the bottom of the left sidebar, under Classic Dashboard, in muted text.
4. Hover it. Make sure the text turns white and the tooltip reads "The Big Legacy of Eric Binnion".
5. Click it. Make sure https://friendsofericbinnion.wordpress.com/ opens in a new browser tab.
6. Go back to the OpenStation tab. Make sure the line still looks muted, with no blue text and no ring around it.
7. Focus Classic Dashboard and press Tab. Make sure the line gets the focus ring and white text.
8. Make the window narrower than about 820px, or open Station Home on a phone. Make sure the line is not in the top bar and shows centered at the end of the page.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- wp-playground-preview:start -->
<a href="https://playground.wordpress.net?blueprint-url=data:application/json,%7B%22%24schema%22%3A%22https%3A%2F%2Fplayground.wordpress.net%2Fblueprint-schema.json%22%2C%22landingPage%22%3A%22%2Fopenstation%2F%22%2C%22preferredVersions%22%3A%7B%22php%22%3A%228.3%22%2C%22wp%22%3A%22latest%22%7D%2C%22features%22%3A%7B%22networking%22%3Atrue%7D%2C%22siteOptions%22%3A%7B%22blogname%22%3A%22OpenStation%22%7D%2C%22steps%22%3A%5B%7B%22step%22%3A%22login%22%2C%22username%22%3A%22admin%22%2C%22password%22%3A%22password%22%7D%2C%7B%22step%22%3A%22installPlugin%22%2C%22pluginData%22%3A%7B%22resource%22%3A%22url%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2FWordPress%2Fopenstation%2Freleases%2Fdownload%2Fci-artifacts%2Fpr-1009-ba5f27728c7fd2e252b57870966ac6035010e16d.zip%22%7D%2C%22options%22%3A%7B%22activate%22%3Atrue%7D%7D%5D%7D" target="_blank" rel="noopener noreferrer">
  <img src="https://raw.githubusercontent.com/adamziel/playground-preview/refs/heads/trunk/assets/playground-preview-button.svg" alt="Open WordPress Playground Preview" width="220" height="57" />
</a>
<!-- wp-playground-preview:end -->
