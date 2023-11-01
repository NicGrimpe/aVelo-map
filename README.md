# avelo-map :bike:

## To generate your map

### How to get the cookie (Mileage may vary if not using firefox)
1. Open a session on the [avelo site](https://avelo.rtcquebec.ca/login).
2. Press F12. 
3. Go to the `Network` tab
4. Press F5 to refresh the page.
5. Click on the call to `avelo.rtcquebec.ca` and select the `Cookies` tab.
6. There should be a cookie named `a_velo_session` this is the one we need!

### Generate the map
```bash
nix-shell
export AVELO_TOKEN=a_velo_session_cookie
python avelo-cli.py generate-map
```

An `index.html` file containing a map similar to [mine](https://map.nicg.ca/) should be present in the directory where you called the script.

Enjoy!
