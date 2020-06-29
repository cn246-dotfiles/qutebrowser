# Commands
c.content.private_browsing = False
c.editor.command = ['urxvt', '-e', 'vim', '{}']
config.bind('<Ctrl-Shift-m>', 'hint links spawn --detach mpv --force-window=immediate {hint-url}')

# COLORS
import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
        'spacing': {
                    'vertical': 6,
                            'horizontal': 8
                                }
        })

#main_color = '#2f343f'
#c.colors.completion.category.bg = main_color
#c.colors.completion.even.bg = '#434a59'
#c.colors.completion.odd.bg = '#393f4d'
#c.colors.completion.scrollbar.bg = main_color
#c.colors.downloads.bar.bg = main_color
#c.colors.messages.error.bg = '#7a2021'
#c.colors.statusbar.command.private.bg = '#5b6b8c'
#c.colors.statusbar.normal.bg = main_color
#c.colors.statusbar.private.bg = '#333333'
#c.colors.statusbar.url.success.https.fg = 'lime'
#c.colors.tabs.even.bg = '#393f4d'
#c.colors.tabs.odd.bg = '#303540'
##c.colors.tabs.selected.even.bg = '#69748c'
##c.colors.tabs.selected.odd.bg = '#69748c'
#

