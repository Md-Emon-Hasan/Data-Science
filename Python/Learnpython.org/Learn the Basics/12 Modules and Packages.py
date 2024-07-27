# Modules and Packages
# Writing modules
print("Writing modules:")
import draw
def play_game():
    ...
def main():
    result = play_game()
    draw.draw_game(result)
if __name__ == '__main__':
    main()
    
def  draw_game():
    ...
def clear_screen(screen):
    ...
    
from draw import draw_game
def main():
    result = play_game()
    draw_game(result)
    
from draw import *
def main():
    result = play_game()
    draw_game(result)
    
if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw
def main():
    result = play_game()
    draw.draw_game(result)
    
def draw_game():
    clear_screen(main_screen)
    ...
def clear_screen(screen):
    ...
class Screen():
    ...

import urllib
urllib.urlopen(...)

import urllib
dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', 
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', 
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', 
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', 
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os', 
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1', 
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 
'urlopen', 'urlretrieve']

# example
print("example:")
import re
find_members = []
for mrmber in dir(re):
    if "find" in member:
        find_members.append(member)
print(sorted(find_members))

